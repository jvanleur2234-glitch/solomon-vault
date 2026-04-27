# QMesh — P2P Distributed LLM Inference Network

**Fork:** https://github.com/jvanleur2234-glitch/qmesh-pear
**Date:** 2026-04-27
**Category:** Distributed AI Compute
**Tags:** P2P, inference, privacy, distributed, llama.cpp

---

## What It Does

QMesh is a decentralized AI inference marketplace powered by Pear Runtime and llama.cpp. Workers earn credits by running LLMs on spare hardware; clients get cheaper, private inference via P2P.

## Key Architecture

- **P2P via Hyperswarm DHT** — No central server, NAT traversal built-in
- **llama.cpp sidecar** — Local model inference, 100% private
- **Cross-platform binaries** — Linux, macOS (Intel/ARM), Windows
- **Phase 3 production** — Health-based routing, bundled binaries

## Why It Matters for Solomon OS

- **P2P compute mesh** — Competes with AgentFM for distributed compute
- **Privacy-first** — On-device inference aligns with JCPaid sovereign compute goals
- **Credit economy** — Could inform JCPaid marketplace token system
- **Worker onboarding** — Simple `pear run` flow for compute sharing

## License & Activity

- MIT License (inferred — no explicit LICENSE file found)
- Active development — Phase 3 complete, Phase 4 (GPU) planned

## Competitive Analysis

| Feature | QMesh | AgentFM | MyCellm |
|---------|-------|---------|---------|
| P2P discovery | Hyperswarm | libp2p | libp2p |
| Model inference | llama.cpp | Any | Any |
| Credit economy | Planned | Yes | Yes |
| Privacy | Local only | Partial | On-device scan |
| Production phase | Phase 3 | Stable | v0.2.5 |
| Platform | Pear Runtime | Podman | Native |

## Decision

**WATCH** — P2P inference with privacy focus. The Pear Runtime dependency is interesting for compute distribution but may add friction vs AgentFM's Podman approach. Worth monitoring for Phase 4 GPU acceleration.

## Relevance to JCPaid

- Credit economy model for compute sharing
- Privacy-first inference aligns with sovereign AI positioning
- P2P discovery mechanism for distributed compute mesh

---
*Scouted by AIQ Scout — 2026-04-27*
