# RD Report: agentverus/agentverus-scanner

**Date:** April 26, 2026  
**Forked:** Already in workspace  
**License:** MIT  
**Latest:** v0.7.1 (Mar 2026)  

## What It Is
Security and behavioral trust scanner for AI agent skills. Analyzes skill files to detect prompt injection, data exfiltration, and trust-boundary risks across 10 threat categories.

## Key Capabilities
- **Permission + capability contract checks** (declared vs inferred behavior)
- **Injection detection:** Prompt injection, instruction override, relay
- **Dependency + content analysis:** External URLs, suspicious downloads, obfuscated/hidden content
- **Behavioral risk scoring:** Exfiltration risks, escalation, stealth patterns
- **Code safety:** Dangerous blocks, eval/exec, exfil patterns
- **Workspace config tampering detection:** AGENTS.md, TOOLS.md, CLAUDE.md, .claude/** modifications

## Solomon OS Fit
**INTEGRATE** — Direct complement to AgentArmor Studio. Their "workspace config tampering" detection (AGENTS.md modification detection) is exactly what we need for Hermes hardening. Trust reports with severity tiers align with our security posture documentation.

## Differentiation from snyk/agent-scan
- agentverus focuses on **skill-level trust contracts** (capability declarations vs actual behavior)
- Snyk focuses on **installed agent configurations** (MCP servers, skills on disk)
- Both are valuable; we need both for full coverage

## Action
Study. Add trust contract checking to AgentArmor Studio Layer 3 (capability verification).