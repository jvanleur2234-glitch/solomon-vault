# RD Report: phero — Go Multi-Agent A2A Framework

**Date:** April 26, 2026  
**Repo:** henomis/phero (Apache-2.0)  
**Fork:** jvanleur2234-glitch/phero ✅  
**Stars:** ~200 | **Language:** Go  

## What It Is
Modern Go framework for building multi-agent AI systems. Agents act like a colony with role specialization, handoffs, and coordinated workflows.

## Key Capabilities
- **A2A Protocol:** Expose agents as HTTP servers, call remote agents as local tools
- **SKILL.md skill system:** Directly compatible with Hermes skills
- **LLM abstractions:** OpenAI-compatible + Anthropic; supports Ollama
- **MCP support:** Native Model Context Protocol integration
- **RAG:** Built-in vector storage + semantic search (Qdrant, pgvector, Weaviate)
- **Tool guardrails:** Blocklist/allowlist, timeouts, safe mode
- **Memory management, tracing, multi-turn orchestration**

## Relevance to Solomon OS
- **A2A protocol** — inter-agent communication standard for Solomon Bus
- **SKILL.md ecosystem** — same skill format as Hermes
- **Go = fast + concurrent** — ideal for Solomon Bus message routing
- **MCP integration** — aligns perfectly with Hermes MCP skills

## Recommendation
**INTEGRATE** — A2A protocol adoption for Solomon Bus. Go performance for high-throughput agent messaging.

## Links
- https://github.com/henomis/phero
- https://github.com/jvanleur2234-glitch/phero