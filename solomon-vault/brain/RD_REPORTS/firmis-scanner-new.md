# Firmis — Security Scanner for AI Agents (269 Rules)

**Fork:** github.com/jvanleur2234-glitch/firmis-scanner-new  
**Original:** Firmislabs/firmis-scanner  
**License:** Apache-2.0  
**Relevance:** 🔴 Critical — AI agent security

## What It Is
AI agent security scanner covering 9 platforms (Claude Skills, MCP Servers, Codex Plugins, Cursor, CrewAI, AutoGPT, OpenClaw, Nanobot, Supabase). 269 detection rules across 26 threat categories. Free scanner, unlimited.

## Standout Capabilities
- **scan** — Auto-detects framework, no `--platform` flag needed
- **bom** — Generates CycloneDX Agent Bill of Materials
- **ci** — Full pipeline: discover → bom → scan → report
- **pentest** — Active security probing (Pro)
- **compliance** — Maps to SOC2, AI Act, OWASP Agentic Top 10 (Pro)
- **fix** — Guided remediation (free) or auto-fix (Pro)

## Threat Categories (26)
credential-harvesting, data-exfiltration, tool-poisoning, prompt-injection, privilege-escalation, agent-identity-spoofing, supply-chain, access-control, and 18 more.

## Research-Backed Benchmarks
- 31.3% of 10,397 OpenClaw skills had security issues
- Blocks 79% of successful InjecAgent attacks
- 99.09% detection rate on MCP-SafetyBench Layer 1 cases

## Comparison to Peers
| Feature | Firmis | AgentSeal | Vigile |
|---------|--------|-----------|--------|
| Rules | 269 | 225 | 59 |
| Platforms | 9 | 28 | 7 |
| BOM generation | ✅ | ❌ | ❌ |
| Compliance mapping | ✅ | ❌ | ❌ |
| Free tier | Full scanner | Full scanner | Full scanner |

## Solomon OS Relevance
**INTEGRATE** — Most comprehensive of the three scanners. Use Firmis for CI/CD BOM generation + compliance. Layer with AgentSeal for semantic analysis and Vigile for MCP-specific scanning.

## Verdict
INTEGRATE — Best overall coverage. Add to Solomon OS security pipeline: `npx firmis-cli scan` as standard pre-deployment gate for any AI agent component.
