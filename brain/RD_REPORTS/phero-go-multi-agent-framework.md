# RD Report: henomis/phero

**Date:** April 26, 2026  
**Forked:** Already in workspace  
**License:** MIT  
**Language:** Go  

## What It Is
Modern Go framework for building multi-agent AI systems. Emphasizes agent orchestration, role specialization, and runtime handoffs. Clean, composable architecture.

## Key Capabilities
- **A2A protocol:** Expose or call remote agents as HTTP endpoints
- **LLM abstraction:** OpenAI, Anthropic, Ollama, etc.
- **Multimodal:** Text, images, audio I/O (speech-to-text, TTS)
- **LLM middleware + function tools** with auto-generated JSON schemas
- **RAG:** Qdrant, pgvector, Weaviate vector stores
- **Memory management + tracing**
- **Skills system via SKILL.md** — same pattern as Hermes
- **MCP support**
- **Tool guards:** Blocklist/allowlist, timeouts, safe-mode

## Solomon OS Fit
**SKILL** — Go-based agent framework with SKILL.md pattern matching Hermes. A2A protocol for inter-agent communication is valuable. Tool guards (blocklist/allowlist, timeouts) directly inform AgentArmor Studio. Study Go concurrency patterns for high-performance agent serving.

## Threat/Competitor
Go-based frameworks are faster than Python. Phero's A2A protocol could become a standard for agent-to-agent communication. MCP + SKILL.md pattern confirms our architectural direction.

## Action
Study. Analyze Go concurrency patterns for Hermes deployment. Monitor A2A protocol standardization.