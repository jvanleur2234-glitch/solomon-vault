# AI-Infra-Guard — Tencent Full-Stack AI Red Teaming Platform

**Fork:** `jvanleur2234-glitch/ai-infra-guard`
**Original:** https://github.com/Tencent/AI-Infra-Guard
**Stars:** 3,574 | **License:** Apache 2.0 | **Lang:** Python

## What It Is
Tencent's comprehensive AI security platform — a "full-stack AI red teaming" framework that scans AI pipelines, agents, skills, and infrastructure for vulnerabilities. It's essentially a Snyk/Qualys for the AI stack.

## Key Components
- **OpenClaw Security Scan (ClawScan)** — vulnerability auditing for AI pipelines
- **Agent Scan** — security posture assessment for deployed AI agents
- **Skills Scan** — capability/risk profiling for AI skills/modules
- **MCP Server & Agent Skills Scan** — validates MCP ecosystem security
- **LLM Jailbreak Evaluation** — red-teams prompt resistance
- **AI Infra Scan** — CVE coverage for AI infrastructure

## Why It Matters for Solomon OS
- OWASP LLM Top 10 aligned
- Covers the exact surfaces Hermes exposes (agents, skills, MCP)
- Docker-based deployment = one-command scan
- CVE database integration means it's always up to date
- Integrates with OpenClaw workflows

## Solomon OS Fit
**INTEGRATE** — Primary security scanner for Hermes/JCPaid. Agent Scan + Skills Scan directly map to our agent ecosystem. MCP scan validates our MCP server integrations. Jailbreak eval for prompt hardening.

## Action
Pull capabilities into AgentArmor Studio. Consider as primary security layer for enterprise JCPaid deployments.

## SWARM Score
⭐⭐⭐⭐⭐ (3,574 stars, Tencent backing, comprehensive coverage)
