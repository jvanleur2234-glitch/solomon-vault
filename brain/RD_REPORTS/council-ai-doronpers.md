# RD Report: Council AI (council-ai)

**Fork:** https://github.com/jvanleur2234-glitch/council-ai
**Source:** https://github.com/doronpers/council-ai
**License:** MIT
**Language:** Python (backend) + React/TypeScript (web UI)
**Stars:** ~400

## What It Is
Python + web UI advisory council system with 14 built-in personas, 15 domain presets, multi-provider support (OpenAI/Anthropic/Gemini/Ollama/LM Studio/custom). Modes: individual, synthesis, debate, vote, sequential, pattern-based. Web UI with Dieter Rams design.

## Key Features
- **14 personas:** advisors, red team, specialists with distinct traits
- **15 domain presets:** business, research, engineering, creative, legal, medical, career
- **Free option:** Local LLM via LM Studio (no API key needed)
- **Modes:** debate (multi-round), vote, synthesis, individual, sequential
- **Web search:** Tavily, Serper, Google Custom Search integration
- **Extended thinking:** reasoning mode for complex analysis
- **Text-to-speech:** ElevenLabs / OpenAI TTS
- **Full API** for programmatic use

## Solomon OS Fit
**SKILL** — Persona framework + multi-mode deliberation pattern. 14 personas could seed Hermes personality system. MIT license.

## Comparison to Existing
- More personas and domain coverage than multi-agent-council or llmcouncil
- Web UI is better than agent_council (ma-serra)
- Free local-LLM option useful for dev testing

## Action
Forked. Persona definitions are reusable for Hermes agent personalities.

**Recommendation:** SKILL — extract 14 persona definitions for Hermes personality system