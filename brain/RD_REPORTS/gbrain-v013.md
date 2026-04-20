# RD Report: GBrain v0.13 — Garry Tan's Agent Knowledge Brain

## What It Is

GBrain is Garry Tan's (Y Combinator President & CEO) open-source personal knowledge brain for AI agents. It builds a self-wiring knowledge graph from ingested data (pages, meetings, emails, tweets, voice calls) and exposes typed relationships without extra LLM calls. Version 0.13 dropped graph queries that extract entity properties into YAML properties — making knowledge retrievable, not just stored.

**Repo:** https://github.com/garrytan/gbrain  
**Stars:** Not publicly listed (internal YC tool, growing fast via OpenClaw/Hermes ecosystem)  
**License:** MIT  
**Stack:** TypeScript + Bun + Postgres/pglite (WASM) + pgvector

---

## Key Innovation (v0.13)

The core insight from Garry's tweet:

> "It's not just about ingesting more info. It's about processing it in a way that makes it retrievable."

GBrain v0.13 graph queries now pull out entity properties into YAML properties. This means:

- Entities (people, companies, meetings) get structured YAML frontmatter
- Graph queries can traverse typed relationships (works_at, invested_in, founded, advises)
- No extra LLM calls for linking — automatic typed link extraction
- Backlink-boosted ranking for hybrid search

---

## Architecture

### Knowledge Model
```
Page = YAML frontmatter + COMPILED TRUTH section + append-only TIMELINE
```

- **Above the line:** Current understanding, structured fields (State), Open Threads, See Also cross-links
- **Below the line:** Append-only chronological evidence log with date/source/actions

### BrainEngine Interface (pluggable backends)
- `PostgresEngine` — Supabase-backed (power users)
- `PGLiteEngine` — Embedded Postgres 17.5 via WASM, zero-config default
- `DuckDBEngine` — Future (researchers)
- `SQLiteEngine` — In progress (contributors)

### Core Operations
- `getPage, putPage, deletePage, listPages` — page CRUD
- `searchKeyword, searchVector` — hybrid search
- `upsertChunks, getChunks` — embedding storage
- `addLink, removeLink, getLinks, getBacklinks, traverseGraph` — graph operations
- `addTimelineEntry, getTimeline` — evidence tracking
- `putRawData, getRawData` — raw ingestion
- `createVersion, getVersions, revertToVersion` — version control

### 26 Skills (dispatched via skills/RESOLVER.md)
- Signal detection (always-on, parallel, non-blocking)
- Brain ops (read/write/lookup/citation)
- Query, enrich, data-research, publish
- Ingest variants: idea-ingest, media-ingest, meeting-ingestion, generic ingest
- Thinking skills (GStack): office-hours, ceo-review, investigate, retro
- Operational: task, daily-prep, briefing, cron, reports, skill-create, autopilot, soul/audit

### Integrations (self-installing recipes)
- ngrok-tunnel, credential-gateway
- voice-to-brain (Twilio + OpenAI)
- email-to-brain, x-to-brain (Twitter)
- calendar-to-brain, meeting-sync

---

## Benchmark Results

- **Graph-only F1:** ~86.6%
- **Recall@5 / Precision@5:** notable improvements over baseline
- **Scalable to:** thousands of pages, people, companies with autonomous background cron tasks

---

## Relevance to Solomon OS

**Direct overlap with:**
- Solomon OS brain/memory architecture
- Russell Tuna's knowledge graph design
- Hermes agent brain system
- Personal knowledge management (Second Brain Portal)

**Specific lessons:**
1. **YAML frontmatter = structured retrieval** — Solomon OS pages should use typed YAML properties for entity attributes (name, role, organization, relationship type)
2. **Self-wiring graph** — entities auto-link via typed relationships without LLM calls (Solomon should do the same)
3. **Compiled truth + timeline** — Solomon OS notes need "current state" above the line and "evidence log" below the line
4. **PGLite for zero-config** — embed Postgres in the agent for portability (consider for Russell Tuna fork)
5. **Skills resolver pattern** — Solomon Bus should use a similar trigger-based skill dispatcher

---

## Recommendation: INTEGRATE

**Priority:** High

GBrain's graph-query + YAML properties pattern is exactly what Solomon OS needs for its brain layer. The self-wiring knowledge graph with typed relationships and compiled truth/timeline split is a proven architecture.

**Next steps:**
1. Clone GBrain to `/home/workspace/agency-agents/gbrain/` 
2. Study `docs/GBRAIN_RECOMMENDED_SCHEMA.md` for Solomon OS page schema
3. Study `skills/RESOLVER.md` for Solomon Bus skill dispatch pattern
4. Consider PGLiteEngine as embedded brain backend for Russell Tuna per-user instances
5. Extract YAML property extraction logic for Solomon OS entity/metadata system

---

## Rating

| Dimension | Score |
|-----------|-------|
| Stars / Popularity | Growing fast via YC ecosystem |
| License | MIT ✓ |
| Technical Depth | High — production-grade brain for OpenClaw/Hermes |
| Complement to Solomon OS | High — direct architectural overlap |
| Differentiation | Unique — self-wiring graph + typed relationships |
| **Overall** | **WORTHWHILE — INTEGRATE** |

---

*Report generated: 2026-04-19*
*Queue entry: gbrain-v013-001*