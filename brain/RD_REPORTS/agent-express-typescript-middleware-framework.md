# Agent Express — Express.js-Style TypeScript Agent Middleware Framework

**Fork:** `agent-express-ai/agent-express` → already in workspace
**Source:** https://github.com/agent-express-ai/agent-express (MIT?)
**Date:** 2026-04-25

---

## What It Does

Minimalist, middleware-style TypeScript framework for building AI agents. Applies an Express.js-style `(ctx, next)` pattern with composable middleware.

Key concepts: Agent, Session, Middleware. Middleware stack follows a 5-layer onion model:
1. Agent layer
2. Session layer
3. Turn layer
4. Model layer
5. Tool layer

Built-in guards: budgets, validation, timeouts, iterations, human-in-the-loop approvals. Multi-provider model support (12+ providers). Observability: structured logs, OpenTelemetry, token tracking. MCP integration. CLI with hot reload (`agent-express dev`). Testing toolkit with capture/replay and snapshots.

## Key Stats

- 12+ LLM providers (Anthropic, OpenAI, Google, Mistral, Groq, etc.)
- 5-layer middleware onion
- Built-in guards: budget, validation, timeout, iteration, human-in-the-loop
- MIT license

## Solomon OS Fit

**FORGE** — Express.js middleware pattern is exactly how Solomon Bus/Odin should work. Guard rails (budget, validation, timeout) = core security primitives for Hermes. MIT allows code use. Study for Hermes security middleware layer.

## Status

**FORGE** — apply 5-layer middleware architecture to Hermes. Guards pattern directly implementable.