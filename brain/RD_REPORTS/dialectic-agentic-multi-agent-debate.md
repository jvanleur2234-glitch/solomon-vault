# RD Report: dialectic-agentic — Multi-Agent Design Debate Framework

## Summary
No-code multi-agent debate system for design problems. Uses separate agent skill files, JSON config, Markdown state — runs on any agentic platform (Cursor, Claude Code).

## What It Is
Defines a design problem, engages specialized agents (architect, security, performance, simplicity) to propose/critique/refine via structured debate rounds. Judge evaluates convergence. Ends when agreement reached or round limit hit.

## Key Features
- **No-code**: define debates via Markdown problem statement + JSON config
- **Agent roles**: architect, security, performance, simplicity (configurable)
- **Judge-based convergence**: evaluates after each round
- **Debate phases**: proposal → critique → refinement → verdict → synthesis
- **Runs on any agentic platform** with subagent dispatch + file I/O
- **Optional tools**: web_search, MCP servers configurable per-agent

## License
MIT (inferred)

## Relevance to Solomon OS / Hermes
- Could be Hermes skill for architectural decision-making
- No-code debate definition maps to Hermes SKILL.md format
- Could power "Council of High Intelligence" deliberation layer

## Verdict
**SKILL** — Study for Hermes deliberation/synthesis capability. No-code format adaptable to skill definition.

## Fork
Not yet forked — needs clone + fork.
