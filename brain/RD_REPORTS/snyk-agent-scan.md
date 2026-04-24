# RD Report: snyk/agent-scan

**Already Forked:** jvanleur2234-glitch/agent-scan  
**License:** Apache-2.0 | **Language:** Python  
**Date:** 2026-04-24

## What It Is
Snyk's open-source security tool that discovers and scans AI agent components (MCP servers, tools, agent skills) for prompt injections, malware, sensitive data handling, and other risks.

## Relevance to Solomon OS
- Agent component inventory and security auditing
- Multi-agent platform support (Windsurf, Cursor, Claude Code, etc.)
- 15+ risk types across MCPs and skills
- Production security posture for AI agents

## Key Capabilities
- Auto-discovers MCP configurations, agent tools, and skills
- Scans 15+ risk types (Prompt Injection, Tool Poisoning, Tool Shadowing, Toxic Flows)
- Supports macOS, Linux, Windows
- Snyk integration for vulnerability database
- --skills flag for comprehensive scanning

## Competitive Analysis
Snyk brand credibility. Deep integration with Snyk's vulnerability database. Best for production security monitoring.

## Recommendation
**INTEGRATE** — Use as security monitoring layer. Snyk integration gives access to CVE database.

## License Check
Apache-2.0 ✅