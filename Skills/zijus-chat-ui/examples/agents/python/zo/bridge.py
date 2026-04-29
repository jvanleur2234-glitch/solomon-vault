"""
Zijus Chat UI + Zo Computer Bridge

Wires the Zijus Chat UI (WebSocket frontend) to Zo Computer via the /zo/ask API.
Gives Zo a beautiful frontend UI — every message routes through the Zo API.
"""
import asyncio
import json
import os
import sys
from typing import Any

from fastapi import FastAPI, Request
from starlette.responses import JSONResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocket
import websockets
import requests

# ── Config ────────────────────────────────────────────────────────────────────
ZIJUS_API_KEY = os.environ.get("ZIJUS_API_KEY", "demo")
ZO_API_KEY = os.environ.get("ZO_API_KEY", os.environ.get("ZO_CLIENT_IDENTITY_TOKEN", ""))
ZO_API_URL = "https://api.zo.computer/zo/ask"
MODEL_NAME = "vercel:minimax/minimax-m2.7"
BRIDGE_PORT = int(os.environ.get("BRIDGE_PORT", 8081))

# ── Zo API caller ────────────────────────────────────────────────────────────
def zo_ask(message: str, conversation_id: str | None = None) -> str:
    """Send a message to Zo and return the text response."""
    payload = {
        "input": message,
        "model_name": MODEL_NAME,
    }
    if conversation_id:
        payload["conversation_id"] = conversation_id

    resp = requests.post(
        ZO_API_URL,
        headers={
            "Authorization": ZO_API_KEY,
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=60,
    )
    if resp.ok:
        result = resp.json()
        return result.get("output", str(result))
    return f"[Zo error] {resp.status_code}: {resp.text}"


async def zo_ask_async(message: str, conversation_id: str | None = None) -> str:
    """Async wrapper for the Zo API call."""
    return await asyncio.get_event_loop().run_in_executor(None, zo_ask, message, conversation_id)


# ── WebSocket bridge ──────────────────────────────────────────────────────────
connections: set[WebSocket] = set()
sessions: dict[str, str] = {}  # websocket_id -> conversation_id


async def websocket_handler(websocket: WebSocket):
    """Zijus UI connects via WS. Relay messages to Zo API."""
    await websocket.accept()
    connections.add(websocket)
    ws_id = str(id(websocket))
    conv_id = sessions.get(ws_id)
    try:
        async for msg in websocket:
            data = json.loads(msg)
            content = data.get("content", "")
            if not content:
                continue
            # First message: optionally extract system prompt
            if data.get("role") == "system":
                continue
            response = await zo_ask_async(content, conv_id)
            await websocket.send_json({"role": "assistant", "content": response})
    except Exception as e:
        print(f"[WS error] {e}")
    finally:
        connections.discard(websocket)
        sessions.pop(ws_id, None)


# ── REST fallback ─────────────────────────────────────────────────────────────
app = FastAPI(title="Zijus-Zo Bridge")


@app.post("/chat")
async def chat(req: Request) -> JSONResponse:
    body = await req.json()
    message = body.get("message", "")
    conv_id = body.get("conversation_id", None)
    response = await zo_ask_async(message, conv_id)
    return JSONResponse({"response": response})


@app.get("/health")
async def health() -> JSONResponse:
    return JSONResponse({
        "status": "ok",
        "model": MODEL_NAME,
        "zo_connected": bool(ZO_API_KEY),
    })


@app.get("/models")
async def models() -> JSONResponse:
    """List available models for the UI."""
    return JSONResponse({
        "models": [
            {"id": MODEL_NAME, "name": "MiniMax M2.7"},
            {"id": "vercel:anthropic/claude-3-5-sonnet", "name": "Claude 3.5 Sonnet"},
            {"id": "vercel:openai/gpt-4o", "name": "GPT-4o"},
        ]
    })


# ── Start ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    print(f"🚀 Zijus-Zo bridge listening on port {BRIDGE_PORT}")
    print(f"   Zo API: {'connected' if ZO_API_KEY else 'demo mode (no key)'}")
    uvicorn.run(app, host="0.0.0.0", port=BRIDGE_PORT)