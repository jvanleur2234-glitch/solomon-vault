# RD Report: Meshcore — Hybrid P2P Compute & LLM Inference

**Fork:** https://github.com/jvanleur2234-glitch/Meshcore
**Source:** https://github.com/elyawhoo/Meshcore
**License:** AGPL-3.0
**Language:** Concept document + plans (Rust/Golang/Python)
**Stars:** <10 (concept stage, no implementation)

## What It Is
Architectural blueprint for a hybrid Web2.5 decentralized compute network. Control Plane (federated/centralized) for ultra-low latency node profiling and task routing. Data Plane (fully P2P) with WASM sandboxing for isolation.

## Key Architecture Points
- **Hybrid Web2.5:** centralized control plane + P2P compute plane
- **WASM sandboxing:** workload isolation without full VMs
- **Auditor nodes:** Shadow prompts + Logit consensus to detect hallucinated inference (replaces cryptographic proof-of-compute)
- **BitTorrent model distribution:** network itself acts as CDN for model weights
- **Tiered storage overlay:** P2P fallback to centralized cold storage (Cloudflare R2)
- **Coturn TURN cluster:** handles symmetric NAT (20% of residential networks)
- **Matches compute by task, not layer:** routing complete prompts to nodes with cached models

## Critical Barriers Acknowledged
1. **Proof of compute:** Cryptographic (FHE/ZK-SNARKs) too slow. Probabilistic consensus + selective auditing.
2. **Data privacy:** TEE adoption limited in consumer hardware. No solution yet.
3. **Cold start:** 40GB+ model loading is slow. Predictive pre-warming across swarm.

## Solomon OS Fit
**SKILL** — Architecture study only. AGPL-3.0 (copyleft) prevents commercial use. Auditor node concept for distributed inference validation useful for Solomon Air.

## Comparison to Existing
- Similar vision to AgentFM but more detailed architecture discussion
- Addresses proof-of-compute problem better than AgentFM
- No implementation yet — pure blueprint

## Action
Forked. Auditor node concept worth studying for future distributed inference validation.

**Recommendation:** SKILL — architectural reference only. No implementation to fork/use.