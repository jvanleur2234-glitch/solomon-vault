# RD Report: gollem — Production-Grade Go Agent Framework

**Date:** 2026-04-25  
**Category:** Agent Framework  
**Status:** SKILL  

## What It Is

A production-grade agent framework for Go with compile-time type safety, zero-allocation streaming, and a single-binary deployment. Aims to prevent runtime type errors common in Python-based frameworks.

## Key Features

- **Compile-time type safety:** Generic `Agent[T]` with automatic compile-time schema generation, validation, deserialization
- **5+ LLM providers:** Anthropic Claude, OpenAI GPT/O-series, Google Gemini/Vertex AI, Claude via Vertex AI
- **FuncTool[P]:** Auto-generates JSON Schemas from typed Go functions
- **Structured output patterns:** `final_result` and streaming via `iter.Seq2`
- **Guardrails:** Input/turn validation, tool result validators, output auto-repair
- **Observability:** Structured run traces, OpenTelemetry middleware, state snapshots
- **Middleware:** Customizable middleware chain (Logging, Timing, MaxTokens)
- **Message interceptors**

## License

MIT

## Why It Matters for Solomon OS

- **Compile-time guarantees:** Prevents runtime type errors (Python-style ValidationError/TypeError) — relevant for Hermes reliability
- **Single-binary deployment:** Zero-dependency Go binary fits distributed compute nodes
- **Guardrails pattern:** Input/turn/output validation maps to Hermes security layer
- **OpenTelemetry:** Native observability aligns with Solomon OS monitoring

## Source

- https://github.com/fugue-labs/gollem
- v0.3.1 (March 2026), MIT license