---
name: openphone-agent
description: Mobile agentic AI for phone automation — learns user patterns, executes tasks on-device, self-improves. Based on HKUDS OpenPhone + PhoneClaw iOS agent.
trigger: phone automation, iOS agent, mobile AI, autonomous phone tasks, self-improving AI
compatibility: Solomon Air (future mobile component)
metadata:
  author: josephv.zo.computer
  source: https://github.com/HKUDS/OpenPhone
  license: MIT
allowed-tools: Bash, Read, Write, Edit
---

# OpenPhone Agent Skill

## What It Is
OpenPhone = 3B-parameter vision-language model that runs entirely on-device (no cloud, no API costs).
PhoneClaw = iOS agent built on OpenPhone that acts as an autonomous AI butler.

## Key Components

### Ralph Loop
EXECUTE → EVALUATE → FIX → REPEAT
Breaks requests into subtasks, acts on phone, checks success, auto-retries with failure context.

### UserMemory
Persistent profile of user (name, city, habits, history) injected into every plan.

### ExperienceLog
App-specific navigation know-how (tap coords, failure patterns, timing) across sessions, auto-compacted into lean knowledge base.

### Memory-first answers
Repeated questions answered instantly from profile with zero device interactions.

### Learning mode
Operate phone normally while PhoneClaw watches — captures screenshots at ~8fps, detects taps via CV, distills actions into reusable navigation lessons.

## Solomon OS Use Cases
- **24/7 client communication** — AI handles calls and texts autonomously
- **Real estate** — AI answers client inquiries, schedules showings, follows up
- **Business answering service** — AI receptionist for small businesses

## Files
- `/home/workspace/solomon-openphone/` — full source
- `/home/workspace/solomon-openphone/PhoneClaw/README.md` — iOS agent docs
- `/home/workspace/solomon-openphone/Communication.md` — community links

## Status
FUTURE — requires mobile app build. Watch this space.