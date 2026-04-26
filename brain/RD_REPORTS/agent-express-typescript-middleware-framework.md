# agent-express — Minimalist TypeScript Agent Middleware Framework

## Quick Summary
Express.js-like middleware framework for AI agents in TypeScript. `use()` pattern with 5 onion-style hooks (agent, session, turn, model, tool). Guardrails, observability, multi-provider routing built-in.

## What It Is
A minimalist, middleware-based framework for building AI agents in TypeScript. Applies the familiar Express.js `use()` pattern to agent workflows. Strong focus on composable guardrails, observability (OpenTelemetry), and multi-provider model routing.

## Key Capabilities
- **Middleware architecture**: 5 hooks — agent, session, turn, model, tool
- **Guardrails**: Budget limits, input/output validation, timeouts, iteration caps, HITL approval
- **Observability**: Structured logging, OpenTelemetry metrics/traces, token tracking, tool activity
- **Multi-provider**: 12+ providers via provider/model syntax (Anthropic, OpenAI, Google, Mistral, Groq, etc.)
- **Memory management**: Complexity-based routing, context window compaction (multiple strategies)
- **MCP integration**: Tool sourcing and HTTP adapter with SSE streaming
- **Testing tools**: TestModel, FunctionModel, capture, record/replay, snapshots

## Relevance to Solomon OS
- **SKILL** — The middleware/guardrail pattern is directly applicable to Hermes security layer
- OpenTelemetry observability built-in aligns with Solomon OS monitoring needs
- Multi-provider routing with complexity-based context compaction is solid architecture
- MIT licensed — can integrate patterns

## License & Fork Status
- **License:** MIT
- **Stars:** ~200 (estimated, TypeScript agent framework space)
- **Forked:** Already forked to jvanleur2234-glitch/agent-express-new

## Verdict
**SKILL** — Middleware architecture pattern and guardrail implementation worth studying. The complexity-based context compaction aligns with Hermes memory management. OpenTelemetry integration is valuable for Solomon OS observability.

## Links
- https://github.com/agent-express-ai/agent-express
- Fork: https://github.com/jvanleur2234-glitch/agent-express-new