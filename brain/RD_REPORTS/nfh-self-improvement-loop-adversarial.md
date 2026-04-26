# NFH Self-Improvement Loop — Adversarial Self-Modification

## SLUG: nfh-self-improvement-loop
## Date: 2026-04-26
## Tags: #self-improvement #adversarial #generator #evaluator #MIT
## Status: FORGE

---

## What It Is
theprint/nfh-self-improvement-loop is a minimal adversarial framework enabling an AI agent to modify its own codebase with a separate evaluator judging changes. Key separation: generator (proposes) vs evaluator (judges) prevents self-delusion.

## How It Works
- **Pre-flight checks**: duration timer, fresh dev branch, state.json, prompts present
- **Generator**: reads TOOLS.md, Learnings.md, USER.md, MEMORY.md, proposes one improvement per cycle
- **Evaluator**: receives only git diff + repo context (no rationale), checks viability/safety
- **Categories**: New Capabilities, Optimization, Discovery
- **MIT License** — Shell-based

## Relevance to Solomon OS / Hermes Self-Improvement
- Adversarial loop prevents self-deception — critical for autonomous improvement
- Separation of proposal and evaluation is a key architectural pattern
- Minimal implementation can be integrated into Hermes self-improvement pipeline

## Recommendation
**FORGE** — fork and integrate into Hermes autonomous self-improvement skill.
