# RD Report: agent-express

**Fork Status:** Already forked  
**License:** MIT  
**Stars:** ~300 (TypeScript middleware framework for AI agents)  
**Relevance:** HIGH — skill framework, middleware architecture, multi-provider routing

## What It Is
Minimalist, TypeScript-based middleware framework for building AI agents. Applies Express.js middleware pattern with (ctx, next) flow centered on Agent, Session, Middleware concepts.

## Key Capabilities
- Middleware architecture with 5 onion hooks: agent, session, turn, model, tool
- Built-in safeguards: budget/input/output validation, timeouts, iteration limits, HITL approval
- Observability: structured logging, OpenTelemetry metrics/traces, token/tool tracking
- Multi-provider model support: 12+ providers via provider/model pattern
- Model routing and memory management: complexity-based routing, context window compaction
- MCP integration and HTTP adapter
- CLI tools: agent-express dev (hot reload) and test (CI-friendly output)

## Relevance to Hermes/Solomon
- Middleware architecture directly maps to Hermes skill system
- Could serve as inspiration for Hermes Agent's skill chaining mechanism
- HITL approval patterns relevant for Solomon OS business workflows

## Integration Recommendation
**SKILL** — Middleware composition patterns could enhance Hermes skill chaining. Study agent-express's provider routing for multi-model Hermes configurations.

## Notes
- MIT licensed
- Active development
- Strong overlap with Hermes's design philosophy