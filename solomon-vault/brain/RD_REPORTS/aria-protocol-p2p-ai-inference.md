# RD Report: ARIA Protocol — P2P Distributed AI Inference

**Repo**: `spmfrance-cloud/aria-protocol`  
**Date**: 2026-04-19  
**License**: MIT  
**Stars**: Not yet prominent  
**Relevance**: DISTRIBUTED AI COMPUTE / AGENTFM COMPETITOR  

## What It Is
Open P2P framework for **decentralized AI inference** using 1-bit model inference (BitNet.cpp), WebSocket P2P networking, and blockchain-style provenance. CPU-friendly, energy-efficient (70-82% cheaper than GPU), consent-based compute sharing.

## Key Features
- **1-bit (ternary weight) inference** — runs on any CPU, no GPU required
- **Real WebSocket P2P network** — not blockchain, no crypto overhead
- **Pipeline parallelism** + OpenAI-compatible API (`/v1/chat/completions`)
- **Provenance ledger** — immutable inference records, proof-of-useful-work
- NAT traversal + Kademlia DHT peer discovery (roadmap v0.6)
- MIT licensed, Python primary

## What We'd Use It For
**AgentFM competitor.** ARIA is a different approach to distributed compute — instead of full GPU pods, it pools CPU inference via 1-bit models. Interesting for edge/low-resource agent deployments. Potential integration for Hermes if we need CPU-friendly inference at the edge.

## Comparison to AgentFM
- **AgentFM**: Podman containers, any language, full GPU/CPU mesh via libp2p
- **ARIA Protocol**: 1-bit models only, WebSocket P2P, provenance ledger, CPU-first
- **AgentFM wins** for flexibility; **ARIA wins** for energy efficiency and CPU-only devices

## Recommendation: **WATCH** 
- Interesting architecture for edge compute distribution
- 1-bit inference research is relevant to OpenMythos/token efficiency work
- No immediate integration need but worth tracking for the compute grid strategy

## Links
- Install: `pip install aria-protocol`
- CLI: `aria node start --port 8765 --model aria-2b-1bit`
- API: `aria api start --port 3000` → OpenAI-compatible endpoint
