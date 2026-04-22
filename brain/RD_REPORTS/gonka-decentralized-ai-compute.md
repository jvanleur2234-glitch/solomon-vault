# RD Report: gonka (gonka-ai)

**Scout Session:** 2026-04-22  
**Fork:** https://github.com/jvanleur2234-glitch/gonka  
**Original:** https://github.com/gonka-ai/gonka  
**License:** Open source (MIT likely based on patterns)

---

## What it does
Decentralized P2P AI compute platform that pools hardware for training/inference workloads:

- **P2P GPU Pooling:** Hosts contribute hardware and earn rewards; developers run inference/training across pooled resources
- **Proof of Work 2.0 + Sprint mechanism:** Performance on AI tasks determines voting weight and governance influence
- **DiLoCo-style geo-distributed training:** Efficient distributed training across global hardware providers
- **Randomized task verification:** Verifies 1–10% of tasks probabilistically to reduce overhead
- **Majority-weighted peer verification:** Higher-weight nodes handle more validation

## Solomon OS fit
**SKILL** — DiLoCo distributed training pattern directly applicable to Solomon OS compute distribution. P2P GPU pooling competitive with AgentFM/hyperspace. Sprint governance mechanism interesting for agent economy. v0.2.11, active development.

## Key patterns to study
- DiLoCo geo-distributed training implementation
- Proof-of-Work 2.0 governance for AI compute
- Randomized verification without centralized authority

## Risk
- May require significant integration effort; P2P networking complexity