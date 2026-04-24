# RD Report: gumbel-ai/agent-debate — Multi-Agent Technical Debate

**Date:** 2026-04-24  
**Fork:** https://github.com/jvanleur2234-glitch/agent-debate-new  
**Source:** https://github.com/gumbel-ai/agent-debate  
**License:** MIT  
**Stars:** ~120 (v0.5.0 released Apr 2026)  

## What It Does

A protocol and tooling to run multi-agent technical debates on code decisions. 2-4 AI agents (Claude, Codex, Gemini, Copilot) collaboratively edit a shared Markdown document, cite exact evidence (file:line), and log disputes. The system emphasizes adversarial code review rather than free-form chat.

**Key Features:**
- Agents edit a shared markdown file in-place with strikethroughs to show disagreement
- Evidence grounded to concrete code locations (file:line references)
- Disputes tracked in a log; agents must converge or escalate
- Debates are documented and reproducible
- Plan phase optional (default 2 rounds), Manual or Auto mode
- Output: production-ready plan or final decision

## Solomon OS Fit

**SKILL** — This is the deliberation pattern for Hermes. The evidence-grounded debate format is exactly what we need for skill validation and complex decision-making. MIT license permits direct use.

**Specific Use Cases:**
- Skill evaluation before adding to Hermes
- Architecture decisions for Solomon OS
- Multi-provider validation (Solomon can query multiple providers and have them debate the answer)

## Comparison to Existing

- **vs Quorum:** More focused on code decisions with file-level evidence citations
- **vs yogirk/agent-council:** agent-debate is more structured with explicit convergence/escalation mechanics
- **vs dnhess/spectra:** Similar blackboard deliberation but agent-debate has concrete code-grounded evidence

## Recommendation

**FORGE** — This IS the deliberation engine for Hermes. The evidence-based debate pattern is directly implementable. MIT permits direct use. Study and integrate.

## Risk Assessment

- **License:** MIT — fully compatible
- **Activity:** Active (v0.5.0 Apr 2026)
- **Dependencies:** Shell scripts + provider APIs — minimal risk