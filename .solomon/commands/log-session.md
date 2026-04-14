---
description: "Archive current session to raw/YYYY-MM-DD.jsonl"
---
Archive current session:

1. Read conversation history (last 50 messages)
2. Format as JSONL with: timestamp, speaker, content, metadata
3. Save to `raw/YYYY-MM-DD-HHMM.jsonl`
4. Update `raw/Sessions.md` index with session summary
5. If session had decisions or action items, create brain/ notes for them
