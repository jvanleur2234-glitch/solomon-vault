# firmis — AI Runtime Security Scanner (Firmislabs)

## What It Is
AI-first security scanner for AI agents, LLM apps, MCP servers. Detects credential harvesting, prompt injection, tool poisoning, and 18 other threat categories.

## Key Signals
- **License:** MIT
- **Lang:** TypeScript
- **Fork:** https://github.com/jvanleur2234-glitch/firmis-scanner

## Core Features
- Platform coverage: Claude Skills, MCP servers (Claude Code, Cursor), Codex plugins
- 268 detection rules, zero-config setup
- Scans both code surface (filesystem, network, shell) AND instruction surface (SKILL.md, AGENTS.md, tool descriptions)
- Auto-detects agent frameworks: LangChain, CrewAI, AutoGen, MetaGPT, AutoGPT, LangFlow, n8n
- Zero-install scan: `npx firmis-cli scan`

## Solomon OS Fit
- **INTEGRATE** — MIT license. Pre-execution security gate for Hermes skills. SKILL.md/AGENTS.md scanning maps directly to our vulnerability surface.
- OWASP ASI alignment for compliance

## Recommendation
INTEGRATE — Core security primitive. Add to Hermes skill pre-execution pipeline alongside ProofLayer.