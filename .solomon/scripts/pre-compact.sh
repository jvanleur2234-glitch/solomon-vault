#!/bin/bash
# Pre-compact: log session transcript to raw/
set -e
VAULT_DIR="${SOLOMON_VAULT:-/home/workspace/solomon-vault}"
SESSION_ID="${CLAUDE_SESSION_ID:-$(date +%s)}"
DATE=$(date +%Y-%m-%d)

mkdir -p "$VAULT_DIR/raw"
echo "{\"timestamp\": \"$(date -Iseconds)\", \"session_id\": \"$SESSION_ID\", \"type\": \"session_end\"}" >> "$VAULT_DIR/raw/$DATE.jsonl"
