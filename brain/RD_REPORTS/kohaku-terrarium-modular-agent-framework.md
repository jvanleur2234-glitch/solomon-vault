# RD Report: KohakuTerrarium

**Repo:** `DNLINYJ/KohakuTerrarium`
**Fork:** `jvanleur2234-glitch/KohakuTerrarium`
**Date:** 2026-04-26
**License:** KohakuTerrarium-1.0 (custom, MIT-like)
**Stars:** ~2.5K+
**Status:** SKILL

## What it does
Framework for building "real agents" (creatures) not LLM wrappers. Each creature has its own controller, input, output, tools, triggers, sub-agents, and memory. Multiple creatures compose into a "terrarium" (horizontal multi-agent wiring layer).

## Key features
- Modular agent architecture — configure prompts + modules without rebuilding runtime
- Built-in session persistence + resume (stores operational state, not just chat)
- Scratchpad + persistent history with FTS and vector-based memory search
- Non-blocking auto-compaction for long-running agents
- CLI, TUI, web UI, desktop app — multiple runtimes
- kt-defaults package: ready-to-use coding agent runtime

## Why it matters
- Creature/Terrarium model is a clean separation of concerns vs flat agent wrappers
- Session persistence = exactly what Solomon OS agents need for interrupted task resume
- Modular config-driven approach aligns with Hermes SKILL.md pattern
- Active ecosystem with plugins and creature marketplace

## Solomon OS fit
**SKILL** — Study the creature model for Hermes skill encapsulation. Session persistence mechanism directly applicable to mission-critical agent workflows. Terrarium wiring pattern could replace simpler orchestration.

## Competitor analysis
Direct competitor to: smolagents, CrewAI, AutoGen — but starts at the agent layer, not above. More composable than most.

## Action
Forked. Deep-read `kt-defaults` package for OOTB creature patterns.
