# RD Report: concilium — Multi-LLM Deliberation Platform

**Repo**: `matiasdaloia/concilium`  
**License**: MIT  
**Language**: TypeScript/Node.js  
**Stars**: ~200+ (estimated)  
**Date**: 2026-04-21

## What It Is

Open-source multi-agent deliberation platform that runs several AI coding agents in parallel, has them anonymously peer-review each other, and synthesizes a single high-quality answer. CLI + Electron desktop, local-first, programmatic API.

## Key Features

- **Parallel execution** — prompts sent to multiple agents simultaneously (Claude, Codex, OpenCode)
- **Anonymous peer review** — juror models critique without bias
- **Synthesis** — chairman model combines best parts into validated answer
- **Local-first** — data stays on machine, MIT licensed
- **CLI + desktop** — Electron interface, programmatic API
- **Multi-provider** — Claude, GPT, Gemini, Ollama via OpenRouter

## For Solomon OS / Hermes

- **Deliberation** — could power Solomon's "Council of High Intelligence" reasoning
- **Anonymous review** — quality gate for agent outputs
- **Synthesis** — combines multi-model reasoning into unified answers

## Comparison to Quorum / Council

concilium is simpler than Quorum (fewer phases) but offers anonymous peer review + synthesis. Good lightweight alternative.

## Recommendation

**SKILL** — concilium's anonymous peer review pattern is worth studying for Hermes's quality assurance layer. Lower priority than Quorum but adds diversity to deliberation stack.
