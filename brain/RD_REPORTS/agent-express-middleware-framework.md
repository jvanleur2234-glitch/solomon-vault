# RD Report: agent-express — Express.js-Style Middleware for AI Agents

## Summary
Minimalist TypeScript middleware framework adapting Express.js patterns to AI agents. 5-layer onion model, multi-provider routing, observability, testing toolkit.

## What It Is
`agent.use(middleware)` pattern for composing AI agent behavior. Middleware hooks: agent → session → turn → model → tool. Built-in safety (budget/input/output validation, timeouts, HITL), observability (OpenTelemetry), memory management with context compaction.

## Key Features
- **5-layer middleware onion**: agent, session, turn, model, tool
- **Safety controls**: budget/input/output validation, timeouts, iteration limits, human-in-the-loop approval
- **Observability**: structured logs, OpenTelemetry traces, token tracking, tool recording
- **Multi-provider**: 12+ models via provider/model syntax (Anthropic, OpenAI, Google, Mistral, Groq...)
- **Model routing**: complexity-based provider selection
- **Memory management**: context window compaction with multiple strategies
- **MCP integration**: connect MCP servers as tool sources
- **Testing toolkit**: TestModel, FunctionModel, capture/record/replay, snapshots
- **Output validation**: Zod schemas for structured responses

## License
MIT

## Relevance to Solomon OS / Hermes
- Middleware pattern directly applicable to Hermes pipeline
- Complexity-based routing useful for cost optimization
- HITL approval + iteration limits map to safety requirements for enterprise Hermes
- Testing toolkit pattern worth stealing for Hermes skill validation

## Verdict
**FORGE** — Middleware architecture directly implementable in Hermes pipeline. MIT license permits direct use. Key patterns: safety middleware, complexity routing, context compaction.

## Fork
Already forked: `jvanleur2234-glitch/agent-express` ✅
