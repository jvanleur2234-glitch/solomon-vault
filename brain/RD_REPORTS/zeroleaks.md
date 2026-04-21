# RD Report: zeroleaks

**Date:** 2026-04-21  
**Slug:** zeroleaks  
**License:** FSL-1.1-Apache-2.0  
**GitHub:** https://github.com/zeroleaks/zeroleaks  
**Forked:** https://github.com/jvanleur2234-glitch/zeroleaks  

## What It Is
Autonomous AI security scanner that tests LLM systems for prompt injection vulnerabilities using multi-agent attack simulation. Strategist/Attacker/Evaluator/Mutator/Inspector/Orchestrator architecture.

## Key Features
- **Multi-Agent Architecture** — 6 coordinated agents for attack simulation
- **Tree of Attacks (TAP)** — systematic exploration with pruning
- **Modern attack techniques** — Crescendo, Many-Shot, Chain-of-Thought Hijacking, Policy Puppetry, Siren, Echo Chamber
- **TombRaider Pattern** — dual Inspector for defense fingerprinting + weakness exploitation
- **Defense Fingerprinting** — identifies specific defenses (Prompt Shield, Llama Guard)
- **Dual scan modes** — system prompt extraction + prompt injection testing
- **Bun + TypeScript + Vercel AI SDK + OpenRouter**
- Open source free, hosted option at zeroleaks.ai

## Relevance to Solomon OS
- **Solomon Guardian competitor** — prompt injection testing for Hermes skills
- **OWASP Top 10 compliance** — aligns with 2026 agentic AI risks
- **Multi-agent red team** — could be integrated as pre-deployment security gate
- **Snyk competitor** — CI/CD integrable security scanning

## Comparison
| Feature | ZeroLeaks | AgentSeal | Guard-Scanner |
|---------|-----------|-----------|---------------|
| License | FSL-Apache | FSL | MIT |
| Agents | 6-type | 225+ tests | 364 patterns |
| Focus | Prompt injection | Full spectrum | A2A/MCP |
| Deployment | Bun/TypeScript | Python | TypeScript |

## Recommendation
**INTEGRATE** — High priority for Solomon Guardian. Defense fingerprinting + modern attack techniques (Crescendo, Many-Shot) align with OWASP 2026 findings. Bun/TypeScript stack is production-ready. Fork already created.

## Status
✅ Forked to jvanleur2234-glitch/zeroleaks