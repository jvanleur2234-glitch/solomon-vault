# RD Report: RAXE Runtime Security

**Repo:** `raxe-ai/raxe-ce`  
**License:** MIT | **Lang:** Python  

## What It Does
Runtime security toolkit for AI agents — stops prompt injections, jailbreaks, encoding attacks, and tool abuse entirely on-device. 515+ rules + ML ensemble detection.

## Why It Matters for Solomon OS
- **Runtime Protection**: Not just static scanning — protects during execution
- **Dual-Layer Detection**: L1 rules (<5ms) + L2 ML (~40ms) for novel attacks
- **94.7% True Positive Rate**: Battle-tested detection
- **100% Local**: No cloud dependency — privacy-preserving
- **Framework Integration**: LangChain, LiteLLM support

## Key Capabilities
- 515+ L1 detection rules (prompt injection, jailbreaks, encoding, tool abuse)
- 5-head neural network ensemble for novel/unknown attacks
- Sub-5ms L1 matching — real-time protection
- ~45ms total latency for combined L1+L2
- On-device only — no data leaves the machine
- Free forever — no API costs

## Comparison to What We Have
vs **guard-scanner**: RAXE is runtime protection, guard-scanner is static analysis. Both needed for complete coverage.

## Recommendation
**INTEGRATE** — Runtime protection layer for Hermes agents. Add to Solomon OS security stack as a guard before agent execution.

**Category:** #security #runtime #protection
