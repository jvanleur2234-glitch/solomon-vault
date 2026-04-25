# RD Report: Gollem — Compile-Time Safe Go Agent Framework

**Fork:** `jvanleur2234-glitch/gollem-fresh` | **Original:** `fugue-labs/gollem` | **License:** MIT | **Stars:** ~500 | **Lang:** Go

## What It Is
Production-grade Go agent framework with compile-time type safety, zero-allocation streaming, and single-binary deployment. Built for agents that need end-to-end type-checked outputs, tool parameters, guardrails, and middleware.

## Key Capabilities
- `Generic Agent[T]` with automatic compile-time schema generation and validation
- Typed `FuncTool[P]` from Go functions with struct-tag-derived schemas
- 5+ LLM providers: Anthropic Claude, OpenAI GPT, Google Gemini, Vertex AI
- Guardrails: `MaxPromptLength`, `ContentFilter`, `MaxTurns`, tool result validators
- Middleware chain: Logging, Timing, MaxTokens + custom interceptors
- OpenTelemetry tracing and conversation state snapshots for time-travel debugging
- Streaming via Go 1.23+ `iter.Seq2`

## Relevance to Solomon OS
- **Security:** Strong compile-time guarantees prevent runtime prompt injection
- **Skill Framework:** Typed tools can be packaged as Hermite skills
- **Go-native:** Could power high-performance agent nodes in distributed compute mesh

## Threat Analysis
- MIT licensed, no known vulnerabilities
- Active small team, recent releases

## Integration Path
```
SKILL: gollem → wraps Go agent as Hermite tool
USE CASE: High-performance agent nodes, security-critical workloads
```

**Recommendation:** SKILL — Fork for Go agent tooling integration.
