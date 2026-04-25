# Gollem — Go Production Agent Framework (Apr 25, 2026)

**Fork:** `jvanleur2234-glitch/gollem-fresh` (MIT)
**Source:** https://github.com/fugue-labs/gollem

## What It Does
Go-based production agent framework:
- Type-safe agents with compile-time schema validation (Agent[T])
- 5+ LLM providers (Claude, OpenAI, Gemini)
- FuncTool with reflection-based JSON Schema
- Zero-allocation streaming via Go iterators
- Guardrails: input/turn/tool validators + auto-output repair
- OpenTelemetry middleware + time-travel state snapshots
- Zero core dependencies, single binary deployment

## Why It Matters for Solomon OS
- Go = single binary = perfect for edge/device deployment (Solomon Connect)
- Compile-time type safety prevents runtime errors in production agents
- Time-travel snapshots align with persistent agent state concept
- Zero-dependency model ideal for constrained environments

## Fit: SKILL
MIT licensed. Architecture study for Go-based Solomon OS components. Single-binary model is aspirational for edge deployment.

## Action Items
- [ ] Study compile-time schema validation pattern
- [ ] Evaluate Go port of core Hermes concepts for edge deployment
- [ ] Note: primarily reference architecture, not immediate integration target
