# Paperclip + Solomon OS Integration Spec
**Status:** Draft — Created 2026-04-22
**Purpose:** Connect Paperclip agent swarm to Solomon OS cloud brain

---

## OVERVIEW

Paperclip runs locally on Jack's T15 (16GB RAM, Windows 11 + WSL2).
Solomon OS cloud brain (Zo Computer) runs in the cloud.

Together they form: **Local execution + Cloud intelligence + Telegram CEO interface**

```
┌─────────────────────────────────────────────────────────────┐
│                    JACK'S T15 (LOCAL)                       │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────────┐  │
│  │  Paperclip  │  │ Hermes Agent │  │  Watch Once (MSS) │  │
│  │  Swarm Hub  │  │  (executor)  │  │  Screen Capture   │  │
│  └──────┬──────┘  └──────┬───────┘  └───────────────────┘  │
│         │                │                                  │
│         └────────────────┼──────────────────────────────────┤
│                          │  Execution happens HERE          │
└──────────────────────────┼──────────────────────────────────┘
                           │ API calls (WSL2 → cloud)
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                   ZO COMPUTER (CLOUD)                         │
│  ┌──────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Russell     │  │ JackConnect │  │  Solomon Vault      │  │
│  │  Tuna (CEO)  │  │  Dashboard │  │  Brain files        │  │
│  │  Telegram    │  │  Time Saved │  │  Audit logs         │  │
│  └──────┬───────┘  └──────┬──────┘  └─────────────────────┘  │
│         │                │                                    │
│         ▼                ▼                                    │
│  ┌──────────────────────────────────────────────────────┐    │
│  │  Paperclip Connector API (/api/paperclip-connect)     │    │
│  │  - Receives task results                              │    │
│  │  - Stores audit logs                                  │    │
│  │  - Syncs agent activity to dashboard                  │    │
│  │  - Triggers Russell Tuna on completion               │    │
│  └──────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘
```

---

## CONNECTION METHODS

### Method 1: Paperclip Cloud Sync (Recommended)
Paperclip has a cloud sync feature — connect to a remote endpoint.

**On T15 (Paperclip):**
1. Settings → Cloud Sync → Enable
2. Endpoint: `https://josephv.zo.computer/api/paperclip-connect`
3. API Key: stored in Zo Computer secrets as `PAPERCLIP_API_KEY`

**What flows:**
- Task completions → audit log stored in Solomon Vault
- Agent activity → synced to JackConnect Dashboard
- Time saved data → updated in real-time

### Method 2: Manual Webhook (Fallback)
Paperclip can POST to a webhook on task completion.

**On T15 (Paperclip):**
1. Settings → Webhooks → Add
2. URL: `https://josephv.zo.computer/api/paperclip-connect`
3. Events: task_complete, agent_spawn, agent_die

**Payload:**
```json
{
  "event": "task_complete",
  "timestamp": "2026-04-22T12:00:00Z",
  "task_id": "abc123",
  "task_name": "Research competitor pricing",
  "agents_used": ["researcher-1", "researcher-2", "synthesizer-1"],
  "duration_seconds": 45,
  "time_saved_minutes": 120,
  "result_summary": "Found 15 competitors, generated comparison table"
}
```

### Method 3: File-Based Sync (Simplest for now)
Paperclip exports JSON logs. Solomon OS reads them.

**On T15:**
- Paperclip log dir: `~/.paperclip/logs/`
- Export format: `paperclip_YYYY-MM-DD.json`

**On Zo Computer:**
- Cron job pulls logs every 5 minutes via SFTP
- Or: T15 pushes via `rsync -e ssh` to Zo Computer

---

## PAPERCLIP AGENT ARCHITECTURE FOR SOLOMON OS

### Default Agent Roles (Paperclip)

| Agent | Role | Model | RAM each |
|-------|------|-------|----------|
| ceo-paperclip | Task delegation + prioritization | qwen3:14b | 200MB |
| researcher-1 | Web research + data collection | qwen3:1.7b x5 | 500MB |
| researcher-2 | Competitor analysis | qwen3:1.7b x5 | 500MB |
| analyst-1 | Data synthesis + report generation | qwen3:14b | 200MB |
| coder-1 | Code generation + debugging | qwen3:14b | 200MB |
| writer-1 | Content creation + email drafting | qwen3:1.7b | 100MB |
| reviewer-1 | QA + fact-checking | qwen3:1.7b | 100MB |
| coordinator-1 | Task scheduling + dependency management | qwen3:1.7b | 100MB |

**Total simultaneous agents: 10-15 on T15 Solo tier**
**With Kimik-style parallel spawning: 50-100 possible**

### Solomon OS Layer on Top

```
You (Telegram) → Russell Tuna → Paperclip (on T15)
                                    ↓
                              Results sync to
                                    ↓
                              Zo Computer Dashboard
```

**Russell Tuna commands for Paperclip:**
- "Run a research swarm on [topic]" → spawns researcher agents
- "Build me a report on [topic]" → orchestrates full pipeline
- "How many agents are running?" → queries Paperclip status
- "Stop all agents" → emergency kill switch

---

## SPECIFIC PAPERCLIP SETUP STEPS (for Jack's T15)

### Step 1: Install Paperclip on T15 (Windows 11)
```bash
# In WSL2 (Ubuntu)
curl -fsSL https://paperclip.ai/install.sh | bash

# OR download from https://paperclip.ai for Windows
```

### Step 2: Configure Cloud Sync
```bash
# In Paperclip settings:
# Cloud Sync → Enable
# Endpoint: https://josephv.zo.computer/api/paperclip-connect
# API Key: (generate from Zo Computer Settings > Advanced)
```

### Step 3: Set Up Agent Team
In Paperclip UI:
1. Create "Solomon OS Swarm" team
2. Add agents with predefined roles (see table above)
3. Set default model: qwen3:14b (shared across agents)
4. Enable parallel execution

### Step 4: Connect to Telegram (via Russell Tuna)
In Solomon OS:
1. Russell Tuna reads brain/Services.md on startup
2. Services.md includes Paperclip endpoint + API key
3. Russell Tuna can POST tasks to Paperclip via `/api/paperclip-task`

### Step 5: Sync Dashboard
Automatically handled via cloud sync or webhook.

---

## API ENDPOINTS TO BUILD

### 1. `/api/paperclip-connect` (POST)
Receives task results from Paperclip cloud sync.

**Request:**
```json
{
  "api_key": "PAPERCLIP_API_KEY",
  "event": "task_complete",
  "data": { ... task payload ... }
}
```

**Response:**
```json
{
  "status": "logged",
  "audit_id": "audit_20260422_001",
  "dashboard_updated": true
}
```

### 2. `/api/paperclip-task` (POST)
Russell Tuna sends a task TO Paperclip.

**Request:**
```json
{
  "task": "Research competitor pricing for real estate agencies in Chicago",
  "swarm_config": {
    "agents": 10,
    "parallel": true,
    "timeout_minutes": 5
  }
}
```

**Response:**
```json
{
  "task_id": "paperclip_task_001",
  "status": "dispatched",
  "estimated_completion": "2026-04-22T12:05:00Z"
}
```

### 3. `/api/paperclip-status` (GET)
Check Paperclip swarm status from T15.

**Response:**
```json
{
  "online": true,
  "agents_active": 8,
  "tasks_completed_today": 23,
  "time_saved_minutes_today": 340
}
```

---

## KIMIK INTEGRATION PATH

Kimik (kimi-2.6 Swarm Workstation) runs ON TOP of Paperclip as the parallel execution layer.

```
Kimik (300 agents) → Paperclip (orchestration) → Hermes (execution) → Zo Computer (brain)
```

**Why this matters:**
- Kimik handles the "300 agents in parallel" parallelism
- Paperclip handles the "agent org chart + roles + ticketing"
- Hermes handles the "actual tool use + memory"
- Zo Computer handles the "cloud brain + dashboard + Telegram"

**Install order:**
1. Paperclip (今夜) — orchestration
2. Kimik (Week 2) — parallelism layer
3. Hermes (Week 3) — execution + tools
4. Zo Computer (Week 4) — cloud brain

---

## FILES TO CREATE

| File | Purpose | Location |
|------|---------|----------|
| paperclip-connect-api.md | API endpoint specs | solomon-vault/brain/ |
| paperclip-swarm-config.md | Recommended agent configs | solomon-vault/brain/ |
| jack-t15-setup.md | Step-by-step T15 install guide | solomon-vault/brain/ |
| PAPERCLIP_AGENTS.md | Agent roster + roles | zo-excellence-package/ |

---

## NEXT STEPS

- [ ] Joseph approves this spec
- [ ] Build `/api/paperclip-connect` endpoint in Zo Space
- [ ] Build `/api/paperclip-task` endpoint in Zo Space
- [ ] Write T15 setup guide
- [ ] Install Paperclip on Jack's T15
- [ ] Test first swarm task via Telegram → Russell → Paperclip
- [ ] Verify dashboard updates

---

*Spec by Zo (Joseph's AI) | 2026-04-22*