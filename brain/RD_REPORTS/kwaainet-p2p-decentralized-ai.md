# KwaaiNet — P2P Decentralized AI Infrastructure
**Forked:** jvanleur2234-glitch/kwaainet | **License:** MIT | **Stars:** ~live | **Updated:** Apr 23, 2026

## What It Is
Decentralized AI infrastructure built in Rust/TypeScript giving users ownership of compute, storage, and data. Uses a Decentralized Trust Graph (DTG) for permissioned trust relationships across nodes.

## Key Components
- **Decentralized Trust Graph (DTG):** Permissioned/credentialed graph establishing trust among nodes without a central control plane
- **GliaNet Fiduciary Pledge:** Guiding principles for fiduciary behavior (quality, trust, responsibility)
- **Native Rust CLI:** Modular architecture, container-less lightweight compute sharing
- **Live Network:** v0.3.24 (2026-03-20), operational with DHT store RPC improvements

## Quick Start
```bash
kwaainet setup        # First-time setup (auto-installs deps)
kwaainet benchmark    # Run benchmark
kwaainet start --daemon  # Start daemon
```

## For Solomon OS / AgentFM
- **Competitor to:** AgentFM, Hyperspace AGI, mycellm
- **DTG trust graph** — interesting for multi-agent trust relationships
- **MIT licensed** — can fork and extend
- Pre-built binaries: macOS, Linux, Windows

## Verdict
**SKILL** — Study DTG architecture for trust graph implementation in Solomon Bus inter-agent communication.
