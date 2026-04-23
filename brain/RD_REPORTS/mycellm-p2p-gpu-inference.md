# RD Report: mycellm — P2P GPU Inference Network

**Repo:** `mycellm/mycellm`
**License:** Apache-2.0 | **Language:** Python/TypeScript
**Forked:** Yes (jvanleur2234-glitch/mycellm)
**Date:** 2026-04-23

## What It Is

Open-source project that pools GPUs across the internet into a P2P inference network. Provides an OpenAI-compatible API, credit-based economy, and private federated networks — without relying on cloud vendors.

## Key Features

- **Credit economy** — earn by seeding GPU, spend by consuming; no cryptocurrency
- **Privacy safeguards** — on-device scanning for API keys/PII; sensitive queries route to local models
- **Private federated networks** — invite-only federation, NAT traversal for P2P connectivity
- **OpenAI-compatible API** — drop-in replacement at `/v1/chat/completions`
- **Cross-device** — iOS app, supports serving on personal hardware (iPad with Metal)
- Uses QUIC from bootstrap relay to GPU seeders; llama.cpp/vLLM for inference

## Comparison to AgentFM

- **AgentFM** — containerized tasks (Podman), ephemeral sandboxing, libp2p mesh
- **mycellm** — credit economy, OpenAI-compatible API, privacy-first, no containers
- Both compete in decentralized GPU compute space

## Solomon OS Fit

**SKILL** — Credit economy and private federated network patterns could enhance AgentFM competitor analysis. The OpenAI-compatible API is a key differentiator.

## Recommendation

**SKILL** — Study credit economy pattern for potential agent compute marketplace.