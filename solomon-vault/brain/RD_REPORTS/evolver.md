# R&D Report: Evolver — Self-Evolution Engine for AI Agents

**Date:** April 18, 2026
**Repo:** github.com/EvoMap/evolver (5K stars, GPL-3.0)
**Forked:** jvanleur2234-glitch/evolver

## What It Does
The GEP-Powered Self-Evolution Engine for AI Agents. Genome Evolution Protocol.

Runs an evolution cycle that:
1. Scans memory/ logs for error patterns and signals
2. Selects the best-matching Gene or Capsule from `assets/gep/`
3. Emits a protocol-bound GEP prompt that guides the next evolution step
4. Records an auditable EvolutionEvent for traceability

**It does NOT auto-edit code** — it generates prompts that guide evolution. Safe by design.

## Key Features
- **Auto-Log Analysis**: scans memory and history files for errors and patterns
- **Self-Repair Guidance**: emits repair-focused directives from signals
- **GEP Protocol**: standardized evolution with reusable Genes/Capsules
- **Mutation + Personality Evolution**: strategy presets (balanced/innovate/harden/repair-only)
- **Signal De-duplication**: prevents repair loops by detecting stagnation
- **Operations Module**: portable lifecycle, skill monitoring, cleanup, self-repair (zero platform dependency)
- **Protected Source Files**: prevents autonomous agents from overwriting core evolver code
- **Skill Store**: download/share reusable skills via `node index.js fetch --skill <id>`
- **A2A Hub**: optional network for skill sharing, worker pool, evolution leaderboards

## Security Model
- Only executes validation commands: `node`, `npm`, `npx` (prefix whitelist)
- No command substitution (backticks, `$(...)` rejected)
- No shell operators after stripping quotes
- 180-second timeout per command
- Genes staged in isolated candidate zone before promotion

## How It Integrates with Host Runtimes
| Mode | Behavior |
|------|----------|
| Standalone (`node index.js`) | Generates prompt, prints to stdout, exits |
| Loop (`node index.js --loop`) | Repeats in daemon loop with adaptive sleep |
| Review (`node index.js --review`) | Pauses before applying, waits for human confirmation |
| Inside OpenClaw | Host runtime interprets stdout directives |

## Evolution Strategies
| Strategy | Innovate | Optimize | Repair | When to Use |
|----------|----------|----------|--------|-------------|
| `balanced` (default) | 50% | 30% | 20% | Daily operation, steady growth |
| `innovate` | 80% | 15% | 5% | System stable, ship new features fast |
| `harden` | 20% | 40% | 40% | After major changes, focus on stability |
| `repair-only` | 0% | 20% | 80% | Emergency state, all-out repair |

## JCPaid Fit
**FIT: ★★★★★ — CRITICAL PIECE FOUND**

This is the self-improvement engine Solomon OS was missing. Combined with:
- **Icarus** (cross-agent shared memory) — feeds error signals TO Evolver
- **Solomon Guardian** (adversarial loop) — provides attack signals for Evolver to harden against
- **agentic-stack** (4 memory layers) — provides the memory/lesson system Evolver reads

The full loop:
```
Guardian detects attack → logs signal → Icarus shares across agents → Evolver scans → selects Gene → GEP prompt → Hermes applies fix
```

Then Evolver's `--review` mode gives you human-in-the-loop approval before any fix applies.

## License Note
Core evolution engine modules are distributed in **obfuscated form**. GPL-3.0 but proprietary core. Forking is fine for personal use/modification but the core logic is not readable.

## Full Docs
- Wiki: https://evomap.ai/wiki
- Skill Store: https://evomap.ai
- GEP Protocol: standardized evolution format

## Status
**CRITICAL** — Forked at jvanleur2234-glitch/evolver. Install as the self-improvement engine for Solomon OS.