# RD Report: gollem (fugue-labs/gollem)

## What It Is
Production-grade agent framework for Go emphasizing compile-time type safety, zero-allocation streaming, and single-binary deployment. Targets multi-provider, multi-agent systems with structured outputs and observability baked in.

## License & Stars
- **License:** MIT
- **Stars:** 25 (small but active development)

## Key Capabilities
- **Type-safe Agent[T]** with compile-time schema generation, validation, deserialization
- **Multi-provider**: Anthropic Claude, OpenAI GPT/O-series, Google Gemini, Vertex AI
- **Tools from typed Go functions** via FuncTool[P] with reflection-based JSON Schema
- **Zero-allocation streaming** via iter.Seq2; node-by-node agent loop iteration
- **Guardrails**: MaxPromptLength, ContentFilter, MaxTurns, tool result validators
- **OpenTelemetry middleware**: structured run traces, JSONFile/Console/Multi exporters
- **Conversation state snapshots** for time-travel debugging
- **Middleware chain**: Logging, Timing, MaxTokens interceptors

## Relevance to Solomon OS
- **Security**: Compile-time type safety catches errors before runtime — more reliable than Python
- **Skill frameworks**: Could serve as the core Go runtime for high-performance agent skills
- **Distributed AI**: Single-binary deployment model fits well with edge/embedded use cases
- **Self-improvement**: Observability + time-travel traces useful for self-improvement loops

## Decision
**SKILL** — Type-safe Go foundation for agent skills requiring reliability. Fork to `jvanleur2234-glitch/gollem`. Write capability into HERMES_CAPABILITIES.md.

## Notes
- Go-native avoids Python GIL issues; good for concurrent tool execution
- Single-binary = easy containerization for distributed compute