# deliberate — Shell-Based Async Deliberation Protocol

## What It Is
Minimal file-based protocol enabling two AI agents on a single machine to deliberate asynchronously via JSONL per room under /tmp/deliberation.

## Key Signals
- **License:** MIT (likely)
- **Lang:** Shell + jq
- **Experimental:** v0.x

## Core Features
- deliberate.sh loop: read → ack → send → wait → repeat → done
- High-level discussions (architecture, code review, prioritization)
- 30sec–2min per exchange; not speed-optimized

## Solomon OS Fit
- **SKILL** — Minimal deliberation protocol worth studying for Solomon Bus inter-agent communication
- Could inspire Hermes inter-agent messaging format

## Recommendation
SKILL — Reference only. Not production-ready.