# RD Report: agent-orcha — Declarative YAML Multi-Agent Framework

**Date:** 2026-04-25  
**Category:** Agent Orchestration  
**Status:** SKILL  

## What It Is

A declarative, TypeScript-based framework (with Svelte, Swift, and other tech) for building, managing, and scaling multi-agent AI systems. Agents, workflows, and knowledge stores are defined in YAML, while orchestration, memory, security, and tooling are handled via MCP.

## Key Features

- **Declarative agent/workflow definitions in YAML**
- **Model-agnostic LLM support** (OpenAI, Gemini, Anthropic, local LLMs)
- **P2P sharing of agents/LLMs without central keys**, with per-peer rate limiting
- **Universal tooling via MCP** to connect to external services, APIs, or databases
- **Built-in knowledge stores** (SQLite vector store) with support for knowledge graphs and semantic search
- **Robust workflow engine** with parallelism, conditional logic, multi-turn prompts (ReAct)
- **Browser sandbox** with noVNC, CDP, Xvfb; Vision Browser for vision LLMs
- **Security features:** Auth, rate limiting, SSRF protection, SQL hardening, sandboxed execution
- **Native desktop apps and Docker/NPM usage**
- **Web dashboard** (Agent Orcha Studio) for testing, monitoring, in-browser IDE

## License

MIT

## Why It Matters for Solomon OS

- **YAML-first:** Declarative config could complement Hermes skill definitions
- **P2P agent sharing:** Per-peer rate limiting could inspire distributed Hermes node concept
- **Knowledge graph + vector store:** Built-in memory aligns with Solomon Vault approach
- **Browser sandbox:** In-browser IDE pattern for Agent Orcha Studio maps to Solomon Browser dashboard

## Source

- https://github.com/ddalcu/agent-orcha