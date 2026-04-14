# Background Research — FaithStep + Solomon Guide
Generated: 2026-04-10 18:28
Worker: Zo background agent

---

# PROJECT A — FaithStep

## What It Is
A Clicky-style cursor overlay companion for Christian walk-throughs. 
Capture any app screen, send to Hermes, receive spiritual insight, 
cursor flies to relevant UI element with encouragement or direction.

## Stack
- Frontend: Clicky overlay pattern (macOS menu bar → NSPanel cursor overlay)
  → For Zo: React PWA + cursor overlay div (web-based, cross-platform)
- Voice I/O: VoxCPM2 (Apache 2.0, 30 languages, free, local)
- AI Brain: Hermes (Ollama qwen3:1.7b, zero API cost)
- Cursor Overlay: CSS position:fixed + JS animation (web) 
  OR NSPanel-based overlay (macOS native)
- Screen Capture: browser tab capture API OR ScreenCaptureKit (macOS native)

## Key Differentiator from Clicky
Clicky = "what button do I press" (tool guidance)
FaithStep = "what is God saying about this" (spiritual guidance)

## Core Loop
1. User presses hotkey (global shortcut)
2. Screen captured + cropped
3. Image sent to Hermes (local Ollama — FREE)
4. Hermes responds with spiritual insight relevant to what user was doing
5. Cursor overlay appears with response text + visual cue pointing to relevant UI
6. Auto-dismisses after user interaction

## Architecture
```
User presses Ctrl+Shift+F (FaithStep hotkey)
  → Screenshot captured (ScreenCaptureKit / tab capture API)
  → Image → Hermes via local Ollama (qwen3:1.7b)
  → Response + [POINT:x,y:label] tag parsed
  → CSS cursor animates to screen coordinates
  → TTS whisper using VoxCPM2 (or ElevenLabs if available)
  → Overlay fades after 3s inactivity
```

## Technical Notes
- macOS version: SwiftUI NSPanel overlay + CGEvent tap for global hotkey
  → Same pattern as Clicky, different AI backend
- Web version: browser extension with content script + overlay div
  → Cross-platform but requires extension install
- Hermes prompt: Christian walk-through coach persona
  → Context: what app they're in, what they were doing
  → Response style: warm, pastoral, scripture-anchored, short

## Next Steps (Build Order)
1. macOS prototype: Clone Clicky, swap AI backend (Claude → Hermes/Ollama)
   → Replace Cloudflare Worker proxy with local Hermes WebAPI
   → Replace AssemblyAI with VoxCPM2 (local, free)
   → Replace ElevenLabs TTS with VoxCPM2 (local, free)
2. Prompt: Write FaithStep Hermes system prompt (Christian coach persona)
3. VoxCPM2: Test local TTS generation
4. Overlay: CSS cursor animation for web version
5. Test: Screenshots from Bible apps, devotional tools, church apps

---

# PROJECT B — Solomon Guide (AI Cursor for Zo)

## What It Is
A Clicky-style cursor overlay that acts as an interactive guide for 
any Zo task. Instead of "press this button" it's "click there, 
type this, here's why." Makes Zo accessible to non-technical users 
through visual cursor guidance.

## Stack
- Frontend: Clicky overlay pattern (same architecture)
- AI Brain: Zo orchestrator + Hermes
- Voice: VoxCPM2 or ElevenLabs
- Screen Context: Uses Zo's existing browser sessions + DOM state

## Key Differentiator from Clicky
Clicky = general screen understanding + voice
Solomon Guide = Zo's full context (files, tasks, memory, projects) + cursor guidance

## Core Loop
1. User presses global hotkey (Ctrl+Shift+S)
2. Zo captures current screen/app context
3. Zo responds with step-by-step guidance
4. Cursor overlay appears showing exactly where to click/type
5. If user asks a question, voice response + cursor points to relevant UI

## Architecture
```
User presses Ctrl+Shift+S (Solomon Guide hotkey)
  → Screen captured + current app detected
  → Zo loaded with full Solomon OS context
  → "What are you trying to do?" voice prompt
  → User speaks answer
  → Zo generates step-by-step instructions
  → Cursor animates to first step, response streamed
  → User clicks → cursor moves to next step
```

## Unique Advantage
Zo knows:
- Your files and projects
- Your goals and priorities  
- Your past questions and answers
- What you're working on right now

Cursor overlay becomes a personal guide with FULL context — 
not just "what's on screen" but "what you're trying to accomplish."

## Different from FaithStep
- FaithStep = spiritual/emotional guidance, soft whispers
- Solomon Guide = task completion, active teaching, clear directions

## Next Steps (Build Order)
1. Hermes WebAPI already running on port 8642 → test with voice input
2. Build lightweight macOS overlay (clone Clicky, simplify)
3. Connect to Hermes (swap Claude for Ollama backend)
4. Add Zo context injection (files, projects, memory)
5. Add cursor coordinate parsing from Hermes responses
6. Test: walk through setting up a CashClaw audit, creating a zo.space page, etc.

---

# SHARED INFRASTRUCTURE

Both projects share:
- VoxCPM2 for local TTS (free, Apache 2.0, 30 languages)
- Hermes WebAPI on port 8642 (already running)
- Clicky architecture as template

The key insight: Clicky solved the HARD parts:
- Global hotkey on macOS
- Screen capture with permissions
- Cursor overlay animation
- Voice input pipeline
- Multi-monitor support

We just swap the AI backend and change the persona.

---

# BUSINESS FIT

FaithStep: 
- Niche: Christian productivity ( underserved)
- Model: Freemium (3 free walks/day, $4.99/mo unlimited)
- Moat: Hermes skill library of Christian walk-throughs
- LINK fit: faith + family + generosity

Solomon Guide:
- Niche: Zo users who want visual guidance
- Model: Included with Zo subscription
- Moat: Full Zo context no other AI has
- LINK fit: new tech/AI + deals + helping others

Both are "Clicky but for [spiritual | productivity]" — 
proven category, proven UX, free backend replacement.

---

*Worker complete. Both projects spec'd and ready to build.*
