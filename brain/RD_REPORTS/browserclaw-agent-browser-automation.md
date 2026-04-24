# RD Report: idan-rubin/browserclaw.agent

**Fork:** Already forked
**Source:** https://github.com/idan-rubin/browserclaw.agent
**Stars:** ~500+ | **License:** MIT | **Language:** TypeScript
**Date:** 2026-04-24

## What It Is
AI-driven browser automation conductor. Acts as the agent layer, using an LLM to decide actions from page snapshots and execute them in the browser. Works with any LLM (Claude, GPT, Gemini, local). Designed as a modular stack (LLM layer → agent → browser vehicle).

## Key Capabilities
- Anti-bot bypass (hold-to-verify, press-and-hold via CDP)
- Cloudflare Turnstile solving via CDP
- Popup/dialog auto-dismissal (cookie banners, modals)
- Loop detection
- Tab management
- **Skill system:** Domain-specific skill files (playbooks) stored in MinIO
- Self-improving: first run explores, subsequent runs reuse skills
- Built-in recovery from failures

## Architecture (3 layers)
1. **LLM layer** — your choice of model
2. **Agent layer** — this project (reasoning, recovery, built-in skills)
3. **BrowserClaw** — browser control and element references

## Relevance to Solomon OS
- **Browser automation:** ClawLess competitor with MIT license
- **Self-improving:** Skills improve across runs — maps to Hermes learning
- **Anti-bot:** Could enable real web scraping for research tasks
- **MIT:** Commercial use permitted

## Recommendation
**SKILL** — Study skill/playbook system for browser automation. Anti-bot bypass could enable real web research. Could enhance Hermes web capabilities.

## License Check
MIT ✅