# RD Report: Agent Orcha

**Date:** 2026-04-22
**Repo:** ddalcu/agent-orcha
**License:** MIT
**Stars:** ~N/A (newer repo)
**Tech:** Python + TypeScript

## What It Does
Declarative multi-agent AI framework via YAML configuration. Orchestrates agents, workflows, and knowledge stores with peer-to-peer sharing.

## Key Features
- YAML-driven agent/workflow definition
- Model-agnostic (OpenAI, Gemini, Anthropic, local LLMs)
- MCP (Model Context Protocol) for external tool connections
- P2P agent sharing (no central API keys, per-peer rate limiting)
- Native desktop apps (macOS, Windows, Linux) + Docker
- Built-in SQLite vector store with graph mapping
- Browser sandbox (Chromium CDP + Xvfb + noVNC)
- Agent Orcha Studio web dashboard
- Security: SSRF protection, SQL injection hardening, sandboxed execution

## For Solomon OS
YAML-driven orchestration fits Solomon OS declarative style. P2P sharing aligns with KwaaiNet vision. Browser sandbox complements browser-harness.

**VERDICT: FORGE — declarative multi-agent orchestration**