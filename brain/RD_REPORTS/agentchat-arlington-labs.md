# RD Report: agentchat by arlington-labs

**URL:** https://github.com/arlington-labs/agentchat
**Repo size:** Small (~20 source files, TypeScript)
**License:** MIT
**Stars:** Not checked (likely small/new repo)
**Submitted:** April 10, 2026 via Telegram

---

## What It Is

AgentChat is a **protocol + skill** for AI-to-AI group messaging over [S2.dev](https://s2.dev) streams. Think of it as a peer-to-peer chat layer between AI agents:

- Create groups (S2 basins named `agentchat-{slug}`)
- Send typed messages routed to streams by type: `bug_report` → `bug-reports`, `prompt_report` → `prompt-reports`, `dx_feedback` → `dx-feedback`, generic `message` → `general`
- Invite other agents via base64url-encoded tokens containing scoped S2 access tokens
- Paginated message reads from any stream
- Config stored in `~/.agentchat/config.json`

The main artifact is `skills/agentchat/SKILL.md` — a complete protocol spec that any AI agent can follow to implement the system. Includes a TypeScript test harness and conformance tests.

**Tech stack:** Node.js >= 20, `@s2-dev/streamstore` SDK, TypeScript, Vitest.

---

## What We'd Use It For

Inter-agent communication inside Solomon OS. Currently Solomon Bus uses **file-based task queues + shell scripts** — functional but crude. AgentChat would give us:

1. **Structured peer messaging** between Zo, Russell Tuna, and Hermes
2. **Bug report / prompt discovery streams** — agents share what they find
3. **Scoped invite tokens** — safe out-of-band agent provisioning
4. **Paginated reads** — history without polling files

Not a replacement for Solomon Bus's task queue (which handles work assignment), but a **complementary communication layer** for non-task-based messages.

---

## How It Compares to What We Have

| Capability | Solomon Bus (current) | AgentChat (proposed) |
|---|---|---|
| Message types | Single queue (JSON tasks) | 4 typed streams + schema |
| Token-based auth | None (file-based) | Scoped S2 tokens with expiry |
| Peer-to-peer | No (all via Zo API) | Yes, direct agent-to-agent |
| Invites / ACL | None | Base64url invite tokens |
| Reads | Poll files | Paginated stream reads |
| Dependencies | Shell + Zo API | Node.js + S2 SDK |

AgentChat is architecturally superior for messaging, but adds S2.dev as a new external dependency.

---

## Caveats

- **S2.dev dependency** — requires an S2 account and access token. Not self-hosted. If S2 goes down or changes terms, the system breaks.
- **Node.js >= 20 required** — our current bot infra is Python-based. Would need a Node wrapper or re-implementation.
- **No obvious immediate pressure** — Solomon Bus works fine for current needs. Russell Tuna is a Telegram bot, not a mesh of communicating agents.
- **New repo, small community** — Arlington Labs is not a huge established player. Could evolve breakingly.

---

## Recommendation: SKIP

The protocol is well-designed and the skill spec is clean. For a future where Solomon OS has multiple autonomous agents that need to share discoveries and status updates peer-to-peer, AgentChat is a solid choice.

**However**, we don't have that architecture yet. Right now it's Zo + Russell Tuna + Hermes, and the communication needs are covered by:
- Zo API for task delegation
- Telegram for human-facing updates
- File-based queues for task distribution

Adding S2.dev integration now would be premature complexity. If we ever get to a true multi-agent mesh (Russell Tuna spawning sub-agents that report back, Hermes workers coordinating), it's worth revisiting.

**Stored:** `/home/workspace/solomon-vault/brain/RD_REPORTS/agentchat-arlington-labs.md`