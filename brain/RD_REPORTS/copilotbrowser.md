# RD Report: CopilotBrowser — Multi-Browser AI Automation

## Metadata
- **Repo:** dayour/copilotbrowser
- **URL:** https://github.com/dayour/copilotbrowser
- **Stars:** ~1 (nascent, March 2026)
- **License:** Apache 2.0
- **Language:** TypeScript
- **Forked:** Already cloned at `/home/workspace/copilotbrowser`
- **Date:** 2026-04-22

---

## What It Does
A Node.js-based, multi-browser automation framework that unifies Chromium, Firefox, and WebKit control via a single API. Ships with an MCP server that lets AI agents (GitHub Copilot, Claude, any MCP client) drive a real browser. Signature feature: **"Follow Me" mode** — records user browsing path and replays exact steps autonomously (forms, multi-step flows, complex UI interactions).

### Key Features
- Single API for Chromium, Firefox, WebKit
- MCP server for AI-agent browser control
- Follow Me mode: agent watches user → replays exact actions autonomously
- Optional capability packs: vision (screenshot), pdf (save as PDF), devtools
- 32+ browser actions: navigate, click, type, screenshot, fill forms, run JS, manage tabs, dialogs
- VS Code extension auto-registers MCP server
- Cross-platform: Windows, macOS, Linux

---

## Solomon OS Fit

### Comparison to Existing Tools
| Feature | CopilotBrowser | Browser-Use | Vibium | HyperAgent |
|---------|---------------|-------------|--------|------------|
| Multi-browser | ✅ (3) | Python-only | Go/Cross | Playwright |
| MCP server | ✅ (native) | ❌ | ✅ | ✅ |
| Follow Me recording | ✅ (novel) | ❌ | ❌ | ❌ |
| VS Code extension | ✅ | ❌ | ❌ | ❌ |
| Stars | ~1 | 1,000+ | 2,700+ | 1,200+ |

### Use Cases for Hermes
1. **Skill recording workflow** — Use "Follow Me" mode to record complex browser tasks as reusable skills
2. **Cross-browser testing** — Run same skill across Chromium/Firefox/WebKit to verify consistency
3. **MCP integration** — Claude Desktop / VS Code agent can directly control browser via copilotbrowser MCP

### Risk Assessment
- **License:** Apache 2.0 — ✅ Compatible with JCPaid
- **Security:** No obvious sandboxing; follows same trust model as other browser automation tools
- **Maintenance:** Very new (1 star), single contributor — monitor for adoption

---

## Recommendation
**SKILL** — The "Follow Me" recording pattern is novel and directly applicable to Hermes skill creation. Could record browser-based workflows hands-free and auto-generate skill definitions. Watch for community adoption before elevating priority.

---

*RD Report — AIQ Scout — 2026-04-22*