# RD Report: Agent-Orcha

**Date:** 2026-04-24  
**Slug:** agent-orcha  
**Tags:** #agent-framework #typescript #declarative #p2p #mcp  

## What It Is
Declarative, end-to-end TypeScript framework for building, managing, and scaling multi-agent AI systems. YAML-defined agents, workflows, and knowledge stores.

## Relevance to Solomon OS / Hermes
- **Declarative YAML** — could complement Hermes skill definitions
- **P2P sharing** — agent/LLM engine sharing without central servers
- **MCP support** — Model Context Protocol integration
- **Knowledge graphs** — built-in SQLite vector store with optional graph mapping
- **Desktop clients** — macOS/Windows/Linux native apps

## License
MIT

## Stars
Active declarative orchestration framework

## Key Capabilities
- Declarative orchestration: YAML-defined agents, workflows, infrastructure
- Model-agnostic: OpenAI, Gemini, Anthropic, local LLMs (Ollama, LM Studio)
- MCP integration
- Built-in SQLite vector store with semantic search
- P2P sharing of agents and LLM engines without central servers
- Per-peer rate limiting and private keys
- Security: auth, rate limits, SSRF/SQL injection hardening, sandboxed execution
- Agent Orcha Studio: web dashboard with visual composition

## Competitive Position
Declarative alternative to imperative agent frameworks. P2P sharing directly competes with AgentFM. Knowledge graph integration is advanced.

## Recommendation
**INTEGRATE** — P2P sharing patterns for AgentFM integration. Study declarative skill definition format.

## Links
- https://github.com/ddalcu/agent-orcha