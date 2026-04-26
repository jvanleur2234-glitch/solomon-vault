# RD Report: AgentVerus Scanner

**Repo:** `agentverus/agentverus-scanner`  
**URL:** https://github.com/agentverus/agentverus-scanner  
**License:** TypeScript (license not explicitly stated — verify before fork)  
**Stars:** Unknown  
**Date:** 2026-04-26

## What It Is
Open-source security scanner that analyzes AI agent skills for trustworthiness. Detects prompt injections, data exfiltration, and 10 ASST threat categories that traditional AV misses.

## Key Capabilities
- Scans SKILL.md and variants for permission/capability contract checks
- Detects injection risks: prompt injection, instruction override, relay
- Dependency and external-URL risk analysis
- Behavioral risk: exfiltration, escalation, stealth patterns
- Code safety: dangerous blocks, eval/exec, exfil patterns
- Workspace/config tampering detection (AGENTS.md, TOOLS.md, CLAUDE.md, .claude/**)
- Content analysis: obfuscation, concealment, social engineering
- Trust reports with risk scoring and capability contracts

## Relevance to Solomon OS
**HIGH** — Directly relevant to Hermes skill ecosystem. Can be integrated as a guard-scanner skill to audit incoming skills for trust boundaries before activation. OWASP LLM Top 10 aligned.

## Use Case for JCPaid/Hermes
Install as pre-flight skill scanner: any skill added to Hermes gets audited automatically. Closes LLM01 (Prompt Injection), LLM06 (Excessive Agency), LLM07 (System Prompt Leakage) gaps.

## Integration Path
- Fork and add to Hermes as `agentverus-scanner` skill
- Run on every skill install/update: `agentverus-scanner scan ./skills/<name>`
- Wire output into Hermes trust score display

## Comparison to Existing
- More focused on agent skills than generic SAST tools
- Covers workspace tampering — unique angle vs firmis-scanner, agentguard

## Verdict
**SKILL** — High value for security posture. Integrate into Hermes skill marketplace quality gates.

## Action Taken
Already cloned in workspace. Fork and SKILL entry to be added.