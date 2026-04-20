# RD Report: ninja — Self-Improving Coding Agent

**Repo**: `unconst/ninja`  
**Fork**: `jvanleur2234-glitch/ninja-new`  
**Date**: 2026-04-19  
**License**: NOASSERTION (⚠️ skip for production use)  
**Relevance**: SELF-IMPROVING AI / AGENT ORCHESTRATION  

## What It Is
A coding agent grown entirely by AI through an automated self-improvement loop. No human wrote its Rust code, tools, or prompts — all generated and refined via the Arbos outer agent loop:
1. Generate tasks from real GitHub PRs
2. Run Ninja against tasks
3. Evaluate (did it work? why not?)
4. Patch Ninja's code (system prompt, tools, agent loop, heuristics)
5. Rebuild & retest (rollback if regression)

Key findings from their loop:
- **Competence cliff**: agents fail suddenly at complexity thresholds
- **4 failure modes**: propagation incompleteness, interface contract violations, difficulty-selective attention, test gaming
- **Interconnection over complexity**: most failures come from component interaction, not individual capability gaps

## Key Features
- Fully AI-generated codebase (Rust + Python + some C/CMake)
- Outer agent (Arbos) orchestrates the improvement loop
- Hundreds of automated experiments identifying failure modes
- Post-edit lint loops for validation
- Rollback on regression

## What We'd Use It For
**Research only — NOASSERTION license.** Study the self-improvement loop architecture for Solomon OS's self-evolution capabilities. The failure mode taxonomy is gold for building resilient agents.

## Comparison to What We Have
- **vs self-improving-agent (xmaks82)**: More rigorous — actual code patching with measurement vs prompt evolution
- **vs ninja (unconst)**: Different from the Go/gollem project; this is a research self-improvement agent
- **vs self_improving_coding_agent (MaximeRobeyns)**: Similar concept but Ninja patches actual code not just prompts

## Recommendation: **RESEARCH / DO NOT USE IN PRODUCTION**
- License is NOASSERTION — not MIT/Apache, not clear for commercial use
- Study the failure mode taxonomy for Hermes resilience engineering
- Forked for research context only

## Links
- Fork: https://github.com/jvanleur2234-glitch/ninja-new
- Outer agent: https://github.com/unconst/arbos
