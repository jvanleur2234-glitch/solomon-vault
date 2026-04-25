# Pantheon-Security/medusa — AI-First Security Scanner (Apr 25, 2026)

**Not yet forked — already in workspace**
**Source:** https://github.com/Pantheon-Security/medusa

## What It Does
9,600+ detection patterns + 200 CVE detections for AI/ML apps, LLM agents, MCP servers:
- Supply chain risks, repo poisoning, prompt injection
- Weaponized AI editor configs
- `medusa scan --git` for GitHub repo security auditing
- Parallel multi-core scanning
- JSON/HTML/Markdown/SARIF output
- VS Code, Claude Code, Cursor, Gemini CLI integrations

## Why It Matters for Solomon OS
- Most comprehensive AI security pattern library found
- Git repo scanning directly useful for Hermes skill security audit
- SARIF + IDE integrations = developer security workflow
- AGPL-3.0 (strongest copyleft — be careful with code reuse)

## Fit: INTEGRATE / SKILL
AGPL-3.0. Use concepts but can't incorporate code directly. Build compatible scanner.

## Action Items
- [ ] Study detection pattern taxonomy for Hermes security layer
- [ ] Consider `medusa scan --git` integration into Hermes skill validation
- [ ] Build compatible-but-original scanner for MIT/Apache ecosystem
