# agent-debate — Evidence-Grounded Multi-Agent Debate

**Repo:** `gumbel-ai/agent-debate` | **License:** MIT | **Lang:** Python/Shell

## What It Is
Enables 2-4 AI agents (Claude, Codex, Gemini, Copilot) to collaboratively edit and debate a shared Markdown document. Claims must cite evidence (file:line references + logs).

## Key Capabilities
- **Adversarial-but-structured debate** using shared Markdown with strikethroughs for disagreement
- Evidence-backed claims: every statement must cite `file:line` references
- Living-document style debates for technical decisions
- Modes: Manual (terminal switching) or Auto (round-robin until convergence)
- **Plan phase control:** `--no-plan`, `--plan-rounds N`
- Human participation option: `--skip-provider` for human-in-the-loop

## Solomon OS Fit
- **Technical decision-making:** Claude Code + Hermes debate architecture choices — fits Solomon OS R&D workflow
- **Evidence-grounded:** Unlike pure deliberation, this requires code-level citations — rigorous
- **Competitor context:** Part of gumbel-ai ecosystem for agent collaboration
- **LINK fit:** ★★★☆☆ — #debate #evidence #code-review #technical-decisions

## Action
Already forked. Write RD report. Add to HERMES_CAPABILITIES as technical debate tool.
