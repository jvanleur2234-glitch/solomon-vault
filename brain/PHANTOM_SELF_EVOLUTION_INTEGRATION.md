# Phantom Self-Evolution → Solomon OS Integration Spec

*Date:* 2026-04-21
*Source:* `/home/workspace/phantom/docs/self-evolution.md`
*Purpose:* Integrate Phantom's self-evolution engine into Solomon OS

---

## What We're Building

Phantom's self-evolution engine is the most production-ready implementation of "AI that gets better over time" we've found. After every session, it reflects and rewrites its own configuration. Day 30 knows things Day 1 didn't.

We integrate this into Solomon OS so Russell Tuna, Hermes, and all agents improve automatically — not just remember, but evolve.

---

## Architecture

```
Session Complete
       │
       ▼
┌─────────────────┐
│  Observe        │ Extract corrections, preferences, domain facts
│  (Step 1)       │ from session transcript
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Self-Critique  │ Compare observations vs current config
│  (Step 2)       │ Ask: what should change?
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Delta Gen      │ Generate minimal, targeted config changes
│  (Step 3)       │ Each targets a specific file + section
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  5-Gate         │ Constitution | Regression | Size | Drift | Safety
│  Validation     │ Sonnet 4.6 as cross-model judge
│  (Step 4)      │ Triple-judge voting, minority veto
└────────┬────────┘
         │ APPROVED
         ▼
┌─────────────────┐
│  Apply          │ Write to solomon-config/, bump version
│  (Step 5)       │ Snapshot metrics
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Consolidate    │ Every N sessions: compress observations
│  (Step 6)       │ into principles, prune redundant entries
└─────────────────┘
```

---

## Directory Structure

```
/home/workspace/solomon-vault/solomon-config/
├── constitution.md       # Tier 1 immutable principles (NEVER modified by evolution)
├── persona.md           # Communication style and personality
├── user-profile.md      # Joseph's preferences and corrections
├── domain-knowledge.md   # Accumulated expertise about JCPaid, clients, tools
├── strategies/
│   ├── task-patterns.md      # Learned approaches to common tasks
│   ├── tool-preferences.md   # Preferred tools and workflows
│   └── error-recovery.md     # Learned error handling
└── version.json          # Current version, parent, metrics snapshot

/home/workspace/solomon-vault/sessions/
└── [session-id].json     # Session transcripts for evolution processing
```

---

## Config Files

### constitution.md (Immutable)
```
# Solomon OS Constitution — Tier 1 (Never Modified by Evolution)

## Core Principles
- JCPaid runs 24/7 — finds clients, does the work, collects payment
- Solomon OS serves Joseph's business, never the other way around
- Every AI action should compound — no throwaway work
- Security is non-negotiable — zero credential exposure

## Hard Rules
- NEVER expose API keys or credentials in config files or logs
- NEVER commit .env files or secrets to version control
- NEVER execute code from untrusted sources without sandbox
- ALWAYS validate before applying config changes
- ALWAYS maintain rollback capability

## Guardrails
- Config changes must pass 5-gate validation
- Safety gates use triple-judge voting with minority veto
- Domain knowledge cannot override constitution
```

### persona.md (Evolvable)
```
# Solomon OS Persona

## Communication Style
- Concise by default, thorough when it matters
- Actions speak louder than filler words
- Earn trust through competence
- Be the assistant you'd actually want to talk to

## Tone
- Smart friend who doesn't work in tech
- No jargon without translation
- Opinions welcome, sycophancy unwelcome

## Behavior
- Resourceful before asking
- Read the file, check the context, search for it
- Then ask only if stuck
```

### user-profile.md (Evolvable)
```
# Joseph's Preferences

## Updated by Evolution Engine
## DO NOT EDIT MANUALLY — changes will be overwritten
```

### domain-knowledge.md (Evolvable)
```
# Accumulated Domain Knowledge

## JCPaid Business
- Primary: AI Employee Agency (Jack Vanleur as first client)
- Secondary: Solomon Browser
- Tertiary: Faceless Kids YouTube

## Tools & Stack
- Ollama: local inference (qwen3:1.7b via Russell Tuna)
- Hermes: hosted execution layer with 94+ skills
- NVIDIA Build: secondary provider (MiniMax M2.7, 40 req/min free tier)
- Meilisearch: hybrid vector+keyword search
- Runline: 188 API plugins

## Clients
- Jack Vanleur: Real estate agent, first AI Employee Agency client
  - Tools: MLS, CRM, email, CMA reports
  - Preferences: [evolved over sessions]

## Learned Patterns
- [Entries added by evolution engine after each session]
```

---

## 5-Gate Validation

| Gate | Check | Failure Action |
|------|-------|----------------|
| Constitution | Violates immutable principles? | Reject |
| Regression | Breaks golden test cases? | Reject |
| Size | Config file over 200 lines? | Reject |
| Drift | Too far from original? | Reject |
| Safety | Touches protected patterns? | Reject |

### Safety Gate Details
- No credential changes
- No permission escalation
- No external network calls in config
- No code execution directives
- No modification of constitution.md

---

## Versioning

```json
{
  "version": 42,
  "parent": 41,
  "timestamp": "2026-04-21T16:30:00Z",
  "session_id": "con_WySXL1kTNKZVOOhb",
  "changes": ["domain-knowledge.md", "user-profile.md"],
  "metrics_snapshot": {
    "total_sessions": 150,
    "success_rate": 0.94,
    "correction_rate": 0.05
  }
}
```

### Rollback
If metrics degrade after evolution (success rate drops, correction rate increases), rollback to previous version:
```bash
# Rollback to version 41
cp solomon-config/version.json solomon-config/versions/v42.json
cp solomon-config/versions/v41.json solomon-config/version.json
```

---

## Implementation Plan

### Phase 1: Core Infrastructure
1. Create `solomon-config/` directory structure
2. Create initial config files (constitution.md, persona.md, user-profile.md, domain-knowledge.md)
3. Create version.json with version 0
4. Create `sessions/` directory

### Phase 2: Evolution Pipeline
1. Create `solomon-evolution/engine.py` — 6-step pipeline orchestrator
2. Create `solomon-evolution/observe.py` — observation extraction
3. Create `solomon-evolution/critique.py` — self-critique
4. Create `solomon-evolution/delta.py` — delta generation
5. Create `solomon-evolution/validate.py` — 5-gate validation
6. Create `solomon-evolution/apply.py` — apply changes
7. Create `solomon-evolution/consolidate.py` — periodic consolidation

### Phase 3: Integration
1. Wire into Solomon Heartbeat (end of session trigger)
2. Wire into Russell Tuna bot (post-session hook)
3. Wire into Hermes (skill evolution)
4. Create CLI: `solomon-evolution run --session-id XXX`

### Phase 4: LLM Judges
1. Implement Sonnet 4.6 as cross-model judge (when API key available)
2. Implement triple-judge voting with minority veto
3. Track judge costs in metrics.json

---

## Files to Create

```
/home/workspace/solomon-evolution/
├── __init__.py
├── engine.py          # Main orchestrator
├── observe.py         # Step 1: extract observations
├── critique.py        # Step 2: self-critique
├── delta.py           # Step 3: generate deltas
├── validate.py        # Step 4: 5-gate validation
├── apply.py           # Step 5: apply approved changes
├── consolidate.py     # Step 6: periodic consolidation
├── judges.py          # LLM judge implementations
├── versioning.py      # Git-like version management
└── cli.py             # CLI interface

/home/workspace/solomon-vault/solomon-config/
├── constitution.md
├── persona.md
├── user-profile.md
├── domain-knowledge.md
├── strategies/
│   ├── task-patterns.md
│   ├── tool-preferences.md
│   └── error-recovery.md
└── version.json

/home/workspace/solomon-vault/sessions/
└── .gitkeep
```

---

## Key Differences from Phantom

| Aspect | Phantom | Solomon OS |
|--------|---------|------------|
| Runtime | Bun + TypeScript | Python + shell |
| Agent | Claude Agent SDK (Opus 4.6) | Russell Tuna + Hermes |
| Memory | Qdrant + Ollama | Solomon OS brain files |
| Channels | Slack/Telegram/Email | Telegram primary |
| Evolution trigger | Post-session | Solomon Heartbeat |

---

## Status

- [ ] Phase 1: Core Infrastructure (pending)
- [ ] Phase 2: Evolution Pipeline (pending)
- [ ] Phase 3: Integration (pending)
- [ ] Phase 4: LLM Judges (pending)

*Created: 2026-04-21*
