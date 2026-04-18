---
name: browser-recorder
description: Watch browser actions, record them as a reusable skill, replay on demand. The AI watches you use a website once, then can do it autonomously forever.
compatibility: Created for Zo Computer
metadata:
  author: josephv.zo.computer
---

# Browser Recorder Skill

Record once. Replay forever.

## Concept
- Watch a user navigate a website (via CDP browser events)
- Save each step as a structured skill file
- Replay the skill later with different parameters

## Workflow

### 1. Record a skill
```bash
agent-browser connect --cdp <port>
python3 /Skills/browser-recorder/scripts/record.py start --name pizza-ranch --port 9222
# User performs actions in connected browser
python3 /Skills/browser-recorder/scripts/record.py stop --name pizza-ranch
```

### 2. List recorded skills
```bash
ls /home/workspace/Skills/browser-recorder/skills/
```

### 3. Replay a skill
```bash
python3 /home/workspace/Skills/browser-recorder/scripts/replay.py pizza-ranch --params "size=large,topping=pepperoni"
```

### 4. Watch mode (auto-record)
```bash
python3 /home/workspace/Skills/browser-recorder/scripts/watch.py --name pizza-ranch --url https://order.pizzaranch.com
```

## Skill File Format
```json
{
  "name": "pizza-ranch",
  "trigger": "order pizza from pizza ranch",
  "base_url": "https://order.pizzaranch.com",
  "steps": [
    {
      "action": "click",
      "selector": "text=Large",
      "description": "Select large pizza size"
    },
    {
      "action": "type",
      "selector": "#address",
      "value": "{{address}}",
      "description": "Enter delivery address"
    }
  ],
  "parameters": ["address", "size", "topping"],
  "variables": {
    "address": "123 Main St, Des Moines, IA"
  }
}
```

## Parameters
Skills support `{{parameter}}` substitution:
- `{{size}}` — replaced at replay time
- `{{topping}}` — replaced at replay time
- `{{address}}` — from saved profile

## CDP Connection
agent-browser uses CDP port 9222 by default when started with `connect`:
```bash
agent-browser connect --port 9222
```
