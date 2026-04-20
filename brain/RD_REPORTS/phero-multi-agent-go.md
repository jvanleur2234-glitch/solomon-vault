# phero — Multi-Agent AI System (Go)

**Already cloned:** `/home/workspace/phero`
**Stars:** Unknown (v0.0.4, April 2026)
**License:** Apache 2.0
**Category:** agent-framework #multi-agent #go

## What It Is
Modern Go framework for building multi-agent AI systems with agent orchestration, role specialization, and runtime handoffs. A2A protocol, LLM abstraction, MCP support.

## Key Features
1. **Agent orchestration + handoffs** — Result.HandoffAgent for multi-agent workflows
2. **A2A (agent-to-agent) protocol** — expose agents as HTTP servers or invoke remote agents as tools
3. **Multi-LLM support** — OpenAI-compatible + Anthropic
4. **Tool-first design** — function tools, automatic JSON Schema, embedded RAG
5. **Memory management** — conversational context, vector stores (Qdrant, pgvector, Weaviate)
6. **Guardrails** — safe-mode, blocklist/allowlist, timeouts
7. **Tracing + observability**

## Key Patterns for Solomon OS
1. **A2A protocol** → maps to Solomon Bus inter-agent communication
2. **Agent handoffs** → how do agents transfer control? Study this pattern
3. **Built-in RAG** → memory layer for Hermes could use this
4. **Go-based** → single binary, type-safe, production-ready

## Verdict
**INTEGRATE** — Apache 2.0, Go, A2A protocol. The agent handoff pattern is directly applicable to Solomon Bus. Study for multi-agent Solomon OS architecture.

## Links
- https://github.com/henomis/phero