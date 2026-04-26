# RD Report: NeuTTS

**Repo:** https://github.com/neuphonic/neutts  
**Stars:** ~1.8k (estimate based on recent growth)  
**License:** Apache 2.0 (NeuTTS-Air), NeuTTS Open License 1.0 (NeuTTS-Nano)  
**Status:** SKILL  

## What It Is

NeuTTS is an open-source, on-device text-to-speech system with instant voice cloning. Built by Neuphonic, a voice AI company. Two model tiers:

- **NeuTTS-Air** (~360M params) — English-only, Apache 2.0 license
- **NeuTTS-Nano** (~120M params) — Multilingual (EN/FR/DE/ES), NeuTTS Open License 1.0

Both run locally via GGUF quantizations on CPU or GPU. Voice cloning works with as little as 3 seconds of reference audio. Watermarked outputs by default (Perth watermark).

## What We'd Use It For

Adding voice synthesis capability to Solomon OS agents. Specifically:

1. **Voice agent output** — When Solomon OS agents need to speak (instead of text), NeuTTS generates the audio locally. No external TTS API calls.
2. **Voice cloning** — Clone a client's voice for brand consistency in outbound calls/messages.
3. **Accessibility** — Audio output for dashboards, reports, summaries.
4. **On-device advantage** — No cloud dependency = lower cost, privacy, offline capability.

## How It Compares to What We Have

Solomon OS currently has no TTS capability. This fills the gap cleanly. Alternative would be ElevenLabs or OpenAI TTS APIs — but those require ongoing API costs and external dependencies.

## Recommendation

**FORGE** — Clone to `/home/workspace/NeuTTS/` and build a TTS skill around it.

Install: `pip install neutts[all]`

Key use cases for Solomon OS:
- Voice output for AI agents (automated calls, voice messages)
- Voice cloning for client brand consistency
- Real-time TTS on low-end devices (phone/laptop/Raspberry Pi)

The Nano model is small enough to run on a Raspberry Pi while still sounding natural. This is a strong differentiator for Solomon OS's "AI on any device" positioning.