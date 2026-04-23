# RD Report: vigile-cli

**Date:** 2026-04-23  
**Repo:** Vigile-ai/vigile-cli  
**Fork:** https://github.com/jvanleur2234-glitch/vigile-cli  
**License:** Apache-2.0  
**Stars:** ~500+ (trending)  
**Category:** AI Security Scanner

## What It Does
Security scanner for AI agent ecosystems — detects tool poisoning, data exfiltration, and supply-chain attacks in MCP servers and agent skills. 59 detection rules across MCP Server Threats (22 patterns) and Agent Skill Threats (32 patterns). Returns trust scores per item.

## Key Features
- MCP server threat detection: tool poisoning, data exfiltration, permission abuse, obfuscation
- Agent skill scanning: instruction injection, malware delivery, stealth operations, safety bypass
- Platform auto-discovery: Claude Desktop/Code, Cursor, GitHub Copilot, Windsurf, VS Code, OpenClaw
- Zero-config: `npx vigile-scan` (no install/config needed)
- JSON output option for CI/CD

## For Solomon OS
- **Use for:** Pre-deployment security scanning of Hermes MCP servers and skills
- **Integration:** Add as guard-scanner skill for agentarmor-studio
- **Complements:** snyk-agent-scan, firmis-scanner, agent-security-scanner-mcp

## LINK Tags
`#security` `#mcp` `#scanner` `#agent-armor` `#hermes`

## Recommendation
**FORGE** — High value security scanner. Integrate with agentarmor-studio's 8-layer security framework.