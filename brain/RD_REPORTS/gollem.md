# gollem — Type-Safe Go Agent Framework

## Metadata
- **URL:** https://github.com/fugue-labs/gollem
- **Fork:** Already forked (`gollem`)
- **License:** MIT
- **Tech:** Go, v0.3.1

## What It Does
Production-grade Go agent framework with compile-time type safety. Generic Agent[T], 5+ LLM backends, FuncTool with JSON Schema generation, streaming via iter.Seq2, guardrails (input/turn/output validation, auto-repair), OpenTelemetry middleware, state snapshots.

## Key Features
- **Compile-time guarantees:** Output schemas, tool parameters, guardrails, middleware, event subscriptions
- **Multi-provider:** Anthropic Claude, OpenAI GPT/O-series, Google Gemini, Vertex AI
- **Streaming:** Go 1.23+ iterators, node-by-node agent looping
- **Guardrails:** MaxPromptLength, ContentFilter, MaxTurns, tool result validators
- **Observability:** OpenTelemetry traces, JSONFileExporter, ConsoleExporter

## Solomon OS Fit
- **MONITOR / REFERENCE** — Architecture study for Hermes 2.0 type-safe patterns
- Guardrail patterns and middleware architecture useful for Hermes security layer
- Go-based components could complement Python Hermes
- MIT license for architecture study

## Action
Already forked. Study middleware patterns for Hermes security middleware.