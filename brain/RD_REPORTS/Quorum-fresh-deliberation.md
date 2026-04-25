# Quorum-fresh — Multi-Provider Deliberation (Apr 25, 2026)

**Fork:** `jvanleur2234-glitch/quorum-fresh` (MIT)
**Source:** https://github.com/Solvely-Colin/Quorum (fresh clone, more recent)

## What It Does
Same as Quorum above but from a fresh clone capturing latest commits. TypeScript-based 7-phase AI deliberation with:
- Multi-provider debate (Claude, GPT, Gemini, Ollama)
- Borda count voting + minority reports
- Deterministic SHA-256 replay ledger
- YAML policy guardrails
- Human-in-the-loop capabilities

## Why It Matters for Solomon OS
- Production-grade deliberation for multi-model confidence scoring
- Audit trail (SHA-256 ledger) = enterprise compliance for JCPaid
- Policy guardrails pattern reusable for Hermes tool permissions

## Fit: INTEGRATE
MIT licensed. Fork already created. Study policy guardrail YAML schema for Hermes permission system.

## Action Items
- [ ] Fork already exists — review latest commits
- [ ] Extract policy YAML schema for Hermes guardrails
- [ ] Map deliberation output to Hermes confidence scores
