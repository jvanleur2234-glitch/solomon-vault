# R&D Report: agent-express

**Date:** April 24, 2026
**Repo:** github.com/agent-express-ai/agent-express
**Forked:** jvanleur2234-glitch/agent-express
**LINK fit:** ★★★☆☆ — #middleware #typescript #governance

## What It Is
Express.js-style middleware framework for AI agents. Applies the (ctx, next) middleware pattern to AI agent execution. 12+ model providers, rich middleware system, built-in safety/governance, OpenTelemetry.

## Relevance to Solomon OS
- **Middleware patterns** for extensibility
- **Built-in safety/governance** aligns with enterprise requirements
- **TypeScript** for browser-based agents

## Key Features
- Onion-style middleware hooks: agent, session, turn, model, tool
- 12+ model/provider support (OpenAI, Anthropic, Google, etc.)
- Built-in governance: budget limits, input/output validation, timeouts, iteration caps, HITL approval
- OpenTelemetry metrics/traces, token tracking, tool usage records
- Context window compaction (multiple strategies)
- MCP integration, HTTP adapter (SSE streaming), CLI

## Tech Stack
- TypeScript
- MIT license

## Comparison to Hermes
| Feature | AgentExpress | Hermes |
|---------|--------------|--------|
| Middleware | Onion-style hooks | Tool decorators |
| Safety/governance | Built-in limits | Via skills |
| Telemetry | OpenTelemetry native | Via mcporter |

## Verdict
**SKILL** — Middleware patterns for extensibility. Built-in governance is reference for enterprise safety requirements.