# RD Report: Agent Express — Express-Style TypeScript Agent Middleware

## Summary
Minimalist TypeScript middleware framework for AI agents. Applies Express.js `use()` pattern (ctx, next) pipeline to AI agents. 5 onion hooks: agent, session, turn, model, tool. Built-in safety (budget guards, input/output validation, timeouts, HITL approval). Multi-provider (12+). MCP integration. MIT licensed.

## What It Does
- **Middleware Architecture**: Express-style `use()` pipeline for agents
- **5 Onion Layers**: agent → session → turn → model → tool
- **Safety Controls**: Budget guards, I/O validation, timeouts, HITL approval
- **Multi-Provider Routing**: 12+ providers, complexity-based routing
- **Context Compaction**: Memory management with multiple strategies
- **MCP Integration**: Connect to MCP servers as tool sources
- **SSE Streaming**: Built-in HTTP adapter
- **Testing Toolkit**: TestModel, FunctionModel, capture/record/replay, snapshots
- **CLI**: dev (hot reload) + test (CI-friendly)

## Tech Stack
- Language: TypeScript
- License: MIT

## Strategic Fit for Solomon OS

**SKILL** — Already forked. Key learnings:
1. **Middleware Pattern**: Hermes skill composition via middleware chain
2. **HITL Approval**: Enterprise safety requirement for Hermes evolution
3. **Complexity Routing**: Cost optimization for JCPaid multi-provider routing
4. **Testing Toolkit**: Production-grade testing for skills

## Risk/Concerns
- Newer project, community size unknown
- TypeScript-only
- Similar to Express.js mental model

## Verdict
STUDY — Middleware pattern for Hermes skill composition is valuable. HITL approval directly applicable to enterprise safety requirements.

## Links
- Repo: https://github.com/agent-express-ai/agent-express
- Fork: jvanleur2234-glitch/agent-express (already forked)