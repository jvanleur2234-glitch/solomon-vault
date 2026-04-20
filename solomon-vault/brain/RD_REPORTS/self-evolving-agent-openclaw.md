# self-evolving-agent — Phase-Aware Capability Evolution

**Forked:** `jvanleur2234-glitch/self-evolving-agent`
**Stars:** Unknown (March 2026)
**License:** Unknown (check before final)
**Category:** self-improvement #capability-evolution #openclaw

## What It Is
An OpenClaw-based runtime that upgrades self-improving agents from reactive error logging to goal-driven capability evolution. Phase-aware operation with modes: task_light, task_full, agenda_review, promotion_review.

## Key Innovation: Learning Lifecycle
`recorded → understood → practiced → passed → generalized → promoted`

Only validated, transferable strategies get promoted. Includes explicit transfer check before promotion.

## Key Patterns for Solomon OS
1. **Phase-aware control plane** → routes tasks into smallest safe mode → reduces token waste
2. **Learning agenda** → keeps 1-3 high-leverage capabilities active at a time → Evolver's priority queue
3. **Capability map** → tracks level, evidence, limits, failure modes, upgrade conditions → Icarus capability registry
4. **Diagnosis layer** → turns incidents into root-cause analysis → Evolver analysis
5. **Promotion gate** → prevents brittle rules from polluting behavior → quality control for self-improvement

## Architecture
```
Task → classify-task → Mode routing → retrieve-context → Execute → record-incident → rebuild-index → ledgers + manifest.json
```

## Verdict
**FORGE** — Phase-aware capability evolution maps directly to Evolver. The promotion gate + capability map combination is the missing piece in Solomon OS self-improvement. Study OpenClaw integration.

## Links
- https://github.com/jvanleur2234-glitch/self-evolving-agent