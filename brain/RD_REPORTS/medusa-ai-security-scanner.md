# RD Report: Medusa — AI-First Security Scanner

**Repo:** https://github.com/Pantheon-Security/medusa
**Forked:** Already in workspace (medusa)
**License:** AGPL-3.0
**Stars:** Active
**Language:** Python

## What It Is
AI-first security scanner for AI/ML and LLM-enabled projects, agents, and MCP servers. 9,600+ AI security patterns, 200 CVE detections, GitHub repo scanning for supply chain attacks. No setup required, cross-platform, multi-format output.

## Key Features
- 9,600+ AI security patterns
- 200 CVE detections (Log4Shell, LangChain RCE, etc.)
- GitHub repo scanning (--git) for supply chain attacks
- No setup: pip install and run
- Fast, multi-core with caching
- IDE integration (Claude Code, Cursor, VS Code)
- SARIF, JSON, HTML, Markdown output
- AGPL-3.0 (not MIT — note for commercial use)

## Solomon OS Fit
**Security pillar.** Complements Snyk/agent-scan, firmis-scanner. Medusa's 9,600+ patterns is the largest coverage seen. Note AGPL-3.0 license — not MIT/Apache, may have share-alike implications for Solomon OS.

## Recommendation: SKIP (License)
Pattern is valuable but AGPL-3.0 is problematic for commercial products. Monitor but don't integrate.
