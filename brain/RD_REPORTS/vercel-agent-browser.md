# RD Report: Vercel Agent Browser — Fast Rust Browser Automation

**Fork:** `jvanleur2234-glitch/vercel-agent-browser` | **Original:** `vercel-labs/agent-browser` | **License:** Apache 2.0 | **Stars:** ~2.5K | **Lang:** Rust

## What It Is
Fast native Rust CLI for browser automation designed for AI agents. Controls Chrome/Chromium programmatically. Zero Python/Node dependency for the core daemon.

## Key Capabilities
- Navigation, click, dblclick, hover, type, fill, press keys
- Snapshot/inspection: accessibility tree + element refs
- Screenshot capture
- CSS + role-based selectors
- Tab management, form/element manipulation
- Global install: `npm install -g agent-browser`
- Works with existing Chrome/Brave/Playwright/Puppeteer

## Relevance to Solomon OS
- **Browser Automation:** ClawLess competitor
- **Performance:** Rust-based = fastest browser automation for agents
- **Hermes Integration:** Could replace Playwright-based browser tools

## Threat Analysis
- Apache 2.0 licensed, Vercel Labs backing
- Actively maintained (v0.26.0)

## Integration Path
```
TOOL: agent-browser → Rust-based browser automation for Hermes
USE CASE: Fast, reliable web browsing for agent tasks
```

**Recommendation:** INTEGRATE — Fork as high-performance browser automation skill for Hermes. Vercel backing = credible.
