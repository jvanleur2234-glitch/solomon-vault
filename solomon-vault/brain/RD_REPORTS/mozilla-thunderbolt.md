# RD Report: Mozilla Thunderbolt (Open-Source AI Client)

## What It Is
Mozilla's Thunderbolt is an open-source AI client for private, self-hosted workflows. Released April 17, 2026 by Mozilla's for-profit arm. MPL-2.0 license. Native apps on web, macOS, Windows, Linux, iOS, Android.

**URL**: https://github.com/thunderbird/thunderbolt
**License**: MPL-2.0
**Integration**: deepset's Haystack framework (RAG + agent orchestration)

## Key Features
- Organizations control their own data and infrastructure
- No vendor lock-in, fully self-hosted
- Built on open standards
- Connects to Haystack for RAG backend + agent orchestration
- Privacy-centric — no tracking
- Extensible via plugins

## How It Compares to What We Have
Solomon OS already has the self-hosted AI concept via:
- Ollama running local models (qwen3:1.7b, etc.)
- Second Brain Portal on port 5011
- Hermes for agent orchestration
- Solomon Bus for inter-agent communication

Thunderbolt is the **frontend client** piece — a polished UI for interacting with self-hosted AI. Solomon OS has Zo + Russell Tuna as the interface. But Thunderbolt brings:
- Cross-platform native apps
- deepset/Haystack integration (enterprise RAG)
- Consumer-friendly interface

## What We'd Use It For
1. **Potential integration**: Thunderbolt → Haystack → Solomon Bus → our agent network
2. **Competing product reference**: Good model for how to package Solomon OS's self-hosted AI offering
3. **Competitive positioning**: We're building the full-stack version (AI worker + orchestration + RAG + UI) — Thunderbolt only does client

## Recommendation: **SKIP**
Not immediately actionable. It's a client, not an orchestration layer. Our stack is more complete. File for competitive awareness.
