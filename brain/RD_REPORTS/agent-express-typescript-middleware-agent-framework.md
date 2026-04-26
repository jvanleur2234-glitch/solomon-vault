# RD Report: agent-express

**Repo:** `agent-express-ai/agent-express`
**Date:** 2026-04-26
**License:** MIT
**Stars:** Growing (2026 project)
**Status:** SKILL

## What it does
Minimalist, middleware-style TypeScript framework for AI agents. Applies Express.js `use()` pattern to AI agents with Agent/Session/Middleware layers.

## Key features
- Express-like middleware: `use()` with `(ctx, next)` onion model
- Hooks: agent, session, turn, model, tool layers
- Safety controls: budget/input/output guards, timeouts, iteration limits, HITL approval
- Observability: structured logs, OpenTelemetry, token tracking, tool recording
- Multi-provider: 12+ providers (Anthropic, OpenAI, Google, etc.)
- Complexity-based model routing
- Context window compaction (multiple strategies)
- Testing toolkit: TestModel, FunctionModel, capture/replay, snapshots
- MCP integration, HTTP SSE adapter, CLI tooling
- Structured output validation with Zod

## Why it matters
Express-like middleware pattern is the most intuitive way to compose agent behaviors. Already familiar to millions of JS developers. HITL approval + iteration limits directly address AI safety concerns for enterprise.

## Solomon OS fit
**SKILL** — Middleware pattern could define Hermes skill composition. HITL approval is a must-have for Solomon OS production agents. Complexity-based routing for cost optimization in JCPaid.

## Action
Clone, fork, write SKILL.md for Hermes.
