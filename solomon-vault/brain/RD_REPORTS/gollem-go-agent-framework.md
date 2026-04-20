# Gollem — Go Agent Framework — RD Report

## Summary
**Repo:** `fugue-labs/gollem`  
**License:** Apache 2.0  
**Stars:** ~1K+ (estimated)  
**Language:** Go  

## What It Does
Production-grade Go agent framework focused on type safety and zero-core dependencies:
- **Type-safe agents:** Generic `Agent[T]` with compile-time output schema generation
- **Multi-provider streaming:** 5+ LLM providers (Anthropic, OpenAI, Gemini, Vertex, etc.)
- **Guardrails:** MaxPromptLength, ContentFilter, MaxTurns, per-tool validators
- **Output repair:** Auto-repair of malformed outputs before retries
- **Observability:** OpenTelemetry integration, lifecycle hooks, state snapshots
- **Middleware chain:** Logging, Timing, MaxTokens, custom message interceptors
- **Streaming:** Real-time token streaming via Go 1.23+ iterators

## For Solomon OS / Hermes
- **Go runtime:** Complements Python/TypeScript agent ecosystems — potential for high-performance Go-based agent nodes
- **Type safety:** Strong compile-time guarantees — could inspire Hermes Go skill development
- **Guardrails:** Well-implemented validation layer — good reference for Guardian input/output filtering
- **Recommendation:** SKILL — watch for ecosystem maturity

## Priority: 🟡 Worthwhile
