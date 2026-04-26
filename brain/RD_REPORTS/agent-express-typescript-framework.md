# RD Report: agent-express — Express-Style Middleware Agent Framework

**Original:** `agent-express-ai/agent-express` | **License:** MIT | **Stars:** ~600 | **Lang:** TypeScript

## What It Is
Minimalist, middleware-based TypeScript framework for AI agents. Models after Express.js middleware with `(ctx, next)` pattern. Centers on Agent, Session, and Middleware concepts.

## Key Capabilities
- Middleware architecture with 5 onion hooks: agent, session, turn, model, tool
- Built-in guards: budgets, validation, timeouts, iteration limits, HITL approvals
- Observability: structured logs, OpenTelemetry metrics/traces, token tracking
- 12+ LLM providers via provider/model string routing
- Memory management with context window compaction strategies
- Testing toolkit: TestModel, FunctionModel, capture/replay, snapshots
- MCP integration
- Zod schema validation for outputs
- HTTP adapter with SSE streaming

## Relevance to Solomon OS
- **Skill Framework:** TypeScript native — aligns with Hermes ACP skill model
- **Security:** Built-in guards for budgets, timeouts, approvals
- **Observability:** OpenTelemetry tracing for audit trails

## Threat Analysis
- MIT licensed, active development
- Express-inspired middleware = well-understood, stable pattern
- Strong typing (TypeScript)

## Integration Path
```
SKILL: agent-express → TypeScript agent harness for Hermes ACP
USE CASE: Lightweight agent with strong safety guards for production
```

**Recommendation:** SKILL — TypeScript native framework with strong safety features. Study middleware patterns for Hermes improvements. Fork for Hermes ACP skill template.