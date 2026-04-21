# RD Report: Grail-Computer/Self-Improving-Agent

**Date:** 2026-04-21  
**Fork:** jvanleur2234-glitch/Self-Improving-Agent  
**License:** MIT  
**Category:** Self-Improving Agent Template  
**Stars:** Novel (template-based)  
**Relevance:** 🟡 Worthwhile — AGENTS.md Compounding Pattern

## What It Is

A minimal starter template for making any AI coding agent compound in effectiveness over time. Paste into any project via `npx skills add` URL. Two files only: `AGENTS.md` (repo memory) + `skills/self-improving-agent/SKILL.md` (meta-skill).

## Key Capabilities

- **AGENTS.md** — Always-on context file agents read at start of every session
  - Codebase Map (navigation)
  - Local Norms (build, test, style rules)
  - Guardrails (what agents must never do)
  - Patterns & Gotchas (hard-won knowledge)
  - Self-Correction Protocol (how this file stays alive)

- **self-improving-agent SKILL.md** — Meta-skill teaching agents how to improve
  - Post-task reflection (diagnose what to improve)
  - Updating AGENTS.md (map, norms, gotchas)
  - Creating new skills from repeated workflows
  - Quality validation for improvements

## The Compounding Loop

```
Work → Complete → Reflect → Record → Next task starts from a better baseline
```

Each improvement makes future improvements easier.

## Solomon OS Fit

**INTEGRATE** — The `AGENTS.md` + self-improving-agent pattern is the exact mechanism Solomon OS brain files should use. This is simpler than T33R0 but establishes the core pattern: agents that compound effectiveness by recording lessons.

**Already have similar:** `brain/SOUL.md`, `brain/AGENTS.md` in Solomon Vault — this template validates the approach and provides the meta-skill implementation.

**Synergy:** Use alongside RangeKing/self-evolving-agent (capability promotion) + T33R0 (self-correction ledger) for full stack

## Status

**INTEGRATE** — Adopt the self-improving-agent SKILL.md pattern into Solomon OS skill ecosystem