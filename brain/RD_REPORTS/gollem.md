# RD Report: Gollem — Go Agent Framework

**Repo:** `fugue-labs/gollem` | **Stars:** ~700+ | **License:** MIT | **Updated:** Apr 2026

## What It Is
Production-grade Go agent framework with compile-time type safety. Targets complex multi-provider agent pipelines with strong guardrails and observability.

## Core Value for Solomon OS
- **Compile-time guarantees** — schemas, validation, deserialization all checked by Go compiler before runtime. Eliminates entire failure categories Python frameworks can't.
- **Type-safe agents** with generic `Agent[T]` and structured output via `final_result` pattern
- **5+ LLM backends** — Anthropic, OpenAI, Gemini, Vertex AI
- **Guardrails** — input/turn validation, content filtering, max prompt length, tool output validators, output auto-repair
- **Observability** — OpenTelemetry middleware, structured run traces, state snapshots for time-travel debugging
- **Zero core dependencies** — single binary deployment
- MIT licensed ✓

## Security Relevance
Guardrails system, middleware chain, content filtering, output validators directly applicable to Hermes security layer. Aligns with AgentArmor/Stelios ecosystem.

## Integration Potential
- **SKILL:** Go agent with type-safe tools → could install as Hermes skill
- **Guardrail patterns** → adapt for Hermes guard-scanner integration
- **Middleware architecture** → useful reference for Hermes plugin system

## Comparison
vs Python frameworks (LangChain, Agno, CrewAI): compile-time safety, zero-allocation streaming, single binary. Significant production reliability advantage.

## Verdict: **INTEGRATE / SKILL**
- Fork: NO (Go project, different tech stack from Hermes)
- RD tracking: YES
- Hermes skill potential: YES (Go agents as external tools via MCP bridge)