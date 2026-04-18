# RD Report: hermes-lcm

**Repo:** https://github.com/stephenschoettler/hermes-lcm
**Stars:** 195 ⭐ | **License:** MIT | **Lang:** Python (100%)
**Release:** v0.5.0 (April 18, 2026)
**Author:** stephenschoettler (community, 2 contributors)

---

## What It Is

Lossless Context Management plugin for Hermes Agent — a DAG-based context engine that replaces Hermes's built-in lossy compression with an immutable SQLite store, hierarchical summary DAG, and agent retrieval tools.

Core claim: "Bounded context, unbounded memory. Nothing is ever lost."

---

## Key Features

- **Immutable-first store** — every message persisted verbatim in SQLite with FTS5 search
- **Summary DAG** — hierarchical compaction: D0 (minutes) → D1 (hours) → D2 (days)
- **3-level escalation** — L1 detailed summary → L2 bullets → L3 deterministic truncate (guaranteed convergence)
- **Agent tools** — `lcm_grep`, `lcm_describe`, `lcm_expand`, `lcm_expand_query`, `lcm_status`, `lcm_doctor`
- **Large tool-output handling** — opt-in externalization for oversized tool results
- **Opt-in transcript GC** — rewrites already-externalized tool-result rows to compact GC placeholders
- **Per-profile storage** — separate DB per Hermes profile
- **Zero external dependencies** — pure Python, no new runtime deps

---

## v0.5.0 Changelog

- feat: opt-in transcript GC for externalized tool output
- fix: isolate LCM storage per profile + source-aware retrieval
- feat: read-only retention analysis command
- docs: contributing guide added
- feat: externalize oversized tool outputs
- refactor: deduplicate search constants, upgrade silent failure logging

---

## How It Works

1. **Ingest** — every message persisted verbatim to immutable SQLite store
2. **Compact** — when context pressure builds, older messages summarized into D0 leaf nodes
3. **Condense** — D0 nodes condense into D1, up through D2
4. **Escalate** — summaries that are too long escalate through L1→L2→L3
5. **Assemble** — active context = system prompt + highest-depth summaries + fresh tail
6. **Retrieve** — agent drills into compacted history via lcm_* tools

---

## Comparison to Hermes Built-in Compression

| | Hermes built-in | hermes-lcm |
|---|---|---|
| Context loss | Possible in active context | Zero — immutable store |
| Retrieval path | Separate cross-session search | Direct in-plugin recall |
| Summary structure | Flat | Hierarchical DAG |
| Agent drill-down | None | `lcm_expand`, `lcm_grep`, etc. |
| Memory boundary | Fixed context window | Bounded context, unbounded store |

Note: Hermes core does persist original history to `state.db` before compression, so built-in is not fully lossy everywhere — but the active prompt window IS lossy. LCM solves the active window problem.

---

## Relevance to Solomon OS

**Status of our Hermes:** Hermes Router S1/S2/S3 is live on Solomon OS.

**Gap this fills:** Russell Tuna Bot (and Hermes workers generally) lose conversation details when context fills. hermes-lcm is a drop-in upgrade that makes our existing Hermes installation remember everything permanently.

**Compatibility:** Requires Hermes Agent with the pluggable context engine slot (PR #7464 merged). Our Hermes should support it.

---

## Installation

```bash
git clone https://github.com/stephenschoettler/hermes-lcm \
  ~/.hermes/hermes-agent/plugins/context_engine/lcm
```

Then set in config:
```yaml
context:
  engine: lcm
```

Restart Hermes. Verify: `hermes plugins` should show `✓ hermes-lcm`.

---

## Recommendation

**→ INTEGRATE**

One of the simplest possible upgrades to Solomon OS. Cloning the repo and adding one config line gives Russell Tuna and all Hermes workers permanent lossless memory. No new dependencies, no breaking changes.

**Action:** Install on Solomon OS Hermes instance and update HERMES_CAPABILITIES.md.

**Priority:** 🟡 Worthwhile (1-2 on effort scale, meaningful capability gain for Russell Tuna and AI staffing use case)
