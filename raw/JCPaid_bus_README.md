# JCPaid Bus — Hermes Inter-Agent Dispatch

**Purpose:** SQLite-based task queue + flag system for Hermes multi-agent coordination  
**Pattern:** Inspired by The Agency ISCP (Inter-Session Collaboration Protocol)  
**License:** MIT

## What It Does

- **Dispatch queue:** Tasks get assigned to agents, tracked to completion
- **Flags:** Inter-agent signals (pause, resume, escalate, approve)
- **QGR receipts:** Hash-chained quality gate receipts for client deliverables
- **Session persistence:** Pause/resume across conversations

## Quick Start

```bash
python bus.py dispatch --agent sales --task "Follow up with lead #123"
python bus.py flag set paused sales-agent
python bus.py receipt create --task-id abc123 --result "Closed $5K deal"
python bus.py queue list --agent sales
```

## Database

SQLite at `./jcpaid-bus.db` with tables:
- `dispatch_queue` — task assignments
- `flags` — inter-agent signals  
- `receipts` — QGR hash-chained delivery receipts
- `sessions` — pause/resume state

## Hermes Skill

Install as Hermes skill: copy `skills/` to your Hermes skills directory.
