# gollem — Production Agent Framework for Go

**URL:** https://github.com/jvanleur2234-glitch/gollem
**Forked from:** https://github.com/fugue-labs/gollem
**License:** MIT | **Stars:** ~500+ | **Language:** Go

## What It Does
Type-safe Go agent framework with compile-time guarantees. Agents, tools, guardrails, middleware, streaming, multi-agent orchestration — all type-checked at compile time.

## Key Features
- Generic `Agent[T]` with automatic compile-time schema generation
- 5+ LLM providers (Anthropic, OpenAI, Google Gemini/Vertex)
- `FuncTool[P]` — typed tools from Go functions with reflection-based JSON Schema
- Streaming via `iter.Seq2` (Go 1.23+ range-over-function)
- Guardrails: input validation, turn limits, tool result validators, output auto-repair
- OpenTelemetry middleware, lifecycle hooks, conversation state snapshots
- Agent middleware chain, message/response interceptors
- Multi-agent team swarms with dynamic personality generation

## Solomon OS Fit
**SKILL** — Study compile-time type safety patterns for Hermes Go agents. The guardrail/middleware chain is directly applicable. Self-contained single-binary deployment aligns with Solomon Air goals. Not MIT-compatible enough for direct code use (Go-specific), but patterns are portable.

## Recommendation
SKILL — Study gollem's guardrail architecture and compile-time safety model for Hermes hardening.