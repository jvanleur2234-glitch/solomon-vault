#!/bin/bash
# Solomon OS — Orchestration Layer Startup Script

# Check required env vars
if [ -z "$TELEGRAM_BOT_TOKEN" ]; then
    echo "ERROR: TELEGRAM_BOT_TOKEN not set."
    echo ""
    echo "To get a Telegram bot token:"
    echo "  1. Message @BotFather on Telegram"
    echo "  2. Send /newbot"
    echo "  3. Follow prompts, copy the token"
    echo ""
    echo "Then run:"
    echo "  TELEGRAM_BOT_TOKEN=your:token ./start_bot.sh"
    echo ""
    echo "Optional: ZO_API_KEY for Russell Tuna delegation"
    exit 1
fi

cd /home/workspace/solomon-vault/orchestration

echo "Starting Solomon OS Telegram Bot..."
echo "PinchTab: http://localhost:9888 (token: solomon123)"
echo "Commands: /agent [url], /tabs, /kill [id], /status, /help"

python3 telegram_handler.py
