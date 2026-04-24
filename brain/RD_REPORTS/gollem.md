# RD Report: gollem

**Fork Status:** Already forked  
**License:** MIT  
**Stars:** ~120 (Go agent framework, v0.3.1 released Feb 2026)  
**Relevance:** MEDIUM — typed agent construction, guardrails, observability

## What It Is
Production-grade agent framework for Go emphasizing compile-time safety and zero-core dependencies. Strong type guarantees and structured outputs.

## Key Capabilities
- Type safety: generic Agent[T] with automatic schema generation, validation, deserialization at compile time
- Multi-provider support: Anthropic Claude, OpenAI GPT/O-series, Google Gemini, Vertex AI
- Streaming: real-time token streaming via iter.Seq2, node-by-node iteration
- Tools and guardrails: FuncTool[P] auto-generates tool schemas, input/turn guardrails, output validators
- Observability: full structured run traces, OpenTelemetry middleware, time-travel debugging

## Relevance to Hermes/Solomon
- Type-safe patterns could inform Hermes's tool schema generation
- Guardrail implementations relevant to Solomon OS security scanner capabilities
- Compile-time safety aligns with Solomon OS reliability goals

## Integration Recommendation
**INTEGRATE** — Study gollem's guardrail patterns and type-safe tool schemas. Could inform AgentArmor Studio's security layer design.

## Notes
- MIT licensed
- Single top contributor (trevorprater)
- Zero-core-dependency Go deployment