# RD Report: Firmis-Scanner — TypeScript AI Agent Security Scanner

**Repo:** https://github.com/Firmislabs/firmis-scanner
**Forked:** Already in workspace (firmis-scanner)
**License:** MIT
**Stars:** Active
**Language:** TypeScript

## What It Is
Runtime security scanner for AI agents detecting malicious behavior and prompt/security threats across multiple platforms. 268 detection rules analyzing code surface (filesystem, network, shell) and instruction surface (prompt/skill descriptions).

## Key Features
- Detects: credential harvesting, prompt injection, tool poisoning, data exfiltration
- Platforms: Claude Skills, MCP servers, Codex plugins
- Zero-configuration setup
- Integrations: LangChain, CrewAI, AutoGen, MetaGPT, n8n
- MIT licensed, TypeScript with strong typing
- Fast scanning with Sardaukar binary

## Solomon OS Fit
**Security pillar.** Directly competes with our existing security scanners (Snyk agent-scan, vigile-scan, agentverus). Firmis adds TypeScript/strong typing angle. Its Sardaukar binary approach is interesting for speed.

## Comparison to What We Have
vs. **snyk/agent-scan**: Both scan AI agents. Firmis is TypeScript-native with more platforms. Snyk has enterprise backing. Complement each other.
vs. **vigile-scan**: Similar coverage. Firmis may have different detection rules.

## Recommendation: SKILL
Add firmis-scanner as an available security scanner option. Its TypeScript foundation makes it potentially integrable into Hermes as a skill. Cross-reference its detection rules with our existing scanners to fill gaps.
