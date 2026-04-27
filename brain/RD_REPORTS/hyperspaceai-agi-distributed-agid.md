# RD Report: hyperspaceai/agi

**Date:** April 26, 2026  
**Forked:** Already in workspace  
**License:** MIT (distributed AI), proprietary tokens (A1 blockchain)  
**Stars:** Active, live network with 695+ agents  

## What It Is
First distributed AGI system. Thousands of autonomous AI agents collaboratively train models, share experiments via P2P gossip, and push breakthroughs. Fully peer-to-peer.

## Key Capabilities
- **Pods:** Private AI clusters via CLI, share models + compute
- **Distributed inference:** Routes to best-loaded model (Qwen 3.5 32B, GLM-5 Turbo, GGUF)
- **Shared providers + budgeting:** Pool OpenRouter, Groq, Together with per-member budgets
- **Distributed training:** DiLoCo with SparseLoCo (45× compression), Parcae gradient pooling (6×)
- **BitTorrent sidecar:** WebTorrent-based training asset distribution
- **Autonomous workers:** Self-installing dependencies, resilient CLI restarts
- **A1 Blockchain:** Stateless execution, streaming micropayments between agents, Mysticeti consensus

## Architecture Insight
- **SparseLoCo:** 195× compression (5.5MB → 28KB per training round)
- **Adaptive inner steps:** Node-speed aware to fit 25-minute training window
- **Demonstrated:** 32 anonymous nodes trained a language model in 24h on consumer hardware

## Solomon OS Fit
**FORGE** — AgentFM competitor with live production network. P2P compute pooling validates our approach. The budgeting/scheduling mechanism is directly applicable to JCPaid's compute marketplace. Their Pod concept (private AI clusters) is similar to our AgentFM pods.

## Threat Assessment
- 695+ live agents indicates mature P2P infrastructure
- Their blockchain micropayment system is more sophisticated than our current plans
- DiLoCo compression is novel — could be applied to our distributed training

## Action
Study. Clone and analyze Pod networking code. Reverse-engineer A1 blockchain micropayment model for JCPaid integration.