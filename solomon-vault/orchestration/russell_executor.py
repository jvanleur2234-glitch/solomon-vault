"""
Russell Tuna Executor — delegates tasks to Russell Tuna via Zo API.
Russell Tuna = Telegram AI worker at t.me/RussellTunaBot, powered by Ollama qwen3:1.7b.
"""

import os
import httpx
import logging
from typing import Optional

log = logging.getLogger("solomon.russell")

ZO_API_KEY = os.environ.get("ZO_API_KEY", "")
SOLOMON_CONTEXT = """
You are Russell Tuna, a worker agent in Solomon OS.
Solomon OS is Joseph Van Leur's 24/7 AI business system.
Your role: Execute tasks delegated by the Telegram bot handler.
Use PinchTab browser automation (port 9888, token: solomon123) for web actions.
Available tools: PinchTab HTTP API, Ollama (localhost:11434), Zo API.

PinchTab usage:
1. POST http://localhost:9888/instances/start with {"mode":"headless"} → get instance port
2. POST :port/navigate with {"url": "..."}
3. GET :port/snapshot?filter=interactive → get element refs
4. POST :port/action with {"kind":"click", "ref":"e1"}
5. POST http://localhost:9888/instances/:id/stop

Report what you did and what you found.
"""


async def execute_task(
    url: str,
    task_description: str,
    zo_api_key: Optional[str] = None,
) -> str:
    """
    Execute a task by spawning Russell Tuna via Zo API.
    Returns the task result as a string.
    """
    api_key = zo_api_key or ZO_API_KEY

    if not api_key:
        return "ERROR: ZO_API_KEY not configured. Cannot delegate to Russell Tuna."

    full_prompt = f"""{SOLOMON_CONTEXT}

TASK: {task_description}

TARGET URL: {url}

Please execute this task. Start by analyzing the URL, then take the necessary actions.
Report back with:
1. What the page/application is
2. What actions you took
3. The results
"""

    try:
        async with httpx.AsyncClient(timeout=120) as client:
            resp = await client.post(
                "https://api.zo.computer/zo/ask",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "input": full_prompt,
                    "model_name": "vercel:minimax/minimax-m2.7",
                }
            )
            resp.raise_for_status()
            result = resp.json()
            output = result.get("output", "No response from Zo API")
            log.info(f"Russell task completed: {task_description[:50]}")
            return output

    except httpx.HTTPStatusError as e:
        log.error(f"Zo API HTTP error: {e.response.status_code} {e.response.text}")
        return f"ERROR: Zo API returned {e.response.status_code}"
    except Exception as e:
        log.error(f"Russell executor error: {e}")
        return f"ERROR: {e}"


if __name__ == "__main__":
    import asyncio

    async def test():
        result = await execute_task(
            "https://example.com",
            "Take a snapshot of this page and describe what you see"
        )
        print(result[:500])

    asyncio.run(test())
