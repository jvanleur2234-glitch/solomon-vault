# AIBYAI — Multi-Agent Deliberative Council

**Fork:** `Yash-Awasthi/aibyai` → already in workspace (not yet forked)
**Source:** https://github.com/Yash-Awasthi/aibyai (MIT?)
**Date:** 2026-04-25

---

## What It Does

Multi-agent deliberative intelligence platform using a council of 4+ AI agents to debate, critique, and reach scored consensus with transparent confidence scores.

Architecture:
- **Router** — classifies queries and routes to multiple providers (OpenAI, Anthropic, Gemini, Groq)
- **Agents** — Empiricist, Strategist, Historian, Skeptic
- **Conflict Detector** — identifies contradictions between agents
- **Cold Validator** — checks for hallucinations
- **Synthesizer** — merges outputs into scored consensus

Output includes numeric score + breakdown of penalties, reflecting agreement and peer-ranking dynamics.

## Solomon OS Fit

**SKILL** — debate architecture pattern (Empiricist/Strategist/Historian/Skeptic personas) maps to Quorum framework we already have. Confidence scoring is novel. MIT license allows study.

## Status

**SKILL** — study confidence scoring and persona-specific critique patterns for Hermes deliberation skill.