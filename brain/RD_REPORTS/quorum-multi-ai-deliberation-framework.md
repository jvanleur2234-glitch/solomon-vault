# RD Report: Quorum — Multi-AI Deliberation Framework

**Date:** 2026-04-25  
**Category:** Multi-Agent Deliberation  
**Status:** FORGE  

## What It Is

Quorum is a multi-AI deliberation framework that pits multiple AI providers against each other to debate, critique, and refine answers, then produces a synthesized result with confidence scores.

## 7-Phase Process Per Query

1. **Gather:** Independent responses from multiple providers
2. **Plan:** Participants anticipate others' takes
3. **Formulate:** Formal position statements
4. **Debate:** Cross-critique of positions
5. **Adjust:** Revise based on critiques
6. **Rebuttal:** Final push unless consensus
7. **Vote:** Ranked-voting (Borda, ranked-choice, Condorcet)
- **Synthesis phase:** Merges top thinking into final answer + minority report

## Key Features

- Multi-provider support (Claude, GPT, Gemini, Kimi, DeepSeek, Mistral, Ollama, etc.)
- Adaptive debating (auto-skip/extend on disagreement)
- Evidence protocol (sources cited, cross-validated)
- Policy guardrails (YAML rules to block/warn/pause)
- Deterministic replay with SHA-256 ledger for auditability
- Human-in-the-loop control
- MCP server compatibility

## License

MIT

## Why It Matters for Solomon OS

- **Council of High Intelligence:** This IS the deliberation engine for Solomon OS. 7-phase debate maps directly to our planned "Council" mode.
- **Multi-model synthesis:** Handles Claude + Gemini + others in structured debate
- **Auditability:** SHA-256 ledger + deterministic replay = compliance-grade deliberation
- **Minority reports:** Captures dissenting views — important for quality decisions

## Source

- https://github.com/Solvely-Colin/Quorum
- TypeScript-based, MIT licensed, active 2026