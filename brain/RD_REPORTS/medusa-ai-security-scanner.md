# Medusa — AI Security Scanner (9,600+ Patterns)

**URL:** https://github.com/jvanleur2234-glitch/medusa
**Forked from:** https://github.com/Pantheon-Security/medusa
**License:** AGPL-3.0 | **Stars:** ~1K+ | **Language:** Python

## What It Does
AI-first security scanner with 9,600+ detection patterns for AI/ML, agents, and LLM applications. Works out of the box — no tool installation required. 200 CVE detections including Log4Shell, Spring4Shell, XZ Utils, LangChain RCE, MCP-Remote RCE.

## Key Features
- `medusa scan --git <URL>` — scan any GitHub repo for AI supply chain attacks
- 9,600+ AI Security Patterns for AI/ML, agents, MCP servers, RAG pipelines
- Repo poisoning detection across 28+ file types (Cursor, Cline, Copilot, Claude Code, Gemini, Kiro)
- Zero setup required — `pip install` and scan
- Parallel processing (10-40x faster than sequential)
- Cross-platform: Windows, macOS, Linux
- Multiple output formats: JSON, HTML, Markdown, SARIF
- IDE integration: Claude Code, Cursor, VS Code, Gemini CLI
- Smart caching for lightning-fast rescans
- v2026.5.2: security hardening (credential leak fixes, XSS protection, symlink safety)

## OWASP LLM Top 10 Coverage
- Prompt injection (tool-call level)
- Sensitive output exposure
- Model denial of service
- Supply chain vulnerabilities
- Data leakage

## Solomon OS Fit
**INTEGRATE** — Medusa is a core security primitive for Hermes/Solomon OS. The `--git` scan capability can pre-check all incoming skills/repos. AGPL-3.0 license requires careful integration (not direct code use, but operational deployment).

## Recommendation
INTEGRATE — Deploy medusa as pre-flight security scanner for all new skills, repos, and agent installations. Monitor OWASP Top 10 alignment.