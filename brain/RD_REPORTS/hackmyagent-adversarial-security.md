# RD Report: HackMyAgent — Adversarial AI Agent Security Toolkit

**Date:** April 26, 2026  
**Repo:** opena2a-org/hackmyagent (MIT) — v0.19.0  
**Fork:** jvanleur2234-glitch/hackmyagent ✅  
**Stars:** ~500+ | **Language:** TypeScript  

## What It Is
Security toolkit that analyzes and hardens AI agent setups. Compiles skills, MCP configs, system prompts, SOUL.md into an Abstract Security Tree and runs semantic checks + adversarial testing.

## Key Capabilities
- **209 static checks** across 44 categories
- **29 semantic checks** via NanoMind semantic compiler (AST-based, fewer false positives)
- **Adaptive red-teaming:** Target-specific payload generation
- **164 adversarial payloads** across 16 categories (prompt injection, data exfiltration, context manipulation)
- **20-probe behavioral simulation battery** with `--deep` mode
- **Self-securing:** Verifies its own binary on startup; tampered binaries trigger QUARANTINE mode

## Relevance to Solomon OS
- **Pre-deployment security hardening** for Hermes skills
- **Semantic analysis** — more sophisticated than regex-based scanners
- **Self-testing** — pattern for Solomon OS self-verification

## Recommendation
**FORGE** — Advanced adversarial testing framework. Essential for production security posture.

## Links
- https://github.com/opena2a-org/hackmyagent
- https://github.com/jvanleur2234-glitch/hackmyagent