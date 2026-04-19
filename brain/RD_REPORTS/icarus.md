# R&D Report: Icarus — Hermes Shared Memory + Wiki

**Date:** April 18, 2026
**Repos:** 
- github.com/esaradev/icarus-daedalus (249 stars, MIT)
- github.com/esaradev/icarus-plugin (51 stars, MIT)
**Forked:** jvanleur2234-glitch/icarus-daedalus, jvanleur2234-glitch/icarus-plugin

---

## What It Is

Icarus is a shared memory + wiki plugin for Hermes agents. The core promise: one agent learns it, every agent can recall it. Knowledge compounds instead of evaporates.

---

## Key Features

### 1. Shared Memory Across All Agents
- All Hermes agents share one brain in ~/fabric/
- fabric_write / fabric_read / fabric_search primitives
- Hot/Warm/Cold tiering with auto-curation
- Cross-platform recall (Telegram ↔ Slack ↔ Discord)

### 2. Self-Building Wiki
- Every write automatically extracts into entity pages, topic pages, and cross-references
- curator.py runs in background, re-tiers and indexes entries
- index.json maintained automatically for fast lookups

### 3. Memory Maintenance
- Quality scoring per entry
- Duplicate detection
- Auto-archival of stale/dead weight entries
- Brain stays clean as it grows

### 4. Training Data Export
- export-training.py → together.jsonl
- Self-train.sh → fine-tune on Together AI
- Your best agent work becomes fine-tuning pairs for replacement models
- Path: shared memory → training data → fine-tuned model

---

## How It Works

### Architecture
```
Hermes Agent → Icarus Plugin (hooks/tools/scoring)
             → ~/fabric/ (Markdown + YAML frontmatter, no DB)
             → curator.py (auto-tiers, indexes)
             → export-training.py → together.jsonl
```

### Entry Schema (Markdown + YAML)
```
---
id: abc12345
agent: russell
platform: telegram
timestamp: 2026-04-18T12:00:00Z
type: decision
tier: hot
summary: Use Icarus for cross-agent memory
project_id: solomon-os
session_id: sess_001
refs: [zo:xyz678]
tags: [memory, hermes, integration]
---
Body text describing the entry...
```

### Tier System
- **Hot** (<24h): loaded in every context
- **Warm** (1-7 days): loaded on relevance
- **Cold** (>7 days): archived, loaded only on explicit request
- Curator auto-re-tiers entries over time

### Hooks
- `on_session_start`: loads baseline context
- `pre_llm_call`: topic-aware retrieval from fabric
- `post_llm_call`: real-time decision capture
- `on_session_end`: auto-writes session summary

---

## Integration with Solomon OS

### Current Gap
Solomon OS / Hermes has per-agent memory but no shared cross-agent memory. Zo, Russell Tuna, and Hermes each have separate contexts. Nothing shared between them persists well.

### What Icarus Adds
1. **Shared brain** — Zo learns something → Russell Tuna can recall it
2. **Cross-platform** — Telegram session writes → CLI session reads
3. **Self-improving** — every decision logged → patterns emerge → training data
4. **Wiki layer** — entities and topics auto-build over time

### Integration Steps
1. Clone icarus-daedalus + icarus-plugin
2. Copy icarus-plugin/* into Hermes plugins dir
3. Set FABRIC_DIR in Hermes .env
4. Optional: TOGETHER_API_KEY for self-training
5. All Solomon OS agents (Zo, Russell, Hermes) now share ~/fabric/

---

## License & Stars
- MIT ✅ — clean license, no share-alike issues
- icarus-daedalus: 249 stars
- icarus-plugin: 51 stars
- Active development (latest release Mar 29, 2026)

---

## Recommendation

**FORGE — Integrate immediately.**

This directly fills the #1 gap in Solomon OS: cross-agent shared memory with a self-building wiki. The training data export feature also makes it the foundation for the "Solomon OS gets smarter over time" vision Joseph described.

Priority: HIGH. Install as the shared memory layer for all Solomon OS agents.
