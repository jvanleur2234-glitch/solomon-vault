# RD Report: decentralized-inference (Mesh-LLM)

**Date:** 2026-04-23  
**Repo:** michaelneale/decentralized-inference  
**Fork:** https://github.com/jvanleur2234-glitch/decentralized-inference  
**License:** Apache-2.0  
**Stars:** ~1,200  
**Category:** Distributed AI Compute / P2P Inference

## What It Does
Pools spare GPU capacity across multiple machines to expose a single OpenAI-compatible API. Enables peer-to-peer compute sharing and collaborative inference across a mesh of nodes. Supports pipeline parallelism for dense models and expert sharding for MoE models.

## Key Features
- Automatic distribution of model workloads across the mesh
- Pipeline parallelism (dense models) and expert sharding (MoE, zero cross-node inference traffic)
- OpenAI-compatible endpoint on every node (`http://localhost:9337/v1`)
- Web console and management API
- Cross-peer collaboration during inference

## For Solomon OS
- **Use for:** Distributed inference for AgentFM competitors — compute grid for AI workloads
- **Alternative to:** AgentFM, Hyperspace, mycellm, TuTu
- **Complements:** OpenMythos (can run OpenMythos models across the mesh)

## LINK Tags
`#distributed` `#compute-grid` `#p2p` `#inference` `#agentfm-competitor`

## Recommendation
**FORGE** — P2P inference mesh. Study for JCPaid distributed compute layer.