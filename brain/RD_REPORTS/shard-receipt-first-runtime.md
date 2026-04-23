# RD Report: TrentPierce/Shard — Receipt-First Multi-Topology Agent Runtime

**Repo:** `TrentPierce/Shard`
**License:** FSL-1.1-ALv2 (Functional Source License — proprietary)
**Forked:** NO (FSL license — cannot use)
**Date:** 2026-04-23
**Category:** Distributed AI Compute / Agent Runtime

## What It Is

Shard is an agent execution runtime for multi-topology workflow orchestration. Agents submit tasks with routing policies and get back: final output + append-only receipt chain + provenance graph + fallback paths + cost/latency/trust metadata per step.

Key topology tiers:
- **Personal**: own laptop/workstation
- **Private**: team/company Shard nodes
- **Public**: shared specialist capacity on broader mesh

## Key Capabilities

- **Receipt-first workflow observability** — every step emits durable receipt with routing, trust, cost, latency, failure details
- **Reconstructable provenance** — graph rebuilt from `parent_receipt_id` links
- **Cross-topology routing** — single workflow uses personal/private/public capacity under explicit policy
- **Graceful degradation** — failed paths stay visible with full cost comparison
- **OpenAI-compatible API** (`/v1/chat/completions`) with differentiated workflow APIs
- **Browser Scout nodes** (WebGPU) + desktop Shard Verifier nodes (BitNet 1.58b)
- **Proof-of-Compute receipts** — cryptographic trust for distributed inference

## Solomon OS Fit

**SKILL** — Receipt/provenance pattern is directly applicable to Solomon OS agent operations. Every skill execution should emit a verifiable receipt. The multi-topology routing concept (personal→private→public) maps to Solomon's: local Ollama → Hermes hosted → external API tier. FSL license prevents code use but concept is valuable.

## Comparison to AgentFM

| | Shard | AgentFM |
|--|-------|---------|
| License | FSL (proprietary) | Apache 2.0 |
| Focus | Provenance/routing receipts | P2P compute grid + containers |
| Browser compute | Scout nodes (WebGPU) | Not primary |
| Desktop nodes | Desktop verifier app | Boss/worker model |
| Topology | Personal/Private/Public tiers | Public encrypted mesh |

## Recommendation

**SKILL** — Study the receipt-chain + provenance graph pattern for Solomon OS operation logging. Do NOT fork (FSL license). The idea of tracking every agent step with cost/trust/failure metadata is directly implementable in Solomon Vault.