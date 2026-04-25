# RD Report: agent-express — TypeScript Middleware Agent Framework

**Date:** 2026-04-25  
**Category:** Agent Framework  
**Status:** SKILL  

## What It Is

A minimalist, middleware-driven TypeScript framework for building AI agents. Applies an Express-like middleware pattern with a simple `(ctx, next)` interface, centered on three concepts: Agent, Session, and Middleware.

## Key Features

- **Middleware architecture:** 5 onion hooks — agent, session, turn, model, tool
- **Built-in guards:** Budget, input/output validation, timeouts, iteration limits, HITL approval
- **Observability:** Structured logging, OpenTelemetry metrics/traces, token tracking, tool recording
- **Model support:** 12+ providers (Anthropic, OpenAI, Google, Mistral, Groq, etc.)
- **Model routing:** Based on task complexity
- **Memory management:** Context window compaction with multiple strategies
- **Testing toolkit:** TestModel, FunctionModel, capture, record/replay, snapshots
- **MCP integration:** For tool sources
- **Output validation:** Zod-based schema validation for model responses
- **CLI:** dev (hot reload) and test (CI-style output)

## License

MIT

## Why It Matters for Solomon OS

- **Middleware pattern:** Express-style middleware could inspire Hermes skill chaining
- **Guardrails:** Built-in budget/time/validation guards map to Hermes safety requirements
- **Observability:** OpenTelemetry integration aligns with Solomon OS monitoring needs
- **Lightweight:** Could serve as reference for Hermes TypeScript skill development

## Source

- https://github.com/agent-express-ai/agent-express