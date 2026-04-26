# RD Report: Pilo — Mozilla's AI Browser Automation

**Date:** 2026-04-26
**Original:** mozilla/pilo
**License:** MPL 2.0
**Stars:** ~500 | **Lang:** TypeScript

## What It Is
Mozilla's Tabstack AI agent infrastructure for natural-language browser automation. Works with Playwright, supports cloud AI (OpenAI, OpenRouter) and local providers. Guardrails to constrain actions.

## Key Capabilities
- Natural language task description → browser automation
- Works with Playwright + CLI or programmatic API
- Safety guardrails to prevent harmful actions
- Structured data inputs for task execution
- Multi-turn task execution with starting URLs

## Threat Analysis
- Mozilla-backed, MPL 2.0 license (permissive but not MIT)
- Active development, v0.18.0 March 2026
- No security issues identified

## Comparison to Browser Stack
- Similar to Browserable/HyperAgent but Mozilla-backed
- Guardrails approach similar to AgentArmor Studio
- Natural language → Playwright matches Solomon Browser concept

## Integration Path
```
SKILL: pilo → Mozilla-backed browser automation skill for Hermes
USE CASE: Production-grade browser automation with enterprise backing
```

**Recommendation:** SKILL — Mozilla brand adds credibility. Good alternative to Browserable/HyperAgent.