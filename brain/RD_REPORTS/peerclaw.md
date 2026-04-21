# RD Report: PeerClaw — P2P Agent Network

**Repo:** `antonellof/peerclaw`  
**License:** MIT/Apache-2.0  
**Language:** Rust  
**Stars:** ~300+ (estimated)  
**Forked:** Yes  
**Date:** 2026-04-21

## What It Is

PeerClaw is a decentralized P2P AI agent network that ships as a **single static Rust binary**. Think BitTorrent meets AI inference — peers contribute compute and earn tokens while agents spend tokens to execute tasks across the network.

## Key Features

- **Single binary** — no containers, orchestrators, or cloud dependencies
- **Local GGUF inference** — Llama, Phi, Qwen, Gemma with Metal/CUDA acceleration
- **P2P networking** — libp2p with Kademlia DHT, GossipSub, mDNS, Noise encryption
- **Token economy** — PCLAW token accounting, escrow, per-request/hour/day budgets
- **Vector memory** — HNSW + BM25 hybrid semantic search, cross-session learning
- **20+ built-in tools** — WASM sandbox, MCP integration, HTTP/fs/shell/memory
- **LLM provider sharing** — share Ollama/GGUF models P2P and earn CLAW tokens
- **OpenAI-compatible API** — drop-in replacement with SSE streaming
- **Web dashboard** — agentic chat, visual workflow builder, network topology
- **Safety layer** — leak detection, prompt injection defense, policy enforcement

## Comparison to AgentFM / Competitors

| Feature | PeerClaw | AgentFM |
|---------|----------|---------|
| Language | Rust (single binary) | Go + Podman |
| Model support | GGUF + Ollama | Any containerized |
| Token economy | Native PCLAW | None |
| Vector memory | Built-in HNSW/BM25 | External |
| Skill system | SKILL.md + MCP | SKILL.md + plugins |

PeerClaw is AgentFM's direct competitor with a more mature token economy and built-in vector memory. Both target P2P distributed compute.

## For Solomon OS

- **P2P compute grid** — idle GPU monetization aligns with Solomon's distributed AI vision
- **Single binary deployment** — much simpler than AgentFM's Podman dependency
- **Token economy** — could power Solomon's agent incentive layer
- **MCP integration** — compatible with Hermes skill ecosystem

## Recommendation

**INTEGRATE** — PeerClaw's tokenized P2P compute model is more advanced than AgentFM for Solomon OS. The built-in vector memory + SKILL.md support makes it a strong candidate for Solomon's distributed skill layer. Study the PCLAW token economy and vector memory implementation.
