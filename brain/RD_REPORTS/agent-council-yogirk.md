# RD Report: agent-council by yogirk

## Summary
Lightweight CLI multi-agent deliberation pattern inspired by Karpathy's LLM Council — parallel agents (Claude Code, Codex, Gemini CLI) debate a problem, anonymized peer review, chairman synthesizes. MIT.

## What It Does
- Stage 1: 3 agents work in parallel, independent opinions
- Stage 2: Anonymized peer review (each reviews others without identity)
- Stage 3: Chairman synthesis with consensus + dissent tracking
- CLI-only, file-based state (no heavy framework)
- Structured ADR output with dissent recorded

## Relevance to Solomon OS
- **Multi-agent deliberation for design decisions** — fits Council of High Intelligence competitor category
- Could enhance Hermes skill deliberation workflow
- Useful for architecture decisions where multiple agent perspectives needed
- Deterministic replay with SHA-256 ledger for auditability

## License
MIT

## Stars / Activity
Novel pattern, lightweight alternative to full deliberation frameworks

## Recommendation
**SKILL** — interesting lightweight deliberation pattern. Consider as Hermes deliberation skill module.

## Links
https://github.com/yogirk/agent-council