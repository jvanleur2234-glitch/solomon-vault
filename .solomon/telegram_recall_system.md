# Telegram Recall System — Solomon OS

## Overview

Zo never forgets what happened in Telegram sessions. Every conversation is summarized and stored as a persistent memory file in the Solomon Vault.

## Architecture

```
Telegram message (JSON)
       ↓
  auto_summary.py      ← Core summarization engine (Python)
       ↓
  summarize_session.sh  ← Bash wrapper / CLI entry point
       ↓
  raw/telegram_SUMMARY_YYYY-MM-DD.md  ← Persisted memory
```

## File Structure

```
solomon-vault/
├── .solomon/
│   ├── telegram_recall_system.md   ← This document
│   ├── auto_summary.py             ← Python summarizer
│   └── summarize_session.sh        ← Bash CLI wrapper
└── raw/
    └── telegram_SUMMARY_YYYY-MM-DD.md  ← Session summaries
```

## Usage

### Option 1 — Bash wrapper (recommended)
```bash
./summarize_session.sh "2026-04-05" '{"messages": [...]}'
```

### Option 2 — Python directly with JSON arg
```bash
python3 auto_summary.py --conversation '{"messages": [...]}'
```

### Option 3 — Pipe JSON via stdin
```bash
cat conversation.json | python3 auto_summary.py
```

### Option 4 — In-process (import as module)
```python
from auto_summary import summarize_conversation
summary = summarize_conversation([{"role": "user", "content": "..."}])
```

## Session Summary Template

Each summary file contains:
- **Date** — Session date
- **Key Decisions** — Choices made, direction confirmed
- **Code Created / Modified** — Files touched, what changed
- **Problems Solved** — Issues resolved during session
- **Unresolved Issues** — Blockers, gaps, open questions
- **Follow-Up Needed** — Next steps, who owns them

## Existing Rule

A Zo rule already triggers this automatically:

> "After every Telegram conversation, save a session summary to /home/workspace/solomon-vault/raw/telegram_SUMMARY_YYYY-MM-DD.md"

The rule calls `summarize_session.sh` as the execution mechanism.

## Summarization Logic

The Python script:
1. Parses the JSON conversation (supports `{"messages": [...]}` or raw `[...]` array)
2. Extracts user intents and assistant responses
3. Identifies code artifacts, decisions, blockers, and next steps
4. Formats into the markdown template
5. Outputs to stdout (wrapper redirects to the .md file)

## Design Decisions

- **No external LLM dependency** — summarization is rule-based (pattern matching on keywords, markers)
- **JSON input only** — conversation must be structured JSON (Zo already captures Telegram sessions this way)
- **Human-readable output** — summaries are meant to be read by a human, not just machines
- **Date-stamped files** — one file per day, same format as the Zo rule expects