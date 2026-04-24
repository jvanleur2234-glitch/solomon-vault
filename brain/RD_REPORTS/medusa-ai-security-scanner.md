# RD Report: medusa — AI-First Security Scanner

**Date:** 2026-04-23
**Repo:** github.com/Pantheon-Security/medusa
**License:** AGPL-3.0
**Forked:** Already in workspace ✅

## What It Is
AI-first security scanner focused on AI/ML systems, agents, and LLM-based applications. 9,600+ detection patterns, 200+ CVE detections, repo poisoning detection across 28+ file types.

## Key Capabilities
- **9,600+ AI security detection patterns** — AI/ML, agents, LLMs, MCP, RAG
- **Repo scanning** — medusa scan --git user/repo
- **200+ CVE detections** — Log4Shell, LangChain RCE, etc.
- **28+ file types** — Cursor, Copilot, Claude Code, Gemini, Kiro
- **Parallel processing** — 10-40x faster than sequential
- **IDE integrations** — Claude Code, Cursor, VS Code, Gemini CLI

## Relevance to Solomon OS / Hermes
- **AI security scanning** — competes with sinewave and firmis-scanner in the portfolio
- **Repo poisoning detection** — critical for skill marketplace trust
- **AGPL** — different license (not MIT/Apache)

## Verdict
**RESEARCH** — Strong detection patterns library. AGPL license limits adoption for proprietary use. Mine for detection rule ideas for agentarmor-studio.

---
**Priority:** 🟡 Worthwhile
**Category:** Agent Security / CVE Detection / Repo Scanning