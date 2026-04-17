#!/usr/bin/env python3
"""
Solomon OS — Telegram Bot Handler
Receives URLs via Telegram, orchestrates PinchTab/Hermes/Russell, returns results.

Usage:
    TELEGRAM_BOT_TOKEN=... python3 telegram_handler.py

Commands:
    /agent [url]           — Analyze URL, propose actions
    /agent [url] --do      — Analyze + execute immediately
    /agent [url] --task [desc] — Delegate to Hermes/Russell
    /tabs                  — List active PinchTab instances
    /kill [instance_id]    — Stop a PinchTab instance
    /status                — Show orchestrator status
"""

import os
import sys
import json
import time
import asyncio
import logging
from typing import Optional

import httpx

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [SOLOMON] %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler("/home/workspace/solomon-vault/raw/orchestration.log"),
        logging.StreamHandler()
    ]
)
log = logging.getLogger("solomon")

# Add orchestration dir to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    ContextTypes, filters
)
from telegram.constants import ParseMode

# Import our modules
from pinchtab_client import PinchTabClient

# Configuration
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
ALLOWED_TELEGRAM_IDS = {7890348781}  # Joseph's Telegram ID
ZO_API_KEY = os.environ.get("ZO_API_KEY", "")

# Active instances managed by this handler
active_instances: dict[str, dict] = {}


# ─── Helpers ─────────────────────────────────────────────────────────────────

def parse_agent_command(text: str) -> dict:
    """Parse /agent command into {url, action, task_description}."""
    text = text.strip()
    url = ""
    action = "analyze"  # analyze | do | task
    task_desc = ""

    if "--do" in text:
        action = "do"
        text = text.replace("--do", "").strip()
    elif "--task" in text:
        action = "task"
        parts = text.split("--task")
        text = parts[0].strip()
        task_desc = parts[1].strip() if len(parts) > 1 else ""

    # Extract URL (first reasonable-looking URL)
    words = text.split()
    for w in words:
        if w.startswith("http://") or w.startswith("https://") or ".com" in w or ".io" in w or ".ai" in w or ".app" in w:
            url = w
            break

    return {"url": url, "action": action, "task_desc": task_desc}


async def send_typing(update: Update, duration: float = 1.0):
    """Send typing indicator."""
    try:
        await update.message.chat.send_action("typing")
        await asyncio.sleep(duration)
    except Exception:
        pass


async def safe_reply(update: Update, text: str, parse_mode: str = ParseMode.MARKDOWN_V2,
                     reply_markup=None, quote: bool = True):
    """Send reply, escaping markdown if needed."""
    try:
        await update.message.reply_text(text, parse_mode=parse_mode, reply_markup=reply_markup, quote=quote)
    except Exception as e:
        log.warning(f"Markdown parse failed, sending plain: {e}")
        try:
            await update.message.reply_text(text, reply_markup=reply_markup, quote=quote)
        except Exception as e2:
            log.error(f"Failed to send message: {e2}")


def escape_md(text: str) -> str:
    """Escape markdown v2 special characters."""
    escape_chars = r'_[]()*~`>#+-=|{}.!'
    for c in escape_chars:
        text = text.replace(c, f"\\{c}")
    return text


# ─── Command Handlers ─────────────────────────────────────────────────────────

async def cmd_agent(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /agent [url] command."""
    if update.effective_user.id not in ALLOWED_TELEGRAM_IDS:
        await safe_reply(update, "Unauthorized.")
        return

    args = " ".join(context.args) if context.args else ""
    if not args:
        await safe_reply(update, "Usage: /agent [url] [--do] [--task description]")
        return

    await send_typing(update, 2)

    parsed = parse_agent_command(args)
    url = parsed["url"]
    action = parsed["action"]
    task_desc = parsed["task_desc"]

    if not url:
        await safe_reply(update, "No URL found in your message. Try: /agent https://example.com")
        return

    log.info(f"Agent command: url={url} action={action} task={task_desc}")

    try:
        if action == "analyze":
            result = await analyze_url(url)
            await safe_reply(update, result)
        elif action == "do":
            result = await execute_on_url(url, update)
            await safe_reply(update, result)
        elif action == "task":
            result = await delegate_task(url, task_desc, update)
            await safe_reply(update, result)
    except Exception as e:
        log.error(f"Agent error: {e}", exc_info=True)
        await safe_reply(update, f"Error: {e}")


async def cmd_tabs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /tabs — list active PinchTab instances."""
    if update.effective_user.id not in ALLOWED_TELEGRAM_IDS:
        await safe_reply(update, "Unauthorized.")
        return

    await send_typing(update, 1)

    try:
        client = PinchTabClient()
        tabs = client.list_tabs()
        instances_resp = httpx.get(f"{client.base_url}/instances",
                                   headers=client._headers(), timeout=10)
        instances = instances_resp.json() if instances_resp.status_code == 200 else {}

        lines = ["*Active Browser Instances:*\n"]
        if isinstance(instances, dict) and "instances" in instances:
            for inst in instances["instances"]:
                status_emoji = "🟢" if inst.get("status") == "running" else "🔴"
                lines.append(f"{status_emoji} `{inst['id']}` — {inst.get('status','?')} @ port {inst.get('port','?')}")
        elif isinstance(instances, list):
            for inst in instances:
                status_emoji = "🟢" if inst.get("status") == "running" else "🔴"
                lines.append(f"{status_emoji} `{inst['id']}` — {inst.get('status','?')} @ port {inst.get('port','?')}")
        else:
            lines.append("_No instances found_")

        await safe_reply(update, "\n".join(lines))
    except Exception as e:
        log.error(f"Tabs error: {e}")
        await safe_reply(update, f"Error: {e}")


async def cmd_kill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /kill [instance_id] — stop a browser instance."""
    if update.effective_user.id not in ALLOWED_TELEGRAM_IDS:
        await safe_reply(update, "Unauthorized.")
        return

    if not context.args:
        await safe_reply(update, "Usage: /kill [instance_id]")
        return

    instance_id = context.args[0]
    await send_typing(update, 1)

    try:
        client = PinchTabClient()
        result = client.stop_instance(instance_id)
        await safe_reply(update, f"✅ Instance stopped: `{instance_id}`")
        log.info(f"Stopped instance {instance_id}: {result}")
    except Exception as e:
        log.error(f"Kill error: {e}")
        await safe_reply(update, f"Error stopping instance: {e}")


async def cmd_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /status — show orchestrator status."""
    if update.effective_user.id not in ALLOWED_TELEGRAM_IDS:
        await safe_reply(update, "Unauthorized.")
        return

    status_lines = [
        "*Solomon OS Orchestrator Status*\n",
        "🟢 PinchTab: port 9888",
        "🟢 Ollama: port 11434",
        f"🟢 Active instances: {len(active_instances)}",
    ]

    try:
        client = PinchTabClient()
        health = client._headers()
        status_lines.append(f"🟢 Telegram bot: running")
    except Exception as e:
        status_lines.append(f"🔴 Error: {e}")

    await safe_reply(update, "\n".join(status_lines))


async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help."""
    help_text = """
*Solomon OS Agent Commands*

`/agent [url]` — Analyze a URL, get summary + suggested actions

`/agent [url] --do` — Analyze + execute actions immediately

`/agent [url] --task [description]` — Analyze + delegate to AI worker

`/tabs` — List active browser instances

`/kill [instance_id]` — Stop a browser instance

`/status` — Show orchestrator health
"""
    await safe_reply(update, help_text)


# ─── Core Orchestration Logic ─────────────────────────────────────────────────

async def analyze_url(url: str) -> str:
    """Analyze a URL using PinchTab snapshot. Returns summary."""
    import httpx

    client = PinchTabClient()

    await asyncio.to_thread(client.start_instance)
    inst = {"id": client.instance_id, "port": client.instance_port}
    active_instances[client.instance_id] = inst

    await asyncio.to_thread(client.navigate, url)
    await asyncio.sleep(2)  # Let page settle

    try:
        snap = await asyncio.to_thread(client.snapshot, "interactive")
        nodes = snap.get("nodes", [])

        if not nodes:
            return f"*Page Analysis*\n\nURL: {url}\n\nNo interactive elements found."

        # Summarize top elements
        elements = []
        for node in nodes[:15]:
            role = node.get("role", "?")
            name = node.get("name", "")
            if name and role not in ("main", "paragraph"):
                elements.append(f"  • [{role}] {name[:60]}")

        summary = [
            f"*Page Analysis*\n",
            f"*URL:* {url}",
            f"*Interactive elements found:* {len(nodes)}\n",
            "*Top elements:*\n" + "\n".join(elements) if elements else "",
            f"\n_Spawning agent to take actions…_",
        ]

        return "\n".join(summary)
    finally:
        # Keep instance alive for follow-up actions
        pass


async def execute_on_url(url: str, update: Update) -> str:
    """Execute a task on URL after user approval."""
    import httpx

    client = PinchTabClient()
    await asyncio.to_thread(client.start_instance)
    inst = {"id": client.instance_id, "port": client.instance_port}
    active_instances[client.instance_id] = inst

    await asyncio.to_thread(client.navigate, url)
    await asyncio.sleep(2)

    snap = await asyncio.to_thread(client.snapshot, "interactive")
    nodes = snap.get("nodes", [])

    elements = []
    for node in nodes[:10]:
        role = node.get("role", "?")
        name = node.get("name", "")
        if name:
            elements.append(f"  `{node.get('ref','?')}` — [{role}] {name[:50]}")

    result = [
        f"*Execution Ready*\n",
        f"*URL:* {url}",
        f"*Interactive elements:*\n" + "\n".join(elements),
        f"\n_Instance kept alive at port {client.instance_port}_",
    ]

    return "\n".join(result)


async def delegate_task(url: str, task_desc: str, update: Update) -> str:
    """Delegate task to Russell Tuna via Zo API."""
    import httpx

    if not ZO_API_KEY:
        return "_Zo API key not configured. Set ZO_API_KEY env var._"

    # Build prompt for Russell Tuna
    prompt = f"""Analyze this URL and complete the task described.

URL: {url}
Task: {task_desc}

Context: You are Russell Tuna, a worker agent in Solomon OS. Use the PinchTab browser automation at port 9888 (token: solomon123) to complete this task.

Steps:
1. Start a browser instance: POST http://localhost:9888/instances/start with {{"mode":"headless"}}
2. Navigate to the URL
3. Take snapshot to find interactive elements
4. Execute the needed actions
5. Report results

Report back with what you found and what actions you took."""

    try:
        resp = httpx.post(
            "https://api.zo.computer/zo/ask",
            headers={
                "Authorization": f"Bearer {ZO_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "input": prompt,
                "model_name": "vercel:minimax/minimax-m2.7",
            },
            timeout=60
        )
        result = resp.json()
        output = result.get("output", "No response from Zo API")
        return f"*Russell Tuna Task*\n\n{output}"
    except Exception as e:
        log.error(f"Zo API error: {e}")
        return f"Error delegating to Russell Tuna: {e}"


# ─── Message Handler (catch plain URLs) ──────────────────────────────────────

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle plain text messages — treat as URL for analysis."""
    if update.effective_user.id not in ALLOWED_TELEGRAM_IDS:
        return

    text = update.message.text.strip()

    # Skip if it's a command
    if text.startswith("/"):
        return

    # Check if it looks like a URL
    if "http://" in text or "https://" in text or ".com" in text or ".io" in text:
        # Treat as /agent command
        context.args = [text]
        await cmd_agent(update, context)


# ─── Error Handler ────────────────────────────────────────────────────────────

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log.error(f"Telegram error: {context.error}")


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    if not TELEGRAM_BOT_TOKEN:
        log.error("TELEGRAM_BOT_TOKEN not set. Exiting.")
        sys.exit(1)

    log.info("Starting Solomon OS Telegram Bot…")

    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("agent", cmd_agent))
    app.add_handler(CommandHandler("tabs", cmd_tabs))
    app.add_handler(CommandHandler("kill", cmd_kill))
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_error_handler(error_handler)

    log.info("Bot started. Polling for updates…")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
