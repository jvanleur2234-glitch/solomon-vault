# Self-Improving-Agent (Grail-Computer) — npx Skill Template

## SLUG: grail-computer-self-improving-agent
## Date: 2026-04-26
## Tags: #self-improvement #skill #npx #AGENTS-md #template
## Status: SKILL

---

## What It Is
Grail-Computer/Self-Improving-Agent is a self-improving agent template using AGENTS.md as repository memory with codebase map, local norms, guardrails, patterns, and self-correction protocol. Installed via `npx skills add`.

## Core Pattern
- **AGENTS.md**: read at session start, guides navigation and behavior
- **Self-improving-agent skill**: reflects after tasks, updates AGENTS.md, creates new skills
- **Compounding loop**: Work → Complete → Reflect → Record → Next task starts from better baseline

## Structure
- `AGENTS.md`: repository-wide context and self-correction rules
- `skills/self-improving-agent/SKILL.md`: meta-skill for self-improvement

## Relevance to Solomon OS / Hermes
- Template-based approach fits Hermes skill ecosystem perfectly
- AGENTS.md pattern already used in Hermes
- Self-improvement skill can be directly installed as Hermes capability

## Recommendation
**SKILL** — add to Hermes skill hub as self-improvement meta-skill.
