# slior/dialectic-agentic — Multi-Agent Design Debate

## Metadata
- **URL:** https://github.com/slior/dialectic-agentic
- **License:** MIT
- **Status:** ALREADY FORKED

## What It Does
No-code agent-native system for software design debates. Runs as skill files, prompts, and JSON config. Assigns expert roles (architect, security, performance, simplicity) to debate design problems through structured rounds.

## Workflow
- Agents propose solutions → critique each other → refine positions across rounds
- Judge evaluates convergence; debate ends on consensus or round cap
- Final solution synthesized by judge

## Output Artifacts
- `debate/synthesis.md` — final solution
- `debate/round-N/proposals/` — each agent's proposal per round
- `debate/round-N/critiques/` — critiques
- `debate/round-N/verdict.json` — convergence assessment

## Solomon OS Fit
- **SKILL** — Structured design review pattern for Hermes skill development
- Could validate skill designs with multiple expert perspectives before deployment
- No-code nature fits Hermes skill framework model

## Action
Already forked. Study structured debate format for Hermes skill validation workflow.