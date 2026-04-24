# RD Report: phero — Go Multi-Agent Framework

**Date:** 2026-04-23
**Repo:** github.com/henomis/phero
**License:** MIT (presumed)
**Forked:** Already in workspace ✅

## What It Is
Modern Go framework for building multi-agent AI systems. Emphasizes agent orchestration, role specialization, runtime handoffs with clean composable architecture. Active release v0.0.4 (April 2026).

## Key Capabilities
- **Agent orchestration and handoffs** (Result.HandoffAgent) for multi-agent workflows
- **A2A protocol** — expose/consume agents over HTTP
- **LLM abstraction** — OpenAI, Anthropic, Ollama compatible
- **MCP support** — Model Context Protocol servers
- **Memory management** — conversational context
- **Tool safety guards** — blocklist/allowlist, timeouts, safe mode
- **RAG built-in** — vector storage (Qdrant, pgvector, Weaviate) + semantic search
- **Skills system** — SKILL.md based like Hermes

## Relevance to Solomon OS / Hermes
- **A2A protocol** — potential interop with Hermes/Solomon Bus
- **Skills system** — identical SKILL.md pattern to Hermes — competitive reference
- **Go-based** — could inspire Go microservices in Solomon stack
- **MCP + RAG** — token-efficient retrieval pattern

## Verdict
**RESEARCH** — Good reference for A2A agent protocol and skills system. Hermes has MCP client; phero has A2A which could complement. Watch for convergence potential.

---
**Priority:** 🟡 Worthwhile
**Category:** Agent Framework / Multi-Agent / A2A Protocol