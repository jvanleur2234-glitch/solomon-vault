# RD Report: PeerClaw — Decentralized P2P AI Compute Network

**Fork:** `jvanleur2234-glitch/peerclaw-new` | **Original:** `antonellof/peerclaw` | **License:** MIT | **Stars:** ~800 | **Lang:** Rust/TypeScript

## What It Is
Single static Rust binary for a decentralized P2P AI compute network. Peers collaborate, share GPU resources, and transact via native token economy. Supports GGUF models (Llama, Phi, Qwen, Gemma) with Metal/CUDA acceleration.

## Key Capabilities
- Decentralized P2P inference with GPU acceleration
- Job marketplace: request → bid → execute → settle via libp2p (Kademlia, GossipSub, mDNS)
- Token economy: Ed25519 wallet, escrow, dynamic pricing, payment channels
- Vector memory with HNSW semantic search + hybrid BM25
- Markdown-based SKILL prompts, trust levels, safety features
- WASM sandbox, MCP integration, OpenAI-compatible API
- Web dashboard for network topology visualization

## Relevance to Solomon OS
- **Distributed AI Compute:** Direct competitor to AgentFM — P2P GPU pooling
- **Skill Framework:** SKILL-based prompt system aligns with Hermes ecosystem
- **Agent Economy:** Token-based compute marketplace model for JCPaid

## Threat Analysis
- MIT licensed, active development
- Token economy requires careful audit for security

## Integration Path
```
SKILL: peerclaw-p2p → integrate as compute provider for AgentFM/Hermes
USE CASE: P2P compute grid, decentralized inference marketplace
```

**Recommendation:** INTEGRATE — Explore as AgentFM competitor for JCPaid compute layer.
