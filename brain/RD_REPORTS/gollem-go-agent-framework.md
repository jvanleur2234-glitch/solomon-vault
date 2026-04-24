# RD Report: gollem — Go Agent Framework

**Date:** 2026-04-23
**Repo:** github.com/fugue-labs/gollem
**License:** MIT
**Stars:** ~low (new project)
**Forked:** Already in workspace ✅

## What It Is
Production-grade Go agent framework with compile-time type safety, zero-core-dependency single binaries, and compile-time guarantees. Targets robust multi-provider AI agents with structured output and streaming.

## Key Capabilities
- **Compile-time type safety** across agent output schemas, tool parameters, guardrails, middleware, event bus subscriptions
- **Zero-allocation streaming** with Go 1.23+ iterators (iter.Seq2) and node-by-node agent looping
- **Multi-provider LLM support:** Anthropic Claude, OpenAI GPT/O-series, Google Gemini/Vertex AI
- **Structured output** via final_result tool pattern; reliable typed extraction
- **Rich guardrails:** input/turn guardrails, tool result validators, output auto-repair
- **Observability:** structured run traces, OpenTelemetry middleware, lifecycle hooks, state snapshots
- **Single binary deployment** — no Python dependencies

## Relevance to Solomon OS / Hermes
- **Language:** Go (not Python) — different from Hermes but could inspire Go-based microservices
- **Compile-time safety** pattern — could inspire safer tool schemas in Hermes
- **Guardrails & validation** — directly relevant to agent-armor-studio security layer
- **Single binary** — good deployment model for edge services

## Verdict
**RESEARCH** — Watch for language-agnostic security patterns. Not immediately actionable since Hermes is Python. Could inspire Go-based Solomon Bus components.

---
**Priority:** 🟡 Worthwhile
**Category:** Agent Framework / Security / Language (Go)