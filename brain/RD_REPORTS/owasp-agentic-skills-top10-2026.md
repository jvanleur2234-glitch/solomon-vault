# RD Report: OWASP Agentic Skills Top 10 — Security Framework

**Date:** 2026-04-23  
**For:** Solomon OS / JCPaid Research  
**Status:** STUDY — Architecture reference only (NOASSERTION license)

## What It Is
OWASP's official security guide for agentic AI skills (ASI01–ASI10) across major platforms: OpenClaw, Claude Code, Cursor, VS Code. Maps to OWASP Top 10 for Large Language Model Applications.

## Key ASI Categories (Agentic Security Issues)
- **ASI01:** Agent Behaviour Hijack (goal hijacking)
- **ASI02:** Tool Misuse & Exploitation
- **ASI03:** Identity & Privilege Abuse
- **ASI04:** Supply Chain Vulnerabilities
- **ASI05:** Unexpected Code Execution (RCE)
- **ASI06:** Memory & Context Poisoning
- **ASI07:** Inter-Agent Communication attacks
- **ASI08:** Cascading Failures
- **ASI09:** Human-Agent Trust exploitation
- **ASI10:** Rogue Agents

## Why It Matters for Solomon OS
This maps the entire OWASP agentic security taxonomy. All security tools we track (sinewave, firmis, agentguard, medusa) should be cross-referenced against ASI01–ASI10. The checklist structure (registry/installation, runtime security, governance/monitoring) is a blueprint for JCPaid enterprise security documentation.

## License
**NOASSERTION** — Study/reference only

## Key Reference
- https://github.com/OWASP/www-project-agentic-skills-top-10

## RD Report
`file 'solomon-vault/brain/RD_REPORTS/owasp-agentic-skills-top10.md'`