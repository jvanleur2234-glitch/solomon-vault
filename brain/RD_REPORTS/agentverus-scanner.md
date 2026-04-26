# AgentVerus Scanner — AI Agent Trust Boundary Security

## Quick Summary
TypeScript security scanner for AI agent skills. Evaluates trust boundaries, detects prompt injections, data exfiltration, and 10 threat categories. Analyzes agent skill files for security and behavioral risks. MIT licensed.

## What It Is
- Open-source security tool (TypeScript/JavaScript) for evaluating AI agent skills
- Focus: trust boundaries between agent skills and the workspace
- Targets prompt injection, instruction override, relay attacks
- Detects workspace/config tampering (AGENTS.md, TOOLS.md, CLAUDE.md)
- Version 0.7.x with refined severity calibrations

## Key Features
- **Permission/capability contract checks**
- **Injection detection**: prompt injection, instruction override, relay
- **Dependency/content analysis**: external URLs, suspicious downloads, obfuscated content
- **Behavioral risk scoring**: exfiltration, escalation, stealth patterns
- **Code safety**: dangerous blocks, eval/exec, exfil patterns
- **Workspace tampering detection**: flags attempts to modify trust files
- Structured trust reports with risk signals

## Threat Categories (10+)
1. Prompt Injection
2. Tool Poisoning/Shadowing
3. Toxic Flows
4. Credential Exposure
5. Workspace Tampering
6. External URL Access
7. Obfuscated Content
8. Eval/Exec Abuse
9. Data Exfiltration
10. Privilege Escalation

## Solomon OS Fit
- **FORGE** — Critical security primitive for Hermes skill verification
- Trust boundary analysis should run on every skill before Hermes loads it
- MIT license permits direct integration into AgentArmor
- Maps to OWASP LLM Top 10 compliance

## Links
- Repo: https://github.com/agentverus/agentverus-scanner
- License: MIT

## Recommendation
**FORGE** — add to AgentArmor security layer. Should be a pre-flight check for skill loading.