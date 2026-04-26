# RD Report: Agent Orcha — Declarative YAML Multi-Agent Framework

**Date:** April 26, 2026  
**Repo:** ddalcu/agent-orcha (MIT)  
**Fork:** Already in workspace — upstream  
**Stars:** ~300 | **Language:** TypeScript  

## What It Is
Declarative, YAML-centric multi-agent AI orchestration framework. Define agents, workflows, and knowledge stores in YAML; supports parallelism, conditional logic, and multi-turn state management.

## Key Capabilities
- **Declarative YAML workflows:** Agents, parallelism, conditional logic, ReAct-style prompts
- **Model-agnostic:** Swappable OpenAI/Gemini/Anthropic/local LLMs (Ollama, LM Studio)
- **MCP (Model Context Protocol):** Connect agents to external services, APIs, databases
- **Knowledge stores:** SQLite vector store + knowledge graph mapping
- **P2P sharing:** Encrypted P2P agent sharing without central servers
- **Security:** Rate limiting, SSRF protection, SQL injection hardening, sandboxed execution
- **Browser sandbox:** Chromium/CDP control, Vision Browser
- **Agent Orcha Studio:** Web dashboard with in-browser IDE and agent composer

## Relevance to Solomon OS
- **YAML-based orchestration** — could simplify Solomon Bus workflow definitions
- **P2P sharing** — peer-to-peer agent distribution pattern for Solomon Air
- **Knowledge graph + vector store** — alternative to cognee for Hermes memory
- **Web IDE** — reference for building agent composer UI

## Recommendation
**SKILL** — Study YAML workflow patterns for Solomon Bus. P2P sharing for distributed agent deployment.

## Links
- https://github.com/ddalcu/agent-orcha