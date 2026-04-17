# RD Report — mobile-use (Minitap)

**URL:** https://github.com/minitap-ai/mobile-use
**Date:** 2026-04-17
**Joseph Handle:** josephv
**Status:** INTEGRATE

---

## What It Is
Open-source AI agent that controls Android/iOS devices via natural language. Connect via USB or WiFi, issue commands like "open Gmail and list unread sender/subject," and it navigates the UI to execute. Achieved 100% on AndroidWorld benchmark — first to do so. Also has an MCP server for tool-calling integrations.

**Architecture (multi-agent pipeline):**
- Orchestrator → Planner → Cortex → Executor + Contextor + Hopper + Outputter
- Uses ADB (Android) or idb (iOS) under the hood
- Supports any OpenAI-compatible LLM (local or cloud)
- Data scraping mode: extract structured data from any app into JSON

**Key differentiators:**
- Top benchmark performer, first to hit 100% on AndroidWorld
- Real device + emulator support
- Works over WiFi (no USB cable needed after initial setup)
- MCP server exposed for tool integrations

---

## What Solomon OS Could Use It For

**1. Russell Tuna as a Phone Bot**
Russell Tuna already runs on Ollama. Hook mobile-use into Russell's toolset so Joseph can say "check my unread emails" or "reply to this text" and Russell navigates the phone to do it. This turns Russell from a chat AI into a real phone automation agent.

**2. AI Staffing Agency — Phone Task Worker**
If businesses hire AI workers to handle customer service, being able to actually interact with a phone (make calls, send texts, check apps) is a massive unlock. mobile-use gives AI workers a hand — they can control a phone the same way a human would, just slower.

**3. Data Scraping from Apps**
No app has an API? No problem. "Open the Shopify app and give me last 10 orders" — mobile-use navigates the UI and extracts the data. Structured JSON output means it feeds directly into downstream tools.

**4. Hermes MCP Tool**
Hermes already has a skills registry. Adding mobile-use as an exposed tool means any agent in Solomon OS can dispatch phone tasks. "Call this person" or "read my notifications" becomes a first-class tool call.

**5. Solomon Air Phone Integration Layer**
If Solomon Air ever expands to mobile (as a node or client), mobile-use is the natural on-device execution layer. It already has the WiFi/NAT connectivity solved.

---

## Risks / Flags

- **Safety**: Granting an AI agent UI control over a phone is powerful and risky. Needs careful permission scoping (read-only vs. action modes).
- **iOS support**: macOS only for iOS physical devices — limits some use cases.
- **Speed**: UI automation is slow compared to API calls. Not suitable for high-frequency tasks.
- **Games don't work**: Apps without accessibility trees (games, some banking apps) are blind spots.
- **USB/WiFi requirement**: Device must be reachable on the same network or connected via ADB.

---

## Recommendation

**INTEGRATE — high value, especially for Russell Tuna + AI Staffing Agency.**

The AI staffing agency use case is the strongest. A phone-capable AI worker that can actually call clients, text leads, and check apps is far more valuable than a chat-only bot. mobile-use bridges the gap between "AI worker" and "does real phone tasks."

**Immediate next step:** Install mobile-use, connect to Joseph's Android device over WiFi, test a few commands (check notifications, open Gmail, list unread). If it works reliably, add to Russell Tuna's tool stack.

Priority: MEDIUM-HIGH — unlocks phone automation for the whole system.