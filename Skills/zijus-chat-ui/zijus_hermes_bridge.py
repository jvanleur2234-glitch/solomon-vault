#!/usr/bin/env python3
"""
Solomon OS — Zijus Chat UI ↔ Hermes Agent Bridge
Bridges Zijus WebSocket Chat UI to Hermes agent via LangChain adapter.
Start: python3 zijus_hermes_bridge.py
UI: http://localhost:8000
"""
import os, json, uuid, logging, base64, asyncio
from datetime import datetime, timezone
from typing import Optional
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

# ── Hermes Import ──────────────────────────────────────────────────────────────
import sys
sys.path.insert(0, "/home/workspace/hermes-agent")
from agent import root_agent

# ── FastAPI App ────────────────────────────────────────────────────────────────
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")

APP_NAME = os.getenv("APP_NAME", "Solomon OS")
ZIJUS_JS = "https://cdn.jsdelivr.net/gh/zijus/zijus-chat-ui@main/dist/zijus-webclient-v0.1.0.js"
ZIJUS_CONFIG = os.getenv("ZIJUS_CONFIG", "")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "agent_name": APP_NAME,
            "zijus_config": ZIJUS_CONFIG,
            "zijus_javascript": ZIJUS_JS,
        }
    )

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    token = ws.query_params.get("token", "")
    session_id = ws.query_params.get("session_id", "")
    
    # ── JWT helpers (from Zijus utils.py) ──────────────────────────────────────
    from jwt import encode as jwt_encode
    from jwt import decode as jwt_decode
    from jwt.exceptions import InvalidTokenError
    SECRET_KEY = os.getenv("JWT_SECRET_KEY", "solomon-os-secret-change-me")
    
    async def generate_jwt(sid):
        from datetime import timedelta
        payload = {
            "session_id": sid or f"{datetime.now(timezone.utc).strftime('%Y%m%d')}-{uuid.uuid4()}",
            "exp": datetime.now(timezone.utc) + timedelta(hours=24)
        }
        return jwt_encode(payload, SECRET_KEY, algorithm="HS256")
    
    async def validate_jwt(tok):
        if not tok: return None
        try: return jwt_decode(tok, SECRET_KEY, algorithms=["HS256"])
        except InvalidTokenError: return None

    payload = await validate_jwt(token) if token else None
    user_id = payload.get("user_id", "anon") if payload else "anon"
    sid = session_id or (payload.get("session_id") if payload else f"sess-{uuid.uuid4()}")
    new_token = await generate_jwt(sid) if not payload else token

    await ws.accept()
    await ws.send_json({"type": "session", "token": new_token})

    current_task: Optional[asyncio.Task] = None

    async def cancel_task(reason: str):
        nonlocal current_task
        if current_task and not current_task.done():
            logger.info(f"Interrupting: {reason}")
            current_task.cancel()
            try:
                await ws.send_json({
                    "source": "assistant", "type": "InterruptMessage",
                    "ts": datetime.now(timezone.utc).isoformat()
                })
            except Exception: pass

    async def send_msg(content: str, m_id: str, msg_type="TextMessage"):
        await ws.send_json({
            "source": "assistant", "type": msg_type, "content": content,
            "m_id": m_id, "ts": datetime.now(timezone.utc).isoformat()
        })

    async def process(input_text: str, m_id: str):
        response_m_id = m_id or str(uuid.uuid4())
        try:
            # ── Build Hermes-style payload ────────────────────────────────────
            payload = [{"role": "user", "content": input_text}]
            config = {"configurable": {"thread_id": sid}}

            streamed = False
            async for event in root_agent.astream_events(
                {"messages": payload}, config=config, version="v2"
            ):
                event_type = event.get("event", "")
                
                # Stream text chunks
                if event_type == "on_chat_model_stream":
                    chunk = event.get("data", {}).get("chunk", {})
                    content = getattr(chunk, "content", None)
                    if content and isinstance(content, str) and content.strip():
                        if not streamed:
                            await send_msg(content, response_m_id, "TextMessage")
                            streamed = True
                        else:
                            # append inline
                            await ws.send_json({
                                "source": "assistant", "type": "TextMessage",
                                "content": content, "m_id": response_m_id,
                                "ts": datetime.now(timezone.utc).isoformat(),
                                "append": True
                            })
                
                elif event_type == "on_tool_start":
                    tool_name = event.get("name", "tool")
                    await ws.send_json({
                        "source": "assistant", "type": "StatusMessage",
                        "content": f"Running {tool_name}...",
                        "m_id": response_m_id,
                        "ts": datetime.now(timezone.utc).isoformat()
                    })

            await ws.send_json({
                "source": "assistant", "type": "FinalMessage",
                "m_id": response_m_id,
                "ts": datetime.now(timezone.utc).isoformat()
            })

        except asyncio.CancelledError:
            logger.info("Hermes run cancelled")
        except Exception as e:
            logger.error(f"Hermes error: {e}")
            await ws.send_json({
                "source": "assistant", "type": "error",
                "content": f"Error: {str(e)}"
            })

    # ── Main Event Loop ────────────────────────────────────────────────────────
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