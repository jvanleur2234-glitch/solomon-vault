#!/usr/bin/env python3
"""
Solomon OS — Zijus Chat UI ↔ Zo AI Direct Bridge
Bridges Zijus WebSocket Chat UI directly to Zo via /zo/ask API.
Start: python3 zijus_zo_bridge.py
UI: http://localhost:8001
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
ZO_API = "https://api.zo.computer/zo/ask"
ZO_TOKEN = os.getenv("ZO_CLIENT_IDENTITY_TOKEN", os.getenv("ZO_API_KEY", ""))
ZIJUS_JS = "https://cdn.jsdelivr.net/gh/zijus/zijus-chat-ui@main/dist/zijus-webclient-v0.1.0.js"
ZIJUS_CONFIG = os.getenv("ZIJUS_CONFIG", "")

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

    async def send_msg(content: str, m_id: str, msg_type="TextMessage", append=False):
        await ws.send_json({
            "source": "assistant", "type": msg_type,
            "content": content, "m_id": m_id,
            "ts": datetime.now(timezone.utc).isoformat(),
            **({"append": True} if append else {})
        })

    async def process(input_text: str, m_id: str):
        response_m_id = m_id or str(uuid.uuid4())
        try:
            async with httpx.AsyncClient(timeout=300.0) as client:
                async with client.stream(
                    "POST",
                    ZO_API,
                    json={
                        "input": input_text,
                        "model_name": "vercel:minimax/minimax-m2.7",
                        "stream": True
                    },
                    headers={
                        "Authorization": f"Bearer {ZO_TOKEN}",
                        "Content-Type": "application/json",
                        "Accept": "text/event-stream"
                    }
                ) as resp:
                    async for line in resp.aiter_lines():
                        if not line.startswith("data: "):
                            continue
                        raw = line[6:].strip()
                        if raw == "[DONE]" or not raw:
                            continue
                        try:
                            event = json.loads(raw)
                            text = event.get("text", event.get("content", ""))
                            if text:
                                await send_msg(text, response_m_id, "TextMessage")
                        except json.JSONDecodeError:
                            continue

            await ws.send_json({
                "source": "assistant", "type": "FinalMessage",
                "m_id": response_m_id,
                "ts": datetime.now(timezone.utc).isoformat()
            })

        except asyncio.CancelledError:
            logger.info("Zo stream cancelled")
        except Exception as e:
            logger.error(f"Zo bridge error: {e}")
            try:
                await ws.send_json({
                    "source": "assistant", "type": "error",
                    "content": f"Error: {str(e)}"
                })
            except Exception: pass

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
    port = int(os.getenv("BRIDGE_PORT", "8001"))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")