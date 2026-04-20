# RD Report: TrentPierce/Shard

**Date:** 2026-04-20
**Fork:** jvanleur2234-glitch/Shard
**License:** FSL-1.1-ALv2 (Functional Source License)
**Category:** Agent Execution / Observability
**Relevance:** 🟡 Worthwhile

## What It Is

Agent execution runtime that decides where workflow steps run (personal/private/public capacity). Receipt-first observability: every step emits a durable receipt with routing, trust, cost, latency details. Provenance graph explains execution choices.

## Key Capabilities

- **Receipt-first execution**: Every step emits a durable receipt
- **Cross-topology routing**: Workflows can use personal, private, and public capacity
- **Reconstructable provenance**: Graph rebuilt from parent_receipt_id links
- **Graceful degradation**: Failed paths stay visible instead of generic errors
- **OpenAI-compatible**: `/v1/chat/completions` still works
- **Live network**: https://shardnetwork.live

## Comparison to Solomon OS Stack

- Receipt/observability → aligns with Solomon's audit trail needs
- Cross-topology routing → relevant for hybrid compute strategies
- Provenance → key for agent decision accountability

## Recommendation

**SKILL** — The receipt-first approach is excellent for agent observability. Would complement Solomon's mission logging. License is FSL (non-standard) — check commercial use terms. Fork already exists.