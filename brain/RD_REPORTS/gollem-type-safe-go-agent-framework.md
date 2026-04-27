# RD Report: Gollem — Type-Safe Go Agent Framework

## Summary
Gollem by Fugue Labs is a production-grade Go agent framework with compile-time type safety. Generic Agent[T], multi-provider (Anthropic Claude, OpenAI, Vertex AI, Gemini), structured output via "final_result" pattern, guardrails, middleware chain, team swarms, graph workflows, MCP client, Temporal durable execution. Zero allocations for streaming, single-binary deployment. MIT, v0.3.1.

## What It Does
- **Compile-Time Guarantees**: Output schemas, tool params, guardrails, event subscriptions checked at compile time
- **Generic Agent[T]**: Strongly typed output across the pipeline
- **Multi-Provider Streaming**: 5+ LLMs with streaming
- **Structured Output**: Reliably typed "final_result" pattern
- **Zero Allocations**: Streaming without GC overhead
- **Single-Binary**: Zero-dependency deployment
- **Guardrails**: Input/turn guards, tool output validators, auto-repair
- **Middleware**: Logging, timing, token limits interceptors
- **Team Swarms**: Multi-agent orchestration
- **Graph Workflows**: Complex orchestration patterns
- **MCP Client**: Connect to MCP servers
- **Temporal**: Durable execution for long-running tasks

## Tech Stack
- Language: Go
- License: MIT
- Latest: v0.3.1 (Mar 2026)

## Strategic Fit for Solomon OS

**FORGE** — Core agent runtime for Solomon OS backend. Go single-binary = zero-dependency Hermes tools.

Key learnings:
1. **Compile-Time Safety**: Type guarantees prevent runtime crashes in production
2. **Temporal Integration**: Durable execution for mission-critical Hermes tasks
3. **Team Swarms**: Multi-agent orchestration pattern for Solomon Bus
4. **Zero-Allocation Streaming**: Performance critical for production

## Risk/Concerns
- v0.3.1 (early)
- 1 contributor listed
- Go required for customization

## Verdict
FORGE — Adopt as core runtime for high-throughput Hermes components. Go single-binary aligns with zero-dependency deployment goal. Team swarms pattern for Solomon Bus v2.

## Links
- Repo: https://github.com/fugue-labs/gollem
- Fork: Already forked