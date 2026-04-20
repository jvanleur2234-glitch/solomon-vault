# Zo1 → Zo2 Coordination Test Spec

**Date:** 2026-04-20
**Status:** Draft — runnable when Zo2 is provisioned
**Goal:** Validate that two Zo instances can coordinate on shared tasks without stepping on each other.

---

## 1. What Is a Coordination Test?

A coordination test verifies that **two independent Zo instances can divide labor, delegate tasks, and share results reliably.**

In Solomon OS, Zo1 is the **orchestrator** (CEO, strategic). Zo2 is a **specialist** or **worker** (executes delegated sub-tasks). Coordination means:

- Zo1 assigns a task to Zo2 and gets a structured result back
- Zo2 operates with the same brain files (shared context)
- Neither instance loses state or produces conflicting output
- The handover between them is **trustworthy and auditable**

---

## 2. Test Scenarios

### Scenario 1: Task Delegation (Zo1 → Zo2)
**Test:** Zo1 POSTs a task to Zo2 via `/zo/ask` API.
**Zo2 task:** "Read `/home/workspace/solomon-vault/brain/Services.md` and summarize the agent roster in 3 bullet points."
**Success:** Zo2 responds with a valid summary. Zo1 logs the response. No errors.

### Scenario 2: File-Backed State Sync (Shared Brain)
**Test:** Zo1 writes a coordination payload to a shared file. Zo2 reads it, processes it, appends a result, and marks it done.
**File:** `/home/workspace/solomon-vault/raw/coordination_test_<timestamp>.json`
**Payload:** `{"task": "echo-test", "input": "hello from zo1", "status": "pending"}`
**Success:** Zo2 reads the file, writes back `{"status": "done", "output": "hello from zo1"}`. Zo1 reads the updated file and confirms.

### Scenario 3: Background Worker Fork (Zo1 spawns Zo2 sub-agent)
**Test:** Zo1 uses `/zo/ask` with a sub-task to run autonomously for up to 5 minutes, writing its output to a designated file.
**Sub-task:** "Run a health check on all services listed in `/home/workspace/solomon-vault/brain/Services.md`. Write results to `/home/workspace/solomon-vault/raw/health_check_<timestamp>.json`."
**Success:** Zo2 completes the health check, writes the file, and Zo1 reads and validates the output within 10 minutes.

### Scenario 4: Reverse Reporting (Zo2 → Zo1 on completion)
**Test:** Zo2 completes a delegated task and POSTs a completion message back to Zo1 via Telegram or a webhook-style file write.
**Mechanism:** Zo2 writes a `done` marker to `/home/workspace/solomon-vault/raw/coordination_test_<id>_done.json` with a `report` field.
**Success:** Zo1 detects the done marker on its next heartbeat loop and reads the report.

### Scenario 5: Idempotency & Conflict Detection
**Test:** Both Zo1 and Zo2 attempt to write to the same coordination file simultaneously (simulate race condition).
**File:** `/home/workspace/solomon-vault/raw/coordination_race_<timestamp>.json`
**Payload:** Each instance tries to write `{ "written_by": "zo1" }` and `{ "written_by": "zo2" }` at the same time.
**Success:** One write succeeds cleanly. The other either fails gracefully or the file contains a valid merged/locked state. No silent data corruption.

### Scenario 6: Full Round-Trip (Delegation → Execution → Report → Acknowledgment)
**Test:** Zo1 delegates a multi-step task to Zo2, Zo2 executes and reports, Zo1 acknowledges.
**Task:** "Look up the current Stripe revenue from the Stripe API and write a 1-paragraph financial summary to `/home/workspace/solomon-vault/raw/stripe_summary_<date>.txt`."
**Steps:**
1. Zo1 writes task to `/home/workspace/solomon-vault/raw/round_trip_<id>.json` with `status: pending`
2. Zo2 reads, executes (calls Stripe API or uses `stripe` CLI), writes summary, sets `status: done`
3. Zo1 reads on next heartbeat, confirms output is valid, sets `status: acknowledged`
**Success:** All 3 state transitions visible in the file. Final output is a coherent paragraph.

---

## 3. Technical Mechanism

### Communication Channels (in priority order)

| Mechanism | How it works | Best for |
|-----------|-------------|----------|
| **Zo API** (`/zo/ask`) | HTTP POST from Zo1 to Zo2's API endpoint | Direct task delegation, synchronous responses |
| **Shared Files** | Both instances read/write `/home/workspace/solomon-vault/raw/` | Async coordination, state files, reports |
| **GitHub Push/Pull** | Zo1 pushes brain files, Zo2 pulls on startup | Shared context / brain sync |
| **Telegram Bot** | Zo2 sends a message to Joseph's Telegram as a signal | Alerts, out-of-band notifications |
| **Solomon Bus** | Existing pub/sub daemon — add Zo2 as a subscriber | Event-driven triggers |

### The Shared Brain Location
Both Zo instances should share:
```
/home/workspace/solomon-vault/brain/   # Read-only context at session start
/home/workspace/solomon-vault/raw/      # Coordination files (read/write both)
```

### Authentication
- **Zo API:** Bearer token from `ZO_API_KEY` secret in [Settings → Advanced](/?t=settings&s=advanced)
- **GitHub:** Personal access token stored in secret `GITHUB_TOKEN`
- **Stripe:** Secret key stored in `STRIPE_SECRET_KEY`

### How Zo2 Receives Tasks (Today — No Second Instance Yet)
Until Zo2 is provisioned, simulate coordination by:
1. Writing a task to a **staging file** in `/home/workspace/solomon-vault/raw/coordination_test_staging.json`
2. Having the **Job Runner** or a **tmux background loop** pick up and execute the task
3. Writing results back to a `coordination_test_results.json`

---

## 4. Success Criteria

| Criterion | How to verify |
|-----------|--------------|
| Zo1 can POST a task to Zo2 and receive a response | API call returns 200, response body is valid JSON |
| Shared file coordination works | Both read/write produces correct state transitions |
| Brain sync is consistent | Brain files on Zo2 match Zo1 after pull |
| No data corruption in concurrent writes | Files are valid JSON after simultaneous writes |
| Round-trip completes end-to-end | Task file transitions: `pending` → `done` → `acknowledged` |
| Zo2 task result is actionable | Output is parseable, correct, and complete |
| Coordination is auditable | All state transitions logged with timestamps |

### Minimum Passing Bar
**All 6 scenarios must pass.** A scenario passes if:
- Expected file state is achieved
- No errors in Zo1 or Zo2 logs
- Output is parseable and matches expected schema

---

## 5. How to Run Today (Single-Zo Simulation)

Since Zo2 is not yet provisioned, run a **self-coordination test** where Zo1 acts as both:

```bash
# Step 1: Write task to staging
cat > /home/workspace/solomon-vault/raw/coordination_self_test.json << 'EOF'
{
  "id": "self-test-001",
  "task": "Read brain/Services.md and list all active agents",
  "status": "pending",
  "created_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
}
EOF

# Step 2: Execute as a background job
cd /home/workspace/solomon-vault && \
  node -e "
    const fs = require('fs');
    const brain = fs.readFileSync('brain/Services.md', 'utf8');
    const agents = brain.match(/^\| [^|]+ \| [^|]+ \| [^|]+ \| [^|]+ \|$/gm) || [];
    const result = { status: 'done', output: agents.join('\n'), completed_at: new Date().toISOString() };
    fs.writeFileSync('raw/coordination_self_test.json', JSON.stringify(result, null, 2));
    console.log('DONE:', JSON.stringify(result));
  "

# Step 3: Verify result
cat /home/workspace/solomon-vault/raw/coordination_self_test.json
```

---

## 6. GitHub Sync

After each coordination test run:
```bash
cd /home/workspace/solomon-vault
git add brain/COORDINATION_TEST.md
git add raw/coordination_*.json  # results
git commit -m "Coordination test run — $(date -u +%Y-%m-%d)"
git push
```

---

## 7. Open Questions

- [ ] Does Zo2 have its own `ZO_API_KEY` we can call?
- [ ] Is Zo2 accessible at a separate subdomain or same domain with different auth?
- [ ] Does Zo2 share the same `/home/workspace/solomon-vault/` filesystem, or is it a separate machine?
- [ ] Do we need a dedicated **coordinator** persona for Zo1 and a **worker** persona for Zo2?
- [ ] Should Solomon Bus be extended to support Zo2 as a subscriber?
