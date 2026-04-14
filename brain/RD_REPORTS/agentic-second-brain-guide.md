# RD Report: Agentic Second Brain Guide

**Repo:** `bbuch82/agentic-second-brain-guide`
**Stars:** ~400 (estimated, based on similar guides)
**License:** MIT
**Date sourced:** 2026-04-14
**Priority:** 🟡 Worthwhile

---

## What It Is

A detailed self-hosted guide for building a personal "Second Brain" AI agent using **OpenClaw + Obsidian + Telegram** on a private server (Hetzner VPS). Emphasizes privacy and local control, avoiding cloud subscriptions.

### Architecture
- **Runtime:** OpenClaw agent (self-hosted on VPS)
- **Interface:** Telegram bot
- **Knowledge base:** Obsidian vault (Markdown)
- **Sync:** Syncthing for real-time mobile ↔ server sync
- **Memory:** Two-tier — compact brain index in conversations + structured memory files + vector embeddings (Gemini Embedding)

### Six Specialist Agents
| Agent | Role |
|---|---|
| Chief of Staff | Weekly reviews, priorities, project/goal tracking |
| Librarian | Reading processing, knowledge-base maintenance, journaling via cron |
| Scout | Intelligence gathering, industry trends |
| Confidante | Private reflection, emotional well-being |
| Strategist | Project/goal/deadline tracking |
| Coder | Automation scripts, vault tooling, integrations |

### Automated Routines
- **Morning Briefing** — 07:00
- **Evening Journal** — 21:00
- **Weekly Review** — Sundays
- **Reading Pipeline** — URLs → structured notes into Obsidian

### Tech Stack
- OpenClaw (agent framework)
- Obsidian (vault, markdown)
- Telegram (interface)
- Syncthing (cross-device sync)
- Gemini Embedding (vector recall)
- Hetzner VPS (~€5/month)

---

## What We'd Use It For

1. **Adapt the multi-agent persona structure** into Hermes — Chief of Staff, Librarian, Scout, etc. map well to Hermes skill-based agents with scheduled routines
2. **Import the Reading Pipeline** — URL → structured note ingestion into our existing solomon-vault/brain structure
3. **Adopt the two-tier memory pattern** — compact brain index + structured recall files — for Hermes's skill memory system
4. **Obsidian vault compatibility** — Our solomon-vault/brain/ could be browseable in Obsidian with graph view and wikilinks (low effort, high utility)

---

## Comparison to What We Have

| Feature | They Have | We Have |
|---|---|---|
| Agent framework | OpenClaw (custom) | Hermes (skill-based) |
| Knowledge base | Obsidian vault | solomon-vault/brain/ |
| Interface | Telegram | Telegram + Zo app |
| Multi-agent personas | 6 specialists | Russell Tuna + Hermes |
| Scheduled routines | Morning/Evening/Weekly | Cron-based via create_agent |
| Reading pipeline | URL → structured note | Manual |
| Vector embeddings | Gemini | Not configured |
| Cross-device sync | Syncthing | Zo cloud sync |
| Cost | ~€5/month VPS | Included in Zo plan |

**Our advantages:** Already hosted, already connected to Telegram, no VPS management, Zo API built-in.
**Their advantages:** Proven reading pipeline, mature Obsidian integration, two-tier memory with embeddings, established persona framework.

---

## Recommendation

**SKILL** — Adapt the **Reading Pipeline** (URL → structured note) and the **multi-agent persona model** into Hermes. Low effort (porting scripts), high long-term value for knowledge management.

The weekly review, morning briefing, and evening journal patterns could replace/create new scheduled agents in Hermes. The reading pipeline fills our biggest gap in the knowledge ingestion flow.

---

## Files Worth Examining

- `README.md` — full guide
- `obsidian vault structure` — directory schema
- `agents/` — persona definitions
- `routines/` — scheduled scripts
- `reading-pipeline/` — URL ingestion

---

*Report generated: 2026-04-14*
*Source: https://github.com/bbuch82/agentic-second-brain-guide*