# RD Report: Agent-Orcha — Declarative YAML Multi-Agent Framework

**Repo:** `ddalcu/agent-orcha`  
**URL:** https://github.com/ddalcu/agent-orcha  
**License:** Unknown (verify)  
**Stars:** Unknown  
**Date:** 2026-04-26

## What It Is
Declarative framework for building, managing, and scaling multi-agent AI systems using YAML. Supports parallelism, conditional logic, state management, multi-turn ReAct-style prompts, SQLite vector store, MCP tooling, and P2P agent sharing.

## Key Capabilities
- YAML-first agent/workflow/knowledge definitions
- Model-agnostic: OpenAI, Gemini, Anthropic, Omni, Ollama, LM Studio
- Built-in SQLite vector store with graph mappings
- P2P encrypted agent sharing with per-peer rate limits
- Chromium browser sandbox with CDP/Xvfb/noVNC
- Vision Browser for vision-LM workflows
- Desktop apps: macOS, Windows, Linux + Docker
- In-browser Studio dashboard

## Relevance to Solomon OS
**MEDIUM** — YAML orchestration is a competitor pattern to Hermes's skill-based approach. The P2P sharing model is interesting for AgentFM competitor analysis. Browser sandbox is relevant to ClawLess.

## Use Case for JCPaid
Inform Hermes dashboard/Studio development. P2P sharing model could inspire Hermes's own skill marketplace P2P layer.

## Verdict
**STUDY** — Fork for competitive intelligence. Monitor development.

## Action Taken
Already cloned in workspace.