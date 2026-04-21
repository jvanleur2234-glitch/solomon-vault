# RD Report: Council of High Intelligence — 18 AI Personas Debating Your Hardest Decisions

**URL:** https://github.com/0xNyk/council-of-high-intelligence
**Date:** 2026-04-20
**Platform:** GitHub + X/Twitter
**Stars:** 136 (growing, MIT)
**License:** MIT

## What It Is
A multi-perspective reasoning framework where 18 AI personas (Aristotle, Feynman, Kahneman, Torvalds, Sun Tzu, Ada Lovelace, Marcus Aurelius, Machiavelli, Lao Tzu, Socrates, Miyamoto Musashi, Alan Watts, and more) deliberate across multiple LLM providers to produce structured verdicts with unresolved questions and next steps.

The tagline: "If your agent stack always agrees, it's probably lying to you."

Core features:
- Multi-provider auto-routing: Claude, OpenAI, Gemini, Ollama — different models for genuine diversity
- Deliberation protocol: polarity pairs, problem restatement, dissent quotas, counterfactual prompts
- Three deliberation modes + unified command: `/council`, `/council --quick`, `/council --duo`, `/council --triad [domain]`, `/council --full`, `/council --members name1,name2,...`
- 11 predefined domain triads (Architecture → Aristotle+Ada+Feynman; Strategy → Sun Tzu+Machiavelli+Aurelius; etc.)
- Built for Claude Code but agent-agnostic

Also available as an OpenClaw skill: openclaw/skills/skills/0xnyk/council-of-high-intelligence/SKILL.md

## What We'd Use It For
1. **Strategic decisions for Solomon OS** — when facing hard choices (e.g., which vertical to pursue, which tech to adopt), run /council to get multi-perspective analysis
2. **Client decision support in AI Employee Agency** — JackConnect could include /council as a premium feature for big decisions
3. **Russell Tuna integration** — teach Russell Tuna to invoke the council for complex tasks
4. **Solomon Bus deliberation** — overnight worker could run council on tomorrow's priorities

## Compares to What We Have
- Solomon OS brain/ files: ad-hoc reasoning, single perspective
- Agency Agents 147 personas: general roles, no structured deliberation
- pm-skills: PM-specific workflows, no multi-model debate
- Council of High Intelligence: structured multi-round deliberation with dissent enforcement — unique in the ecosystem

## Recommendation
🟡 SKILL — Clone to /Skills/council-of-high-intelligence/. Add as a Solomon OS decision-making skill. Study the deliberation protocol for potential integration into Solomon Bus overnight loop.

Install: `claude plugin marketplace add 0xNyk/council-of-high-intelligence` or clone directly.

Also: follow 0xNyk for related tools (xint CLI, mission-control, lacp, truthlens) — they're building a coherent agent infrastructure stack.