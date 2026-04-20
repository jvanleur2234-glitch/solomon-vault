# recursive-improve — Recursive Self-Improvement Framework

**Forked:** `jvanleur2234-glitch/recursive-improve`
**Stars:** ~150
**License:** Apache 2.0
**Category:** self-improvement #agent-framework #tracing

## What It Is
A Python framework that closes the self-improvement loop for ANY AI agent. Captures LLM execution traces → analyzes failures → applies targeted fixes → future runs perform better automatically.

## Core Workflow
1. Install: `uv tool install "recursive-improve[all] @ git+..."`
2. Add `ri.patch()` to agent to capture traces
3. Run agent multiple times to generate traces
4. Run `/recursive-improve` to apply fixes
5. Benchmark and view dashboard at localhost:8420

## Key Pattern
- Stateless agents start from scratch every run → recursive-improve closes this loop
- Traces go in `eval/traces/`, improvements organized by cycle
- Dashboard visualizes before/after metrics

## Key Patterns for Solomon OS
1. **ri.patch() tracing** → could be added to Hermes to capture all LLM calls
2. **Per-run trace capture** → Icarus could store traces as memories
3. **Dashboard** → Evolver could have a visual improvement dashboard
4. **Selective retention** → overnight/autonomous loop with `/ratchet`

## Verdict
**INTEGRATE** — Apache 2.0, fits directly into Icarus/Evolver pipeline. The `ri.patch()` pattern for transparent trace capture is exactly what Solomon OS self-improvement needs. Could wrap as a Hermes skill.

## Links
- https://github.com/jvanleur2234-glitch/recursive-improve