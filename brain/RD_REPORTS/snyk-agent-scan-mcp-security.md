# snyk/agent-scan — AI Agent Security Scanner

## SLUG: snyk-agent-scan
## Date: 2026-04-26
## Tags: #AI-security #MCP #skills #scanner #prompt-injection #Apache-2.0
## Status: SKILL

---

## What It Is
snyk/agent-scan is an open-source security scanner for AI agents, MCP servers, and agent skills. Discovers and inventories installed AI agent components and scans them for security risks.

## Key Capabilities
- **Auto-discovers MCP configurations**, agent tools, and skills
- **Scans popular agents**: Claude, Cursor, Windsurf, Gemini CLI, Amp, Amazon Q
- **15+ risk categories** for MCPs (Prompt Injection, Tool Poisoning, Tool Shadowing, Toxic Flows)
- **Skills risk categories**: Prompt Injection, Malware Payloads, Untrusted Content, Credential Handling
- **Apache-2.0 License** — Python-based

## Relevance to Solomon OS / AgentArmor
- Industry-standard scanner from Snyk adds credibility
- MCP server scanning directly applicable to Hermes MCP integration
- Skill risk categories align with AgentArmor skill vetting

## Recommendation
**SKILL** — integrate into AgentArmor workflow, add to Hermes skill installation pipeline.
