# RD Report: Hivemind — Decentralized Deep Learning

**Fork:** https://github.com/jvanleur2234-glitch/hivemind  
**Source:** https://github.com/DandinPower/hivemind  
**Date:** 2026-04-22  
**License:** Apache 2.0  
**Stars:** 4,000+  
**Language:** Python/PyTorch  

## What It Does
PyTorch library for decentralized, peer-to-peer training of neural networks across the Internet. Connects machines from different universities, companies, and volunteers without a master node. Used in production for training large models via collaborative computing.

## Key Features
- **Distributed Hash Table (DHT):** Decentralized peer discovery and coordination
- **Fault-tolerant backpropagation:** Training continues even with unresponsive/slow peers
- **Decentralized parameter averaging:** Aggregates model updates without global synchronization
- **Decentralized Mixture-of-Experts:** Distributes layer portions across participants
- **Production users:** Petals (100B+ LLM inference/fine-tuning), Transformers Together, CALM, sahajBERT

## Solomon OS Fit
**SKILL** — Architecture study for Solomon Air (decentralized compute). DiLoCo-style distributed training patterns useful for future agent training workloads. DHT peer discovery is battle-tested. Apache 2.0 permits direct code reference.

## Competitor Notes
Direct competitor: AgentFM (container-based P2P), Hyperspace AGI (P2P training), gonka (P2P compute with Sprint governance). Hivemind is the most mature (6+ years) with academic backing.

## Recommendation
SKILL — Study DHT-based peer coordination for Solomon Air. No code adoption needed (Apache 2.0), but architecture patterns Inform future distributed training design.