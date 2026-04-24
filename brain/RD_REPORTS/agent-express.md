# RD Report: Agent-Express

**Date:** 2026-04-24  
**Slug:** agent-express  
**Tags:** #agent-framework #typescript #middleware #observability  

## What It Is
Minimalist, middleware-style TypeScript framework for building AI agents. Applies Express-like use(next) pattern with agent-centric concepts (Agent, Session, Middleware).

## Relevance to Solomon OS / Hermes
- **TypeScript** — aligns with Hermes's skill ecosystem (skills written in TS)
- **Middleware architecture** — similar pattern to how Hermes chains tools/skills
- **Built-in guards** — budgets, input/output validation, timeouts, HITL approvals
- **Observability** — OpenTelemetry metrics/traces, token tracking
- **MCP integration** — native MCP client support

## License
MIT

## Stars
Active TypeScript agent framework with growing community

## Key Capabilities
- Middleware architecture with 5 hooks: agent, session, turn, model, tool
- Built-in guards: budgets, validation, timeouts, iteration limits, HITL approvals
- 12+ model providers (Anthropic, OpenAI, Gemini, Mistral, Groq, etc.)
- Model routing and complexity-based provider selection
- Memory management with context window compaction
- MCP integration
- HTTP adapter with SSE streaming
- CLI tools: agent-express dev, agent-express test
- Structured output validation with Zod schemas

## Competitive Position
Lightweight TypeScript alternative to heavier frameworks. Comparable to agent-orcha but more minimalist. Good reference for Hermes skill middleware patterns.

## Recommendation
**SKILL** — Study middleware patterns for Hermes skills. Reference implementation only.

## Links
- https://github.com/agent-express-ai/agent-express