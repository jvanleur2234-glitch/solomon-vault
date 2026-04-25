# gollem — Type-Safe Go Agent Framework

**URL:** https://github.com/fugue-labs/gollem
**Forked:** Already in workspace (/home/workspace/gollem) — Go project, different tech stack from Hermes
**License:** MIT

## What It Does
Production-grade Go agent framework with compile-time type safety for agent outputs, tool parameters, guardrails, middleware, and event subscriptions. Zero core dependencies, single-binary deployment.

## Key Features
- Generic `Agent[T]` with automatic schema generation/validation
- 5+ LLM providers (Anthropic, OpenAI, Google Gemini, Vertex AI)
- `FuncTool[P]` with JSON Schema generation from Go structs
- Streaming via Go 1.23+ iter.Seq2
- Guardrails: input validation, turn limits, output validators, auto-repair
- OpenTelemetry middleware with lifecycle hooks
- State snapshots for time-travel debugging
- 561+ tests, active CI

## Why It Matters
Go's type system provides compile-time guarantees that Python frameworks can't. Entire categories of bugs (ValidationError, TypeError) are eliminated before code ever runs. The middleware architecture and guardrail patterns are production-proven.

## Solomon OS Fit
**MONITOR / REFERENCE** — Different tech stack (Go vs Python), but guardrail patterns, middleware chain architecture, and type-safe tool design are worth studying for future Go-based Hermes components. Already in workspace for reference.

## License
MIT

## RD Report
/home/workspace/gollem/