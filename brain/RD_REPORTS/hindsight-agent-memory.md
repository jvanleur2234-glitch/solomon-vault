# RD Report: Hindsight — Agent Memory That Learns

**URL:** https://github.com/vectorize-io/hindsight
**Date:** 2026-04-20
**Platform:** GitHub
**Stars:** 7,100+
**License:** MIT

## What It Is
Agent memory system that helps AI agents **learn over time**, not just recall past conversations. State-of-the-art performance on long-term memory benchmarks (LongMemEval), independently reproduced by Virginia Tech and The Washington Post.

## Key Features
- **2-line LLM wrapper** to add memory to existing agents
- Memory operations: retain (store), recall (search), reflect (disposition-aware response)
- Supports: OpenAI, Anthropic, Gemini, Groq, Ollama, LMStudio, MiniMax
- Docker one-command deploy
- Python + TypeScript clients
- Production use at Fortune 500 companies

## What We'd Use It For
**CRITICAL MISSING PIECE for Solomon OS.** The ML-Master HCC architecture identified 3-tier memory (short/medium/long) — Hindsight is the proven solution for the long-term memory layer we've been missing.

Integrates with:
- Russell Tuna (persistent memory across sessions)
- Solomon Bus (learn from job outcomes)
- Solomon Heartbeat (accumulate wisdom over time)
- AI Employee Agency offerings (each AI employee has persistent memory)

## How It Compares to What We Have
- GBrain v0.13: self-wiring knowledge graph — overlapping but Hindsight is proven in production at scale
- Supermemory AI: icarus backend — complementary
- Solomon OS brain/ files: manual, not automatic — Hindsight automates this

## Recommendation
🟢 NICE TO HAVE — Clone and test. This fills the long-term memory gap identified in the ML-Master HCC research. Deploy via Docker, wrap Russell Tuna or Solomon Bus with it, see if it improves persistent context.

## Next Steps
- Clone to /home/workspace/Skills/hindsight/
- Deploy Docker instance
- Test 2-line wrapper with Russell Tuna
- Evaluate benchmark results vs. GBrain

## Resources
- Docs: hindsight.vectorize.io
- Paper: arXiv:2512.12818
- Cookbook: github.com/vectorize-io/hindsight-cookbook