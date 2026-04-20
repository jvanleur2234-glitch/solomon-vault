# RD Report: MEDUSA Security Scanner

**Repo:** `Pantheon-Security/medusa`  
**License:** AGPL-3.0 | **Lang:** Python  

## What It Does
AI-first security scanner with 9,600+ detection patterns for AI/ML, agents, and LLM applications. Detects repo poisoning, prompt injection, tool poisoning, and 200 CVEs.

## Why It Matters for Solomon OS
- **AI/Agent Focus**: Specifically targets the attack surface AI agents expose
- **Repo Poisoning Detection**: Scans for weaponized AI editor configs (Cursor, Cline, Copilot, Claude Code, Gemini)
- **Zero Setup**: Works immediately after pip install — no external tools needed
- **IDE Integration**: Claude Code, Cursor, VS Code, Gemini CLI support
- **Parallel Processing**: 10-40x faster than sequential scanning

## Key Capabilities
- 9,600+ AI security patterns
- 200 CVE detections (Log4Shell, Spring4Shell, LangChain RCE, MCP-Remote RCE)
- Repo poisoning detection across 28+ file types
- `medusa scan --git <URL>` for remote repo scanning
- Multi-format output: JSON, HTML, Markdown, SARIF
- Cross-platform (Windows, macOS, Linux)

## Comparison to What We Have
vs **agent-security-scanner-mcp**: MEDUSA has more patterns and CVE coverage. MCP scanner has better AI agent integration.

## Recommendation
**SKILL** — Add to Solomon OS security scanning arsenal. Could be integrated into Hermes Guard for pre-deployment checks.

**Category:** #security #scanning #agent-security
