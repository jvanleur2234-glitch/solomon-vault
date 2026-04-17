# RD REPORT: Parlor (fikrikarim/parlor)

## Summary
On-device, real-time multimodal AI voice assistant. Camera + mic → Gemma 4 E2B (LiteRT-LM) + Kokoro TTS. WebSocket streaming, browser UI, ~2.5-3s end-to-end latency on M3 Pro.

**Stats:** 1.5k stars, Apache 2.0, 165 forks, active development

## What It Is
- Local voice AI: you talk, show camera, it talks back — all on-device
- Real-time TTS streaming (Kokoro), voice activity detection (Silero VAD), barge-in
- Cross-platform: Apple Silicon (MLX) or Linux (ONNX)
- ~3GB RAM, ~2.6GB model download

## Architecture
```
Browser (mic + camera) → WebSocket → FastAPI server → Gemma 4 E2B + Kokoro TTS
                                              ↓
Browser (audio playback + transcript)
```

## What We Have
- **Jack Connect / Clicky**: AI companion overlay with cursor pointing, screen observation, Cloudflare Worker API proxy
- **Screenpipe**: Continuous screen capture (via pipe to a server endpoint)
- **Parlor**: Real-time voice/camera AI with streaming TTS — BUT no screen capture, no cursor pointing

## Integration Analysis: Jack Connect + Parlor + Screenpipe

The idea: Parlor's voice AI becomes Jack Connect's "brain" — real-time voice conversation while Screenpipe captures the screen. Parlor sees and hears what the user is doing, responds naturally via voice, and can point at UI elements (Clicky-style cursor).

**Overlap with what we have:**
- Parlor replaces the Cloudflare Worker + AssemblyAI + ElevenLabs stack for voice
- Parlor is fully on-device = zero per-minute API costs (unlike Clicky which costs $)

**Gaps to fill:**
- Parlor has no screen capture — needs Screenpipe for screen observation
- Parlor has no cursor overlay / pointing mechanism — needs Clicky's overlay window
- Parlor has no persistent memory of workflows — needs Solomon OS skill system

## Recommendation: INTEGRATE

**How it fits Solomon OS:**
1. Replace Clicky worker (AssemblyAI + ElevenLabs) with Parlor's on-device stack → free forever
2. Screenpipe feeds screen context to Parlor → AI "sees" what you're doing
3. Parlor speaks back with Kokoro TTS → natural voice interaction
4. Solomon OS skill system learns from Parlor's observations → Watch Once engine

**Priority use case:** Watch Once for Jack Connect — AI watches you do a workflow once, learns it, automates it forever. Voice-native (no clicking required).

**What to build:**
- Parlor as voice/TTS layer (swap out Cloudflare Worker)
- Screenpipe integration into Parlor's server (feed screen frames alongside camera)
- Clicky's cursor overlay integrated into Parlor's browser UI

**Key risk:** Gemma 4 E2B is small (fast on M3 Pro) but quality vs Claude/haiku for understanding complex workflows is unknown. Worth testing.

## Verdict
🟡 Worthwhile. Parlor solves Clicky's cost problem (on-device = free). The combo (Parlor + Screenpipe + Jack Connect) maps directly to Solomon OS's "Watch Once" vision — an AI that watches, listens, speaks, and learns. Fork and test.
