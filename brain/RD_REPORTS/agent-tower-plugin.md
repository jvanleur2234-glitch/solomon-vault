# Agent-Tower-Plugin — Multi-Agent Deliberation for Claude Code

**Fork**: `BayramAnnakov/agent-tower-plugin` → already in workspace
**License**: MIT
**Stars**: New
**Language**: TypeScript

## What It Is

A multi-agent deliberation plugin for Claude Code that orchestrates Claude, Codex, and Gemini to provide diverse perspectives on coding tasks.

## Key Features

- **Modes**: 
  - `/tower:council` — Parallel independent agent opinions with anonymous peer ranking + chairman synthesis
  - `/tower:debate` — Adversarial debate between two agents with judge
  - `/tower:deliberate` — Producer/reviewer loop for iterative refinement
- **Backend support**: Claude Code CLI, Codex CLI, Gemini CLI
- **Quick install**: `npx agent-tower-plugin`

## Relevance to Council of High Intelligence

- **Direct pattern match**: Council mode, adversarial debate, producer/reviewer loop
- **Already forked**: Already in workspace — good sign we recognized its value
- **Implementation**: TypeScript plugin for Claude Code — could port patterns to Hermes

## Verdict

🟢 INTEGRATE — Study the prompt patterns and mode structures. Already forked, so focus on extracting deliberation logic for Solomon OS.

**Action**: Read SKILL.md and orchestrator.ts for council/debate implementations.