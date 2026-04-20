# Parlor → JackConnect Integration Spec

*Date:* 2026-04-20
*Purpose:* Wire Parlor voice AI into JackConnect real estate agent portal

---

## What We Have

### Parlor (Voice AI)
- **Location:** `/home/workspace/parlor/`
- **What it does:** On-device multimodal AI. Voice + vision conversations. Uses Gemma 4 E2B (speech/vision understanding) + Kokoro TTS (speech synthesis)
- **Stack:** Browser ↔ WebSocket ↔ FastAPI + LiteRT-LM + MLX/ONNX
- **Requirements:** macOS Apple Silicon or Linux with GPU, ~3GB RAM
- **Already forked:** ✅ at /home/workspace/parlor/

### JackConnect Portal
- **URL:** https://josephv.zo.space/jackconnect/
- **Pages:** Landing, Portal, Worker Dashboard, Submit Job, Status
- **API:** `/api/jackconnect/submit-job`, `/api/jackconnect/jobs`

### Screenpipe (Screen + Audio Capture)
- **Location:** `/home/workspace/screenpipe/`
- **What it does:** AI memory for your screen. Runs agents in background based on screen content
- **Stack:** Rust, desktop app, P2P engine

---

## Integration Architecture

```
Client (real estate agent)
    │
    │  "Talk to AI" button on JackConnect portal
    ▼
JackConnect Portal (/jackconnect/portal)
    │
    │  WebRTC or WebSocket
    ▼
Parlor Voice AI (local or server)
    │
    │  Speech → Gemma 4 E2B → Intent + entities
    │  Entities: listing address, client question, follow-up request
    ▼
JackConnect API (job creation, CMA lookup, lead info)
    │
    │  Structured response
    ▼
Parlor TTS (Kokoro) → Spoken response to client
```

---

## How Voice Integrates Into JackConnect

### The Flow
1. Agent clicks "Talk to AI" on portal
2. Browser asks for mic permissions
3. Voice stream goes to Parlor via WebSocket
4. Parlor transcribes + understands intent
5. Parlor calls JackConnect API for relevant data
6. Parlor speaks back the result + shows on screen
7. Optionally: full conversation logged as a job note

### What Parlor Can Do for Real Estate Agents
- **Listing questions:** "What's the CMA for 123 Oak Street?" → Parlor queries JackConnect API → speaks back the report
- **Lead follow-up:** "Call my last 5 leads" → Parlor reads from JackConnect → schedules outreach
- **Voice notes:** Agent talks, Parlor transcribes and creates a job note automatically
- **Market questions:** "What's the average DOM in this zip?" → Parlor queries → speaks data

### Parlor Endpoints We Need
```python
# /api/parlor/voice — Voice conversation endpoint
POST /api/parlor/voice
  Body: { audio_chunk: bytes, session_id: str }
  Response: { transcript: str, response_audio: bytes }

# /api/parlor/session — Start a voice session
POST /api/parlor/session
  Body: { client_id: str, context: "listing|cma|leads|general" }
  Response: { session_id: str }

# /api/parlor/stop — End session
POST /api/parlor/stop
  Body: { session_id: str }
```

---

## Screenpipe Integration (Training Data)

### The Flow
1. Real estate agent uses JackConnect (screen active)
2. Screenpipe captures screen frames + audio
3. Relevant sessions (voice calls, CMA work) are tagged
4. Data feeds into JackConnect training set
5. Russell Tuna learns from actual client interactions

### What Screenpipe Captures
- Screen recordings (with consent)
- Audio from voice calls
- UI interactions in JackConnect
- Job submission patterns

---

## Actual Code Changes Needed

### 1. Add "Talk to AI" Button to Portal
**File:** `/jackconnect/portal` route
**Change:** Add a floating mic button. On click, starts WebSocket to Parlor.

```tsx
// Add to portal.tsx
const [voiceActive, setVoiceActive] = useState(false);

const startVoice = async () => {
  setVoiceActive(true);
  const ws = new WebSocket("ws://localhost:8765/voice");
  ws.onmessage = (e) => {
    const data = JSON.parse(e.data);
    if (data.type === "transcript") showTranscript(data.text);
    if (data.type === "audio") playAudioChunk(data.audio);
  };
  // Send mic stream to WebSocket
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  const recorder = new MediaRecorder(stream);
  recorder.ondataavailable = (e) => ws.send(e.data);
  recorder.start();
};
```

### 2. Parlor API Stub in zo.space
**File:** `/api/parlor/voice` route
**Change:** Stub that proxies to Parlor server at `localhost:8765`

```typescript
import type { Context } from "hono";

export default async (c: Context) => {
  const session_id = c.req.header("X-Session-ID");
  const audio = await c.req.arrayBuffer();
  
  // Proxy to Parlor server
  const parlorr = await fetch("http://localhost:8765/voice", {
    method: "POST",
    body: audio,
    headers: { "X-Session-ID": session_id }
  });
  
  const result = await parlorr.json();
  return c.json(result);
};
```

### 3. JackConnect API → Parlor Context
**File:** `/api/parlor/context/[job_id]` route
**Change:** When Parlor asks about a job, return structured data

```typescript
export default async (c: Context) => {
  const job_id = c.req.param("job_id");
  const job = await getJob(job_id); // from jobs.json
  return c.json({
    client_name: job.clientName,
    property_address: job.propertyUrl || job.notes,
    service_type: job.jobType,
    status: job.status,
    created_at: job.createdAt
  });
};
```

---

## Files to Create/Modify

| File | Action | Purpose |
|------|--------|---------|
| `/api/parlor/voice` | Create | Voice proxy to Parlor |
| `/api/parlor/session` | Create | Start voice session |
| `/api/parlor/context/[job_id]` | Create | Get job context for Parlor |
| `/jackconnect/portal` | Modify | Add voice button + WebSocket |
| `parlor/src/voice_router.py` | Modify | Add JackConnect API calls |
| `/jack-connect/screenpipe/session_tags.json` | Create | Tag relevant sessions |

---

## Status

- [x] Parlor forked ✅
- [ ] Parlor server running
- [ ] Voice endpoint in zo.space
- [ ] Portal voice button
- [ ] JackConnect API → Parlor context bridge
- [ ] Screenpipe integration
- [ ] End-to-end test

---

*Last updated: 2026-04-20*