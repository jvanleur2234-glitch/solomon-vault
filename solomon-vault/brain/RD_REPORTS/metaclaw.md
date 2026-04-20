# RD Report: MetaClaw

**Repo:** https://github.com/aiming-lab/MetaClaw
**Stars:** ~1,400+ | **License:** MIT | **Last updated:** April 2026 (v0.4.1)

## What it is

MetaClaw is a meta-learning agent framework that sits between your LLM API and a personal AI agent (OpenClaw, CoPaw, NanoClaw, Hermes, etc.). It intercepts every conversation turn, injects relevant skills, accumulates memory across sessions, and optionally runs RL fine-tuning (via Tinker/MinT/Weaver cloud backends) during idle windows.

Three modes: `skills_only` (lightweight, no GPU), `rl` (continuous fine-tuning), `auto` (default — skills + RL + smart scheduler that only trains during sleep/idle/meetings).

## Key components

- **Skill injection proxy** — transparent OpenAI-compatible proxy at port 30000; injects top-k relevant skills at every turn
- **Skill auto-summarization** — after each session, extracts new skills automatically
- **Skill evolution** — optional LLM-powered skill improvement via OpenAI API
- **Long-term memory** — episodic, semantic, preference, and project-state memory across sessions (v0.4.0+)
- **RL training** — GRPO-style online fine-tuning via cloud backends (Tinker/MinT/Weaver), hot-swaps weights during idle windows
- **Scheduler** — calendar integration, sleep hours, keyboard idle detection; only trains when you're away

## How it compares to what we have

| Capability | Solomon OS | MetaClaw |
|---|---|---|
| Skill injection | ✅ Hermes has skill registry | ✅ More mature, auto-summarizes |
| Memory | ❌ | ✅ Cross-session episodic/semantic memory |
| RL from live chats | ❌ | ✅ Via Tinker/MinT cloud |
| Scheduler (idle/calendar) | ❌ | ✅ Built-in |
| Agent variety supported | Hermes, Russell Tuna | OpenClaw, CoPaw, NanoClaw, Hermes, +more |
| No GPU required | ✅ (Ollama) | ✅ Skills-only; RL uses cloud API |

## What we'd use it for

1. **Memory for Russell Tuna Bot** — Currently Russell has no cross-session memory. MetaClaw's memory layer could give him persistent context across conversations (preferences, project state, ongoing tasks).

2. **Skill evolution** — Instead of manually writing skills, MetaClaw auto-generates them from failed/lengthy conversations. Could feed directly into Hermes skill registry.

3. **Hermes as a claw_type** — Hermes is already listed as a supported agent. Could wire MetaClaw → Hermes for RL-enhanced skill injection on our own agent.

4. **Goal-Driven workload** — Complex multi-week tasks (compiler builds, DB implementations) could benefit from MetaClaw's persistent agent loop + memory.

## Integration complexity

- **Skills-only mode:** Low. `pip install metaclaw`, `metaclaw setup`, `metaclaw start`. No GPU needed. Works with any OpenAI-compatible endpoint (including Ollama if wrapped).
- **RL mode:** Medium. Requires Tinker/MinT/Weaver cloud account and API key. RL happens on remote GPU clusters, not local.
- **Memory:** Medium-low. Works standalone or as sidecar service. Storage is local (`~/.metaclaw/memory`).
- **Hermes integration:** Not tested. The README mentions Hermes support but it's in the CLAW_TYPE table — needs verification.

## Risks / concerns

- MetaClaw is designed for a *single* human using their own personal agent. It doesn't have multi-tenant or team-collaboration features.
- The RL path (even cloud-based) adds cost and complexity. For Solomon OS's use case, skills-only mode may be enough.
- Clifford, our current Hermes setup, is pretty different from standard OpenClaw. Hermes `claw_type` integration might need custom work.

## Recommendation

**SKILL / INTEGRATE** — Medium priority.

MetaClaw's memory system is the most valuable piece for Solomon OS. Russell Tuna Bot currently has no persistent cross-session memory — every conversation starts from scratch. Adding MetaClaw's memory layer (even just skills-only + memory, no RL) would be a meaningful upgrade.

The skill evolution is also compelling — auto-generating skills from conversations rather than manual authoring.

**Action:** Install `metaclaw` in skills-only mode, wire it to Russell Tuna Bot's Ollama endpoint, and test memory persistence across sessions. Don't enable RL until we have a clear use case and budget for Tinker/MinT API calls.
