# RD Report: LLM Armor

## What It Is
OWASP LLM Top 10 security scanner for AI-powered applications. Combines regex pattern-matching with AST-based taint analysis to detect prompt injection, leaked secrets, exposed system prompts, improper output handling, excessive agent permissions, and unbounded API consumption.

## License
MIT

## Relevance to Solomon OS
- **Security**: Directly maps to OWASP LLM Top 10 — critical for Hermes Agent hardening
- **Skill Framework**: Could be integrated as a Hermès security scanning skill
- **Agent Security**: Core competency for any AI agent OS

## Key Features
- Dual-layer analysis: pattern matching + taint analysis
- Scans Python files, config files, notebooks
- Multiple output formats: grouped, JSON, markdown, SARIF
- Modes: strict, verbose, quiet (CI)
- OWASP LLM Top 10 mapped findings

## Stars/Status
Early release, active development as of April 2026

## Fork
https://github.com/jvanleur2234-glitch/llmarmor

## Action
**SKILL** — integrate as `hermes-security-scan` skill for OWASP compliance checking

---
*Generated: 2026-04-24 by AIQ Scout*