# RD Report: medusa — AI-First Security Scanner

**Original:** `Pantheon-Security/medusa` | **License:** Apache-2.0 | **Stars:** ~1K+ | **Lang:** Python

## What It Is
AI-first security scanner for AI/ML systems, agents, LLM apps, MCP servers. Over 9,600 detection patterns, 200 CVE detections. New `--git` scan analyzes GitHub repos for AI supply-chain attacks.

## Key Capabilities
- 9,600+ detection patterns
- 200 CVE detections (Log4Shell, Spring4Shell, XZ Utils, LangChain RCE, MCP RCE, React2Shell)
- `--git` scan for GitHub repo AI supply-chain attacks
- Parallel multi-core processing
- Smart caching, cross-platform
- Output: JSON, HTML, Markdown, SARIF
- IDE integration (Claude Code, Cursor, VS Code, Gemini CLI)
- Zero-config usage

## Relevance to Solomon OS
- **Security:** Pre-deployment scanning for Hermes MCP servers and skills
- **OWASP Alignment:** LLM01-LLM10 coverage
- **Supply Chain:** Git repo scanning for poisoning

## Threat Analysis
- Apache-2.0 licensed, clean
- Active development, comprehensive CVE coverage
- Strong community adoption

## Integration Path
```
SKILL: guard-scanner → Hermes pre-deployment security scanner
USE CASE: Scan all Hermes skills/MCP servers before production deployment
```

**Recommendation:** FORGE — Comprehensive security scanner with massive pattern database. Aligns with agentarmor-studio 8-layer defense. Add to security stack immediately.