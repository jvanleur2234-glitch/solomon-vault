# Solomon Vault — External Brain for Solomon OS

Personal vault for Joseph's AI business. Every conversation with Zo, Russell Tuna, or Hermes builds on the last. No context lost.

## Core Principle

**Folders group by purpose. Links group by meaning.** A note lives in one folder (its home) but links to many notes (its context). Agents maintain this graph — linking client notes to projects, decisions, and results automatically. A note without links is a bug.

## Session Workflow

### Start of Session

Run `/standup` — loads North Star, active projects, recent changes, open tasks, leads, and services status.

### During Session

Talk naturally. Mention a decision you made, a client you found, a win, a tool that broke, a new idea. The classify-message.py hook auto-detects:
- Decisions → Decision Record
- Leads → Lead note + leads index
- Wins → Brag doc
- Clients → Client note + org/clients
- Tools/Services → Services status
- Business ideas → Ideas pipeline

For freeform dumps, say `/dump` and narrate everything — routing is automatic.

### End of Session

Say "wrap up" to invoke `/wrap-up` — verifies notes, updates indexes, spots uncaptured wins, logs session to raw/.

---

## Folder Structure

| Folder | Purpose |
|--------|---------|
| `brain/` | Solomon OS memory — North Star, Key Decisions, Patterns, Gotchas, Memories |
| `work/active/` | Active projects, current client work |
| `work/leads/` | Prospect clients and leads |
| `work/archive/` | Completed/signed clients |
| `work/incidents/` | Service outages, errors, troubleshooting |
| `org/clients/` | Signed client notes — one per client |
| `org/people/` | Personal contacts, partners, contractors |
| `perf/brag/` | Wins, revenue, milestones |
| `reference/` | Tool docs, API references, architecture |
| `templates/` | Note templates |
| `raw/` | Session logs (daily .jsonl) |
| `.solomon/commands/` | Slash commands |
| `.solomon/scripts/` | Hooks and utilities |
| `.solomon/agents/` | Subagents |

---

## Note Types

| Type | Location | Key Fields |
|------|----------|------------|
| Client | `org/clients/` | name, services[], status, revenue, contact |
| Lead | `work/leads/` | name, source, status, score, follow_up |
| Project | `work/active/` | client, services, status, progress |
| Win | `perf/brag/` | date, description, revenue, evidence |
| Service | `reference/` | name, status, url, last_check |
| Business Idea | `brain/` | title, effort, revenue_ceiling, status |
| Decision | `brain/Key Decisions.md` | date, decision, rationale, outcome |

---

## Slash Commands

| Command | What It Does |
|---------|--------------|
| `/standup` | Morning kickoff — load context, show status, suggest priorities |
| `/dump` | Freeform capture — route everything to right notes |
| `/wrap-up` | End-of-session review — verify notes, update indexes, brag doc |
| `/capture-lead <name> <source>` | Log a new lead with auto-scoring |
| `/capture-win <description> <revenue>` | Log a win to brag doc |
| `/new-client <name> <services>` | Onboard a new client |
| `/service-status` | Check all live services |
| `/ideas-pipeline` | Show ranked business ideas with status |
| `/log-session` | Archive current session to raw/ |
| `/weekly` | Cross-session synthesis — patterns, wins, next week |

---

## Hooks

**classify-message.py** — runs on every message, auto-detects:
- Decision signals → routing hint
- Lead signals → routing hint  
- Win signals → routing hint
- Client signals → routing hint
- Service/tech signals → routing hint

**session-start.sh** — runs on session start:
- Reads brain/North Star.md
- Lists active work
- Checks service status
- QMD re-index

**pre-compact.sh** — runs before context compaction:
- Logs session transcript to raw/YYYY-MM-DD.jsonl

---

## Linking Rules

- A note without links is a bug
- Client notes link to their projects, wins, and decisions
- Lead notes link to source (where discovered)
- Win notes link to client/project that generated them
- Service notes link to incidents when applicable
- North Star goals link to projects advancing them

---

## Tags Convention

Frontmatter tags (not inline):
- `type: client | lead | win | service | idea | decision`
- `status: active | closed | won | lost | archived`
- `quarter: Q1-2026 | Q2-2026 | etc.`
- `revenue: $X` (for wins and clients)

## Memory System

All durable knowledge lives in `brain/`. The key files:
- `brain/North Star.md` — current goals, priority order
- `brain/Key Decisions.md` — significant decisions + reasoning
- `brain/Patterns.md` — what works, what repeats
- `brain/Gotchas.md` — what broke and why
- `brain/Memories.md` — index of all memory topics
- `brain/Services.md` — live services, URLs, status, last check
- `brain/Business Ideas.md` — ranked idea pipeline
