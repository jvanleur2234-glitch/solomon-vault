"""
Zijus Chat UI + Hermes Agent Bridge

Wires the Zijus Chat UI (WebSocket frontend) to the Hermes agent,
giving Hermes a beautiful frontend UI instead of just Telegram.
"""
import asyncio
import json
import os
import sys
from typing import Any

import websockets
from FastAPI import FastAPI
from starlette.routing import Route
from starlette.requests import Request
from starlette.responses import JSONResponse

# Zijus client
sys.path.insert(0, "/home/workspace/zijus-chat-ui/dist")
from zijus_webclient import ZijusClient

# Hermes integration
sys.path.insert(0, "/home/workspace/hermes-agent")
from hermes import agent as hermes_agent

# ── Config ────────────────────────────────────────────────────────────────────
ZIJUS_API_KEY = os.environ.get("ZIJUS_API_KEY", "demo")
HERMES_BASE = os.environ.get("HERMES_BASE", "http://localhost:8000")
PORT = int(os.environ.get("BRIDGE_PORT", 8080))

# ── WebSocket bridge ──────────────────────────────────────────────────────────
# Zijus Chat UI connects via WebSocket. We relay messages to Hermes.
connections: set[Any] = set()


async def hermes_chat(message: str, session_id: str = "default") -> str:
    """Send a message to Hermes and return the response."""
    try:
        async with websockets.connect(f"{HERMES_BASE}/chat") as ws:
            await ws.send(json.dumps({"message": message, "session_id": session_id}))
            response = await asyncio.wait_for(ws.recv(), timeout=60)
            return json.loads(response).get("text", str(response))
    except Exception as e:
        return f"[Hermes error] {e}"


async def websocket_handler(websocket: Any):
    """Bridge Zijus UI <-> Hermes agent."""
    await websocket.accept()
    connections.add(websocket)
    try:
        async for msg in websocket:
            data = json.loads(msg)
            content = data.get("content", "")
            session_id = data.get("session_id", "default")
            # Route through Hermes
            response = await hermes_chat(content, session_id)
            await websocket.send_json({"role": "assistant", "content": response})
    except Exception as e:
        print(f"[WS error] {e}")
    finally:
        connections.discard(websocket)


# ── REST fallback ──────────────────────────────────────────────────────────────
app = FastAPI(title="Zijus-Hermes Bridge")


@app.post("/chat")
async def chat(req: Request) -> JSONResponse:
    body = await req.json()
    message = body.get("message", "")
    session_id = body.get("session_id", "default")
    response = await hermes_chat(message, session_id)
    return JSONResponse({"response": response})


@app.get("/health")
async def health() -> JSONResponse:
    return JSONResponse({"status": "ok", "hermes": HERMES_BASE})


# ── Broadcast (for Hermes push notifications) ───────────────────────────────────
async def broadcast_to_ui(message: str):
    """When Hermes wants to push to the UI (e.g. a background task completes)."""
    for conn in connections:
        try:
            await conn.send_json({"role": "assistant", "content": message})
        except Exception:
            connections.discard(conn)


# ── Start ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn

    print(f"🚀 Zijus-Hermes bridge listening on port {PORT}")
    print(f"   Hermes: {HERMES_BASE}")
    print(f"   Zijus key: {'set' if ZIJUS_API_KEY else 'demo mode'}")
    uvicorn.run(app, host="0.0.0.0", port=PORT)