# Arena Commands for Russell Tuna

## Overview
Russell Tuna votes on Arena.ai battles and logs results to build Solomon OS's model routing intelligence.

## Vote Logging

**Log file:** `/home/workspace/arena-responses/battle_log.jsonl`

**Format (one JSON object per line):**
```json
{"task":"coding","model_a":"gpt-5.4","model_b":"gemini-3-pro","winner":"gemini-3-pro","prompt":"Write a Python quicksort","timestamp":"2026-04-05T14:30:00Z"}
```

**Fields:**
- `task` — category: coding, creative, math, reasoning, general, long-context, speed
- `model_a` — first model name (as shown on Arena)
- `model_b` — second model name
- `winner` — which model won: `model_a`, `model_b`, or `tie`
- `prompt` — the exact prompt used (truncate to 500 chars if long)
- `timestamp` — ISO 8601 UTC

**Example log entry:**
```json
{"task":"creative","model_a":"claude-4-sonnet","model_b":"gpt-5.4","winner":"claude-4-sonnet","prompt":"Write a haiku about a robot learning to garden","timestamp":"2026-04-05T15:45:00Z"}
```

## Query Ranking Engine (Port 8090)

Russell can ask which model is best for a task:

**Command:** `arena best [task]`

**Example (Russell says in Telegram):**
```
arena best coding
```

**What Russell does:**
```bash
curl -s -X POST http://localhost:8090/query \
  -H "Content-Type: application/json" \
  -d '{"task":"coding","available_models":["gpt-5.4","gemini-3-pro","claude-4-sonnet"]}'
```

**Response:**
```json
{"task":"coding","best_model":"gemini-3-pro","confidence":0.73,"sample_size":142}
```

## Russell Tuna Telegram Commands

| Russell says | What happens |
|---|---|
| `arena vote` | Russell opens arena.ai/text/side-by-side, runs a battle, logs the result |
| `arena best coding` | Query ranking engine for best coding model |
| `arena best creative` | Query ranking engine for best creative model |
| `arena status` | Show total votes logged and sample sizes |
| `arena log [task] [model_a] [model_b] [winner]` | Manually log a vote |

## Workflow for Voting

1. Open https://arena.ai/text/side-by-side
2. Pick two models from dropdowns
3. Enter a real prompt (coding, creative, etc.)
4. Read both responses carefully
5. Vote for the better one
6. Log the result to `battle_log.jsonl`

## Directory Structure
```
/home/workspace/arena-responses/
├── battle_log.jsonl        ← all votes go here
└── prompts/
    ├── coding/
    ├── creative/
    ├── math/
    └── general/
```

## Tips
- Log EVERY vote, even close ones
- Use real, varied prompts — not templated
- If Arena shows a captcha, skip that vote and try again later
- For tie votes, use `"winner":"tie"`
