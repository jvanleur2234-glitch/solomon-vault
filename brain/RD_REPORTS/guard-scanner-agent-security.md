# RD Report: guard-scanner

**Repo**: `koatora20/guard-scanner`  
**License**: MIT  
**Language**: TypeScript + Rust  
**Stars**: ~300+ (estimated)  
**Date**: 2026-04-21  
**Relevance**: 🔴 Critical — AI Security Scanner (OWASP ASI aligned)

## What It Is

Agent security scanner designed for MCP/A2A agent ecosystems. Detects prompt injection, identity hijacking, memory poisoning, and A2A contagion with 364 detection patterns across 35 threat categories and 27 runtime checks.

## Key Features

- **364 detection patterns**, 35 threat categories, 27 runtime checks
- **OWASP ASI mapping** — filtered findings aligned to OWASP Agentic Top 10
- **Prompt injection detection** — invisible Unicode, homoglyphs, Base64 evasion, zero-width chars
- **Identity hijacking** — SOUL.md overwrites, persona swaps
- **Memory poisoning** — crafted conversation attacks
- **A2A contagion** — session smuggling, lateral propagation, confused deputy
- **Output**: structured JSON with rule_id, category, severity, rationale, remediation, evidence
- **Modes**: CLI, MCP server, watch mode (real-time)

## For Solomon OS / Hermes

- **OWASP ASI alignment** — directly maps to agent security requirements
- **MCP/A2A support** — aligns with Hermes's MCP architecture
- **Identity protection** — critical for persona/SOUL.md integrity
- **Memory poisoning detection** — protects agent conversation history

## Recommendation

**INTEGRATE** — guard-scanner's OWASP ASI mapping and A2A contagion detection are directly relevant to Solomon's agent security posture. Add to Solomon's security stack immediately.
