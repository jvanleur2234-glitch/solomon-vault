# RD Report: gumbel-ai/agent-debate

**Fork:** https://github.com/jvanleur2234-glitch/gumbel-agent-debate
**Source:** https://github.com/gumbel-ai/agent-debate
**Stars:** ~1K+ | **License:** MIT | **Language:** Shell/Python
**Date:** 2026-04-24

## What It Is
Multi-agent system protocol for adversarial-style technical debates over a shared markdown document. 2-4 AI agents (Claude, Codex, Gemini, Copilot) edit in-place, cite exact evidence (file:line), and track disputes until consensus or escalation. Designed as rigorous code-review/debate framework.

## Key Capabilities
- Shared markdown debate surface with strikethrough/citations
- Evidence-based claims must cite actual code
- Plans phase after debates to finalize recommendations
- Modes: Manual (switch between terminals) or Auto (round-robin until convergence)
- Evidence-based dispute resolution
- Parking-lot for non-core ideas to avoid scope creep

## How It Works
1. Agents propose edits to shared doc
2. Disputes cite exact file:line evidence
3. Agents converge or escalate
4. Optional Plan phase for final recommendations

## Relevance to Solomon OS
- **Multi-agent deliberation:** Adversarial review pattern for Hermes
- **Evidence-based:** Forces agents to ground claims in code/data
- **Audit trail:** Debates stored as markdown files for review
- **MIT:** Commercial use permitted

## Recommendation
**SKILL** — Adversarial deliberation pattern could enhance Hermes quality control. Evidence-based debate ensures high-stakes decisions are well-reasoned. Could power skill validation pipeline.

## License Check
MIT ✅