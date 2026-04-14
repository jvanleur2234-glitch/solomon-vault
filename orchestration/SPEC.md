# Solomon OS — Paste-to-Agent Orchestration Layer

**Status:** Implementation Started  
**Date:** 2026-04-11  
**Token:** `solomon123` | **PinchTab Port:** 9888

---

## Vision

Build an **OpenClaw Convo Messenger**-style workflow for Solomon OS:
1. User pastes any app URL (or zo.pub link) into Telegram
2. Zo receives it, reads/analyzes the URL
3. Zo determines: Hermes skill? Russell Tuna task? Browser action via PinchTab?
4. Executes the action
5. Results sent back via Telegram

---

## Architecture

```
User sends URL in Telegram
       ↓
Zo (orchestrator) receives via Telegram DM
       ↓
Zo reads/analyzes URL (read_webpage or PinchTab)
       ↓
Decision engine:
  ├── "analyze" → Summarize + propose actions (no browser)
  ├── "do task" → Spawn Hermes agent or Russell Tuna worker
  └── "act on app" → Use PinchTab browser automation
       ↓
PinchTab: instance start → navigate → snapshot → action → results
       ↓
Response sent back to user via Telegram
```

---

## Components

### 1. Telegram Bot Handler (`/agent [url]`)
- Receives URLs via Telegram
- Authenticates user (Joseph only)
- Routes to appropriate handler
- Sends results back via Telegram

### 2. Orchestration Router
- Reads URL, determines action type
- `browser` — PinchTab automation
- `agent` — Hermes or Russell Tuna sub-agent
- `analyze` — Read + summarize without browser

### 3. PinchTab Integration (port 9888, token: solomon123)
- **Start instance:** `POST /instances/start` → returns `port` (e.g. 9870)
- **Navigate:** `POST :port/navigate` with `{url}`
- **Snapshot:** `GET :port/snapshot?filter=interactive`
- **Act:** `POST :port/action` with `{kind, ref, value?}`
- **Stop:** `POST /instances/:id/stop`

### 4. Context Injection
- Russell Tuna receives full Solomon OS context via Zo API
- Hermes gets task + skills registry

### 5. Approval Flow
- AI proposes action → user approves → execute
- Quick win: analyze first, act only on approval

---

## Telegram Commands

| Command | Action |
|---------|--------|
| `/agent [url]` | Analyze URL, propose actions |
| `/agent [url] --do` | Analyze + execute immediately |
| `/agent [url] --task [description]` | Analyze + delegate to Hermes/Russell |
| `/tabs` | List active PinchTab instances |
| `/kill [instance_id]` | Stop a PinchTab instance |

---

## API Endpoints (PinchTab)

Base: `http://localhost:9888`  
Auth: `Authorization: Bearer solomon123`

```
POST /instances/start
  Body: {"mode": "headless"|"attached"|"dashboard"}
  Response: {"id", "port", "status"}

POST /:port/navigate
  Body: {"url": "https://..."}
  Response: {"tabId", "title", "url"}

GET /:port/snapshot?filter=interactive
  Response: {"nodes": [{"ref", "role", "name", ...}]}

POST /:port/action
  Body: {"kind": "click"|"type"|"fill"|"press"|"scroll", "ref": "e1", "value": "..."}
  Response: {"success", "result": {...}}

POST /instances/:id/stop
  Response: {"status": "stopped"}
```

---

## File Structure

```
/home/workspace/solomon-vault/
├── orchestration/
│   ├── SPEC.md                          # This file
│   ├── telegram_handler.py               # Telegram bot (main entry)
│   ├── pinchtab_client.py                # PinchTab HTTP client
│   ├── router.py                         # Decision engine
│   ├── agents/
│   │   ├── hermes_executor.py            # Hermes agent spawner
│   │   └── russell_executor.py           # Russell Tuna via Zo API
│   └── tasks/
│       └── task_queue.py                 # Solomon Bus task queue
```

---

## Implementation Steps

- [x] 1. SPEC.md written
- [ ] 2. PinchTab client (`pinchtab_client.py`)
- [ ] 3. Telegram bot handler (`telegram_handler.py`)
- [ ] 4. Orchestration router (`router.py`)
- [ [ ] 5. Hermes executor
- [ ] 6. Russell executor
- [ ] 7. Task queue
- [ ] 8. Integration test with live Telegram DM

---

## Security Notes

- Telegram bot token from `TELEGRAM_BOT_TOKEN` env var
- PinchTab auth token: `solomon123`
- Only Joseph's Telegram ID accepts commands
- Approval flow for destructive/write actions
