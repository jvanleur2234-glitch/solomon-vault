# Zo1→Zo2 Coordination Test Spec

*Date:* 2026-04-20
*Purpose:* Test communication between two Zo instances on josephv.zo.computer

---

## What Is a Coordination Test?

A coordination test verifies that two independent AI agents can:
1. **Delegate** tasks to each other without conflict
2. **Report back** results reliably
3. **Avoid duplication** of work
4. **Maintain context** across the handoff
5. **Escalate** when one instance needs help

---

## Test Scenarios

### Scenario 1: Task Delegation
- **Zo1** receives a complex task (e.g., "Build a CMA report for 123 Main St")
- Zo1 breaks it into subtasks and delegates the research step to Zo2
- Zo2 completes research and reports back with structured data
- Zo1 assembles the final CMA report

**Mechanism:** Zo1 calls Zo2 via `/zo/ask` API with the subtask prompt

### Scenario 2: Parallel Processing
- Zo1 splits a bulk task (e.g., "SEO audit 10 real estate agent websites")
- Zo2 handles 5 of them in parallel while Zo1 handles the other 5
- Both write results to shared file storage
- Zo1 merges final report

**Mechanism:** Shared `/home/workspace/jack-connect/jobs.json` as coordination point

### Scenario 3: Health Check Monitoring
- Zo1 monitors Zo2's health via status endpoint
- If Zo2 goes down, Zo1 alerts and routes tasks to alternative
- Zo2 does the same for Zo1

**Mechanism:** Periodic curl to `localhost:3101/health` on each instance

### Scenario 4: Context Wire
- Zo1 starts a conversation with a client
- Client switches to Telegram (Zo2/Russell Tuna)
- Zo2 has full context of what Zo1 discussed
- Zo2 continues seamlessly

**Mechanism:** Shared brain files in `/home/workspace/solomon-vault/brain/`

### Scenario 5: Solomon Bus Relay
- A task comes into Solomon Bus
- Zo1 and Zo2 both see it but only one picks it up (SKIP LOCKED)
- Completed work is marked with the agent ID that did it

**Mechanism:** Postgres SKIP LOCKED via Solomon Bus daemon

---

## Technical Mechanism

### Option A: Zo API (Recommended)
```
Zo1                           Zo2
  │                             │
  └─ POST /zo/ask ─────────────►│ (delegation)
  │                             │
  │◄── JSON response ───────────┘ (result reporting)
```

- Use `conversation_id` to maintain context across agents
- Zo1 passes shared context files as part of the prompt
- Zo2 writes results to shared location

### Option B: Shared Files
- Both agents read/write to `/home/workspace/solomon-vault/brain/COORDINATION/`
- Task queue: `task_queue.json` (same file both can access)
- Results written to `brain/COORDINATION/results/`

### Option C: Solomon Bus
- Solomon Bus already handles inter-agent communication
- Add a `zo_instances` channel
- Both Zo1 and Zo2 publish/subscribe to it

---

## Success Criteria

| Test | Pass Condition |
|------|---------------|
| Delegation | Task delegated, result returned, no data loss |
| Parallel | Both agents work simultaneously, results merged |
| Health Check | Down agent detected within 60s, tasks rerouted |
| Context Wire | Client sees seamless handoff, no repeated questions |
| Solomon Bus | Only one agent picks up each task |

---

## How to Run

1. **Health test:** Zo1 pings Zo2 every 60s, logs result
2. **Delegation test:** Zo1 delegates one CMA task to Zo2, verify output
3. **Parallel test:** Submit 10 jobs, verify both agents work and results merge

---

*Status: SPEC COMPLETE — ready to run*