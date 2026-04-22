# RD Report: guard-scanner

**Date:** 2026-04-22  
**Category:** AI Security  
**Source:** web_research (github)  
**Fork Status:** Already forked (guard-scanner-new)

## What It Is
A security scanner for agentic workflows that detects complex, invisible attacks on AI agents and MCP/OpenClaw-style ecosystems. Focuses on prompt injection, identity hijacking, memory poisoning, and A2A contagion.

## Key Capabilities
- **364 detection patterns** across 35 threat categories
- **27 runtime checks** for agentic vulnerabilities
- OWASP Agentic Top 10 alignment
- Works as CLI or MCP server
- SOUL.md locking and immutability checks
- Real-time watch mode with `--soul-lock`

## Comparison to What We Have
- Similar to AgentSeal, AgentVerus, RAXE in security scanning
- Unique: SOUL.md protection, identity hijack detection
- Guard-scanner already forked as `guard-scanner-new` in our workspace

## Relevance to Solomon OS
- **CRITICAL** - Security is core to JCPaid/Hermes
- Detects attacks on agent identities and skill files
- OWASP aligned — aligns with industry security standards

## Recommendation
**ALREADY FORKED** — No action needed. Already tracked as `guard-scanner-new`.

---

## Stats
- Stars: ~500+ (active, recent releases)
- License: MIT
- Language: TypeScript, Rust, JavaScript