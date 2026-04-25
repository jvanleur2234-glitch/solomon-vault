# RD Report: Vibium — Standards-Based Browser Automation for AI Agents

**Date:** 2026-04-25
**Repo:** VibiumDev/vibium
**Fork:** jvanleur2234-glitch/vibium
**License:** Apache 2.0
**Stars:** 2,784
**Category:** Browser Automation / AI Agent

## What It Is
Lightweight browser automation framework (~10MB binary) using WebDriver BiDi standard. AI-native: install as Hermes skill. Zero-config browser download. Semantic element mapping (no CSS selectors needed), screenshot capture, PDF export.

## Key Features
- WebDriver BiDi (not proprietary) — standards-based
- ~10MB binary, zero-config setup
- Semantic element finding (text/labels/placeholders/ARIA)
- Session recording + replay
- MCP server + CLI + JS/Python/Java libraries
- Screenshot capture with annotations
- PDF export
- Apache 2.0 licensed

## For Solomon OS
- **Use for:** Browser automation skill. One of 3 good options (with Magnitude + agent-browser).
- **Advantage:** Standards-based (WebDriver BiDi) means better longevity and cross-tool compatibility.
- **Install as skill:** `npm install -g vibium; npx skills add https://github.com/VibiumDev/vibium`

## Comparison with Alternatives
| Feature | Vibium | Magnitude | agent-browser |
|---------|--------|-----------|---------------|
| Approach | WebDriver BiDi | Vision | Rust CLI |
| Size | ~10MB | Node.js | Rust binary |
| Mobile | Yes | Yes | No |
| License | Apache 2.0 | Apache 2.0 | Apache 2.0 |
| Stars | 2,784 | 4,026 | 30,517 |

## LINK Tags
`#browser-automation` `#webdriver-bidi` `#standards-based` `#mcp-server` `#semantic`

## Recommendation
**INTEGRATE** — Already forked. WebDriver BiDi standard makes it the most standards-compliant option. Install as Hermes MCP skill.