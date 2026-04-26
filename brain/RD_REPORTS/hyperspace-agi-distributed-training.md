# hyperspaceai/agi — Distributed AGI P2P System

## SLUG: hyperspaceai-agi
## Date: 2026-04-26
## Tags: #distributed-AI #P2P #compute-grid #training #DePIN #AGI
## Status: FORGE

---

## What It Is
hyperspaceai/agi is the first distributed AGI system where thousands of autonomous AI agents collaboratively train models, share experiments via P2P gossip, and push breakthroughs. Fully peer-to-peer with pods, distributed inference, and DiLoCo-based training.

## Key Capabilities
- **Pods**: private AI clusters pooling multiple machines into distributed cluster
- **Distributed inference**: routes to best-loaded model (Qwen 3.5 32B, GLM-5 Turbo, GGUF)
- **DiLoCo training**: 32 nodes trained a language model in 24 hours across consumer devices
- **Compression**: SparseLoCo (~45x), Parcae (~6x), overall ~195x compression
- **BitTorrent sidecar**: training weights distributed via WebTorrent
- **Blockchain economy** (Hyperspace A1): Mysticeti consensus, streaming payment channels
- **MIT License**

## Relevance to Solomon OS / AgentFM
- P2P distributed training is directly competitive with AgentFM
- Pod concept aligns with Solomon OS autonomous agent clusters
- DiLoCo algorithm is proven for cross-device training

## Recommendation
**FORGE** — fork for P2P compute grid infrastructure, study DiLoCo implementation for distributed training capability.
