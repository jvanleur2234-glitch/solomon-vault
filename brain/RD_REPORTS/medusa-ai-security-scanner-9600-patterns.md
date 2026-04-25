# Medusa — AI Security Scanner (9600+ Patterns)

**Fork:** `Pantheon-Security/medusa` → already in workspace (not yet forked to GitHub)
**Source:** https://github.com/Pantheon-Security/medusa (AGPL-3.0)
**Date:** 2026-04-25

---

## What It Does

AI-first security scanner with 9,600+ detection patterns focused on AI/ML applications, agents, and LLM systems. New `--git` feature scans GitHub repos for AI supply chain risks, repo poisoning, and MCP tool poisoning across 28+ file types.

Key capabilities:
- 200+ CVEs relevant to AI/ML (Log4Shell, LangChain RCE, MCP RCE, React2Shell)
- Parallel fast scanning with smart caching
- IDE integrations (VS Code, Claude Code, Cursor, Gemini CLI)
- Outputs: JSON, HTML, Markdown, SARIF

## Key Stats

- 9,600+ detection patterns
- 28+ file types scanned
- Multi-core parallel execution (10-40x faster than sequential)
- Zero-setup: `pip install medusa`

## Solomon OS Fit

**INTEGRATE** — Security scanner for pre-execution gate. 9,600 patterns vs sinewave's 1,700 = broader coverage but less agent-specific. AGPL-3.0 (copyleft) — can study patterns but not use code directly in MIT projects.

## Status

**SKILL** — study detection patterns for security skill development. Copyleft license prevents direct code integration.