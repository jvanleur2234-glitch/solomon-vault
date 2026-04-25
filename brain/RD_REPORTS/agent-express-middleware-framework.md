# Agent-Express — Express-Style Middleware Framework for AI Agents

**URL:** https://github.com/jvanleur2234-glitch/agent-express
**Forked from:** https://github.com/agent-express-ai/agent-express
**License:** MIT
**Stars:** Unknown (new discovery)

## What It Does
Minimalist TypeScript framework with 3 core concepts: `Agent`, `Session`, `Middleware`. Applies the Express.js middleware pattern to AI agents — 5 onion hooks (`agent`, `session`, `turn`, `model`, `tool`) with one `(ctx, next)` interface.

## Why It Matters
- If you know Express, you already know the mental model
- Built-in guards: budget caps, input/output validation, timeouts, iteration limits, HITL approval
- 12+ model providers via provider/model string syntax
- Model routing with complexity-based selection
- Context window compaction with 5 strategies
- MCP integration, SSE streaming, Zod schema validation
- CLI with hot-reload dev mode (`agent-express dev`) and CI test mode

## Solomon OS Fit
- DIRECT INTEGRATION — lightweight, composable architecture maps to Hermes skill system
- HITL (human-in-the-loop) approval middleware directly usable for Solomon enterprise workflows
- MIT license permits direct code use
- Could be reference for Hermes middleware/Observable pattern

## Recommendation
**INTEGRATE** — Study middleware architecture for Hermes. Express-style pattern is clean and familiar. MIT license allows direct use of patterns.

## Status
Already forked to jvanleur2234-glitch/agent-express