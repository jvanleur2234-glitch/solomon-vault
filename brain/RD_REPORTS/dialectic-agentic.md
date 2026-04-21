# slior/dialectic-agentic — Multi-Agent Design Debate System

**Date:** 2026-04-21  
**Category:** Multi-Agent Deliberation (Council of High Intelligence Competitor)  
**License:** MIT  
**Stars:** ~400  
**Forked:** `/home/workspace/dialectic-agentic`

## What It Does
Configurable, self-contained multi-agent design debate system. Runs as skill files + JSON config — no code required. Expert roles (architect, security, performance, simplicity) debate design problems through structured rounds.

## Key Features
- Role-based agents: architect, security, performance, simplicity, etc.
- Structured rounds: proposals → critiques → refinements
- Judge assesses convergence, synthesis final solution
- Output: debate/synthesis.md + per-round artifacts
- Agentic platform agnostic (needs Task tool + read/write)
- No code required — pure config + skill files

## For Solomon OS / Hermes
- Design review/debate automation for Hermes workflows
- Could power "Hermes Council" deliberation skill
- Structured debate → better architecture decisions than single agent
- Config-only = easy to customize without code

## Recommendation
**SKILL** — Unique approach (debate-as-skill). Could enhance Hermes with structured design review capability. MIT licensed, no dependencies.