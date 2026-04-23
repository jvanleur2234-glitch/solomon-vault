# RD Report: agent-express — Express-Style Agent Middleware Framework

**Repo:** https://github.com/agent-express-ai/agent-express
**Forked:** Already in workspace (agent-express)
**License:** MIT
**Stars:** Active
**Language:** TypeScript

## What It Is
Minimalist TypeScript middleware framework for AI agents using Express.js-style (ctx, next) middleware pattern. Five onion-layer hooks: agent, session, turn, model, tool. Built-in safeguards (budget/input/output checks, timeouts), observability, 12+ provider support.

## Key Features
- Middleware architecture with 5 onion hooks
- Budget/time/iteration limits + HITL approval
- OpenTelemetry metrics/traces
- 12+ model providers with complexity-based routing
- Context window compaction strategies
- MCP integration
- Zod schema validation on outputs
- CLI: agent-express dev (hot reload), test (CI-friendly)

## Solomon OS Fit
**Agent Orchestration pillar.** Express.js middleware pattern for AI is elegant. Could inspire Hermes middleware patterns. Hot reload dev mode is valuable for agent development.

## Comparison to What We Have
vs. **VoltAgent**: Both TypeScript, both middleware. VoltAgent is more feature-rich. agent-express is more minimalist and Express-idiomatic.

## Recommendation: SKILL
Study for Hermes middleware inspiration. The hot reload dev mode is directly useful.
