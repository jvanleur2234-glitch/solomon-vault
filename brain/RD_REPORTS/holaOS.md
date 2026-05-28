# RD Report: holaOS

**Date:** 2026-05-27
**Source:** https://x.com/i/status/2059732022579572908 + https://github.com/holaboss-ai/holaOS
**Tag:** 🟡 Worthwhile
**Recommendation:** SKILL — study their memory/workspace model, integrate ideas into JCPaid

---

## What It Is

holaOS is an open-source "agent computer" built on Electron + TypeScript (macOS-first, Linux/Windows in progress). It treats AI as a persistent desktop environment — not a chat window — where agents share the same browser, files, and tools as the user, and memory/rules/workflows persist across sessions.

**GitHub:** https://github.com/holaboss-ai/holaOS (MIT licensed)
**Docs:** https://www.holaos.ai/docs
**Stars:** ~5.5K (growing fast, posted May 22-27 2026)

---

## Core Architecture

### Workspace Model
Each "workstream" gets a persistent workspace on disk:
```
os-root/
├── state/runtime.db          # SQLite: sessions, turns, integrations, notifications
├── workspace/<workspace-id>/
│   ├── AGENTS.md             # Standing workspace policy (human-authored)
│   ├── workspace.yaml         # Agent config, skills, commands, MCP registry
│   ├── ONBOARD.md            # Onboarding instructions
│   ├── skills/               # Workspace-local skills (SKILL.md per skill)
│   ├── apps/                 # Workspace-local apps (app.runtime.yaml)
│   └── .holaboss/            # Runtime state (harness session, auth, checkpoints)
└── memory/                   # OS-global, not per-workspace
    ├── workspace/<workspace-id>/runtime/    # Resume-only continuity
    │   ├── latest-turn.md
    │   ├── session-state/
    │   ├── session-memory/   # Resume-friendly snapshots
    │   ├── recent-turns/
    │   └── blockers/
    ├── workspace/<workspace-id>/knowledge/  # Durable recall
    │   ├── facts/
    │   ├── procedures/
    │   └── reference/
    ├── preference/           # User preferences (durable)
    └── identity/             # User identity (durable)
```

### Three Memory Layers (key insight)
| Layer | Purpose | Durable? |
|-------|---------|----------|
| `runtime/` | Session continuity, resume snapshots | No — ephemeral |
| `knowledge/` | Facts, procedures, reference | YES — permanent |
| `runtime.db` | Execution truth, profile state | YES — permanent |

This is a deliberate split: **runtime continuity ≠ durable knowledge**. Sessions resume from snapshots; facts live in knowledge/. This prevents memory bloat and keeps "what I'm working on" separate from "what I know."

### Agent Harness
A stable boundary layer between the runtime and the LLM executor. The harness:
- Receives a compiled execution package per run (prompt + capability manifest + workspace checksum)
- Persists harness session state between runs
- Supports multiple executor backends (Pi agent configured in `.holaboss/pi-agent/`)

### Independent Runtime Deploy
holaOS is actively building a **portable runtime that runs without the desktop app** (see docs/contribute/runtime/independent-deploy). This is the key convergence point with Zo Computer — they recognize that the desktop UI is optional; the headless agent runtime is the real product.

---

## What We'd Use It For

### 1. Study Their Memory Model → Improve JCPaid here.now
Their `knowledge/procedures/` split is exactly what here.now needs. Currently here.now stores everything in a blob. We could adopt their pattern:
- `procedures/` = repeatable workflows (how to run a Facebook post, how to evaluate a pallet)
- `facts/` = client facts (name, preferences, past interactions)
- `reference/` = external data (platform pricing, market rates)

This makes here.now **queryable** rather than just a vector store.

### 2. Adopt workspace.yaml Pattern for JCPaid Client Onboarding
Every new JCPaid client could get a workspace scaffold:
```
/home/workspace/jcpaid/clients/<client-id>/
├── AGENTS.md        # Client-specific rules (FB account, posting style, do-not-post categories)
├── workspace.yaml   # Skills active for this client, alert thresholds, platform credentials
├── procedures/     # Client's standard workflows
└── memory/         # Client's here.now memory
```

This gives each client **isolation** and **continuity** — exactly what a scalable agency needs.

### 3. Independent Runtime → Deploy JCPaid Bus as a Headless Service
holaOS is building exactly the pattern Zo Computer already has: a cloud-hosted agent runtime. This validates the JCPaid Bus architecture. We could:
- Document that JCPaid Bus uses the same runtime separation concept
- Potentially fork holaOS's runtime for specialized agent orchestration

---

## How It Compares to What We Have

| | **holaOS** | **Zo + JCPaid** |
|---|---|---|
| Platform | Electron desktop app (local) | Cloud sandbox (remote) |
| Memory | `memory/` dir + SQLite | here.now (10GB/client) |
| Workspaces | Per-workstream on disk | Per-client in workspace |
| Agent harness | Pi agent, configurable | The Agency (147 agents) + custom |
| Continuity | Session snapshots + git checkpoints | Persistent conversation + here.now |
| Skills | Per-workspace SKILL.md | Hermes (1,223 skills) |
| Fleet/multi-client | Not mentioned | JCPaid Bus (fleet dispatch) |
| Deployment | Local-first, cloud runtime coming | Cloud-native already |
| License | MIT | Proprietary |

**Key takeaway:** holaOS is solving the LOCAL desktop problem. Zo + JCPaid is solving the CLOUD agency problem. The architectures are converging toward the same answer — but we're already cloud-native.

---

## Competitive Context

holaOS just posted publicly (May 22-27 2026) and is getting strong developer buzz. Their "independent runtime deploy" confirms that the market is moving toward persistent agent environments — which validates the entire JCPaid thesis.

However:
- They're LOCAL (desktop app), we're CLOUD (any device, 24/7)
- They have NO multi-agent fleet dispatch
- They have NO SaaS billing/payment layer
- They have NO Telegram/notification integration out of the box

JCPaid wins on: cloud access, fleet management, multi-client isolation, payment integration, and communication channels.

---

## Recommendation

**SKILL** — Study and integrate selectively.

1. **File:** Adopt their `knowledge/procedures/` and `knowledge/facts/` pattern into here.now
2. **File:** Create a JCPaid client workspace template modeled after their workspace model
3. **Monitor:** Watch their independent runtime deploy progress — if it goes well, potential integration or fork
4. **Pass on:** Running holaOS locally — it doesn't add anything we don't have, and it's desktop-only

**Bottom line:** This is a validation signal, not a threat. Another team just confirmed that persistent agent workspaces + memory separation + continuous execution is the right architecture. JCPaid is already ahead on cloud, fleet dispatch, and multi-client.
