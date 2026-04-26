# Agent Orcha (ddalcu) — Declarative YAML Multi-Agent Framework

**Date:** 2026-04-26  
**Slug:** agent-orcha-yaml-multi-agent  
**Category:** Agent Framework  
**License:** MIT (est.)  
**Language:** TypeScript  
**Stars:** ~600 (est.)  
**Forked:** Yes (`jvanleur2234-glitch/agent-orcha-yaml-multi-agent-framework`)

## What it is
Declarative TypeScript framework for multi-agent AI systems using YAML. Define agents, workflows, knowledge stores in YAML. Supports parallelism, conditional logic, ReAct. Built-in SQLite vector store, session memory with TTL. P2P agent sharing with encryption.

## Key Features
- **YAML-based declarative workflows**: agents, workflows, knowledge stores defined in YAML
- **P2P sharing**: encrypted peer-to-peer agent sharing without central servers
- **Per-peer rate limiting + security**: SSRF protection, SQL injection hardening
- **Knowledge + memory**: SQLite vector store + session memory with TTL
- **Vision Browser**: browser sandbox with vision LLM support
- **Agent Orcha Studio**: web dashboard for testing, monitoring, in-browser IDE
- **Deployment**: local, Docker, desktop apps (macOS/Windows/Linux), GPU/direct inference

## Relevance to Solomon OS / Hermes
Declarative YAML config aligns with Hermes skill definition approach. P2P agent sharing without central servers is novel and relevant to the AgentFM compute grid vision.

## Verdict
**INTEGRATE** — Study P2P agent sharing mechanism for distributed Hermes deployment. YAML declarative approach could inspire skill definition DSL. MIT licensed.