# Mesh LLM — Distributed P2P GPU Inference Pool

**Fork:** `Mesh-LLM/mesh-llm` → `jvanleur2234-glitch/mesh-llm`
**Source:** https://github.com/Mesh-LLM/mesh-llm (Apache-2.0)
**Date:** 2026-04-25

---

## What It Does

Mesh LLM pools spare GPU capacity across machines into a single OpenAI-compatible API. Dense models use pipeline parallelism; MoE models use expert sharding with zero cross-node inference traffic. Multiple models can collaborate during inference (e.g., a vision model consults a text peer).

## Solomon OS Fit

**DIRECT COMPETITOR to AgentFM / P2P compute grid.** Key value:
- `http://localhost:9337/v1` endpoint = drop-in for any agent wanting LLM inference
- Pools uneven hardware into one inference cluster
- Expert sharding for MoE = relevant for OpenMythos-style architectures
- MIT license permits code reference

## How It Works

- Single binary, start with `mesh-llm serve --auto`
- Every node gets same local API endpoint
- Automatic GPU detection, model download, mesh joining
- Rust-based, Apache-2.0

## Status

**SKILL** — study architecture for AgentFM/PeerClaw competitive analysis. Pool-based inference routing is exactly what JCPaid's compute grid needs.