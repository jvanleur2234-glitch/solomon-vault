# CopilotBrowser — Unified Multi-Browser AI Agent Framework

**Fork**: `dayour/copilotbrowser` → no existing fork in workspace
**License**: Apache-2.0
**Stars**: New (v2.0.0, Mar 2026)
**Language**: TypeScript

## What It Is

High-level Node.js browser automation framework that unifies Chromium, Firefox, and WebKit under a single API. Ships with a built-in MCP server so AI agents (GitHub Copilot, Claude) can directly control a real browser.

## Key Features

- **Unified browser support**: Chromium 146, Firefox 146, WebKit 26
- **Follow-me mode**: AI observes user navigation → autonomously replays actions (form fills, multi-step flows)
- **MCP server**: 32+ browser tools exposed (navigate, click, type, screenshot, observe, fill forms, run JS, tabs, record)
- **Capability packs**: vision (screenshot reasoning), pdf (save as PDF), devtools (CDP access)
- **Requirements**: Node.js >= 25.6.1

## Relevance to Solomon OS

- **Browser automation**: Directly competes with ClawLess, HyperAgent, browser-use
- **MCP integration**: Deepens Hermes-style skill ecosystem
- **Follow-me mode**: Interesting for creating agentic workflows from human demonstrations

## Verdict

🟡 SKILL — Good for browser-based agent workflows. Clone, analyze "follow-me" mode implementation, potentially integrate as a Hermes skill.

**Action**: Read the MCP server implementation for browser tool exposure patterns.