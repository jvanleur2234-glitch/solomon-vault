# RD Report: Firmis — Runtime Security Scanner for AI Agents

**Date:** 2026-04-25
**Repo:** Firmislabs/firmis-scanner
**Fork:** jvanleur2234-glitch/firmis-scanner
**License:** Apache 2.0
**Language:** TypeScript
**Stars:** ~18 (as of search)

## What It Is
Runtime security scanner for AI agents. Detects malicious behavior, credential harvesting, prompt injection, tool poisoning across 268 detection rules. Scans Claude Skills, MCP Servers, Codex Plugins, Cursor, and more.

## Key Features
- 268 detection rules across credential harvesting, prompt injection, tool poisoning, code injection, sandbox escapes
- Platform coverage: Claude Skills, MCP Servers, Codex Plugins, Cursor, LangChain, CrewAI, AutoGen, n8n
- Code surface analysis: file access, network calls, shell usage
- Instruction surface analysis: SKILL.md, AGENTS.md, tool descriptions
- SOC2/GDPR compliance evidence collection
- AST-based static analysis
- MITRE ATT&CK + CWE mappings
- Zero-config: `npx firmis-cli scan`
- No API key required

## Solomon OS Fit
- **INTEGRATE** — Apache 2.0 license. Strong security posture for JCPaid skill deployment. Pre-deployment gate for Hermes skills. Closes the "which skills are safe" question.

## Comparison
| Feature | Firmis | Snyk Agent Scan | MEDUSA |
|---------|--------|-----------------|--------|
| License | Apache 2.0 | Apache 2.0 | MIT |
| Rules | 268 | 15+ categories | 9600+ patterns |
| Platforms | Broad | Broad | Broad |
| SOC2/GDPR | Yes | Partial | No |
| API Key | No | Yes (Snyk) | No |

## Recommendation
**INTEGRATE** — Apache 2.0 security scanner for Hermes skill deployment. No API key needed, runs locally.
