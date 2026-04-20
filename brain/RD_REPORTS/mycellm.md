# RD Report: mycellm/mycellm

**Date:** 2026-04-20
**Fork:** jvanleur2234-glitch/mycellm
**License:** Apache 2.0
**Category:** Distributed AI Compute (P2P)
**Relevance:** 🟡 Worthwhile (AgentFM competitor)

## What It Is

P2P GPU inference network that pools hardware across the internet. Run models (llama.cpp, vLLM) via QUIC transport. Credit economy, privacy safeguards, private networks, OpenAI-compatible API. iOS app available.

## Key Capabilities

- **P2P GPU pooling**: Distributed inference across seeders
- **Credit economy**: Earn credits by seeding, spend when consuming. Ed25519-signed receipts
- **Sensitive Data Guard**: On-device scanning for API keys/PII
- **Private networks**: Invite-only federation for teams/orgs
- **OpenAI-compatible API**: `/v1/chat/completions` drop-in
- **iOS app**: Native iPad/iPhone serving inference at 30+ tokens/sec on Metal

## Comparison to Solomon OS Stack

- P2P GPU inference → AgentFM direct competitor
- Credit economy → model for compute tokenization
- Privacy safeguards → important for enterprise trust

## Recommendation

**SKILL** — Well-architected P2P inference with good privacy features. Direct competitor to AgentFM. Study the credit economy and NAT traversal patterns. Fork already exists.