# RD Report: PeerClaw — Rust P2P AI Agent Network

## Summary
PeerClaw is a Rust-based decentralized P2P AI agent network for distributed AI compute without centralized infrastructure. Single static binary, shares compute resources, trades tokens, executes AI tasks. Libp2p (Kademlia, GossipSub, mDNS, Noise). MIT licensed.

## What It Does
- **P2P Network**: Libp2p-based mesh for compute sharing
- **Local AI Inference**: GGUF models (Llama, Phi, Qwen, Gemma) with GPU acceleration
- **Vector Memory**: Semantic/hybrid search
- **P2P Job Marketplace**: Request→Bid→Execute→Settle with escrowed payments
- **Skill System**: YAML prompts
- **WASM Tools**: Sandboxed tool execution
- **MCP Interface**: Model Context Protocol integration
- **OpenAI-Compatible API**: `/v1/chat/completions` drop-in
- **Native Token Economy**: Micro-payments and trust-based access

## Tech Stack
- Language: Rust
- License: MIT
- Network: Libp2p (Kademlia, GossipSub, mDNS, Noise)

## Strategic Fit for Solomon OS

**WATCH** — AgentFM competitor. P2P job marketplace + escrowed payments + token economy is the exact model for JCPaid compute marketplace. Key patterns:
- Escrowed payment system for P2P compute
- WASM sandboxed tools
- MCP integration
- OpenAI-compatible API for easy adoption

## Risk/Concerns
- Rust codebase requires Go/Rust expertise
- Early stage, community size unknown
- Token economy adds complexity

## Verdict
STUDY — Monitor closely. The escrowed payment model and P2P job marketplace pattern is directly relevant to AgentFM/Hermes compute grid. Watch for integration opportunities.

## Links
- Repo: https://github.com/antonellof/peerclaw
- Fork: Not yet forked