# RD Report: agent-express — Middleware Agent Framework

**Date:** 2026-04-23
**Repo:** github.com/agent-express-ai/agent-express
**License:** MIT (presumed)
**Forked:** Already in workspace ✅

## What It Is
Minimalist, middleware-based framework for building AI agents in TypeScript. Express-like (ctx, next) pattern with 5 onion hooks: agent, session, turn, model, tool.

## Key Capabilities
- **Middleware architecture** — composable, Express-style
- **12+ model providers** — Anthropic, OpenAI, Google, Mistral, Groq, etc.
- **Built-in safety:** budget/input/output validation, timeouts, iteration limits, HITL approvals
- **Observability:** structured logs, OpenTelemetry metrics/traces, token tracking
- **MCP integration** — tool sources, HTTP SSE streaming
- **Testing toolkit** — TestModel, FunctionModel, capture/record/replay
- **CLI:** dev (hot reload) + test (CI-friendly)

## Relevance to Solomon OS / Hermes
- **Middleware pattern** — elegant composable security layers (could inspire agentarmor-studio)
- **Budget validation** — token/budget guards directly applicable to Hermes cost control
- **HITL approvals** — human-in-the-loop for high-risk actions

## Verdict
**RESEARCH + INTEGRATE** — Clean middleware architecture for composable agent behaviors. Budget validation + HITL approval pattern could be added to Hermes as a skill.

---
**Priority:** 🟡 Worthwhile
**Category:** Agent Framework / TypeScript / Security / Middleware