#!/usr/bin/env python3
"""
Solomon OS — Zijus Chat UI ↔ Hermes SSE Bridge
Bridges Zijus WebSocket Chat UI to Hermes agent via SSE.
Zijus connects via WebSocket → this bridge → Hermes SSE → response streamed back.

Start: python3 zijus_bridge.py
UI: http://localhost:8000
"""
import os, json, uuid, logging, asyncio
from datetime import datetime, timezone
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import httpx

load_dotenv()
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
templates = Jinja2Templates(directory="templates")

APP_NAME = os.getenv("APP_NAME", "Solomon OS")
HERMES_HOST = os.getenv("HERMES_HOST", "http://localhost:8001")
ZIJUS_JS = "https://cdn.jsdelivr.net/gh/zijus/zijus-chat-ui@main/dist/zijus-webclient-v0.1.0.js"
ZIJUS_CONFIG = os.getenv("ZIJUS_CONFIG", "")

# ── JWT helpers ───────────────────────────────────────────────────────────────
from jwt import encode as jwt_encode, decode as jwt_decode
from jwt.exceptions import InvalidTokenError
from datetime import timedelta

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "solomon-os-secret-change-me")

async def generate_jwt(sid):
    payload = {
        "session_id": sid or f"{datetime.now(timezone.utc).strftime('%Y%m%d')}-{uuid.uuid4()}",
        "exp": datetime.now(timezone.utc) + timedelta(hours=24)
    }
    return jwt_encode(payload, SECRET_KEY, algorithm="HS256")

async def validate_jwt(tok):
    if not tok: return None
    try: return jwt_decode(tok, SECRET_KEY, algorithms=["HS256"])
    except InvalidTokenError: return None

# ── Routes ────────────────────────────────────────────────────────────────────
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"agent_name": APP_NAME, "zijus_config": ZIJUS_CONFIG, "zijus_javascript": ZIJUS_JS}
    )

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    token = ws.query_params.get("token", "")
    session_id = ws.query_params.get("session_id", "")
    payload = await validate_jwt(token) if token else None
    sid = session_id or (payload.get("session_id") if payload else f"sess-{uuid.uuid4()}")
    new_token = await generate_jwt(sid) if not payload else token

    await ws.accept()
    await ws.send_json({"type": "session", "token": new_token})

    current_task: asyncio.Task | None = None

    async def cancel_task(reason: str):
        nonlocal current_task
        if current_task and not current_task.done():
            current_task.cancel()
            try:
                await ws.send_json({
                    "source": "assistant", "type": "InterruptMessage",
                    "ts": datetime.now(timezone.utc).isoformat()
                })
            except Exception: pass

    async def process(input_text: str, m_id: str):
        response_m_id = m_id or str(uuid.uuid4())
        try:
            async with httpx.AsyncClient(timeout=300.0) as client:
                # Call Hermes SSE endpoint
                async with client.stream(
                    "POST",
                    f"{HERMES_HOST}/api/sessions/{sid}/chat/stream",
                    json={
                        "message": input_text,
                        "model": os.getenv("HERMES_MODEL", "anthropic/claude-sonnet-4-6"),
                    },
                    headers={"Content-Type": "application/json"},
                ) as resp:
                    async for line in resp.aiter_lines():
                        if not line.startswith("data: "):
                            continue
                        data_str = line[6:].strip()
                        if not data_str or data_str == "[DONE]":
                            continue

                        # Parse SSE event
                        event_type = None
                        event_data = {}
                        for part in data_str.split("\n"):
                            if part.startswith("event: "):
                                event_type = part[7:].strip()
                            elif part.startswith("data: "):
                                raw = part[6:].strip()
                                try:
                                    event_data = json.loads(raw)
                                except json.JSONDecodeError:
                                    continue

                        if not event_type:
                            continue

                        if event_type in ("assistant.delta", "message.started"):
                            delta = event_data.get("delta", "")
                            if delta:
                                await ws.send_json({
                                    "source": "assistant", "type": "TextMessage",
                                    "content": delta, "m_id": response_m_id,
                                    "ts": datetime.now(timezone.utc).isoformat()
                                })

                        elif event_type in ("tool.started", "tool.pending"):
                            tool = event_data.get("tool_name", "tool")
                            preview = event_data.get("preview", "")
                            await ws.send_json({
                                "source": "assistant", "type": "StatusMessage",
                                "content": f"Running {tool}...",
                                "m_id": response_m_id,
                                "ts": datetime.now(timezone.utc).isoformat()
                            })

                        elif event_type in ("assistant.completed", "run.completed"):
                            await ws.send_json({
                                "source": "assistant", "type": "FinalMessage",
                                "m_id": response_m_id,
                                "ts": datetime.now(timezone.utc).isoformat()
                            })

                        elif event_type == "error":
                            await ws.send_json({
                                "source": "assistant", "type": "error",
                                "content": str(event_data.get("message", "Error"))
                            })

        except asyncio.CancelledError:
            logger.info("Hermes run cancelled")
        except Exception as e:
            logger.error(f"Bridge error: {e}")
            try:
                await ws.send_json({
                    "source": "assistant", "type": "error",
                    "content": f"Error: {str(e)}"
                })
            except Exception: pass

    # ── Main Event Loop ──────────────────────────────────────────────────
    try:
        while True:
            raw = await ws.receive_text()
            try: data = json.loads(raw)
            except Exception: continue

            msg_type = data.get("type")
            m_id = data.get("m_id", str(uuid.uuid4()))

            if msg_type in ("session", None): continue
            if msg_type == "feedback": continue
            if msg_type == "send_email": continue
            if msg_type == "AudioMessage":
                await cancel_task("User interrupted with audio")
                continue

            if msg_type == "TextMessage":
                await cancel_task("New user message")
                content = data.get("content", "")
                if content:
                    current_task = asyncio.create_task(process(content, m_id))

    except WebSocketDisconnect:
        logger.info(f"Client disconnected: {sid}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("BRIDGE_PORT", "8000"))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")