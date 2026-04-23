# RD Report: claude-synod-debate — Multi-Agent Judicial Deliberation

**Date:** 2026-04-23  
**Classification:** SKILL  
**License:** MIT  
**Stars:** ~500+  
**Fork:** https://github.com/jvanleur2234-glitch/claude-synod-debate

---

## What it is

A multi-agent deliberation system that orchestrates Claude, Gemini, and OpenAI in a structured 4-phase judicial debate (Solver → Critic → Defense → Synthesis) to produce higher-quality decisions than any single model.

## Key Capabilities

- **4-Phase Judicial Debate:** Solver (parallel), Critic (cross-validation with CRIS trust scores), Defense (adversarial court), Synthesis (weighted confidence)
- **CRIS Trust Score:** C × R × I / S formula for credibility, reliability, intimacy, self-orientation
- **SID Format:** Structured confidence scoring with semantic focus per agent
- **Multi-Model Ensemble:** Claude (orchestrator/judge), Gemini (architect), OpenAI (explorer)
- **5 Modes:** review, design, debug, idea, general — auto-classified
- **Claude Code Plugin:** /synod command for direct integration

## What we'd use it for

- High-stakes business/technical decisions requiring multi-perspective validation
- Architecture reviews for Solomon OS components
- Security threat modeling with adversarial court model

## Comparison to what we have

- More rigorous than our existing council/deliberation setups — formal phase structure with trust scoring
- Adversarial defense/prosecution pattern is novel
- CRIS trust scoring gives quantifiable confidence vs. our subjective deliberations

## Recommendation: SKILL

MIT licensed. Sophisticated deliberation algorithm. Forked. Would integrate as a /synod skill for Hermes or as a decision-making component in Solomon OS workflow.