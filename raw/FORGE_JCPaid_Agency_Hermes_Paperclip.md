# FORGE: JCPaid × The Agency × Hermes × Paperclip Integration

**Status:** FORGE — In Progress  
**Date:** 2026-04-30  
**Goal:** Unified multi-agent business management stack

---

## What The Agency Is

- **88K GitHub stars**, 147 AI agents, 12 departments
- Multi-agent development framework for Claude Code
- NOT self-contained — runs inside Claude Code as the agent harness
- Key pattern: **ISCP** (Inter-Session Collaboration Protocol) via SQLite
- Key pattern: **Quality Gates** via parallel reviewer agents
- Key pattern: **Session lifecycle** (pause/resume across conversations)

**What The Agency IS NOT:**
- Not a standalone AI runtime
- Not a business management platform
- Not hosted — requires Claude Code CLI
- Not multi-tenant (one repo = one team)

---

## What The Agency Does Well

1. **Multi-agent orchestration** — captain, tech-lead, reviewers working together
2. **Cross-session memory** — SQLite-based dispatch/flag system
3. **Quality enforcement** — hash-chained QGR receipts, parallel reviewers
4. **Workstream isolation** — organized areas of work with artifacts
5. **Convention over config** — agency init, agency update pattern

---

## How This Fits JCPaid

### Pattern 1: Multi-Agent Classes
The Agency's agent class pattern (captain, reviewer, designer) = Hermes skills + personas
- Hermes already has 80+ skills
- We need: Sales Agent, Marketing Agent, Support Agent, Finance Agent

### Pattern 2: ISCP (Inter-Session Collaboration)
SQLite dispatch/flag system = Hermes Bus + Memory Bridge
- Build `jcpaid-bus` as Hermes skill using ISCP pattern
- SQLite tables for dispatch queue, flags, QGR receipts

### Pattern 3: Quality Gates
Parallel reviewer agents = Hermes deliberation layer
- Add reviewer skills: content-reviewer, code-reviewer, strategy-reviewer
- Hash-chained receipts for client deliverables

### Pattern 4: Session Lifecycle
Pause/resume = Hermes session persistence
- Hermes already has session persistence
- Build `session-pause` / `session-pickup` as Hermes Bus commands

---

## What To Build (FORGE Tasks)

### Task 1: Hermes Bus (jcpaid-bus)
```
/home/workspace/jcpaid-bus/
├── bus.py              # Main bus service
├── db.py               # SQLite ISCP-style dispatch queue
├── skills/
│   ├── pause.py        # Session pause
│   ├── resume.py       # Session resume
│   ├── dispatch.py     # Dispatch task to agent
│   └── flag.py         # Set/clear flags
└── README.md
```
**Status:** TODO  
**Priority:** HIGH

### Task 2: Agent Personas for JCPaid
```
/home/workspace/jcpaid/personas/
├── sales-agent/        # Sales AI employee
├── marketing-agent/     # Marketing AI employee  
├── support-agent/      # Support AI employee
├── finance-agent/      # Finance AI employee
└── common/             # Shared tools, memory
```
**Status:** TODO  
**Priority:** HIGH

### Task 3: Hermes Workspace Branding
- White-label Hermes Workspace for JCPaid clients
- Custom logo, colors, client dashboard
- URL: client.jcpaid.ai → points to their Hermes Workspace

### Task 4: Quality Gate Receipts
- JSON receipts for completed tasks
- Hash-chained for tamper evidence
- Shows: what was done, time spent, result
- Client sees in dashboard

---

## Stack Integration Map

```
JCPaid Client
    ↓ (signs up, gets dashboard)
JCPaid Dashboard (web UI) ← Hermes Workspace (white-labeled)
    ↓
Paperclip (company = client account)
    ↓ (tasks, org chart, budgets)
hermes-paperclip-adapter
    ↓ (delegates work)
Hermes Agent (AI employee doing the actual work)
    ↓ (uses tools, writes memory)
Memory Bridge (persistent memory)
    ↓ (session continuity)
Hermes Bus (dispatch, queue, flags)
```

---

## What NOT To Do

❌ Don't try to replace Paperclip with The Agency  
❌ Don't run The Agency as a standalone service (requires Claude Code)  
❌ Don't clone 147 agents wholesale (start with 4-5 key ones)  
✅ DO adopt ISCP pattern for Hermes Bus  
✅ DO add quality gate reviewers as Hermes skills  
✅ DO white-label Hermes Workspace for client dashboards  

---

## Reference Links

- The Agency: https://github.com/the-agency-ai/the-agency
- Paperclip: https://github.com/paperclipai/paperclip
- Hermes: https://github.com/NousResearch/hermes-agent
- Hermes Workspace: https://github.com/NousResearch/hermes-workspace
- hermes-paperclip-adapter: https://github.com/NousResearch/hermes-paperclip-adapter