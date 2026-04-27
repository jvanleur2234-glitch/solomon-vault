# Gollem — Production Agent Framework for Go (Apr 27, 2026)

**Fork:** `jvanleur2234-glitch/gollem-fresh` (MIT)
**Source:** https://github.com/fugue-labs/gollem

## What It Does
Production-grade Go agent framework with compile-time type safety and zero core dependencies.

**Key features:**
- Generic `Agent[T]` with compile-time output schema validation
- 5+ LLM providers (Anthropic, OpenAI, Google Gemini, Vertex AI)
- `FuncTool[P]` — tools from typed Go functions with reflection-based JSON Schema
- Streaming via Go 1.23+ `iter.Seq2`
- Guardrails: input validation, turn limits, tool result validators, output auto-repair
- OpenTelemetry middleware + structured run traces
- Agent middleware chains (Logging, Timing, MaxTokens)

## Why It Matters for Solomon OS
- Go = single binary deployment, no runtime errors — fits JCPaid infrastructure needs
- Compile-time type safety eliminates Python-class runtime bugs in production
- Multi-provider routing matches Hermes model-agnostic design

## Fit: INTEGRATE
MIT licensed. Good architectural reference for Go-based Hermes tools or standalone agents. 561+ tests, active development (v0.3.1 March 2026).

## Action Items
- [ ] Already forked — confirm gollem-fresh is current
- [ ] Study guardrail implementation for Hermes security layer
