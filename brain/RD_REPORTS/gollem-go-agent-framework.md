# RD Report: Gollem — Production Go Agent Framework

**Repo:** https://github.com/fugue-labs/gollem
**Fork:** jvanleur2234-glitch/gollem
**License:** MIT
**Stars:** ~500+ (active, v0.3.1 Mar 2026)
**Language:** Go

## What It Is
Production-grade agent framework for Go with compile-time type safety, zero-allocation streaming, and single-binary deployment. Type-safe agents with auto-generated validated output schemas, multi-provider streaming (Anthropic, OpenAI, Google, etc.), and tool integration via FuncTool with reflection-based JSON Schema.

## Key Features
- Generic `Agent[T]` with compile-time output schema validation
- 5+ LLM providers (Claude, GPT, Gemini, Vertex AI)
- FuncTool[P] — tools from typed Go functions
- Streaming via Go 1.23+ iter.Seq2
- Guardrails: input/turn/tool validators, output auto-repair
- OpenTelemetry middleware + structured run traces
- Agent middleware chains with LoggingMiddleware, TimingMiddleware
- Multi-agent team swarms with dynamic personalities
- 561+ tests, MIT licensed

## Solomon OS Fit
**Security & Resilience pillar — agent orchestration layer.** Go's type safety means fewer runtime crashes in production agents. Single-binary deployment fits Solomon OS self-hosted model. Compile-time guarantees prevent the class of bugs that plague Python agent frameworks.

## Comparison to What We Have
vs. **PraisonAI** (Python): Python is more accessible but runtime errors are common. Gollem's type safety is superior for production hardening.
vs. **agent-framework** (Microsoft, Python/.NET): More mature but Python/.NET vs Go. Gollem fills a gap if we ever want a Go-based agent runtime.

## Recommendation: SKILL
Create a `gollem` skill for Go-based agent deployments. Particularly valuable for security-critical production agents where Python runtime errors are unacceptable. Monitor for Solomon OS integration potential.
