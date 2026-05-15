# FORGE: /goal Autonomous Loop → JCPaid Stack
**Status:** FORGE COMPLETE  
**Date:** 2026-05-14  
**Stack:** JCPaid Bus + The Agency (147 agents) + Hermes (1,223 skills) + /goal autonomous loop

---

## What We Forged

### 1. /goal Skill (`jcpaid-bus/skills/goal_skill.py`)

The `/goal` command from Claude Code / Codex / Hermes, adapted for JCPaid:

**Pattern:**
```
/goal [do the work] until [measurable end state] without [constraints]
```

**What it does:**
- Parses goal text into: task, end_state, constraints
- Logs each step in SQLite with validation
- Internal fast-model validation loop (no human approval per step)
- Hash-chained receipts for deliverables
- Pause / resume / clear lifecycle

**Real JCPaid /goal examples:**
```
/goal research EZ Heating & Cooling and write a $299/mo SEO pitch until draft is complete without leaving the research folder
/goal find 10 HVAC contractors in Sioux Falls and write cold emails until all 10 emails are drafted without contacting them  
/goal audit my Gmail for leads and create a follow-up sequence until 5 follow-ups are queued without modifying any sent emails
/goal build a landing page for my AI agency until it's live on here.now without modifying any existing routes
```

---

### 2. JCPaid Bus Integration

The `/goal` skill writes to the same SQLite DB as JCPaid Bus:

| Table | Purpose |
|---|---|
| `goals` | /goal execution state |
| `goal_steps` | Step-by-step validation log |
| `dispatch_queue` | Tasks dispatched to agents |
| `receipts` | Hash-chained delivery receipts |
| `flags` | Inter-agent signals (pause, resume, escalate) |

**Flow:**
```
Human: "/goal find 10 HVAC clients and write cold emails"
  → goal_skill.py: parses goal, creates goal_id
  → JCPaid Bus: dispatches subtasks to Sales Agent via dispatch_queue
  → Sales Agent: works autonomously, each step logged in goal_steps
  → Internal validation loop: fast model checks if step brings goal closer
  → Receipt created on completion: hash-chained into receipts table
  → Human notified: "✅ Goal complete — 10 cold emails drafted"
```

---

### 3. The Agency Integration (ISCP Pattern)

The Agency's **ISCP** (Inter-Session Collaboration Protocol) pattern — adapted for Hermes:

**The Agency ISCP → JCPaid equivalents:**

| The Agency Concept | JCPaid Implementation |
|---|---|
| ISCP SQLite dispatch | JCPaid Bus `dispatch_queue` table |
| Quality Gate Reviewers (QGR) | `goal_steps` validation + `receipts` hash-chain |
| Pause / Resume | `sessions` table + `pause()` / `resume()` |
| Captain → Reviewers flow | Innovator → Closer → Support flow |
| 147 agent classes | 4 JCPaid personas + Hermes skills |

**JCPaid Agent Flow (The Agency pattern):**
```
Innovator (Captain)
  → breaks down goal into tasks
  → dispatches to Closer (Sales Agent)
  → dispatches to Support (Research Agent)  
  → Quality Gate: receipts hash-chain validates output
  → Client receives QGR receipt
```

---

### 4. Hermes Skill Installation

**Location:** `/home/workspace/jcpaid-bus/skills/goal_skill.py`

To install as a Hermes skill, copy to Hermes skills directory:
```bash
cp /home/workspace/jcpaid-bus/skills/goal_skill.py $HERMES_SKILLS_DIR/
```

**Commands available:**
```bash
python goal_skill.py start --text "/goal find 10 HVAC clients..."
python goal_skill.py plan --text "/goal research Jon's business..."
python goal_skill.py step --goal-id abc123 --action "Researched competitor pricing"
python goal_skill.py complete --goal-id abc123 --result "10 cold emails drafted"
python goal_skill.py pause --goal-id abc123
python goal_skill.py resume --goal-id abc123
python goal_skill.py list
python goal_skill.py active
```

---

## /goal vs. Normal Prompt — Comparison

| | Normal Prompt | /goal Autonomous |
|---|---|---|
| **Task completion** | Multiple back-and-forth | Single prompt, done |
| **Human bottleneck** | Every step needs approval | Only start/end |
| **Autonomy** | Narrow | Full autonomous loop |
| **Speed** | Slow (human delays) | Fast (AI runs continuously) |
| **Validation** | Human validates each step | Fast model validates internally |
| **Use case** | Complex, multi-step with human oversight | Repetitive, high-volume tasks |

---

## JCPaid /goal Use Cases by Persona

### Innovator (Captain)
```
/goal research the HVAC industry in Sioux Falls until I have a complete competitive analysis without leaving the research folder
```

### Closer (Sales Agent)
```
/goal find 20 local service businesses in Sioux Falls and write personalized cold emails until all 20 emails are drafted without contacting anyone
/goal follow up with all warm leads in my Gmail until 5 follow-up emails are sent without modifying any sent emails
```

### Support (Research Agent)
```
/goal audit EZ Heating & Cooling's online presence until I have a complete SEO audit with specific recommendations without modifying any external systems
```

### Admin (Operations)
```
/goal create invoices for all outstanding JCPaid clients until all invoices are drafted without sending them automatically
/goal reconcile my Stripe transactions until all income is categorized in a CSV without modifying any source data
```

---

## Files Created

```
/home/workspace/jcpaid-bus/
├── bus.py              # JCPaid Bus core (dispatch + flags + receipts + sessions)
├── db.py               # SQLite initialization
├── jcpaid-bus.db       # SQLite database (created on first run)
├── skills/
│   └── goal_skill.py   # /goal autonomous loop skill [NEW]
└── README.md
```

---

## Next Steps

1. **Install Printify API key** → developers.printify.com → API token → Zo secrets
2. **Test /goal with real JCPaid task** — when Hermes is stable: `/goal research EZ Heating & Cooling and write me a $299/mo SEO pitch`
3. **Wire Russell Tuna** to read Solomon Vault brain/Services.md and brain/Business Ideas.md at session start
4. **First client outreach** — Jon at EZ Heating & Cooling (605-940-0650), $299/mo SEO + leads

---

*FORGE complete. /goal is now part of the JCPaid stack.*