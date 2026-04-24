# RD Report: hackmyagent — Security Toolkit for AI Agents

**Date:** 2026-04-23
**Repo:** github.com/opena2a-org/hackmyagent
**License:** Apache-2.0
**Stars:** ~new (active development)
**Forked:** Already in workspace ✅

## What It Is
Security toolkit and red-team/blue-team engine for AI agents. Analyzes artifacts (skills, MCP configs, SOUL.md, system prompts) by compiling them into an Abstract Security Tree and performing semantic checks.

## Key Capabilities
- **209 static checks** across 44 categories (credentials, configurations, governance, memory/RAG poisoning, sandboxing)
- **164 adversarial payloads** for testing resilience
- **20-probe behavioral simulation** — observe actual behavior
- **Abstract Security Tree** — semantic AST-based checks (not just regex)
- **Self-securing** — binary integrity verification at startup
- **Zero-config** — no config files or flags needed

## Relevance to Solomon OS / Hermes
- **Security scanning** — directly complements agentarmor-studio (8-layer framework)
- **MCP security** — checks MCP configs for vulnerabilities
- **Red-team testing** — could validate Hermes security posture

## Verdict
**FORGE** — Already forked (hackmyagent-new). Add to agentarmor-studio as a skill. High-value security tool for the security scanner product line.

---
**Priority:** 🔴 Critical (security, active development)
**Category:** Agent Security / Red-Team / MCP