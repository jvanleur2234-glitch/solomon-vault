# agent-orcha — Declarative YAML Multi-Agent Orchestration

## Quick Summary
YAML-based declarative framework for building, coordinating, and scaling multi-agent AI systems. Includes visual Studio, P2P encrypted sharing, and browser sandbox.

## What It Is
Agent Orcha lets you define agents, workflows, and knowledge stores in YAML, then executes the orchestration. Supports local, Docker, or native desktop runtimes. Built-in SQLite vector store, MCP integration, and P2P agent sharing over encrypted networks.

## Key Capabilities
- **Declarative YAML design**: Define once, run anywhere
- **Multi-environment**: Local, Docker, macOS/Windows/Linux desktop apps
- **Model-agnostic**: OpenAI, Gemini, Anthropic, local LLMs
- **MCP integration**: Universal tooling via Model Context Protocol
- **Built-in vector store**: SQLite-based semantic search + graph mapping
- **P2P encrypted sharing**: Share agents/LLMs over encrypted P2P networks with per-peer rate limits
- **Browser sandbox**: Chromium CDP + Xvfb + noVNC for automation
- **Agent Orcha Studio**: Visual dashboard for testing, monitoring, in-browser IDE

## Relevance to Solomon OS
- **SKILL** — The P2P sharing model (per-peer rate limits, private keys, sandboxing) is directly applicable to AgentFM/Hermes P2P compute
- YAML orchestration is similar to the declarative skill patterns we're already using
- Browser sandbox (Chromium + CDP) could enhance Hermes browser tooling
- MIT licensed — can reference patterns directly

## License & Fork Status
- **License:** MIT
- **Stars:** 11 (low but novel P2P + YAML approach)
- **Forked:** Already cloned to /home/workspace/agent-orcha

## Verdict
**SKILL** — Study P2P sharing model (rate limits, key exchange, sandboxing). The YAML orchestration pattern is already well-established in our ecosystem. Browser sandbox is useful for Hermes browser automation expansion.

## Links
- https://github.com/ddalcu/agent-orcha