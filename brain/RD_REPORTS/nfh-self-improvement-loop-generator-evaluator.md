# theprint/nfh-self-improvement-loop — Minimal Adversarial Self-Improvement Framework (MIT)

## Quick Summary
Minimal adversarial framework where an AI agent modifies its own codebase while a separate evaluator judges if the change is beneficial. Strict separation: generator proposes one improvement per cycle, evaluator reviews diff without context.

## What It Does
- **Generator (proposer)**: context-aware agent inspects workspace (TOOLS.md, Learnings.md, USER.md, MEMORY.md, projects/, skills) and proposes one improvement per cycle
- **Evaluator (judge)**: separate model reviews git diff and codebase to determine if change is valuable, non-duplicative, safe
- **Pre-flight checks**: timers, fresh dev branch, state.json, prompts, executable verifier
- **Improvement categories**: New Capabilities, Optimization, Discovery
- **Constraints**: no edits to identity/memory files, no external API calls, no pushes to main, no cross-cycle leakage

## Architecture Highlights
- Production-tested loop to prevent runaway behavior
- Strict evaluator isolation to reduce bias and risk
- Changes prepared on dev branch, not directly pushed to main

## Relevance to Solomon OS
- **SKILL** — Self-improvement governance pattern for Hermes evolution loop. The generator/evaluator separation provides a template for safe autonomous improvement.
- Pre-flight checks and rollback mechanisms are directly applicable

## License & Status
- **License:** MIT
- **Latest:** v1.0.0 (April 13, 2026)
- **Repo:** https://github.com/theprint/nfh-self-improvement-loop

## Verdict
**SKILL** — Study the generator/evaluator separation pattern for Hermes self-improvement governance. Clean MIT implementation of safe autonomous improvement.
