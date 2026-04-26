# hivemind — Decentralized Deep Learning in PyTorch

## SLUG: hivemind
## Date: 2026-04-26
## Tags: #distributed-AI #P2P #training #volunteer-computing #PyTorch
## Status: FORGE

---

## What It Is
hivemind (DandinPower/hivemind) is a PyTorch library for decentralized AI training across a P2P network. Enables training large models on thousands of volunteer machines without a central master node.

## Key Capabilities
- **DHT-based peer discovery**: distributed hash table for connectivity
- **Fault-tolerant backpropagation**: tolerates slow/unresponsive nodes
- **Decentralized parameter averaging**: aggregate updates without global sync
- **MoE support**: Decentralized Mixture-of-Experts for large models
- **PyTorch Lightning integration**
- **Apache-2.0 / MIT License**

## Relevance to Solomon OS / JCPaid
- Volunteer computing model fits JCPaid distributed compute concept
- Proven academic backing (used for research training)
- Fault-tolerant design essential for resilient agent training

## Recommendation
**FORGE** — fork for distributed training layer, integrate with JCPaid compute sharing.
