# RD Report: agent-express

## What It Is
Minimalist TypeScript middleware framework for building AI agents. Applies Express.js `use()` pattern to AI agent development — three concepts: Agent, Session, Middleware.

## License
MIT

## Relevance to Solomon OS
- **Agent Orchestration**: Clean middleware model for Hermes-style skill chaining
- **TypeScript/Node.js Ecosystem**: Could power Hermes MCP server implementations
- **Multi-Provider**: 12+ model providers, complexity-based routing
- **Observability**: OpenTelemetry built-in, structured logging

## Key Features
- 5 onion hooks: agent, session, turn, model, tool
- Built-in guards: budget caps, input/output validation, timeouts, iteration limits, HITL approval
- 12+ model providers via provider/model syntax
- Model routing by complexity
- Context window compaction strategies
- MCP integration (connect to MCP servers as tool sources)
- SSE streaming out of the box
- Testing toolkit: TestModel, FunctionModel, capture, record/replay

## Stars/Status
Active, 2026 release

## Action
**SKILL** — Evaluate for Hermes Agent's middleware/skill chain architecture. Good reference for `hermes-skill-factory` design patterns.

---
*Generated: 2026-04-24 by AIQ Scout*