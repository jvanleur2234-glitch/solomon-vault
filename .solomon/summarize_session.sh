#!/bin/bash
# Saves summary to /home/workspace/solomon-vault/raw/telegram_SUMMARY_$1.md
# Usage: echo '[{"role":"user","content":"hi"}]' | ./summarize_session.sh "2026-04-05"

DATE="${1:-$(date +%Y-%m-%d)}"
OUTPUT="/home/workspace/solomon-vault/raw/telegram_SUMMARY_${DATE}.md"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

python3 "${SCRIPT_DIR}/auto_summary.py" > "${OUTPUT}"
echo "Summary saved to ${OUTPUT}"
