# KwaaiNet — Rust-Based Decentralized AI Infrastructure

**Fork:** Already forked to `jvanleur2234-glitch/KwaaiNet`  
**License:** MIT  

## What It Is
A Rust-first, open-source project for sovereign, decentralized AI infrastructure. Users own and operate their own compute, storage, and data within a peer-to-peer network. The DTG (Decentralized Trust Graph) provides trust, credentials, and identity management.

## Key Features
- **Rust-native CLI** (`kwaainet`) for end-user interaction
- **Ed25519 keys** and `did:peer` DIDs derived from libp2p PeerIds
- **W3C verifiable credentials** with time-decayed trust scoring
- **Parallel bootstrap peers** with automatic failover for network resilience
- **Pre-built binaries** for macOS, Linux, Windows; builds from source via Cargo
- **Active development**: latest v0.3.24 (2026-03-20), multiple contributors
- **GliaNet Fiduciary Pledge** governance model

## Why It Matters for AgentFM Competitors
- Direct competitor to **AgentFM**, **mycellm**, **PeerClaw** for P2P AI compute
- Rust-based = high performance, memory safety, production-grade
- Trust graph is a differentiator — none of the other P2P AI nets have W3C VC-based identity
- Network is live and operational

## Comparison to AgentFM / PeerClaw / mycellm
| Feature | KwaaiNet | AgentFM | PeerClaw | mycellm |
|---|---|---|---|---|
| Language | Rust | Go | Rust | Python |
| License | MIT | ? | MIT | ? |
| Trust model | W3C VC + DTG | None | Token economy | Credit system |
| DID method | did:peer | None | None | None |
| Status | v0.3.24 live | Active | Active | Active |
| Binary releases | ✅ | ✅ | ✅ | ✅ |

## Verdict
**FORGE** — KwaaiNet is a serious competitor to AgentFM. The Rust + W3C VC identity layer is a differentiator. Fork and study the DTG implementation for potential Hermes trust framework integration.