# Gollem — Production-Grade Go Agent Framework

**No fork needed** (local study)
**URL:** https://github.com/fugue-labs/gollem
**Stars:** ~200+ | **License:** MIT | **Lang:** Go

## What It Is
A production-grade Go agent framework with compile-time type safety, zero-allocation streaming, and single-binary deployment. Built by fugue-labs for teams wanting typed, observable, multi-provider AI agents in Go.

## Key Features
- **Generic Agent[T]** — compile-time schema generation, validation, deserialization
- **5+ LLM providers** — OpenAI GPT, Claude, Gemini/Vertex AI with streaming via Go iterators
- **Guardrails** — input/turn guardrails, tool result validators, output auto-repair
- **Observability** — Full run traces, OpenTelemetry middleware, lifecycle hooks, conversation snapshots
- **Middleware chain** — Logging, Timing, MaxTokens built-ins + custom interceptors
- **FuncTool[P]** — reflection-based JSON Schema from typed Go functions
- **Zero core dependencies** — single binary, compile-time guarantees

## Why It Matters for Solomon OS
- Go = perfect for Hermes backend services that need type safety + performance
- Single-binary = trivial deployment in Solomon Air containers
- OpenTelemetry = direct integration with Solomon OS observability
- Type-safe agents = fewer runtime errors in critical paths

## Solomon OS Fit
**STUDY** — Architecture patterns for Hermes Go services. Compile-time type safety for mission-critical agent code. Middleware chain model for Hermes request pipeline.

## SWARM Score
⭐⭐⭐ (MIT, active, Go = high value for Solomon Air backend)
