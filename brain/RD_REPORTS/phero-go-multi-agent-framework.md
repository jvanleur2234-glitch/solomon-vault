# RD Report: phero — Go Multi-Agent Framework with A2A Protocol

**Original:** `henomis/phero` | **License:** Apache-2.0 | **Stars:** ~500+ | **Lang:** Go

## What It Is
Modern Go 1.25+ framework for multi-agent AI systems. Agent orchestration, role specialization, runtime handoffs. A2A protocol to expose/consume agents as HTTP services.

## Key Capabilities
- Agent orchestration and handoffs (Result.HandoffAgent guides routing)
- A2A protocol (agent-to-agent HTTP services)
- LLM abstraction: OpenAI, Ollama, Anthropic
- Multimodal inputs (text, images), audio I/O (STT/TTS)
- LLM middleware for cross-cutting behaviors
- Function tools with automatic JSON schema
- RAG: built-in vector storage + semantic search
- Memory management, tracing (text + JSONL), tool guardrails (blocklists, timeouts, safe mode)
- Skills system via SKILL.md, MCP support, multiple vector stores (Qdrant, pgvector, Weaviate)

## Relevance to Solomon OS
- **A2A Protocol:** Agent-to-agent communication standard — aligns with Solomon Bus
- **Skills:** SKILL.md-based skill system — matches Hermes ecosystem
- **RAG:** Built-in vector storage for memory layer

## Threat Analysis
- Apache-2.0 licensed, clean
- Active development (latest v0.0.4, Apr 2026)
- Go 1.25+ requirement = modern codebase

## Integration Path
```
RESEARCH: phero → Study A2A protocol + skill system for Solomon Bus improvements
USE CASE: Agent-to-agent communication pattern for multi-agent orchestration
```

**Recommendation:** SKILL — A2A protocol + SKILL.md system is directly relevant to Solomon Bus. Study phero's agent communication patterns. Fork for Solomon OS enhancements.