# RD_REPORT: cass_memory_system (Dicklesworthstone)

## What It Is
**cass-memory (cm)** — Procedural memory for AI coding agents. Transforms scattered agent sessions (Claude Code, Cursor, Codex, etc.) into persistent, cross-agent memory so every agent learns from every other's experience.

**342 stars**, MIT License, 778 commits, active development. Supports Linux/macOS/Windows.

## Core Concept
```
Sessions → ACE Pipeline (Annotate → Codify → Extract) → Playbook (rules)
Query → Retrieve relevant rules + history snippets for any task
```

The playbook is a YAML file of scored rules (bullet points) that agents query before tasks. Cross-pollination across agents: Claude Code's auth debugging strategy becomes available to Cursor, etc.

## Key Features

**Commands:**
- `cm context "<task>" --json` — Get relevant rules + history before starting work
- `cm onboard` — Guided onboarding: analyze sessions, extract rules, fill playbook gaps
- `cm outcome success/failure` — Record rule outcomes, update confidence scores
- `cm quickstart --json` — Self-documenting API for agents
- `cm doctor --json` — System health check

**ACE Pipeline:** Annotate → Codify → Extract. Agents read sessions with template context, extract rules to playbook, track outcomes.

**Scoring Algorithm:** Rules scored by effectiveness (outcome history) × relevance (task similarity). Mature rules ("proven") vs new ("experimental").

**MCP Server:** Can serve as MCP server for Claude/other agents.

**Privacy:** Local-first. `~/.cass-memory/playbook.yaml`. Remote history opt-in only.

**Trauma Guard:** Safety system to prevent harmful rule propagation.

## What We'd Use It For
1. **Russell Tuna onboarding** — Build a Solomon OS playbook from our session history
2. **Cross-agent memory** — Every new session queries accumulated rules before working
3. **Session → playbook pipeline** — Auto-extract rules from Telegram sessions + Zo conversations
4. **Hermes memory layer** — Complement existing brain/ with procedural rules

## Comparison to What We Have
- **vs Solomon OS brain/**: brain/ is static knowledge (docs, ideas). cass-memory is procedural (how to do things, anti-patterns, debugging strategies). Different but complementary.
- **vs ML-Master HCC**: ML-Master is 3-tier memory architecture. cass-memory is rule extraction + scoring from sessions. cass-memory is more concrete/practical.
- **vs Supermemory AI**: Supermemory is web content + chat memory. cass-memory is coding session procedural memory.

## Recommendation: **INTEGRATE**

**Rationale:** 342 stars, MIT, proven architecture. The `cm context` pattern (query before task) + ACE pipeline (session → rules) fills a gap in Solomon OS. We already have session history (Telegram summaries, Zo conversations). Hooking cass-memory into Russell Tuna workflow = agents that actually learn from past sessions.

**Next Steps:**
1. Install: `curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/cass_memory_system/main/install.sh" | bash -s -- --easy-mode --verify`
2. Run `cm onboard status` to see current playbook state
3. Point `cm onboard read` at our Telegram session summaries in `solomon-vault/raw/telegram_SUMMARY_*.md`
4. Extract rules into playbook
5. Add `cm context "<task>" --json` to Russell Tuna workflow start

**Risk:** Dependencies on Bun runtime. MIT license allows integration.
