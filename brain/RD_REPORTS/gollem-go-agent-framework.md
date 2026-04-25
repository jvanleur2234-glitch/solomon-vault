# Gollem — Production Agent Framework for Go

**URL:** https://github.com/jvanleur2234-glitch/gollem
**Forked from:** https://github.com/fugue-labs/gollem
**License:** MIT
**Stars:** Unknown (new discovery)

## What It Does
Go-based production agent framework with compile-time type safety, zero-core dependencies, and single-binary deployment. Provides typed agents, multi-provider streaming, guardrails, middleware, cost tracking, and multi-agent team orchestration.

## Why It Matters
- Compile-time guarantees catch entire bug classes Python frameworks can't
- 561+ tests, Go 1.23+ iter.Seq2 streaming, OpenTelemetry tracing
- Type-safe `Agent[T]` with auto schema generation from struct tags
- Input/turn/output guardrails, output auto-repair, retry with backoff
- Team orchestration with durable task stores and lease-based claiming

## Solomon OS Fit
- SKILL — Go-based agents for Hermes compute layer (high-performance workloads)
- Could be wrapper for GPU compute tasks in distributed scenarios
- Type-safe agent definitions complement Hermes skill system
- MIT license permits direct code use

## Competitive Analysis
- **vs. Python frameworks (LangChain, AutoGen):** Compile-time safety vs. runtime validation
- **vs. agent-express:** Go performance + type safety vs. TypeScript ergonomics
- **vs. Docker Agent (cagent):** Native Go vs. YAML config + Docker dependency

## Recommendation
**SKILL** — Study for type-safe agent design patterns. Consider Go agent for compute-intensive Hermes workloads.

## Status
Already forked to jvanleur2234-glitch/gollem