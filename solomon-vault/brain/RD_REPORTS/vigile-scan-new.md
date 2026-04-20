# Vigile-Scan — Trust Scoring for MCP Servers & AI Skills

**Fork:** github.com/jvanleur2234-glitch/vigile-scan-new  
**Original:** Vigile-ai/vigile-scan  
**License:** Apache-2.0  
**Relevance:** 🔴 Critical — AI agent security

## What It Is
Security scanner for MCP servers and AI agent skills. Detects tool poisoning, credential theft, data exfiltration, and supply chain attacks with 59 detection rules.

## Key Capabilities
- Auto-discovers MCP configs (Claude Desktop, Claude Code, Cursor, Copilot, Windsurf, VS Code, OpenClaw)
- MCP threats (22 patterns): Tool poisoning, data exfil, permission abuse, obfuscation
- Agent skill threats (32 patterns): Instruction injection, malware delivery, stealth ops, persistence abuse
- Trust scores 0-100 with severity breakdown
- Sentinel runtime monitoring (Pro) — intercepts outbound network for C2 beaconing, credential theft, DNS tunneling

## What Makes It Different
Lightweight, no-install (`npx vigile-scan`), free tier unlimited. Sentinel adds runtime monitoring but free static scanning is comprehensive.

## Comparison
- AgentSeal: 225 probes, semantic analysis, baseline tracking
- Vigile: 59 rules, trust scoring, MCP-first focus, Sentinel runtime
- Firmis: 269 rules, CI/CD BOM generation, compliance mapping

## Solomon OS Relevance
**INTEGRATE** — Add to skill vetting pipeline alongside AgentSeal. Different rule sets = better coverage. Free tier is fully usable.

## Verdict
INTEGRATE — Add to Hermes security stack. Run `npx vigile-scan --all` before activating any third-party MCP server or skill.
