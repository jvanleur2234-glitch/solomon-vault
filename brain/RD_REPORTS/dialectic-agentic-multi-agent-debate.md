# RD Report: dialectic-agentic

**Date:** 2026-04-23  
**URL:** https://github.com/slior/dialectic-agentic  
**Fork:** `jvanleur2234-glitch/dialectic-agentic` (already forked)  
**License:** MIT  

## What It Does
Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Multiple agents (architect, security, performance, simplicity) take turns proposing, critiquing, and refining. Judge evaluates convergence. Outputs full debate transcript + synthesis.

## Core Components
- `problem.md` — design problem statement
- `debate/round-N/proposals` — each agent's proposal per round
- `debate/round-N/critiques` — critiques of proposals  
- `debate/synthesis.md` — final synthesized solution
- `debate-config.json` — agent config, convergence criteria, tools

## Key Patterns
- 7-phase debate: propose → critique → refine → converge
- Agents are personas (architect, security, critic, etc.)
- Judge evaluates convergence or round limit reached
- Works inside agentic platforms (Cursor, Claude Code) via Task tool

## Solomon OS Fit
**FORGE** — Deliberation pattern directly maps to "Council of High Intelligence" concept. MIT license permits direct use. Skill-file based architecture is compatible with Hermes skill ecosystem.

## Status
**FORGE** — Implement deliberation pattern for Hermes skill validation and architectural decisions.
