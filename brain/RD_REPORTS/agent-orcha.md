# R&D Report: agent-orcha

**Date:** April 24, 2026
**Repo:** github.com/ddalcu/agent-orcha
**Forked:** jvanleur2234-glitch/agent-orcha
**LINK fit:** ★★★★☆ — #multi-agent #p2p #yaml-orchestration #MCP

## What It Is
Declarative YAML-based multi-agent orchestration framework. Define agents, workflows, and knowledge stores in YAML — Orcha handles execution. Supports local bare metal, Docker, or native desktop apps.

## Relevance to Solomon OS
- **YAML orchestration** competitor to Hermes skills (SKILL.md format)
- **P2P agent sharing** aligns with agent economy vision
- **Built-in browser sandbox** with Chromium/CDP/Xvfb — competes with Solomon Browser POC
- **MCP integration** first-class citizen

## Key Features
- Declarative YAML config for agents/workflows
- P2P encrypted agent sharing (no central server, per-peer rate limiting)
- Built-in SQLite vector store with graph mapping
- ReAct autonomous multi-turn workflows
- Browser sandbox (Chromium, Xvfb, noVNC) + Vision Browser
- Agent Orcha Studio web UI (monitoring, IDE, visual composer)
- Security: SSRF protection, SQL injection hardening, rate limiting

## Tech Stack
- TypeScript (CLI, Studio)
- Node.js for orchestration
- Docker for containerized deployment
- SQLite for vector storage

## Comparison to Hermes
| Feature | Agent Orcha | Hermes |
|---------|-------------|--------|
| Config format | YAML | SKILL.md |
| P2P sharing | ✅ native | ❌ |
| Browser sandbox | ✅ built-in | ❌ |
| Studio UI | ✅ full IDE | minimal |
| MCP | ✅ first-class | ✅ |
| Local models | ✅ Ollama, LM Studio, Omni | via OpenRouter |

## Verdict
**FORGE** — Declarative YAML pattern is worth studying for potential Hermes skill format evolution. P2P sharing is a gap in current Solomon OS. Browser sandbox is direct competition to Solomon Browser.