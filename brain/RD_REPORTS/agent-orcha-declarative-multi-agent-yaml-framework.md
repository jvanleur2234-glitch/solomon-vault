# agent-orcha — Declarative Multi-Agent YAML Framework

**Fork:** Already forked to `jvanleur2234-glitch/agent-orcha`  
**License:** MIT  
**Latest:** 2026.409.2132

## What It Is
A TypeScript-based declarative multi-agent AI framework where agents, workflows, and infrastructure are defined in **YAML** and version-controlled. Built-in knowledge stores (SQLite vector + graph mapping), P2P sharing, native desktop apps, and browser sandbox.

## Key Features
- **Declarative YAML** for agents, workflows, infrastructure
- **Model-agnostic**: OpenAI, Gemini, Anthropic, local LLMs — swap without rewriting
- **MCP (Model Context Protocol)** universal connectivity
- **Knowledge stores**: SQLite vector store + optional graph mapping for semantic search
- **P2P sharing**: encrypted peer-to-peer sharing without central keys, per-peer rate limits
- **Native desktop apps**: macOS, Windows, Linux binaries with system tray + auto-updates
- **Browser sandbox**: Chromium CDP + Xvfb/noVNC; experimental Vision Browser
- **Workflow engine**: parallel execution, conditional logic, state management, ReAct-style autonomous prompts
- **Security**: rate-limited auth, SSRF/SQL injection hardening, sandboxed execution

## Why It Matters
- Declarative YAML is a **natural fit for Hermes skill definitions**
- P2P sharing model could inform AgentFM competitor analysis
- Desktop app + browser sandbox suggests a consumer-facing AI agent product

## Verdict
**SKILL** — Worth studying for the YAML-based agent definition pattern. Could inspire Hermes skill factory improvements. P2P sharing model is interesting for distributed compute discussions.