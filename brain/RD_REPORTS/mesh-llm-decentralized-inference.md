# Mesh LLM — P2P Distributed Inference Pool

**Fork:** N/A (already in workspace, reference only)  
**License:** MIT  
**Stars:** ~1.2K (estimated)  
**Date:** 2026-04-25

## What It Is

Rust-first framework that pools spare GPU capacity across multiple machines to expose a single OpenAI-compatible API for distributed inference. Automates cross-node work distribution for large dense and MoE models.

## Key Features

- **Pipeline parallelism** for dense models + expert sharding for MoE
- **Unified local API** at `localhost:9337/v1` + embedded web console
- **Public/private mesh** participation — join shared inference pools or private clusters
- **OpenAI-compatible** chat completions API for drop-in integration
- **Multi-backend:** CUDA, ROCm/HIP, Vulkan, CPU
- **Auto-selects backends**, downloads models, joins best public mesh

## Quick Start

```bash
mesh-llm serve --auto
# API at localhost:9337/v1
# Console at localhost:3131
curl localhost:9337/v1/chat/completions -d '{"model":"...","messages":[...]}'
```

## Solomon OS Fit

**COMPETITOR / REFERENCE** — Mesh LLM is a P2P compute competitor to AgentFM and Shard. The Rust-based approach with OpenAI-compatible API is architecturally similar to what a Solomon Air inference aggregator would need. Worth studying for the mesh orchestration patterns.

## Verdict

**SKILL** — Study the mesh-aware orchestration logic for distributed inference. Not forkable (MIT but Rust-only). Relevant to Solomon Air P2P compute vision.
