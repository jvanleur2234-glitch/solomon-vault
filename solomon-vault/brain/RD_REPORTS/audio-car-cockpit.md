# R&D Report: Audio Car Cockpit — Voice AI Architecture

**Date:** April 19, 2026
**Repo:** github.com/Liquid4All/cookbook (1.8K stars, MIT)
**Subdirectory:** examples/audio-car-cockpit

## What It Is

Real-time voice AI cockpit. Combines LFM2.5-Audio-1.5B (TTS/STT) + LFM2-1.2B-Tool via Llama.cpp, running locally. Voice command → AI understands → executes tool → responds audibly.

**Architecture:**
```
Mic → LFM2.5-Audio (STT) → LFM2-1.2B-Tool (intent + tools) → Action → LFM2.5-Audio (TTS) → Speaker
                   ↑
            WebSocket (like a simplified CAN bus)
                   ↓
              HTML/JS UI (vanilla, no framework)
```

**Key specs:**
- Real-time, local, no cloud dependency
- Llama.cpp for both audio model + tool model inference
- Custom audio runner for STT/TTS
- WebSocket messaging between frontend and backend
- Supported: macOS ARM64, Ubuntu ARM64, Ubuntu x64, WSL2

## Why It Fits Solomon Air

This is EXACTLY the voice layer Solomon Air was missing:

**Before:** vPhone CLI (SIP/VoIP calling) — no voice AI
**Now:** voice-car-cockpit architecture → voice commands for ALL phone functions

The `functions.json` defines tool-calling schema. Replace car functions with:
- `dial_contact(name)` → VoIP call
- `send_message(contact, message)` → SMS/voicemail
- `query_calendar(event)` → schedule check
- `dispatch_agent(task)` → Solomon OS task execution
- `play_voicemail()` → audio playback

**On Be Like You! OS:**
This becomes the default phone UI. No app grid. Speak → AI does it.

## For Be Like You! OS

Voice-first interface:
1. User speaks
2. LFM2.5-Audio STT → transcribed
3. LFM2-1.2B-Tool analyzes intent, calls function
4. VoIP call placed OR message sent OR AI responds
5. LFM2.5-Audio TTS → spoken response
6. All local, all private, all free

## Action Items

1. Fork the cookbook repo specifically for this example
2. Study `functions.json` (tool schema for voice commands)
3. Study `server.py` (WebSocket + model orchestration)
4. Adapt voice architecture for Solomon Air's VoIP stack

## Forked

**Location:** /home/workspace/cookbook/examples/audio-car-cockpit/

## LINK Fit

★★★★★ — CRITICAL. This gives Solomon Air its voice layer.

- Local voice AI = free + private + real-time
- Tool-calling architecture = voice controls everything
- WebSocket backend = easy to integrate with vPhone CLI
- No cloud = works without internet (off-grid scenario)