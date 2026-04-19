# R&D Report: Browser Harness

**Date:** April 18, 2026
**Repo:** github.com/browser-use/browser-harness (309 stars, MIT)
**Forked:** github.com/jvanleur2234-glitch/browser-harness

---

## What It Is

Self-healing browser harness. LLM encounters a missing function → writes it mid-task directly into helpers.py. Built on CDP (Chrome DevTools Protocol). ~592 lines of Python total. No framework, no rails, one WebSocket to Chrome.

## What It Does

- Connects to user's already-running Chrome via remote debugging
- Agent gets a `helpers.py` with ~195 lines of starting tools (goto, click, screenshot, js, etc.)
- When a tool is missing, the agent writes it into helpers.py mid-task and immediately uses it
- Domain skills: teach the agent site-specific selectors, APIs, and flows (PRs welcome)
- Free remote browsers: cloud.browser-use.com (3 concurrent, no card)
- Architecture: Chrome → CDP WS → daemon.py → socket → run.py

## Why It's Critical for JCPaid

Solomon Browser needs exactly this self-healing capability. Instead of writing "I can't click that" when a function doesn't exist, the agent writes the function and keeps going.

**Key insight from the README:** "You will never use the browser again."

## How It Compares to What We Have

| Capability | Before Browser Harness | After Browser Harness |
|---|---|---|
| Self-healing browser | ❌ | ✅ Agent writes missing functions |
| DOM access | Basic | ✅ CDP-level (raw Chrome) |
| Domain-specific knowledge | ❌ | ✅ domain-skills/ (LinkedIn, Amazon, etc.) |
| Remote browsers | ❌ | ✅ Free tier: 3 concurrent |
| Agent learning | ❌ | ✅ Contributes back what it learns |

## What We'd Use It For

1. **Solomon Browser core** — Replace our basic browser with self-healing CDP harness
2. **Web scraping at scale** — Browser harness + Ollama = autonomous scraper
3. **Business intelligence** — Monitor competitor prices, job boards, lead lists
4. **Cross-browser testing** — QA Solomon OS web apps

## Recommendation

**🔥 FORGE — INTEGRATE INTO SOLOMON BROWSER**

Forked. MIT license = commercial use. Self-healing is the missing piece. Integrate into our browser layer immediately.

**Priority:** HIGH
**Effort:** Low-Medium (1-2 weeks to integrate)
**License:** MIT — fully commercial
