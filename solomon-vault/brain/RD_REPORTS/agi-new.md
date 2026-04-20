# Hyperspace AGI — Distributed P2P AI Training & Inference

**Fork:** github.com/jvanleur2234-glitch/agi-new  
**Original:** hyperspaceai/agi  
**License:** MIT  
**Relevance:** 🟡 Useful — distributed compute (AgentFM competitor)

## What It Is
First experimental distributed AGI system. Fully P2P, runs on Hyperspace network (2M+ nodes). Agents run experiments, gossip findings, push results to GitHub. Includes distributed training via DiLoCo + SparseLoCo + Parcae.

## Key Capabilities
### Distributed Training
- 32 anonymous nodes completed first collaborative training run in 24 hours
- **195× compression**: 5.5 MB → 28 KB per round via SparseLoCo (top-k sparsity) + Parcae (layer-wise gradient pooling)
- BitTorrent-sidecar for model weight distribution — no central download server
- Adaptive inner steps: fast GPUs do 100+ steps, slow CPUs do 5-10

### Pods (Private AI Clusters)
- Pool machines into shared cluster
- Distributed inference across Qwen 3.5 32B, GLM-5 Turbo, GGUF models
- Shared provider pools (OpenRouter/Groq/Together keys)
- Pod Capsule: encrypted `.tar.gz` of full pod state

### Blockchain Layer
- Hyperspace A1: blockchain for autonomous AI agents
- Mysticeti consensus (DAG-based), stateless execution
- Streaming micropayments for agent-to-agent compute
- 695+ live agents on chain

## Architecture
```
GitHub (durable archive) ← proxy ← Hyperspace P2P (GossipSub/DiLoCo/Pulse/CRDT)
                              ↓
                 Agent A (H100) · Agent B (browser) · Agent C (laptop)
```

## 5 Research Domains
Machine Learning (val_loss), Search Engine (NDCG@10), Financial Analysis (Sharpe ratio), Skills & Tools (test_pass_rate), Causes

## Comparison to AgentFM
- AgentFM: Go-based, ephemeral sandboxed containers, libp2p networking
- Hyperspace AGI: Research-focused, DiLoCo distributed training, blockchain economy, CRDT leaderboards
- Both: P2P compute grids, no central infrastructure

## Solomon OS Relevance
**WATCH** — Not immediately actionable. Hyperspace node could be part of Solomon Air (decentralized infra). The distributed training innovations (Parcae gradient pooling) are technically interesting for future compute sharing. Monitor for now.

## Verdict
SKIP (for now) — Interesting research but not immediately integrable into Solomon OS. Keep fork for reference on P2P training techniques.
