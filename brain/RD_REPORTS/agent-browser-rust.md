# RD Report: vercel-labs/agent-browser

**Already Forked:** jvanleur2234-glitch/agent-browser  
**License:** Apache-2.0 | **Language:** Rust  
**Date:** 2026-04-24

## What It Is
Fast, native Rust CLI to automate browser actions for AI agents. Enables end-to-end web interactions via a scriptable command interface with snapshot/ref system.

## Relevance to Solomon OS
- Browser automation for AI agents
- Fast, native execution (no Node.js/Playwright dependency)
- Scriptable browser control for autonomous web tasks
- Accessibility tree with element refs for reliable interaction

## Key Capabilities
- Open, click, fill, type, screenshot, scroll
- Snapshot to get accessibility tree with refs (@e1, @e2)
- Click/fill by refs for reliable interaction
- Chrome auto-download on install
- No Playwright or Node.js required for daemon

## Competitive Analysis
ClawLess competitor. Native Rust = faster than Node-based alternatives. Already forked to jvanleur2234-glitch.

## Recommendation
**SKILL** — Install as Hermes browser automation skill. Compare with existing ClawLess implementation.

## License Check
Apache-2.0 ✅