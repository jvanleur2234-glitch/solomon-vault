# PeerClaw — Decentralized P2P AI Agent Network

**Date:** 2026-04-26  
**Slug:** peerclaw  
**Category:** Distributed Compute / P2P AI  
**License:** MIT  
**Language:** Go + TypeScript  
**Stars:** ~1,800  
**Forked:** Yes (`jvanleur2234-glitch/peerclaw`)

## What it is
Decentralized P2P AI agent network. Runs as single static binary (no containers). Peers contribute compute, share models and memory, transact via native token. Built on libp2p (Kademlia DHT, GossipSub, mDNS, Noise).

## Key Features
- **Single static binary**: no containers, easy deployment
- **Local GGUF models**: Llama, Phi, Qwen, Gemma with GPU acceleration
- **Vector memory (vectX)**: semantic + hybrid search (HNSW + BM25)
- **P2P job marketplace**: request → bid → execute → settle
- **Token economy**: Ed25519 wallet, escrow, micro-payments
- **Skills system**: SKILL.md-based with activation scoring, trust levels
- **WASM sandbox + MCP integration**
- **Web dashboard**: network topology visualization

## Relevance to Solomon OS / Hermes
PeerClaw's skills system (SKILL.md-based) is directly relevant to Hermes skill ecosystem. P2P compute marketplace is a competitor to AgentFM. The token economy + micro-payment system is a model for compute distribution.

## Verdict
**INTEGRATE** — Study PeerClaw's skill activation scoring and trust levels for Hermes skill security. P2P compute marketplace is a direct AgentFM competitor. MIT licensed, actively maintained.