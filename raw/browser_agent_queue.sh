#!/bin/bash
# Solomon Browser Agent — Background Queue Worker
# Watches browser_agent_queue.jsonl and runs tasks sequentially.
# Auto-starts on boot via this runner.

QUEUE_FILE="/home/workspace/solomon-vault/raw/browser_agent_queue.jsonl"
LOG_FILE="/home/workspace/solomon-vault/raw/browser_agent_queue.log"
AGENT_SCRIPT="/home/workspace/solomon-vault/raw/browser_agent.py"

echo "🚀 Browser agent queue worker starting..." >> "$LOG_FILE"

# Process queue line by line
while true; do
  if [ -f "$QUEUE_FILE" ] && [ -s "$QUEUE_FILE" ]; then
    # Read first line
    LINE=$(head -1 "$QUEUE_FILE")
    # Remove it from queue
    tail -n +2 "$QUEUE_FILE" > "$QUEUE_FILE.tmp" && mv "$QUEUE_FILE.tmp" "$QUEUE_FILE"

    TASK=$(echo "$LINE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('task',''))")
    MODEL=$(echo "$LINE" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('model','groq'))")

    if [ -n "$TASK" ]; then
      echo "[$(date)] Running: ${TASK:0:60}..." >> "$LOG_FILE"
      python3 "$AGENT_SCRIPT" "$TASK" "$MODEL" >> "$LOG_FILE" 2>&1
      echo "[$(date)] Done: exit=$?" >> "$LOG_FILE"
    fi
  else
    sleep 5
  fi
done
