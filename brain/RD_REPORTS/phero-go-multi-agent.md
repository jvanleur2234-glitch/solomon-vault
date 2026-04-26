# phero — Modern Go Multi-Agent AI Framework

## SLUG: phero
## Date: 2026-04-26
## Tags: #agent-framework #go #multi-agent #A2A #MCP #skills #Apache-2.0
## Status: FORGE

---

## What It Is
`phero` (henomis/phero) is a Go framework for building multi-agent AI systems with emphasis on orchestration, role specialization, and runtime handoffs. Implements A2A protocol for HTTP-based agent communication.

## Key Capabilities
- **A2A protocol**: expose agents as HTTP servers, call remote agents as tools
- **LLM abstraction**: OpenAI, Ollama, Anthropic compatible
- **Skills system + MCP support**
- **Memory for conversational context**
- **Audio I/O**: speech-to-text, TTS
- **Tracing and performance metrics**
- **Apache-2.0 License**

## Relevance to Solomon OS / Hermes
- A2A protocol implementation is valuable for Hermes inter-agent communication
- Go-based framework offers performance alternative to Python agent frameworks
- Skills system mirrors Hermes skill ecosystem

## Recommendation
**FORGE** — study A2A protocol implementation, potentially integrate into Hermes skill system.
