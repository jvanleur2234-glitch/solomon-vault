# RD Report: Gollem

**Date:** 2026-04-24  
**Slug:** gollem  
**Tags:** #agent-framework #go #type-safety #compile-time  

## What It Is
Production-grade Go agent framework focused on type safety and zero-dependency deployment. Compile-time guarantees for agent outputs, tool schemas, guardrails, and middleware.

## Relevance to Solomon OS / Hermes
- **Go ecosystem** — potential for high-performance agent components
- **Type safety** — compile-time validation aligns with Hermes security-first approach
- **Single-binary deployment** — resource-efficient edge deployment
- **Observability** — OpenTelemetry middleware, structured run traces
- **Guardrails** — input/turn guardrails, MaxPromptLength, ContentFilter, MaxTurns

## License
MIT

## Stars
Niche but active — trevorprater sole contributor

## Key Capabilities
- Type safety at compile time: Generics-Driven Agent[T]
- Multi-provider streaming: Anthropic Claude, OpenAI GPT/O, Google Gemini/Vertex
- FuncTool[P] via reflection-based JSON Schema
- Guardrails: input/turn guardrails, output validation, automatic repair
- OpenTelemetry middleware
- Streaming with Go 1.23+ iter.Seq2
- Agent.Iter with explicit Close() handling
- Time-travel debugging via serializable conversation state snapshots

## Competitive Position
Go-based alternative to Python/TypeScript frameworks. Niche but valuable for high-performance compute nodes. Single-binary deployment is ideal for distributed edge.

## Recommendation
**SKILL** — Reference for Go-based agent components. Study guardrails and type-safety patterns.

## Links
- https://github.com/fugue-labs/gollem