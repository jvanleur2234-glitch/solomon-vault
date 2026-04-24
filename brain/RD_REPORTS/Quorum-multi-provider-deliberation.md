# RD Report: Quorum — Multi-AI Deliberation Framework

**Date:** 2026-04-23
**Repo:** github.com/Solvely-Colin/Quorum
**License:** MIT
**Forked:** Already in workspace ✅

## What It Is
Multi-AI deliberation framework in TypeScript that runs debates among multiple AI providers to produce synthesized answers with confidence scores. 7-phase deliberation (Gather → Plan → Formulate → Debate → Adjust → Rebuttal → Vote → Synthesis).

## Key Capabilities
- **Multi-provider deliberation** — Claude, GPT, Gemini, Kimi, DeepSeek, Mistral, Ollama
- **Adaptive debate length** — auto-skip on consensus
- **Evidence protocol** — providers cite sources, cross-validate claims
- **Policy guardrails** — YAML rules for blocking/warning
- **Deterministic replay** — SHA-256 hash-chained ledger for auditability
- **Diverse topologies** — mesh, star, tournament, pipeline
- **MCP server compatibility** + Red Team packs

## Relevance to Solomon OS / Hermes
- **Deliberation** — directly competes with Agent Council in captain-claw
- **Evidence protocol** — could enhance Hermes reasoning transparency
- **Audit trail** — deterministic replay valuable for compliance

## Verdict
**RESEARCH** — Competitive deliberation framework. Compare to captain-claw Agent Council. Both MIT — could cross-pollinate features.

---
**Priority:** 🟢 Nice to have
**Category:** Multi-Agent / Deliberation / TypeScript