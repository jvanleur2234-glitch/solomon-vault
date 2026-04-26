# RD Report: CASS Memory System (cass)

**URL:** https://github.com/Dicklesworthstone/cass_memory_system
**Stars:** 342 (growing fast — viral post April 26, 2026)
**License:** NOASSERTION (custom — check repo)
**Language:** TypeScript (Bun)

---

## What It Is

CASS = "Cassandra" Memory System. A **procedural memory framework for AI coding agents** that transforms scattered session history into persistent, cross-agent memory. Think of it as a "collective intelligence" layer — every agent learns from every other agent's experience.

**3-Layer Cognitive Architecture (ACE Framework):**
```
Episodic Memory (cass)     → Raw session logs from ALL agents
        ↓ cass search
Working Memory (Diary)     → Structured summaries: accomplishments, decisions, challenges, outcomes
        ↓ reflect + curate
Procedural Memory (Playbook) → Distilled rules with confidence scoring
```

**Key Features:**
- **Cross-agent learning**: Sessions from Claude Code, Codex, Cursor, Aider, Gemini, ChatGPT all feed the shared playbook
- **ACE Pipeline**: Accumulate → Curate → Extract (automated)
- **Confidence decay**: 90-day half-life; rules lose confidence without revalidation
- **Harmful multiplier**: One "harmful" mark counts 4x as much as one "helpful" mark
- **Maturity progression**: candidate → established → proven
- **Trauma Guard**: Safety system preventing harmful rule propagation
- **File-based storage**: Playbook YAML + diary JSON; no database dependency
- **Local embeddings** via `@xenova/transformers`: semantic search without API calls
- **Multi-provider LLM**: Anthropic, OpenAI, Google via Vercel AI SDK
- **MCP server mode**: Can serve as MCP tool for external agents
- **Concurrent access**: File locking for multi-agent safety

**CLI Commands:**
- `cm context "<task>"` — retrieve relevant rules + history before starting work
- `cm onboard` — analyze session logs, extract rules
- `cm playbook add "rule"` — add rules manually
- `cm serve` — MCP server mode

---

## What We'd Use It For

- **Russell Tuna cross-session memory**: Instead of each session starting fresh, Russell Tuna could query `cm context` before tasks and learn from past sessions
- **Solomon Bus institutional memory**: Daily sessions write to cass → Diary → Playbook pipeline; overnight worker reflects and distills
- **Hermes skill**: Install `cm` as a Hermes-capable tool; agents can query the shared playbook
- **Shared playbook for AI staffing agency**: When multiple agents work on client projects, they all learn from each other's solved problems

---

## How It Compares to What We Have

| | CASS | Solomon OS Current |
|---|---|---|
| **Memory type** | Procedural (rules + confidence) | Brain files + session summaries |
| **Cross-agent** | Yes — all agents contribute | No — each session is siloed |
| **Confidence decay** | 90-day half-life | None |
| **Automated distillation** | ACE pipeline (LLM reflect) | Manual |
| **MCP native** | Yes | No |
| **Storage** | YAML + JSON files | Markdown files |
| **Learning signal** | Inline feedback: `// [cass: helpful b-xyz]` | Implicit from session reviews |

**CASS is the missing piece** for Solomon OS self-improvement loop. We have the reflection mechanism (via gn hf iteration engine) but CASS has the cross-agent, confidence-tracked, automated curation pipeline that actually makes it work at scale.

---

## Verdict

**🔴 CRITICAL — FORGE NOW**

CASS solves the "Russell Tuna forgets everything between sessions" problem. This is the missing procedural memory layer for Solomon OS. 

Direct integration path:
1. Clone to `/home/workspace/cass_memory_system/`
2. Add `cm context` to Russell Tuna's pre-task protocol
3. Hook Solomon Bus daily session output into `cass onboard`
4. Confidence decay replaces our manual "stale rules" cleanup

Tom Dörr's post just went viral (17 bookmarks, 2379 views in hours). Stars will grow fast. Getting in early matters.

**Recommendation:** FORGE — immediate integration. Clone, test `cm onboard` on Solomon OS session logs, wire into Russell Tuna protocol.
