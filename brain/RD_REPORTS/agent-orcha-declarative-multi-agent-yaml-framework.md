# agent-orcha — Declarative Multi-Agent YAML Framework

## SLUG: agent-orcha
## Date: 2026-04-26
## Tags: #agent-framework #multi-agent #yaml #orchestration #p2p #MIT
## Status: FORGE

---

## What It Is
`agent-orcha` (ddalcu/agent-orcha) is a TypeScript-first declarative multi-agent AI framework that defines agents, workflows, and knowledge stores in YAML. Supports parallelism, conditional logic, state management, and P2P encrypted sharing of agents.

## Key Capabilities
- **YAML-driven orchestration**: define entire agent ecosystems in YAML configs
- **Model-agnostic**: OpenAI, Gemini, Anthropic, Ollama, LM Studio
- **Built-in vector store (SQLite)** + knowledge graphs
- **P2P encrypted sharing**: share agents/LLMs without central keys
- **Security**: rate limiting, SSRP protection, SQL injection hardening, sandboxed execution
- **Browser sandbox**: Chrome CDP, noVNC, vision-enabled
- **MIT License** — v2026.409 (Apr 2026)

## Relevance to Solomon OS / Hermes
- Declarative YAML config aligns with Hermes skill format
- P2P agent sharing is competitive with AgentFM / distributed compute
- Built-in security features (SSRF protection) are directly relevant to AgentArmor

## Recommendation
**FORGE** — fork for skill ecosystem, P2P compute layer, and declarative orchestration patterns.
