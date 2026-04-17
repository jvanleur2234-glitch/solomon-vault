# VideoLingo Setup on Zo Computer

**Date:** 2026-04-16
**Purpose:** Video transcription + dubbing as a service via Solomon OS
**Repo:** `/home/.z/workspaces/con_d8HQ6zgAf8q434AC/VideoLingo/`

---

## What VideoLingo Does

- Downloads video from YouTube or local file
- Transcribes with WhisperX (word-level timestamps)
- Segments subtitles using NLP AI (single-line, Netflix-quality)
- Translates with GPT/Claude (translate → reflect → adapt 3-step process)
- Generates dubbing audio (Edge-TTS, Azure, OpenAI TTS, GPT-SoVITS, etc.)
- Burns subtitles + dubbing into final video

## Stack Used

| Component | Status on Zo |
|---|---|
| Python 3.10 (uv) | ✅ Installed via `setup_env.py` |
| PyTorch 2.8.0 (CPU) | ✅ Installed |
| WhisperX | ✅ Installed |
| Edge-TTS | ✅ Installed (free, no API key) |
| Ollama (port 11434) | ✅ Available locally |
| FFmpeg | ✅ Available |
| Streamlit UI | ✅ Launches headless |
| demucs | ✅ Installed |

## Installation Steps

### 1. Environment Setup (Already Done)

```bash
cd /home/.z/workspaces/con_d8HQ6zgAf8q434AC/VideoLingo
python setup_env.py   # Interactively installs uv + venv + deps
```

> **Note:** `setup_env.py` runs `install.py` which is interactive (language picker, mirror selector). It fails in headless/non-TTY environments. The workaround is to pre-set `config.yaml` display_language to `"en"` before running.

### 2. Non-Interactive Install (Alternative)

If running headless, bypass `install.py` and install directly:

```bash
cd VideoLingo
uv venv --seed --python 3.10 .venv
.venv/bin/pip install torch==2.8.0 torchaudio==2.8.0 --index-url https://download.pytorch.org/whl/cpu
.venv/bin/pip install -r requirements.txt
.venv/bin/pip install -e .   # from repo root
```

### 3. Verify FFmpeg

```bash
ffmpeg -version   # Already on Zo at /usr/bin/ffmpeg
```

---

## Configuration

File: `config.yaml` (in repo root)

### For Ollama (local LLM, free)

```yaml
api:
  key: 'ollama'
  base_url: 'http://localhost:11434/v1'
  model: 'llama3.2'        # or your installed model
  llm_support_json: false

whisper:
  model: 'large-v3'
  language: 'en'
  runtime: 'local'         # uses faster-whisper on CPU/GPU

max_workers: 4
reflect_translate: true
summary_length: 8000
```

### For TTS (Dubbing) — Edge-TTS (Free)

```yaml
tts_method: 'edge_tts'

edge_tts:
  voice: 'en-US-AriaNeural'    # source language voice
  # For target dubbing:
  #   Spanish: 'es-ES-AlvaroNeural'
  #   French:  'fr-FR-HenriNeural'
  #   German:  'de-DE-ConradNeural'
  #   Chinese: 'zh-CN-XiaoxiaoNeural'
  #   Japanese: 'ja-JP-KeitaNeural'
```

### Other TTS Options

| Method | Cost | Config Key |
|---|---|---|
| Edge-TTS | Free | `edge_tts.voice` |
| Azure TTS | Paid API | `azure_tts.api_key`, `azure_tts.voice` |
| OpenAI TTS | Paid API | `openai_tts.api_key`, `openai_tts.voice` |
| GPT-SoVITS | Local GPU | `gpt_sovits.character` |
| F5-TTS | 302.ai API | `f5tts.302_api` |

---

## How to Launch

```bash
cd /home/.z/workspaces/con_d8HQ6zgAf8q434AC/VideoLingo
.venv/bin/streamlit run st.py --server.headless=true --server.port=8502
```

Access at: `http://localhost:8502` (internal) or via proxy

---

## Usage Flow

1. **Input**: Paste YouTube URL or upload video file
2. **WhisperX Transcription**: Downloads + transcribes with word-level timestamps
3. **NLP Segmentation**: AI splits text into single-line subtitle chunks
4. **Translation**: Translate → AI reflects on translation → AI adapts for dubbing
5. **Dubbing**: Generates TTS audio per segment using selected method
6. **Merge**: Burns subtitles + audio into final dubbed video

---

## Performance Notes

- **No GPU**: WhisperX runs on CPU (slow — factor of 10-30x vs GPU). A 10-min video could take 1-2 hours on CPU.
- **With Ollama**: Translation uses local LLM (free, no rate limits)
- **Edge-TTS**: Free, fast, good quality neural voices
- **Recommended for production**: Add GPU (RTX 3080+ for whisperX) or use cloud Whisper API

---

## Files

| File | Purpose |
|---|---|
| `config.yaml` | All runtime settings |
| `st.py` | Streamlit UI entry point |
| `core/_1_ytdlp.py` | YouTube download |
| `core/_2_asr.py` | WhisperX transcription |
| `core/_3_1_split_nlp.py` | NLP sentence splitting |
| `core/_4_2_translate.py` | Translation with LLM |
| `core/_5_split_sub.py` | Subtitle segmentation |
| `core/_8_2_dub_chunks.py` | TTS audio generation |
| `core/_12_dub_to_vid.py` | Final video merge |

---

## As a Solomon OS Client Service

### Offering

> "Send us any YouTube video and we'll dub it into any language — $X per minute of output video."

### Workflow to Integrate

1. **Input**: Client submits YouTube URL + target language via a web form (Zo Space route)
2. **Processing**: Trigger VideoLingo pipeline via background agent
3. **Output**: Deliver dubbed video via download link or cloud storage
4. **TTS Choice**: Edge-TTS (free, fast) keeps costs zero; upgrade to Azure/OpenAI for premium quality

### API Integration Points

- Could call `streamlit run` programmatically with config pre-set for target language
- Could hook into `core/` pipeline directly for programmatic control
- Background job queue: use Zo's `/zo/ask` API to spin up child session for each job

### Limitations for SaaS

1. **CPU-only** = slow transcription (1-2 hrs per 10-min video without GPU)
2. **No job queue** = one video at a time per instance
3. **Storage** = large video files need managed storage
4. **Scaling** = would need multiple GPU instances for parallel processing

### Recommendation

Use as a **premium manual service** ("1-week delivery") rather than instant自动化, at least until GPU is added. The transcription + translation quality is genuinely Netflix-level — that's the differentiator.
