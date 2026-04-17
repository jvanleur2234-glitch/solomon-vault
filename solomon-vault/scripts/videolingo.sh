#!/bin/bash
# VideoLingo Launch Script
# Usage: bash /home/workspace/solomon-vault/scripts/videolingo.sh
#
# Starts VideoLingo Streamlit UI on port 8502 (headless mode)
# Requires: VideoLingo repo at /home/.z/workspaces/con_d8HQ6zgAf8q434AC/VideoLingo
#           .venv must exist (run setup_env.py first if not)

set -e

REPO_DIR="/home/.z/workspaces/con_d8HQ6zgAf8q434AC/VideoLingo"
PORT="${PORT:-8502}"

if [ ! -d "$REPO_DIR/.venv" ]; then
    echo "ERROR: .venv not found. Run setup_env.py first:"
    echo "  cd $REPO_DIR && python setup_env.py"
    exit 1
fi

if [ ! -f "$REPO_DIR/.venv/bin/streamlit" ]; then
    echo "ERROR: streamlit not found in .venv. Run setup_env.py first."
    exit 1
fi

echo "Starting VideoLingo on port $PORT..."
echo "Repo: $REPO_DIR"
echo "Press Ctrl+C to stop"

cd "$REPO_DIR"

.venv/bin/streamlit run st.py \
    --server.headless=true \
    --server.port="$PORT" \
    --server.address="127.0.0.1"
