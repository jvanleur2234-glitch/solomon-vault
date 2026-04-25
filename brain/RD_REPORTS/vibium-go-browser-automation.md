# Vibium — Go Browser Automation Framework (Apr 25, 2026)

**Fork:** `jvanleur2234-glitch/vibium` (Apache 2.0)
**Source:** https://github.com/VibiumDev/vibium

## What It Does
Go-based browser automation:
- WebDriver BiDi standard (not proprietary)
- Zero-config, ~10MB binary
- MCP server option
- JS/Python/Java library wrappers
- Semantic element finding (text, label, placeholder, ARIA role)
- Session recording, screenshot, PDF export
- Form automation (fill, select, check, key press)

## Why It Matters for Solomon OS
- WebDriver BiDi = standards-based, vendor-neutral
- Go binary = could compile to WASM or edge device
- MCP server option = direct Hermes integration path
- Lightweight vs Playwright for simple automation tasks

## Fit: SKILL
Apache 2.0. Vibium MCP mode could replace or complement ClawLess browser automation in Hermes. Study for browser skill layer.

## Action Items
- [ ] Evaluate as lighter-weight alternative to Playwright-based browser tools
- [ ] Test MCP server mode for Hermes integration
- [ ] Compare with existing agent-browser (Rust) implementation
