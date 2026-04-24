# phero — Go Agent Framework (henomis/phero)

## What It Is
Modern Go framework for building multi-agent AI systems with A2A protocol, MCP integration, role-based handoffs, and vector store support.

## Key Signals
- **License:** Apache-2.0
- **Stars:** ~500+ (recent)
- **Lang:** Go 1.25.5+
- **Latest:** v0.0.4 (Apr 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/phero

## Core Features
- Agent orchestration with Result.HandoffAgent for routing between agents
- A2A protocol (HTTP-based agent-to-agent calls as servers or local tools)
- LLM abstraction: OpenAI-compatible + Anthropic; multimodal (text, images, audio I/O)
- Tool-first design with JSON Schema auto-generation
- MCP (Model Context Protocol) integration; SKILL.md-based skills system
- Vector stores: Qdrant, pgvector, Weaviate
- RAG, memory management, tracing (JSON NDJSON), guardrails (tool safety, timeouts)
- Go-only deployment — single binary, no Python dependency

## Solomon OS Fit
- **SKILL** — Study the A2A protocol and Go architecture for potential Solomon Bus replacement
- MIT-equivalent Apache-2.0 license allows direct use
- Go runtime aligns with RustDesk/Thoth stack already in Solomon Air

## Recommendation
FORGE — A2A protocol + Go agent model worth studying for Solomon Bus v2 inter-agent communication spec.