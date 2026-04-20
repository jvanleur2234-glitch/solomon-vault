# Ninja — AI-Built Coding Agent (Arbor OS Loop)

**Forked:** `jvanleur2234-glitch/ninja`
**Stars:** Unknown (March 2026 repo)
**License:** Unknown (check before final)
**Category:** self-improvement #autonomous #coding-agent

## What It Is
A coding agent written ENTIRELY by AI through a continuous self-improvement loop (orchestrated by "Arbos"). Every line of Rust, every tool, every prompt directive — all generated and refined automatically by running the agent against tasks, feeding failures back as code changes.

## The Self-Improvement Loop
```
Generate Tasks → Run Ninja → Evaluate → Patch Ninja's Code → Rebuild & Retest → Repeat
```
Outer agent (Arbos) orchestrates: analyzes rollouts, finds failure patterns, writes Rust patches, rebuilds binary, measures delta, pushes net-positive changes.

## Key Discovery: Competence Cliff
The loop discovered that **interconnection** (not complexity) breaks agents:
- Isolated bug fixes: immune to scale (8+ bugs, 8+ files = 100% pass rate)
- Interconnected fixes: cliff at 4-6 bugs
- Code construction: cliff at 4 files / 6 endpoints
- Refactoring: hardest — cliff at 2 modules

Four failure modes identified and fixed by the loop:
1. Propagation incompleteness → breadth-first directive
2. Interface contract violation → signature checking
3. Difficulty-selective attention → anti-analysis-paralysis alerts
4. Test gaming → unfalsifiable test design principles

## Key Patterns for Solomon OS
1. **Outer orchestrator loop** → maps to Evolver's genetic algorithm
2. **Competence cliff insight** → important for Hermes task sizing
3. **Isolated vs interconnected fixes** → Solomon OS should prefer isolated improvements
4. **99 commits of self-generated improvements** → measurable self-improvement trace

## Verdict
**FORGE** — The Arbos/Ninja outer loop pattern is exactly what Evolver needs. The "competence cliff" insight is critical for task design. Study for integration.

## Links
- https://github.com/jvanleur2234-glitch/ninja