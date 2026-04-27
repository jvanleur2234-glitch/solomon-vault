# RD Report: Mesh-LLM — Rust Distributed Inference Pool

## Summary
Mesh-LLM by Michael Neale is a Rust-first distributed AI/LLM platform that pools spare GPU capacity across machines to expose a single OpenAI-compatible API. Pipeline parallelism for dense models, expert sharding for MoE. Collaborative inference. Local API at http://localhost:9337/v1. Apache 2.0, v0.64.0.

## What It Does
- **Distributed Inference**: Pool GPU resources, scale models beyond single machine
- **OpenAI-Compatible API**: /v1/chat/completions drop-in
- **Pipeline Parallelism**: Dense model distribution
- **Expert Sharding**: MoE with zero cross-node traffic
- **Collaborative Inference**: Cross-peer model checks
- **Auto-Detection**: Download models as needed
- **Web Console**: http://localhost:3131

## Tech Stack
- Language: Rust
- License: Apache 2.0
- Latest: v0.64.0 (2026-04-20)
- Build: Linux, Windows; CUDA/ROCm/Vulkan; CPU-only

## Strategic Fit for Solomon OS

**WATCH** — AgentFM competitor. Rust-first = high performance. OpenAI-compatible = easy adoption.

Key learnings:
1. **Rust Performance**: Low-latency distributed inference
2. **OpenAI API Compatibility**: Drop-in for existing applications
3. **MoE Expert Sharding**: Efficient multi-expert distribution
4. **Collaborative Inference**: Cross-peer validation

## Risk/Concerns
- Rust expertise required
- GPU cluster needed for full benefit
- Still maturing

## Verdict
WATCH — Monitor as AgentFM competitor. OpenAI compatibility for JCPaid compute marketplace integration. MoE sharding for Hermes distributed inference.

## Links
- Repo: https://github.com/MichaelNeale/decentralized-inference (mesh-llm)
- Fork: Already forked