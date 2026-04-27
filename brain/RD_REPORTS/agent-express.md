# RD Report: Agent Express

## Project: Agent Express
- **URL:** https://github.com/agent-express-ai/agent-express
- **License:** MIT
- **Stars:** 5 (very new)
- **Language:** TypeScript (74.4%)
- **Date:** April 27, 2026

## What it does
Minimalist middleware framework for building AI agents in TypeScript. Three core concepts: `Agent`, `Session`, `Middleware`. Applies Express.js middleware pattern to AI agents — `(ctx, next)` onion model with 5 hooks: agent, session, turn, model, tool.

## Key Features
- **5 middleware namespaces**: `guard` (budget, input/output validation, timeouts, HITL), `observe` (usage, tools, traces), `model` (retry, router), `memory` (compaction, store), `tools` (function, MCP)
- **12+ model providers** via `"provider/model"` string (Anthropic, OpenAI, Google, Mistral, Groq, etc.)
- **Model routing** — complexity-based selection across providers
- **Memory management** — context window compaction with 5 strategies
- **Testing toolkit** — TestModel, FunctionModel, capture/record/replay, snapshots
- **MCP integration** — connect to MCP servers as tool sources
- **HTTP adapter** — SSE streaming
- **CLI** — `agent-express dev` (hot reload), `agent-express test` (CI)
- **Structured output** — Zod schema validation on responses

## Architecture
```
agent → session → turn → model → [LLM call]
                       → tool  → [tool execution]
```
Onion model — code before `next()` runs on way in, after on way out.

## Comparison
| Feature | agent-express | Mastra | Vercel AI SDK |
|---|---|---|---|
| Core concepts | 3 | 15-20 | 5-8 |
| Built-in testing | Yes | No | No |
| Cost control | guard.budget() | Manual | Manual |

## Solomon OS Fit
**SKILL** — Study middleware pattern for Hermes plugin architecture. Express-style `(ctx, next)` is clean and familiar. Memory compaction strategies useful for Hermes long-running sessions. MIT = fork freely.

## Status
**SKILL** — Study only. Very new (5 stars), minimal community. Middleware architecture pattern is worth studying for Hermes design.
