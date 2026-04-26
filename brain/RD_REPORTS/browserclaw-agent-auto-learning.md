# browserclaw-agent — AI Agent Browser Automation with Learning

## SLUG: browserclaw-agent
## Date: 2026-04-26
## Tags: #browser-automation #agent #anti-bot #MCP #learning #MIT
## Status: FORGE

---

## What It Is
idan-rubin/browserclaw-agent is a modular AI agent that automates web browser tasks using snapshot→LLM→action→repeat loop. Built-in skills handle anti-bot bypass (Cloudflare Turnstile), popup dismissal, loop detection, and tab management.

## Key Capabilities
- **Snapshot-based page understanding**: semantic structured page models
- **Built-in anti-bot handling**: Cloudflare Turnstile, hold-to-verify, etc.
- **Domain-specific skill files**: Playbooks stored in MinIO, learned per domain
- **MCP server compatibility**: Claude Code, LangChain integration
- **Multi-LLM support**: Claude, GPT, Gemini, local models
- **MIT License** — TypeScript

## Relevance to Solomon OS / Hermes
- Learning playbooks per domain is innovative — improves over time
- Anti-bot handling directly applicable to web scraping capabilities
- MCP compatibility fits Hermes MCP tool ecosystem

## Recommendation
**FORGE** — study skill/playbook learning mechanism for Hermes autonomous improvement.
