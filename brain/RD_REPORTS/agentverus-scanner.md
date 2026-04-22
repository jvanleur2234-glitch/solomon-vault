# RD Report: agentverus/agentverus-scanner

**Date:** 2026-04-22
**Category:** AI Security Scanner
**License:** MIT
**Type:** TypeScript

## What It Is
Security scanner that analyzes AI agent skills for trust and safety. Performs structured scans to detect prompt injections, data exfiltration, and broad risk signals across 10 threat categories.

## Key Features
- **Permission/capability checks:** filesystem/network/exec vs declared vs inferred
- **Injection + exfiltration risk detection**
- **Dependency + content analysis:** external URLs, downloads, obfuscation
- **Behavioral risk scoring:** escalation, stealth, exfiltration
- **Workspace tampering detection:** AGENTS.md, TOOLS.md, CLAUDE.md, .claude/**
- **Code safety checks:** dangerous eval/exec, exfil patterns

## Why It Matters
- Direct competitor to our AgentArmor Studio skill
- Open-source alternative to commercial agent security products
- Focuses on trust boundary analysis

## Fit for Solomon OS
- **INTEGRATE** — study patterns for Solomon's own security scanner
- **MIT license** ✅
- Could enhance AgentArmor with additional detection rules

## Sources
- https://github.com/agentverus/agentverus-scanner