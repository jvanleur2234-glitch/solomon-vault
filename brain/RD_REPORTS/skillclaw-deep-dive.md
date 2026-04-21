# SkillClaw Deep Dive — AMAP-ML Cross-Agent Skill Evolution

*Date:* 2026-04-21
*Source:* https://github.com/AMAP-ML/SkillClaw + agent_evolve_server README
*Stars:* 4,200+
*License:* MIT

---

## What It Is

SkillClaw is a system for **collective, agentic evolution of AI skills** across sessions, agents, devices, and users. Skills improve automatically through ordinary interactions — no manual updates, no version management, no siloed learning.

The core innovation: skills learned by ONE agent on ONE device become available to ALL agents on ALL devices instantly. This is the missing piece in Solomon OS — we have skills that live in Hermes, but they're static. SkillClaw makes them evolve.

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│              SkillClaw Network                      │
│                                                      │
│  Agent A        Agent B        Agent C               │
│  (Hermes)       (OpenClaw)     (PicoClaw)           │
│     │               │               │                │
│     ▼               ▼               ▼                │
│  ┌─────────────────────────────────────────────┐    │
│  │          agent_evolve_server                 │    │
│  │                                             │    │
│  │  1. Drain sessions from all agents          │    │
│  │  2. Summarize sessions + metadata           │    │
│  │  3. Prepare compact workspace JSON          │    │
│  │  4. Run OpenClaw agent (reads EVOLVE_       │    │
│  │     AGENTS.md, analyzes, writes skills)      │    │
│  │  5. Collect diffs                           │    │
│  │  6. Upload to storage (OSS/S3/local)       │    │
│  │  7. Acknowledge + delete consumed sessions  │    │
│  └─────────────────────────────────────────────┘    │
│                          │                           │
│                          ▼                           │
│              ┌─────────────────────┐                 │
│              │  Unified Skill Lib │                  │
│              │  (evolved skills)  │                  │
│              └─────────────────────┘                 │
└─────────────────────────────────────────────────────┘
```

### Key Components

1. **agent_evolve_server** — The autonomous evolution engine
   - Replaces fixed 3-stage LLM pipeline with OpenClaw agent session
   - Agent reads `EVOLVE_AGENTS.md` bootstrap + session data
   - Agent writes evolved SKILL.md files directly
   - Uses `workspace/sessions/` for input, `workspace/skills/` for output

2. **Skill Library** — Shared across all agents and devices
   - Auto-deduplication (no duplicate skills)
   - Quality improvements compound over time
   - Version-controlled with rollback

3. **Claw Family Integration** — Works with:
   - OpenClaw
   - PicoClaw
   - ZeroClaw
   - Hermes (native)

---

## How agent_evolve_server Works

### Input: Session Data

Sessions stored as compact JSON in `workspace/sessions/`:
```json
{
  "session_id": "abc123",
  "agent_id": "hermes-01",
  "timestamp": "2026-04-21T10:00:00Z",
  "events": [
    {"type": "tool_call", "tool": "read_file", "args": {...}},
    {"type": "tool_result", "result": "..."},
    {"type": "user_feedback", "feedback": "no, do it this way instead"}
  ]
}
```

### Bootstrap: EVOLVE_AGENTS.md

The agent reads this file to understand its mission:
```
# Evolution Agent

Your job is to evolve skills based on session data.

## Task
1. Read sessions from workspace/sessions/
2. Identify patterns: corrections, preferences, errors
3. Analyze what works and what doesn't
4. Write improved SKILL.md files to workspace/skills/

## Constraints
- Keep skills minimal and focused
- Prefer clarity over completeness
- Remove duplicate skills
- Quality over quantity
```

### Processing Pipeline

```
Session Data → Summarize → Compact Workspace JSON → OpenClaw Agent
                                                          │
                                                          ▼
                                                     [Agent Session]
                                                     Reads bootstrap
                                                     Analyzes sessions
                                                     Writes evolved skills
                                                          │
                                                          ▼
                                                Diffs collected + uploaded
```

### Output: Evolved Skills

Skills written to `workspace/skills/` as standard SKILL.md files:
```markdown
---
name: file-reader
description: Read and analyze files efficiently
---

# File Reader Skill

## When to Use
- User asks to read or analyze a file
- Need to understand code structure
- Checking for patterns or errors

## How It Works
1. Use read_file for text files
2. Use grep_search for content searches
3. Use list_files for directory exploration

## Best Practices
- [Evolved best practices from sessions]
```

---

## Why This Matters for Solomon OS

### Current Problem
- Hermes skills are static — they don't improve from mistakes
- Russell Tuna corrections are forgotten between sessions
- What Joseph teaches Russell Tuna isn't learned by Hermes
- No cross-agent skill sharing

### SkillClaw Solution
- Skills evolve after every session
- Corrections become updated skill behavior
- New patterns spread to all agents
- Skill quality compounds over time

### Integration with Phantom Self-Evolution

Phantom evolves its OWN config. SkillClaw evolves SHARED skills across agents. Together:

```
Session Complete
       │
       ├──────────────────────┐
       ▼                      ▼
Phantom Config             SkillClaw Skills
Evolution                 Evolution
       │                      │
       ▼                      ▼
solomon-config/          Hermes Skills Registry
(Self-improving          (Shared across all agents)
 agent)
```

Both run after each session. Config improvements go to `solomon-config/`, skill improvements go to Hermes skills.

---

## For Hermes Integration

### What We Need

1. **Session Capture** — Hermes sessions → JSON in shared storage
2. **agent_evolve_server** — Run on session data
3. **Skill Sync** — Evolved skills → Hermes skills registry

### Quick Start

```bash
# Install
git clone https://github.com/AMAP-ML/SkillClaw
cd SkillClaw
pip install -r requirements.txt

# Configure
export OPENCLAW_API_KEY=...
export ANTHROPIC_API_KEY=...  # for default Sonnet 4.6 judge

# Run evolution
python -m agent_evolve_server run --storage local --storage-path /tmp/evolve
```

### Model Configuration

Default: `claude-opus-4-6` via Anthropic Messages API
Override:
```bash
skillclaw evolve --model openai/gpt-4o --api-base https://api.openai.com/v1
skillclaw evolve --model anthropic-messages  # default
```

### Storage Backends

- **Local:** `~/.skillclaw/storage/`
- **S3:** AWS S3 bucket
- **OSS:** Alibaba Object Storage Service

---

## Comparison to Alternatives

| Aspect | SkillClaw | Phantom Self-Evolution | agentic-stack |
|--------|-----------|----------------------|---------------|
| What evolves | Shared skills | Own config | Lessons |
| Scope | Cross-agent | Single agent | Cross-agent |
| Model | OpenClaw agent | Sonnet judge | Host review |
| Storage | OSS/S3/local | Git versioned | Python files |
| Trigger | Session batch | Post-session | Post-session |
| Deduplication | Auto | N/A | Manual |

---

## Decision

**RECOMMENDATION: FORGE**

**Rationale:** SkillClaw's cross-agent skill evolution fills the exact gap in Hermes. Combined with Phantom's self-evolution, we get:
- Self-improving agent config (Phantom pattern)
- Self-improving shared skills (SkillClaw pattern)

Both are needed for JCPaid to run 24/7 without manual skill maintenance.

**Next Steps:**
1. Install SkillClaw + OpenClaw
2. Configure for Hermes sessions
3. Set up local storage
4. Test with a few sessions
5. Integrate with Solomon Heartbeat

---

## Files to Reference

- Main repo: `/home/workspace/SkillClaw/` (clone when ready)
- agent_evolve_server README: `agent_evolve_server/README.md`
- Evolution agent bootstrap: `EVOLVE_AGENTS.md`
- Skills examples: `skills/`

*Report created: 2026-04-21*