# RD Report: opena2a-org/hackmyagent

**Date:** 2026-04-20
**Fork:** jvanleur2234-glitch/hackmyagent
**License:** Apache 2.0
**Category:** AI Security / Red Team
**Relevance:** 🔴 Critical

## What It Is

Security toolkit for AI agents: scanner, red-team, behavioral simulation, skill builder. Powered by NanoMind Semantic Compiler. 209 security checks + 29 semantic checks. Self-securing (verifies own binary integrity).

## Key Capabilities

- **NanoMind Semantic Compiler**: Compiles artifacts into Abstract Security Tree — catches what regex can't
- **Self-securing**: Binary integrity check on startup, QUARANTINE mode if tampered
- **Behavioral simulation**: 20-probe battery observes actual skill behavior, not just text
- **209 security checks** across 44 categories
- **164 adversarial payloads** across 16 categories
- **Skills builder**: `hackmyagent create-skill` generates secured skills with SOUL.md governance

## Comparison to Solomon OS Stack

- Semantic security analysis → superior to pattern matching for Hermes
- Self-securing → the scanner that secures itself — first of its kind
- Behavioral simulation → key for testing Hermes skills before deployment
- SOUL.md governance → aligned with Solomon's agent identity concepts

## Recommendation

**FORGE** — Best-in-class security analysis for AI agents. The semantic compiler approach is novel and high-value. Fork for deep study and potential integration into Solomon's security layer. Fork already exists.