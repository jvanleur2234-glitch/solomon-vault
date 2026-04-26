# phero — Go Framework for Multi-Agent AI Systems (Apache 2.0)

## Quick Summary
Modern Go framework for building multi-agent AI systems with A2A protocol, LLM abstraction, multimodal I/O, RAG, skills via SKILL.md, MCP support, and tool guardrails.

## What It Does
- **Agent orchestration** with runtime handoffs and role specialization
- **A2A protocol** (Agent-to-Agent) over HTTP
- **LLM abstraction**: OpenAI-compatible + Anthropic
- **Multimodal input**: text, images, audio I/O (speech-to-text, text-to-speech)
- **LLM middleware**: reusable cross-cutting behaviors
- **Function tools** with automatic JSON Schema generation
- **RAG**: built-in vector storage and semantic search
- **Skills system**: SKILL.md, MCP support, memory management
- **Tool guardrails, tracing**, per-run token/latency metrics
- **Vector stores**: Qdrant, pgvector, Weaviate

## Relevance to Solomon OS
- **SKILL** — Go-based agent framework. A2A protocol study for Solomon Bus inter-agent communication. SKILL.md ecosystem parallels Hermes skills. Apache 2.0.
- RAG + vector stores align with Hermes knowledge management
- Tool guardrails pattern worth studying

## License & Status
- **License:** Apache 2.0
- **Already cloned:** /home/workspace/phero
- **Repo:** https://github.com/henomis/phero

## Verdict
**SKILL** — Clean Go implementation of multi-agent patterns. A2A protocol and SKILL.md system are directly relevant to Hermes/Solomon Bus. Apache 2.0 is business-friendly.
