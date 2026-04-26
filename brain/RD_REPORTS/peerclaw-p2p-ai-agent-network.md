# RD Report: PeerClaw — Decentralized P2P AI Agent Network

**Date:** April 26, 2026  
**Repo:** antonellof/peerclaw (MIT)  
**Fork:** jvanleur2234-glitch/peerclaw ✅  
**Stars:** ~800+ | **Language:** Rust + TypeScript  

## What It Is
PeerClaw is a decentralized, peer-to-peer AI agent network built in Rust. It pools GPU compute across a network of peers who share resources, transact with a native token economy, and run local AI inference — all in a single static binary (no containers).

## Key Capabilities
- **AI Inference:** Local GGUF models (Llama, Phi, Qwen, Gemma) with GPU acceleration (Metal/CUDA via llama-cpp-2)
- **Vector Memory:** Semantic search (HNSW), hybrid vector+BM25, named collections, pluggable embeddings
- **P2P Network:** Decentralized peer discovery (libp2p, DHT, GossipSub, mDNS), job marketplace
- **Token Economy:** Native wallet, Ed25519, escrow, dynamic pricing, payment channels
- **Skills:** SKILL.md prompts, activation scoring, trust levels, P2P sharing, leak/prompt-injection defenses
- **Tools, WASM sandbox, MCP integration**
- **OpenAI-compatible API:** Drop-in replacement at `/v1/chat/completions` with SSE streaming
- **Web Dashboard:** Network topology visualization

## Relevance to Solomon OS
- **Competitor to AgentFM/Hyperspace:** Direct P2P compute grid alternative
- **Token economy patterns** for Solomon Air credit system
- **Rust-based = fast + memory-safe** for high-performance agent components
- **MCP integration** aligns with Hermes ecosystem
- **Skill sharing via SKILL.md** matches our skill framework

## Recommendation
**INTEGRATE** — P2P compute mesh patterns. Study token economy for Solomon Air credits. Rust components for performance-critical parts.

## Links
- https://github.com/antonellof/peerclaw
- https://github.com/jvanleur2234-glitch/peerclaw