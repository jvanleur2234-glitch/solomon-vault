#!/usr/bin/env python3
"""
Solomon Browser Agent — Interactive Web Agent (v2)
Direct Playwright + LLM = no framework overhead, no event bus timeouts.
Polgia-style: natural language task → browser actions → structured result.
"""

import os
import sys
import json
import asyncio
import uuid
from datetime import datetime, timezone
from typing import Optional

# ── Playwright ────────────────────────────────────────────────────────────────
from playwright.sync_api import sync_playwright, Browser, Page
import playwright

# ── LLM clients ─────────────────────────────────────────────────────────────
def get_llm(model: str):
    if model == "anthropic" or model == "claude":
        from anthropic import Anthropic
        return Anthropic(), "anthropic"
    elif model == "openai" or model == "gpt4":
        from openai import OpenAI
        return OpenAI(), "openai"
    elif model == "groq" or model == "local":
        from openai import OpenAI
        key = os.getenv("GROQ_API_KEY") or os.getenv("OPENAI_API_KEY")
        if not key:
            raise RuntimeError("No GROQ_API_KEY or OPENAI_API_KEY set")
        return OpenAI(api_key=key, base_url="https://api.groq.com/openai/v1"), "groq"
    else:
        raise ValueError(f"Unknown model: {model}")

# ── State ────────────────────────────────────────────────────────────────────
HISTORY_DIR = "/home/workspace/solomon-vault/raw/browser_agent_history"
TASKS_FILE  = "/home/workspace/solomon-vault/raw/browser_agent_tasks.json"
os.makedirs(HISTORY_DIR, exist_ok=True)

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE) as f:
            return json.load(f)
    return {}

def save_tasks(tasks: dict):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2, default=str)

def create_task(task: str, model: str = "groq") -> dict:
    task_id = str(uuid.uuid4())[:8]
    entry = {
        "id": task_id,
        "task": task,
        "model": model,
        "status": "pending",
        "created": datetime.now(timezone.utc).isoformat(),
        "completed": None,
        "result": None,
        "error": None,
        "steps": [],
        "history_file": f"{HISTORY_DIR}/{task_id}.json",
    }
    tasks = load_tasks()
    tasks[task_id] = entry
    save_tasks(tasks)
    return entry

def update_task(task_id: str, **kwargs):
    tasks = load_tasks()
    if task_id in tasks:
        tasks[task_id].update(kwargs)
        save_tasks(tasks)

# ── Action primitives ─────────────────────────────────────────────────────────
class BrowserTools:
    """Available browser actions the LLM can request."""

    def __init__(self, page: Page, task_id: str):
        self.page = page
        self.task_id = task_id
        self.last_screenshot: Optional[str] = None

    def navigate(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded", timeout=15000)
        return f"Navigated to {self.page.url}, title: {self.page.title()}"

    def click(self, selector: str):
        self.page.click(selector, timeout=10000)
        return f"Clicked {selector}"

    def fill(self, selector: str, text: str):
        self.page.fill(selector, text)
        return f"Filled '{text[:50]}{'...' if len(text)>50 else ''}' in {selector}"

    def press(self, key: str):
        self.page.keyboard.press(key)
        return f"Pressed {key}"

    def scroll(self, pixels: int):
        self.page.mouse.wheel(0, pixels)
        return f"Scrolled {pixels}px"

    def wait(self, seconds: float):
        self.page.wait_for_timeout(seconds * 1000)
        return f"Waited {seconds}s"

    def extract(self, query: str) -> str:
        """Extract content from page using textContent."""
        try:
            content = self.page.text_content("body") or ""
            return f"Page content ({len(content)} chars):\n{content[:3000]}"
        except Exception as e:
            return f"Extract error: {e}"

    def screenshot(self, label: str = "screenshot") -> str:
        path = f"/tmp/{self.task_id}_{label}.png"
        self.page.screenshot(path=path)
        self.last_screenshot = path
        return f"Screenshot saved to {path}"

    def get_page_info(self) -> str:
        return json.dumps({
            "url": self.page.url,
            "title": self.page.title(),
            "viewable_text": self.page.inner_text("body")[:500] if self.page.inner_text("body") else "",
        }, indent=2)

AVAILABLE_ACTIONS = ["navigate", "click", "fill", "press", "scroll", "wait", "extract", "screenshot", "get_page_info"]

SYSTEM_PROMPT = f"""You are a browser automation agent. A user gives you a task to perform on a website.
You control a browser via Playwright. You must call ONE action at a time.

Available actions:
- navigate(url) — go to a URL
- click(selector) — click an element by CSS selector
- fill(selector, text) — type text into an input
- press(key) — press a keyboard key (Enter, Escape, Tab, etc.)
- scroll(pixels) — scroll by pixels (positive=down, negative=up)
- wait(seconds) — wait for n seconds
- extract(query) — get page text content
- screenshot(label) — take a screenshot
- get_page_info() — get URL, title, and visible text

Rules:
1. Start by calling get_page_info() or navigate() to see where you are
2. Work step-by-step — one action per turn
3. After click/fill, always wait 1s for page to update
4. Use extract() to get the final answer, then say DONE: <your answer>
5. If stuck, try scroll or wait
6. NEVER try to solve captchas — report them and stop
7. Keep extract() calls to 2000 chars max

Output format — respond with ONLY this JSON:
{{"action": "action_name", "args": ["arg1"], "reasoning": "why this action"}}

Example: Task: "Go to example.com and tell me the heading"
{{"action": "navigate", "args": ["https://example.com"], "reasoning": "Start by navigating to the site"}}
"""

USER_PROMPT_TEMPLATE = 'Task: "{task}"\n\nRespond with the next action as JSON.'

# ── Main agent loop ───────────────────────────────────────────────────────────
def run_agent(task: str, model: str = "groq", max_steps: int = 20) -> dict:
    task_id = create_task(task, model)["id"]
    update_task(task_id, status="running")

    steps = []
    browser = None

    try:
        llm, provider = get_llm(model)
        model_name = (
            "claude-sonnet-4-20250514" if provider == "anthropic"
            else "llama-3.3-70b-versatile" if provider == "groq"
            else "gpt-4o"
        )

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
            context = browser.new_context(
                viewport={"width": 1280, "height": 800},
                user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
            )
            page = context.new_page()
            tools = BrowserTools(page, task_id)

            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT_TEMPLATE.format(task=task)},
            ]

            for step_num in range(max_steps):
                # Call LLM
                if provider == "anthropic":
                    response = llm.messages.create(
                        model=model_name,
                        max_tokens=512,
                        system=SYSTEM_PROMPT,
                        messages=[{"role": "user", "content": USER_PROMPT_TEMPLATE.format(task=task)}],
                    )
                    raw = response.content[0].text.strip()
                else:
                    response = llm.chat.completions.create(
                        model=model_name,
                        messages=messages,
                        temperature=0.1,
                        max_tokens=512,
                    )
                    raw = response.choices[0].message.content.strip()

                # Parse JSON action
                try:
                    # Strip markdown code blocks if present
                    if raw.startswith("```"):
                        raw = raw.split("```")[1]
                        if raw.startswith("json"):
                            raw = raw[4:]
                        raw = raw.strip()

                    action_data = json.loads(raw)
                    action = action_data.get("action", "")
                    args = action_data.get("args", [])
                    reasoning = action_data.get("reasoning", "")

                except json.JSONDecodeError:
                    steps.append({"step": step_num + 1, "action": "parse_error", "input": raw[:300], "result": "Failed to parse LLM response"})
                    # If raw text contains a direct answer, use it
                    raw_lower = raw.lower().strip()
                    if raw_lower.startswith("done"):
                        answer = raw.split(":", 1)[1].strip() if ":" in raw else raw.strip()
                        update_task(task_id, status="done", result={"answer": answer}, steps=steps)
                        return {"done": True, "answer": answer, "steps": steps}
                    if any(raw_lower.startswith(x) for x in ["title:", "the title", "the heading", "answer:", "result:"]):
                        update_task(task_id, status="done", result={"answer": raw}, steps=steps)
                        return {"done": True, "answer": raw, "steps": steps}
                    # Fallback: extract page and ask LLM to summarize
                    try:
                        result_text = tools.extract("body")
                        steps[-1]["result"] = result_text[:500]
                        # Don't add parse_error turn to messages — just summarize
                        messages.append({"role": "user", "content": f"Page content:\n{result_text[:2000]}\n\nTask: {task}\nWhat is the final answer? Reply with just the answer."})
                        continue
                    except Exception as e:
                        steps.append({"step": step_num + 1, "error": str(e)})
                        break

                # Execute action
                if action == "DONE" or action == "done":
                    final_answer = args[0] if args else reasoning
                    update_task(task_id, status="done", result={"answer": final_answer}, steps=steps)
                    return {"done": True, "answer": final_answer, "steps": steps}

                if action not in AVAILABLE_ACTIONS:
                    steps.append({"step": step_num + 1, "action": action, "result": f"Unknown action: {action}"})
                    messages.append({"role": "assistant", "content": raw})
                    messages.append({"role": "user", "content": f"Unknown action '{action}'. Available: {AVAILABLE_ACTIONS}. Try extract() or get_page_info()."})
                    continue

                # Execute
                try:
                    if action == "navigate":
                        result = tools.navigate(args[0])
                    elif action == "click":
                        result = tools.click(args[0])
                        tools.wait(1)
                    elif action == "fill":
                        result = tools.fill(args[0], args[1])
                        tools.wait(0.5)
                    elif action == "press":
                        result = tools.press(args[0])
                    elif action == "scroll":
                        result = tools.scroll(int(args[0]))
                    elif action == "wait":
                        result = tools.wait(float(args[0]))
                    elif action == "extract":
                        result = tools.extract(args[0] if args else "body")
                    elif action == "screenshot":
                        result = tools.screenshot(args[0] if args else "step")
                    elif action == "get_page_info":
                        result = tools.get_page_info()
                    else:
                        result = f"Action {action} not implemented"

                    steps.append({"step": step_num + 1, "action": action, "args": args, "reasoning": reasoning, "result": str(result)[:300]})
                    messages.append({"role": "assistant", "content": raw})
                    messages.append({"role": "user", "content": f"Action result: {str(result)[:500]}\n\nWhat is the next action? Output JSON."})

                except Exception as e:
                    steps.append({"step": step_num + 1, "action": action, "args": args, "error": str(e)})
                    messages.append({"role": "assistant", "content": raw})
                    messages.append({"role": "user", "content": f"Error: {str(e)}\nTry a different action or extract page content."})

            # Max steps reached
            update_task(task_id, status="partial", steps=steps)
            return {"done": False, "steps": steps, "reason": "max_steps_reached"}

    except Exception as e:
        update_task(task_id, status="error", error=str(e), steps=steps)
        return {"done": False, "error": str(e), "steps": steps}

    finally:
        if browser:
            try:
                browser.close()
            except:
                pass

# ── CLI ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 browser_agent.py <task> [model]")
        print("  task  — Natural language task")
        print("  model — groq (default), anthropic, openai")
        print("")
        print("Examples:")
        print("  python3 browser_agent.py 'Go to example.com and extract the heading'")
        print("  python3 browser_agent.py 'Search Google for AI agents and list results' anthropic")
        sys.exit(1)

    task  = sys.argv[1]
    model = sys.argv[2] if len(sys.argv) > 2 else "groq"

    print(f"Task: {task[:80]}{'...' if len(task) > 80 else ''}")
    print(f"Model: {model}")
    print("---")

    result = run_agent(task, model)

    if result.get("done"):
        print(f"\n✅ DONE:\n{result.get('answer', 'N/A')}")
    else:
        print(f"\n⚠️  {result.get('reason', result.get('error', 'unknown'))}")
        if result.get("steps"):
            print("\nSteps taken:")
            for s in result["steps"][-5:]:
                print(f"  [{s['step']}] {s.get('action','?')}: {str(s.get('result', s.get('error','')))[:100]}")

    sys.exit(0 if result.get("done") else 1)
