# KohakuTerrarium — Modular Python Agent Framework (Creatures + Terrariums)

**Local study**
**URL:** https://github.com/DNLINYJ/KohakuTerrarium
**License:** MIT | **Lang:** Python

## What It Is
A Python general-purpose agent framework built around "creatures" (agents) and "terrariums" (multi-agent ecosystems). Each creature has its own controller, input, output, tools, triggers, sub-agents, and memory. Can operate standalone or wired into terrariums.

## Key Features
- **Modular agent architecture** — build customized creatures with only needed modules
- **Session persistence + resume** — operational state stored, supports long-running tasks
- **Scratchpad + persistent memory** — searchable session history, FTS or vector-based retrieval
- **Non-blocking auto-compaction** — background context pruning for long-running agents
- **Rich toolset + sub-agents** — file, shell, web, JSON, search, editing, planning
- **Multiple runtime surfaces** — CLI, TUI, web, and desktop apps
- **Reusable creatures + plugins** — ecosystem of ready-to-use kt-defaults

## Why It Matters for Solomon OS
- Memory/session persistence = directly applicable to Hermes long-running sessions
- Auto-compaction = solves context overflow for Solomon OS 24/7 operation
- Plugin ecosystem model = how Hermes skills could be packaged
- Sub-agent pattern = multi-agent Solomon OS architecture

## Solomon OS Fit
**SKILL** — Study memory management + session persistence for Hermes 24/7 operation. Auto-compaction for context overflow prevention. Plugin architecture for Hermes skill ecosystem.

## SWARM Score
⭐⭐⭐ (MIT, novel modular architecture, strong memory system)
