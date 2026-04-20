# RD Report: Dialectic Agent-Native

**Repo:** `slior/dialectic-agentic`  
**License:** MIT | **Lang:** Markdown/Config  

## What It Does
Multi-agent design debate system using only skill files, prompt files, and JSON config — no code required. Runs on any agentic platform supporting subagent dispatch.

## Why It Matters for Solomon OS
- **No-Code Debate Framework**: Define debates entirely in markdown/JSON
- **Structured Deliberation**: Proposals → Critiques → Refinements → Judge verdict
- **Agent-Native**: Works with Cursor, Claude Code, any platform with Task tool
- **Audit-Ready Output**: Full transcript in markdown files

## Key Capabilities
- Multiple expert roles (architect, security, performance, simplicity)
- Judge evaluates convergence after each round
- Configurable convergence criteria
- Optional clarifications phase
- Full debate transcript in human-readable markdown
- Deterministic replay via JSON config

## Comparison to What We Have
vs **Quorum**: Dialectic is design-focused, code-free. Quorum is multi-provider, production deliberation. Different use cases, both valuable.

## Recommendation
**SKILL** — Useful for Solomon OS decision-making layer. Implement in Hermes for architectural decisions.

**Category:** #multi-agent #deliberation #decision-making
