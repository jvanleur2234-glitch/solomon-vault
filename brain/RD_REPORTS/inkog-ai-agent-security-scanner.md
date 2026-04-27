# Inkog — AI Agent Security Scanner

**Forked:** https://github.com/jvanleur2234-glitch/inkog  
**Source:** https://github.com/inkog-io/inkog  
**License:** Apache 2.0  
**Stars:** ~N/A (newer repo)  
**Language:** Go  

## What It Is

Go-based static analyzer for AI agent code. Scans 20+ frameworks in one shot for logic bugs, prompt injection, missing guardrails, hardcoded secrets, and compliance gaps (EU AI Act, NIST AI RMF, OWASP LLM Top 10). Generates MLBOM (Machine Learning Bill of Materials) and supports multi-agent A2A/delegation loop auditing. CI/CD ready via GitHub Actions.

## What We'd Use It For

- Pre-deployment security gate for Hermes skills and agent code
- OWASP LLM Top 10 compliance scanning for JCPaid/Solomon OS agents
- MLBOM generation for AI agent supply chain transparency
- Detecting prompt injection and guardrail gaps in skill frameworks

## Comparison to What We Have

- **vs. AgentArmor/Sentine/Snyk:** More framework-agnostic, MLBOM focus, EU AI Act mapping — complements rather than replaces
- **vs. Firmis/MEDUSA:** Go-based (faster CI), compliance mappings are unique

## Recommendation

**FORGE / INTEGRATE** — Apache 2.0, Go binaries for CI/CD, compliance mapping is differentiated. Install as `guard-scanner` alternative for Hermes skill pre-flight checks.

## Key Files

- `README.md` — overview + quick start
- `docs/` — compliance mapping docs
- `cmd/inkog/` — CLI entry point
