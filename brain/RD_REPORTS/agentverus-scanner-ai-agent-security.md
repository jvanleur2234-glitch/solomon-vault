# agentverus-scanner — AI Agent Trust & Safety Scanner

## SLUG: agentverus-scanner
## Date: 2026-04-26
## Tags: #AI-security #agent-scanner #prompt-injection #trust-boundary #MIT
## Status: SKILL

---

## What It Is
AgentVerus Scanner (agentverus/agentverus-scanner) is an open-source security tool that evaluates AI agent skills for trust and safety. Analyzes skill files to detect prompt injection, data exfiltration, and 10+ threat categories.

## Key Capabilities
- **Permission/capability analysis**: checks declared permissions vs inferred behavior
- **Injection/exfiltration detection**: flags prompt injection, instruction overrides, relay attempts
- **Dependency/content analysis**: inspects URLs, downloads, obfuscated content, eval/exec patterns
- **Behavioral risk scoring**: escalation, stealth, misbehavior patterns
- **Workspace tampering detection**: monitors AGENTS.md, TOOLS.md, CLAUDE.md modifications
- **MIT License** — v0.7.1 (Mar 2026)

## Relevance to Solomon OS / AgentArmor
- Directly competitive with AgentArmor scanner
- Monitors workspace tampering — critical for Hermes AGENTS.md integrity
- Trust-boundary scoring aligns with AgentArmor security posture

## Recommendation
**SKILL** — integrate into AgentArmor as complementary scanner, study trust-boundary scoring algorithm.
