# Agent Express — Minimalist TypeScript Agent Framework

**Date:** 2026-04-26  
**Slug:** agent-express-typescript  
**Category:** Agent Framework  
**License:** MIT  
**Language:** TypeScript  
**Stars:** ~1,500 (est.)  
**Forked:** Yes (`jvanleur2234-glitch/agent-express-typescript-agent-framework`)

## What it is
Express-like middleware framework for AI agents in TypeScript. `(ctx, next)` pattern with built-in guards (budget, input/output validation, timeouts, iteration limits, HITL approval). 12+ model providers, memory management, MCP integration, CLI with hot reload.

## Key Features
- **Middleware architecture**: agent, session, turn, model, tool hooks
- **Built-in guards**: budget, validation, timeouts, iteration limits, HITL approval
- **Observability**: structured logs, OpenTelemetry, token tracking
- **12+ model providers**: Anthropic, OpenAI, Google, Mistral, Groq, etc.
- **Memory management**: context window compaction strategies
- **MCP integration**: tool sources via MCP
- **CLI**: `agent-express dev` with hot reload, `agent-express test` for CI
- **Testing toolkit**: TestModel, FunctionModel, capture, record/replay

## Relevance to Solomon OS / Hermes
Express-like middleware pattern is clean and could inspire Hermes ACP skill architecture. Built-in observability (OpenTelemetry) is important for production monitoring. TypeScript aligns with Hermes ACP.

## Verdict
**INTEGRATE** — Study the middleware guard pattern for Hermes skill security. OpenTelemetry observability is a gap in current Hermes. MIT licensed, actively maintained.