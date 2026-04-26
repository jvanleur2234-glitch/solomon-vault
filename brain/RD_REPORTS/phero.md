# Phero — Go-based Multi-Agent AI Framework

**Date:** 2026-04-26
**URL:** https://github.com/henomis/phero
**Fork:** jvanleur2234-glitch/phero
**License:** Apache 2.0
**Stars:** ~500+ (early but active)
**Language:** Go

## What It Does
Modern Go framework for building multi-agent AI systems. Focuses on agent orchestration, coordination, and handoffs within multi-agent workflows.

## Key Features
- Composable primitives, tool-first design
- LLM abstraction (OpenAI-compatible + Anthropic)
- A2A protocol for remote/local agent interaction
- MCP and RAG support (Qdrant, pgvector, Weaviate)
- Memory management, tracing, tool guardrails
- Skills defined in SKILL.md (Hermes-compatible pattern)
- Multi-modal inputs (text, images; audio via transcription/synthesis)
- Function tools with automatic JSON Schema generation

## Architecture
- Go-first (1.25.5+ requirement)
- Clean APIs, opt-in tracing
- No heavy dependencies
- ~100 lines for simple agent, scales up

## Solomon OS Fit
**SKILL** — Study Go agent patterns for Hermes backend. SKILL.md format matches Hermes skill system. A2A protocol aligns with multi-agent orchestration. RAG + memory patterns useful for Hermes knowledge layer.

## Competitive Relevance
- AgentFM competitor (Go vs Rust)
- Phero's A2A protocol + SKILL.md pattern = Hermes interoperability potential
- Lightweight alternative to Microsoft agent-framework

## Action
Fork exists. RD written. Monitor for stars growth.