# RD Report: agent-express — Express-style TypeScript Agent Framework

**Date:** April 26, 2026  
**Author:** AIQ Scout  
**Status:** SKILL  
**License:** MIT  
**Stars:** Active, recent releases  

## What It Is
Minimalist, middleware-driven TypeScript framework for building AI agents. Express-like `use()` pattern for orchestrating AI workflows. 12+ model providers, model routing, built-in safeguards, MCP integration.

## Key Features
- 5 onion middleware hooks: agent, session, turn, model, tool
- Budget/input/output validation, timeouts, iteration limits, HITL approval
- OpenTelemetry observability, token tracking, tool usage recording
- Model routing based on complexity
- Context window compaction with multiple strategies
- Zod-based output validation
- CLI: `agent-express dev` (hot reload), `agent-express test` (CI output)
- MCP integration for tool sources

## Solomon OS Fit
STUDY — Middleware architecture clean and well-designed. Observability patterns worth studying for Hermes monitoring. Model routing for complexity-based delegation aligns with Solomon OS multi-model strategy.

## Action
- Clone and study: `git clone --depth 1 https://github.com/agent-express-ai/agent-express`
- No fork (not critical priority)
- Study middleware + observability for Hermes enhancement

## Links
- https://github.com/agent-express-ai/agent-express