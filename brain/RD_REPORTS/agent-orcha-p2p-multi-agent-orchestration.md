# RD Report: Agent Orcha

**Repo:** `ddalcu/agent-orcha`
**Date:** 2026-04-26
**License:** MIT
**Stars:** 11 (novel)
**Status:** SKILL

## What it does
Declarative, YAML-based multi-agent AI framework. Define agents, workflows, and knowledge stores in YAML. Built-in SQLite vector store, MCP integration, P2P encrypted agent sharing with per-peer rate limits, browser sandbox (Chromium CDP + Xvfb + noVNC), visual Studio.

## Key features
- YAML declarations for agents/workflows — non-coders can author agents
- Model-agnostic: OpenAI, Gemini, Anthropic, Ollama, LM Studio
- MCP for tools/external services
- P2P sharing: encrypted networks, per-peer rate limits, private keys
- Browser sandbox: full Chromium with CDP + Xvfb + noVNC
- Vision Browser for vision LLMs
- Agent publishing: standalone chat pages per agent, password protection
- Built-in memory, session-based with TTL cleanup
- Security: rate limiting, SSRF protection, SQL injection hardening, sandboxed execution

## Why it matters
P2P encrypted agent sharing with per-peer rate limits is novel. Browser sandbox with noVNC means agents can run in a real browser without Docker complexity. YAML-first = accessible to non-engineers.

## Solomon OS fit
**SKILL** — P2P sharing model (rate limits, key exchange) directly applicable to AgentFM/Hermes distributed compute. Browser sandbox aligns with Solomon Browser. YAML authoring could power a low-code agent builder.

## Competitor analysis
Unique blend of: YAML authoring + P2P sharing + browser sandbox. Not competing directly with any existing project.
