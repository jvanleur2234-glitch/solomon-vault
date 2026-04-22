# RD Report: Agent Express — Express.js-Style Agent Framework

**Date:** 2026-04-22
**URL:** https://github.com/agent-express-ai/agent-express
**License:** MIT
**Fork:** https://github.com/jvanleur2234-glitch/agent-express

---

## What It Is
Minimalist, middleware-based AI agent framework in TypeScript. Applies Express.js `(ctx, next)` pattern to AI agent orchestration. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, multi-provider routing (12+), memory management, and MCP integration.

---

## Key Capabilities
- Middleware architecture: 5 hooks (agent/session/turn/model/tool), standard `(ctx, next)` flow
- Safety: budget guards, I/O validation, timeouts, iteration limits, HITL approval
- Observability: OpenTelemetry metrics/traces, token tracking, tool recording
- Multi-provider: Anthropic, OpenAI, Google, Mistral, Groq, Cerebras, Ollama, etc.
- Model routing: cross-provider decisions based on cost/latency/quality
- Memory: context window compaction (multiple strategies)
- MCP: connect MCP servers as tool sources
- Testing: TestModel, FunctionModel, capture, record/replay, snapshots
- Structured output: Zod schema validation on model responses

---

## Why It Matters
Express.js middleware is the most proven async composition pattern in server-side JS. Applying it to agents gives a clean, predictable way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. Contrast with AutoGen/CrewAI which use class inheritance.

---

## Solomon OS Fit
- **SKILL** — Middleware pattern directly maps to Hermes skill pipeline. Study for skill composition architecture.
- MIT license — can integrate patterns directly.

---

## Comparison
| Aspect | Agent Express | AutoGen | CrewAI |
|--------|--------------|---------|--------|
| Style | Middleware (ctx/next) | Message passing | Role-based |
| Safety | Built-in guards | Minimal | Minimal |
| Providers | 12+ | 4 | 4 |
| MCP | Native | Via tools | Via tools |
| License | MIT | MIT | Apache |

---

## Recommendation
**SKILL** — Study middleware composition pattern for Hermes skill pipeline.