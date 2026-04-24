# RD Report: slior/dialectic-agentic — Multi-Agent Design Debate System

**Date:** 2026-04-24  
**Fork:** https://github.com/jvanleur2234-glitch/dialectic-agentic-new  
**Source:** https://github.com/slior/dialectic-agentic  
**License:** MIT  
**Stars:** 1 (very early)  

## What It Does

A software system design multi-agent debate tool, implemented as an AI-Agent native application. It runs entirely from agent skill files, prompts, and JSON config — no traditional code required. Multiple AI agents (architect, security, performance, simplicity) debate design problems via structured rounds, with a judge evaluating convergence and synthesizing a final solution.

**Key Features:**
- No code required — runs from SKILL.md + JSON config
- Requires agentic platform with subagent dispatch (Cursor, Claude Code)
- Structured debate workflow: problem → round-based proposals/critiques/refinements → judge convergence → final synthesis
- State stored in human-readable Markdown/JSON
- Configurable agents, convergence criteria, tools, per-agent hints
- Output artifacts: synthesis.md, round proposals/critiques/refinements, verdict.json

## Solomon OS Fit

**SKILL** — Novel deliberation pattern. Can serve as inspiration for Hermes skill validation. The "no code" design is interesting — runs from skill files and prompts. Low stars but the pattern is sound.

**Specific Use Cases:**
- Architecture review before building new capabilities
- Skill evaluation with multi-perspective review

## Comparison to Existing

- **vs gumbel-ai/agent-debate:** dialectic focuses on design problems vs code decisions. More abstract/systems-level.
- **vs agent-council (yogirk):** dialectic uses a judge-based convergence model vs anonymized peer review

## Recommendation

**SKILL** — Study the pattern. The "no code" approach using SKILL.md files aligns with Hermes skill ecosystem. MIT license permits use.

## Risk Assessment

- **License:** MIT — compatible
- **Activity:** Low (1 star, last push Feb 2026) — monitor for activity
- **Dependencies:** Agentic platform (subagent dispatch) — requires Hermes to have equivalent