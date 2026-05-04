# RD Report: Hermes Agent Kanban — Multi-Agent v0.12.0

**Date:** 2026-05-03
**Source:** Teknium @ Nous Research, 1,521 likes, 94 reposts

## What It Is

Hermes Agent v0.12.0 ships multi-agent orchestration via a shared Kanban board. Multiple named Hermes profiles claim tasks from a board, work in parallel, hand off when blocked, with crash recovery and human oversight from one dashboard.

**Docs:** https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban-tutorial

**Key features:**
- Shared SQLite task board
- Parallel task execution across agents
- Structured handoffs when blocked
- Agent-to-agent comments
- Crash recovery and retries
- Human-in-the-loop supervision
- Web dashboard (Hermes Workspace)

**Video:** The launch video was planned and narrated by the Hermes Kanban system itself — the most honest demo possible.

## Architecture

```
Hermes Profile A ──┐
Hermes Profile B ──┼──▶ Shared Kanban Board ──▶ Parallel Execution
Hermes Profile C ──┘         │
                               ▼
                         Human Supervisor
                         (unblock, approve)
```

**Core file:** `swarm-kanban-store.ts`

## What This Means for JCPaid

**This IS the JCPaid Bus we were building.** Hermes just shipped it as a native feature. We don't need to build it ourselves.

**New strategy:**
1. Adopt Hermes Kanban as the JCPaid Bus backbone
2. Each client = one Hermes profile
3. Agents claim tasks from shared board
4. Clients see their board via Hermes Workspace dashboard
5. We manage all profiles from our dashboard

**Competitive position:** JCPaid clients get a managed Hermes Kanban experience — we handle setup, monitoring, and scaling. Raw Hermes costs $9.99-$19.99/mo + crypto.

## Priority for JCPaid

**FORGE IMMEDIATELY —** Integrate Hermes Kanban into JCPaid workflow:
1. Test Hermes Kanban locally (we have hermes-workspace at /home/workspace/hermes-workspace)
2. Define JCPaid client profiles as Hermes profiles
3. Build client-facing dashboard on top of Hermes Workspace
4. Add billing layer (per-agent, per-month)

## Competitive Alert

**HermesOS (April 30):** Cloud-hosted Hermes, $9.99-$19.99/mo, requires crypto
**Hermes Kanban (May 3):** Self-hosted multi-agent orchestration, SQLite-backed, MIT

These two releases back-to-back from the Hermes ecosystem. The community is moving fast.

## Recommendation

**FORGE** — Adopt Hermes Kanban as core orchestration layer. Ship JCPaid on top of it.