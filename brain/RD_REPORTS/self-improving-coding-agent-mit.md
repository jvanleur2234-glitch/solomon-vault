# RD Report: Self-Improving Coding Agent (MIT)

## Summary
A coding agent that iteratively improves its own codebase based on benchmark evaluation. Self-referential improvement loop: evaluate → archive → modify → repeat. 310 stars, MIT.

## What It Does
- Docker-isolated self-modification loop
- Evaluates on SWE-bench benchmarks
- Archives results, then runs agent on its own code
- Multi-LLM support (Claude, GPT, Gemini, Vertex, Fireworks, DeepSeek)
- Web research via Modal (visits pages, reads papers)
- MIT licensed

## Why It Matters for Solomon OS / Hermes
Proves autonomous self-improvement is possible. The evaluation→modification loop pattern can inspire:
- Hermes agent skill self-evolution
- Auto-improvement of Solomon OS workflows
- Self-patching capabilities in production agents

## Relevance: 🟡 WORTHWHILE — Self-improvement Pattern
Interesting architecture but Docker-isolated (can't directly integrate). Use as inspiration for self-evolution layer.

## License: MIT ✅
## Stars: 310 ✅ (low but novel pattern)

## Verdict: **STUDY** — Architecturally significant for self-improvement loops
