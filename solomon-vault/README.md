# Solomon Vault

External brain for Solomon OS — Joseph's 24/7 AI business system.

## What It Is

A vault of notes that compounds over time. Every conversation with Zo, Russell Tuna, or Hermes adds to it. No context lost between sessions.

## Core Structure

```
brain/          — Solomon OS memory (North Star, decisions, patterns, gotchas)
work/active/    — Active client projects
work/leads/     — Prospect clients
work/archive/   — Completed/signed clients
org/clients/    — Client notes
perf/brag/      — Wins and milestones
reference/      — Tool docs and architecture
templates/      — Note templates
raw/            — Session logs (.jsonl)
.solomon/       — Commands, scripts, agents
```

## Quick Start

1. Run `/standup` to load context
2. Talk naturally — mention leads, wins, clients, ideas, problems
3. Say "wrap up" at end of session

## Key Principles

- **A note without links is a bug**
- **Folders group by purpose. Links group by meaning.**
- **Every win goes to the brag doc**
- **Every lead gets scored**
- **Memory compounds — session logs → brain/ notes → next session**

## Commands

| Command | Purpose |
|---------|---------|
| `/standup` | Morning kickoff |
| `/dump <text>` | Freeform capture |
| `/capture-lead <name> <source>` | Log a lead |
| `/capture-win <description>` | Log a win |
| `/new-client <name> <services>` | Onboard a client |
| `/service-status` | Check services |
| `/ideas-pipeline` | Ranked business ideas |
| `/weekly` | Weekly synthesis |
| `/wrap-up` | End-of-session review |

## Hooks

- **classify-message.py** — auto-detects leads, wins, clients, decisions, incidents, ideas
- **session-start.sh** — loads context at session start
- **pre-compact.sh** — logs session before context compaction

## Inspired By

- [obsidian-mind](https://github.com/breferrari/obsidian-mind) — the vault that made Claude remember everything
- [Karpathy's system](https://karpathy.ai/) — self-compiling knowledge base
