# RD Report: Deliberate — Shell-Based Async Deliberation

**Date:** 2026-04-22
**URL:** https://github.com/kyleparrott/deliberate
**License:** MIT (inferred)
**Fork:** https://github.com/jvanleur2234-glitch/deliberate

---

## What It Is
Experimental shell-based protocol (`deliberate.sh`) for two AI agents sharing a local machine to deliberate asynchronously. Uses JSONL log per room to store events (seed, messages, acks). Simple read → ack → send → wait → repeat → done loop.

---

## Key Capabilities
- File-based protocol: no network, no API, just shared filesystem
- Two-agent deliberation using Bash + jq
- Rooms stored in `/tmp/deliberation/` as `.jsonl` files
- Seed with context via file or stdin
- Suitable for architecture, code reviews, prioritization decisions

---

## Why It Matters
Asynchronous deliberation between two agents on the same machine using a file-based protocol is the minimal viable multi-agent communication primitive. No complex middleware needed.

---

## Solomon OS Fit
- **SKILL** — Minimal deliberation pattern. File-based IPC is interesting for Hermes subprocess agents. Shell-based = zero dependencies.

---

## Recommendation
**SKILL** — Study for minimal Hermes multi-agent IPC. File-based approach could work for Hermes sub-agents.