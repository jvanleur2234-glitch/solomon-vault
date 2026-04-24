# RD Report: Agent Orcha — Declarative Multi-Agent with P2P

## Summary
Declarative, YAML-driven multi-agent AI framework with P2P sharing, knowledge graphs, and browser sandbox.

## What It Is
TypeScript-based framework defining agents/workflows/knowledge in YAML. Built-in workflow engine with parallelism, conditional logic, state management. Model-agnostic (OpenAI/Gemini/Anthropic/local LLMs). MCP support.

## Key Features
- **P2P Sharing**: encrypted peer-to-peer agent/LLM sharing without central keys, per-peer rate limiting
- **Knowledge Stores**: SQLite-based vector store + optional knowledge graph mapping; semantic search + graph analysis
- **Browser Sandbox**: CDP control, in-browser IDE, real-time monitoring
- **Security**: SSRF protection, SQL injection hardening, sandboxed execution
- **Agent Orcha Studio**: web dashboard for testing, knowledge browsing, workflow execution

## License
MIT

## Relevance to Solomon OS / Hermes
- P2P sharing model maps to AgentFM competitors — worth studying
- Knowledge graph + vector store combo could enhance Hermes memory system
- Declarative YAML approach vs code-first — different paradigm than our current skills

## Verdict
**SKILL** — Study P2P sharing architecture for distributed Hermes deployment. Knowledge graph integration pattern useful for Hermes memory.

## Fork
`/home/workspace/agent-orcha` → `jvanleur2234-glitch/agent-orcha` ✅
