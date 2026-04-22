# KohakuTerrarium — Modular Agent Framework (Creatures + Terrariums)

**Forked:** jvanleur2234-glitch/KohakuTerrarium  
**License:** KohakuTerrarium-1.0  
**Stars:** N/A (new discovery)  
**Language:** Python 3.10+

## What It Is

A framework for building "real agents, not just LLM wrappers." Core abstraction is the **creature** — a standalone agent with controller, tools, sub-agents, triggers, memory, and I/O. Creatures can run solo or be composed into a **terrarium** (pure multi-agent wiring layer).

## Key Features

- **Creature-centric design** vs tool/utility wrappers
- Persistent sessions with searchable history (text + vector)
- Non-blocking background context compaction for long-running agents
- Sub-agents and multi-agent teams
- Multiple runtimes: CLI, TUI, web, desktop
- `kt-defaults` package: ready-to-use creatures + plugins (coding agent runtime out of the box)
- Python-first with composition algebra for orchestrating agents in applications

## Architecture

```
creature = controller + tools + sub-agents + triggers + memory + I/O
terrarium = pure multi-agent wiring layer (composes creatures)
```

## Solomon OS Fit

- **Pattern match:** AgentFM/AgentOrcha competitor — modular agent composition
- **Use for:** Hermes Agent orchestration patterns, agent-as-creature mental model
- **Why fork:** KohakuTerrarium's creature/terrarium abstraction is more intuitive than traditional agent frameworks. Could inform Solomon OS agent design.
- **Competitive:** vs agent-express (middleware), vs Gollem (Go/type-safe), vs Dapr agents (workflow)

## RD Status

✅ Forked — needs RD report completion  
**Recommendation:** FORGE — modular agent design pattern worth studying