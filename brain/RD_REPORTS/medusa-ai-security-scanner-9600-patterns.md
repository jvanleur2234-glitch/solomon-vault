# Medusa — AI-First Security Scanner (9,600+ Patterns)

**Fork:** `jvanleur2234-glitch/medusa-sec`
**URL:** https://github.com/Pantheon-Security/medusa
**Stars:** 258 | **License:** MIT | **Lang:** Python

## What It Is
AI-first security scanner with 9,600+ detection patterns and 200 CVE detections (Log4Shell, Spring4Shell, XZ Utils, LangChain RCE, MCP RCE, React2Shell). Supports Git repo scanning for supply-chain attacks.

## Key Features
- **9,600+ AI security patterns** — comprehensive coverage
- **200 CVE detections** — including LangChain RCE, MCP RCE
- **Git repo scanning** — `medusa scan --git` for supply-chain/repo poisoning
- **24+ file types** — broad attack surface coverage
- **Parallel multi-core scanning** — 10-40x faster than sequential
- **Zero setup** — works after `pip install`
- **IDE integration** — VS Code, Claude Code, Cursor, Gemini CLI
- **SARIF output** — CI/CD integration

## Why It Matters for Solomon OS
- MCP RCE detection = directly relevant to Hermes MCP security
- LangChain RCE patterns = covers common AI stack vulnerabilities
- Git repo scanning = audit Hermes dependencies before deployment
- OWASP LLM Top 10 aligned

## Solomon OS Fit
**SKILL** — CVE database for AgentArmor Studio. Git repo scanning for Hermes supply-chain audit. Pattern database = comprehensive threat coverage.

## SWARM Score
⭐⭐⭐ (MIT, massive pattern database, MITRE ATLAS aligned)
