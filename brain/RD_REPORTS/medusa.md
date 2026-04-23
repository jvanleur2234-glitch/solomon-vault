# MEDUSA — AI Security Scanner

**Repo:** `Pantheon-Security/medusa` | **License:** AGPL-3.0 | **Lang:** Python

## What It Is
AI-first security scanner for AI/ML apps, agents, and LLM workflows. 9,600+ detection patterns, 200 CVE detections (Log4Shell, Spring4Shell, LangChain RCE, MCP RCE).

## Key Capabilities
- `medusa scan --git user/repo` — scan any GitHub repo for AI supply chain risks
- Repo poisoning detection across 28+ file types
- AST + taint analysis, multi-core parallel scanning (10-40x faster)
- SOC2/PCI/DISA compliance evidence collection
- IDE support (VS Code, Claude Code, Cursor, Gemini CLI)
- Multi-format reports: JSON, HTML, Markdown, SARIF

## OWASP LLM Alignment
Maps to OWASP Top 10 for LLM Applications — directly relevant to Hermes agent security posture.

## Solomon OS Fit
- **Security layer:** Could integrate medusa into Hermes as a pre-flight security scan skill
- **MCP security:** MCP remote code execution detection is critical for Hermes' MCP ecosystem
- **LINK fit:** ★★★★☆ — #security #scanner #mcp #owasp

## Action
Already forked. Write RD deep-dive. Add to HERMES_CAPABILITIES as security scanner integration.
