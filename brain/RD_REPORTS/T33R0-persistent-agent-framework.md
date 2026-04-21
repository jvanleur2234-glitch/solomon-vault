# RD Report: T33R0/persistent-agent-framework

**Date:** 2026-04-21  
**Fork:** jvanleur2234-glitch/persistent-agent-framework  
**License:** MIT  
**Category:** Self-Improving Agent / Persistent Memory  
**Stars:** ~500+ (novel)  
**Relevance:** 🔴 Critical — Self-Evolution Engine for Hermes/OpenClaw

## What It Is

Production-tested architecture turning stateless Claude Code into a persistent, self-correcting AI agent. Runs across CLI, Telegram, Discord, and web from a single agent definition. No Docker/Kubernetes required — built on Claude Code + Supabase + macOS launchd.

## Key Capabilities

- **Persistent identity** via SOUL.md files + shared Supabase database
- **Self-correction loop**: mistake → ledger → daemon detects pattern (3+ occurrences) → auto-generates behavioral directive → future behavior updated
- **Multi-terminal continuity**: parallel sessions share memory across terminals
- **Marker processing engine**: invisible side-effects (memory, state, learning) extracted from LLM responses
- **Multi-provider LLM cascade**: Claude → Gemini → OpenAI → Ollama with automatic fallback
- **Agent hierarchy**: subordinate agents, inter-agent communication, security boundaries
- **Sweep-based daemon**: with circuit breakers and health monitoring
- **Onboarding**: agent discovers its own personality through conversation

## Architecture Modules

| Module | Purpose |
|--------|---------|
| `marker-engine.mjs` | Marker extraction, pluggable handler registry |
| `agent-boot.mjs` | System prompt assembly from soul, memory, state, ledger |
| `session-manager.mjs` | Date-scoped sessions with automatic day-boundary handoff |
| `llm-providers.mjs` | Normalized multi-provider interface |
| `daemon.mjs` | Sweep-based runner with circuit breakers |
| `semantic-memory.mjs` | Hybrid importance + semantic search (Ollama embeddings) |

## Self-Correction Flow

```
Mistake occurs
  → Log to ledger (what, why, should_have, signal_traced)
  → Daemon counts pattern frequency
  → Pattern 3+ times? → Generate behavioral directive automatically
  → Directive still violated? Escalate priority
```

## Solomon OS Fit

**FORGE** — This IS the self-evolution engine for Hermes/OpenClaw. The self-correction loop (mistake → ledger → pattern detection → directive generation) directly maps to how Solomon OS agents should learn from failures. MIT license permits direct use.

**Key files to steal:**
- `runtime/marker-engine.mjs` — Marker processing pattern
- `runtime/agent-boot.mjs` — Soul + memory + state assembly
- `runtime/daemon.mjs` — Sweep-based autonomous operation
- `runtime/semantic-memory.mjs` — Hybrid memory search
- `templates/SOUL.md` — Identity/personality template

**Synergy with existing forks:** RangeKing/self-evolving-agent (phase-aware promotion) + T33R0 (self-correction ledger) = complete self-evolution system for Hermes

## Status

**FORGE** — Study carefully, implement core patterns in Hermes agent runtime