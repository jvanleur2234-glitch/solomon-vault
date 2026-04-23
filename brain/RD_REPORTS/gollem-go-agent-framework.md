# Gollem — Type-Safe Go Agent Framework

**Source:** https://github.com/fugue-labs/gollem  
**License:** Apache 2.0  
**Stars:** ~700+  
**Date:** 2026-04-23

## What it does
Gollem is a production-ready agent framework for Go that emphasizes compile-time type safety, zero-allocation streaming, and a single-binary deployment model. It aims to prevent common runtime errors by validating schemas, tool parameters, and guardrails at compile time.

Key features:
- Type-safe agents with generics (Agent[T]) and automatic compile-time schema generation/validation
- Multi-provider support (5+ LLMs: Anthropic Claude, OpenAI GPT/O-series, Google Gemini/Vertex AI)
- Structured, reliable output via final_result pattern and robust streaming (iter.Seq2)
- Comprehensive guardrails (input/turn constraints, tool output validators, auto-repair)
- Observability & tracing (structured run traces, OpenTelemetry middleware, state snapshots)
- 50+ primitives, guardrail configurations, multi-agent orchestration
- Zero core dependencies

## Solomon OS Fit
**SKILL** — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements. No direct use (different language), but architecture study valuable.

## Key Components
- `Agent[T]` generic type system
- `FuncTool[P]` with reflection-based JSON Schema
- Guardrail system with auto-repair
- OpenTelemetry middleware
- Multi-agent team orchestration

## Recommendation
SKILL — Study compile-time safety patterns. Valuable for understanding how to build more robust agent frameworks.