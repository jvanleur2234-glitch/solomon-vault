# RD Report: hyperspaceai/agi

**Forked:** https://github.com/jvanleur2234-glitch/hyperspaceai-agi  
**License:** MIT  
**Language:** Python + Rust (blockchain)

## What It Is
Living research repo for distributed AGI on Hyperspace P2P network. Agents collaboratively train models, share experiments via gossip, and push results. First distributed training run: 32 nodes, 24 hours.

## Relevance to Solomon OS
- **AgentFM/swarms competitor**: P2P compute grid for AI workloads
- **Distributed training**: DiLoCo + SparseLoCo + Parcae = 195× compression for weight deltas
- **Blockchain component**: A1 chain for agent-to-agent micropayments
- **Solomon Air alignment**: Decentralized AI infra vision matches

## Key Innovations
- **Pods**: Private AI clusters with distributed inference across mesh
- **Distributed training**: 32-node collaborative training in 24hrs (no trusted infra)
- **BitTorrent sidecar**: P2P model weight distribution
- **5 research domains**: ML, Search, Finance, Skills, Causes
- **CRDT leaderboards**: GossipSub → CRDT → GitHub pipeline

## Comparison to Solomon Air
| Aspect | Hyperspace | Solomon Air (Bonsai/Thoth) |
|--------|------------|---------------------------|
| P2P training | ✅ DiLoCo | ❌ |
| Token economy | ✅ Points | ❌ |
| Browser agent | ✅ WebGPU | ❌ |
| Blockchain | ✅ Mysticeti DAG | ❌ |

## Verdict
**SKILL** — P2P distributed training is ahead of our current Solomon Air implementation. Bonsai + Thoth could integrate DiLoCo-style compression. Fork for architecture reference on P2P AI compute.
