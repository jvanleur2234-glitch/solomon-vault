# RD Report: RangeKing-self-evolving-agent

## What It Is
**self-evolving-agent** — OpenClaw-first, phase-aware capability-evolution runtime. Extends OpenClaw framework with goal-driven capability evolution (not just error logging). Phases: `task_light`, `task_full`, `agenda_review`, `promotion_review`. Learning states: `recorded→understood→practiced→passed→generalized→promoted`. Capability map tracks level, evidence, limits, failure modes.

## License & Stars
MIT licensed. GitHub stars badge present (star count not visible in excerpt).

## Why It Matters for Solomon OS
- **OPENCLAW-BASED** = directly compatible with Solomon's Hermes/OpenClaw stack
- **UPGRADE** from self-improving-agent: goes beyond "log mistake → write rule" to capability evolution
- **Phase-aware control plane** routes tasks into smallest safe mode = efficiency + safety
- **Learning agenda** keeps only 1-3 high-leverage capabilities active = focus
- **Promotion gate** prevents brittle one-off rules from polluting long-term behavior
- **Canonical records** + human-readable ledgers = transparency for clients
- **Transfer awareness** = strategies validated before promotion to new contexts
- Built by RangeKing = known OpenClaw contributor

## What We'd Use It For
Replace Hermes's current self-improvement with this phase-aware capability evolution. The promotion gate ensures only validated improvements persist. The learning agenda prevents capability overload. The OpenClaw skill format means direct integration into Hermes.

## Solomon OS Fit
**FORGE** — this is the self-evolution engine for Hermes/OpenClaw. MIT license permits direct use. The phase-aware architecture maps directly to Solomon's "agent maturity" concept.

## Risk / Caveats
- OpenClaw dependency required
- Still experimental per date
- May need adaptation for non-OpenClaw contexts

## Action
Fork to jvanleur2234-glitch ✅ (done). Install as OpenClaw skill. Integrate phase-awareness into Hermes core loop.