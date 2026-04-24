# RD Report: m2star

**Repo:** lamenting-hawthorn/m2star
**Forked:** https://github.com/jvanleur2234-glitch/m2star
**License:** MIT
**Stars:** ~200
**Relevance:** self-improvement, skill framework, Claude Code

## What It Is
Skill pack for Claude Code implementing a self-learning agent loop. Claude extracts feedback, conventions, and project context into persistent memory (sessions.tsv) that survives across sessions. Implements /self-learn, /self-review, /discover-conventions, /chain, /reflect, /escalate, /quality-dashboard commands.

## Key Features
- Self-Learn: saves feedback/conventions to sessions.tsv at end of every session
- Self-Review: checks correctness, conventions, completeness, blast radius before shipping
- Discover Conventions: scans new codebase, infers patterns, saves to memory
- Quality Dashboard: computes metrics (success rate, correction rate, trends) from sessions.tsv
- Experiment Chain: autonomous hypothesis-test-keep/revert loop (hill-climbing)
- m2star-loop.sh: runs experiment iterations autonomously overnight
- Memory auto-loads each session → Claude avoids past mistakes
- Escalate command: configure autonomy level (conservative/balanced/aggressive)

## Relevance to Solomon OS / Hermes
- Directly maps to Hermes's self-improvement loop capabilities
- Quality Dashboard metric tracking could enhance Solomon OS heartbeat reporting
- Discover conventions → similar to Hermes's skill discovery mechanism
- Experiment chain → autonomous testing framework for Solomon OS components

## Potential Uses
- Implement quality metrics in Solomon OS heartbeat (success rate, correction rate)
- Use as template for Hermes's /self-learn equivalent skill
- Experiment chain for autonomous testing of Solomon Browser / JackConnect

## Recommendation
**SKILL** — Strong defaults pattern (123 skills out of box). Study quality dashboard implementation for Solomon OS metrics.

## Related
- ai-agent-blueprint (sentinel-dev2026) — same orchestrator + PDCA concept
- NFH self-improvement loop — adversarial generator/evaluator pattern
