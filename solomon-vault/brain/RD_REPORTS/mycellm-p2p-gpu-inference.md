# RD Report: mycellm

**Repo:** `mycellm/mycellm`  
**Stars:** Growing | **License:** Apache 2.0 | **Lang:** Python/TypeScript  

## What It Does
P2P GPU inference network that pools heterogeneous hardware across the internet. OpenAI-compatible API with credit economy, privacy guards, and federation support.

## Why It Matters for Solomon OS
- **Credit Economy**: Earn credits by seeding, spend by consuming — bootstrap the network
- **Privacy-First**: On-device prompt scanning, sensitive queries route to local model
- **Federation**: Private networks for teams/orgs — enterprise-ready
- **Drop-in Replacement**: OpenAI-compatible API at /v1/chat/completions
- **iOS App**: Native iOS peer earning credits on mobile

## Key Capabilities
- QUIC transport with NAT traversal across internet
- Ed25519-signed receipts for credit economy (no blockchain)
- Sensitive data guard: on-device scanning for API keys/passwords/PII
- Private federations with fleet management
- Works with Claude Code, aider, Continue.dev, any OpenAI-compatible tool
- iOS app for peer participation

## Comparison to What We Have
vs **AgentFM**: More focused on inference credits than general compute. Less agent-oriented, more API credits marketplace.

## Recommendation
**INTEGRATE** — Credit economy pattern is useful for KwaaiNet. Could use mycellm as inference layer while AgentFM handles general compute.

**Category:** #distributed-ai #inference #p2p #credits
