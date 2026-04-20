# gollem — Type-Safe Go Agent Framework

**Already cloned:** `/home/workspace/gollem`
**Forked:** `jvanleur2234-glitch/gollem`
**Stars:** Unknown (v0.3.1, March 2026)
**License:** MIT
**Category:** agent-framework #go #type-safety

## What It Is
Production-ready Go agent framework emphasizing compile-time type safety, zero-allocation streaming, and single-binary deployment. Prevents runtime type errors that plague Python agent frameworks.

## Key Features
1. **Generic Agent[T]** — automatic schema generation, validation, deserialization
2. **5+ LLM providers** — Anthropic Claude, OpenAI GPT, Google Gemini/Vertex
3. **FuncTool[P]** — typed tools with reflection-based JSON Schema
4. **Guardrails** — input/turn guards, tool result validators, output auto-repair
5. **Observability** — structured run traces, OpenTelemetry middleware, lifecycle hooks
6. **Conversation snapshots** — time-travel debugging
7. **Zero core dependencies** — single binary, compile-time guarantees

## Key Patterns for Solomon OS
1. **Type-safe at compile time** → Go-based agents could replace fragile Python patterns in Solomon Bus workers
2. **Guardrails pattern** → maps to Solomon Guardian input validation
3. **OpenTelemetry middleware** → structured logging for all agents
4. **Time-travel debugging** → conversation snapshots for Russell Tuna debugging
5. **Single binary deployment** → Solomon OS agents could be compiled Go binaries

## Verdict
**INTEGRATE** — MIT, type-safe, production-grade. The guardrails + observability + time-travel combination is powerful. Consider for Solomon Bus worker rewrite in Go.

## Links
- https://github.com/jvanleur2234-glitch/gollem