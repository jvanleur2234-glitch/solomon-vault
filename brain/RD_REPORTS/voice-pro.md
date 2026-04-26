# RD Report: Voice-Pro

**Repository:** https://github.com/abus-aikorea/voice-pro  
**Cloned:** 2026-04-26  
**Stars:** ~1.3K  
**License:** LGPL  
**Language/Stack:** Python 3.10, Gradio, PyTorch, CUDA

---

## What It Is

Voice-Pro is a **local Windows desktop app** (also runs on Mac/Linux) for AI voice processing. It's a Gradio web UI that wraps multiple open-source voice models:

- **Speech-to-text:** Whisper, Faster-Whisper, WhisperX
- **Voice cloning:** F5-TTS, E2-TTS, CosyVoice (zero-shot, needs ~30s reference audio)
- **TTS:** Edge-TTS (free, 100+ languages), kokoro (ranked #2 on HuggingFace TTS Arena)
- **YouTube download + audio separation** via yt-dlp + Demucs
- **Translation:** Deep-Translator (100+ languages)

It has built-in celebrity voice clones — Joe Rogan, Trump, Elon, Kanye, Jordan Peterson, etc. for English; BTS members, K-pop idols for Korean; and others for Chinese/Japanese.

---

## Faceless YouTube Comedy Angle

**Idea: "Celebrity Fight Club"** — Take viral Reddit posts, AITA stories, or arguments and dub them with celebrity voices.

**How it would work:**
1. Scrape Reddit/AITA for content (script already has the story)
2. Use Voice-Pro to clone a funny voice (e.g., Joe Rogan, Kanye, Trump)
3. Generate TTS narration with comedic timing
4. Add reaction-style b-roll clips from YouTube (via yt-dlp)
5. Post as faceless channel

**Why this fits:**
- Celeb voices already bundled in (Trump, Kanye, Joe Rogan, etc.)
- Fully automated pipeline possible
- Comedy + outrage content does very well on YouTube Shorts + long-form
- No face needed — audio-driven content

**Comparison to current pipeline:**
- Currently using xtts for voice cloning — Voice-Pro's F5-TTS/CosyVoice are higher quality
- Voice-Pro has better multilingual support
- This would be a local Windows app, not cloud — so no API costs
- However, it's not a hosted service — user needs a GPU (Windows/NVIDIA recommended)

---

## Technical Considerations

- Requires **NVIDIA GPU with 4GB+ VRAM** (8GB+ for full quality)
- **First-run download:** CosyVoice2-0.5B is 9GB, can take 1+ hour
- Runs **locally** on Windows/Mac/Linux — not a SaaS or API
- Supports **batch processing** via the Dubbing Studio tab
- yt-dlp integrated for video downloading

---

## Verdict

**Recommendation: SKIP for cloud-hosted pipeline — GOOD for local "studio in a box" build**

The tool is excellent quality but it's a **local desktop app**, not an API or hosted service. For Solomon OS / Russell Tuna's use case (automated, cloud-based content pipeline), this doesn't directly fit — unless we build a dedicated Windows rig as part of the operation.

**Could be a future "hardware product"** — sell a pre-built "Voice Studio" mini-PC with Voice-Pro pre-installed + presets for different content styles. That's a more legitimate physical product angle.

For now: document it as a **reference implementation** for voice cloning quality benchmarks. The F5-TTS and CosyVoice models inside it are what we'd want to serve via API in the cloud pipeline.