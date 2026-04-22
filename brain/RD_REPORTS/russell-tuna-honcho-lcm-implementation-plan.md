# Russell Tuna Persistent Agent Stack — Implementation Plan
**Date:** 2026-04-21
**Status:** Draft

---

## The Problem

Russell Tuna currently reads brain/Services.md and brain/Business Ideas.md at session start. But between sessions:
- Context is lost
- Memory decays
- No continuity
- Cannot track what was decided vs what was executed
- No measurement of whether the agent is improving

## The Solution Architecture

```
User Input
    ↓
Russell Tuna (Hermes Agent)
    ↓
Gateway API / CLI
    ↓
Honcho Memory Layer ← persistent cross-session context injection
    ↓
LCM Measurement Layer ← audit, verify, track repeatability
    ↓
Session logs + Token analytics + Usage tracking
```

**Three layers:**
1. **Hermes Agent** — execution (Russell Tuna)
2. **Honcho** — persistent memory (dual-peer: user model + agent knowledge)
3. **Hermes-LCM** — measurement + control (proves it works)

---

## Implementation Steps

### Phase 1: Self-Host Honcho (Keep Memory Local)
Since we don't want Russell's conversations sent to third-party cloud APIs:

1. Deploy elkimek/honcho-self-hosted
   - Postgres + Redis on your Zo server
   - Works with OpenRouter/Ollama for inference
   - No data leaves your machine
2. Configure Honcho in Russell Tuna's setup:
   - recallMode: hybrid
   - writeFrequency: async
   - sessionStrategy: per-directory
   - dialecticReasoningLevel: low
   - messageMaxChars: 25000
3. Test: verify session resume picks up previous context

### Phase 2: Connect to Hermes Agent (Russell Tuna)
1. Point Russell Tuna to the self-hosted Honcho API
2. Enable honcho_conclude, honcho_context, honcho_profile, honcho_search tools
3. Remove cloud Honcho from Russell's config

### Phase 3: Add Hermes-LCM (Proof Layer)
1. Deploy Hermes-LCM (stephenschoettler/hermes-lcm)
2. Hook to Russell's sessions
3. Track:
   - Tasks completed vs promised
   - Token usage over time
   - Session continuity metrics

### Phase 4: Control Interface (Optional)
1. Deploy Hermes Control Interface dashboard
2. Manage terminals, files, sessions, cron jobs, token analytics
3. Password-gated team access
4. This becomes the "mission control" for Russell Tuna

---

## Privacy vs Capability Decision

| Option | Data stays local | LLM inference local | Setup complexity |
|--------|------------------|---------------------|-------------------|
| Self-hosted + API | ✓ | ✗ | Low |
| Self-hosted + local model | ✓ | ✓ | High (needs GPU) |
| Managed cloud (default) | ✗ | N/A | Lowest |

**Recommendation:** Self-hosted + API (OpenRouter) — data local, inference via API, balanced approach.

---

## Files to Update

- Russell Tuna's AGENTS.md or SOUL.md — add Honcho memory layer config
- Solomon OS brain/Services.md — document the stack
- HERMES_CAPABILITIES.md — update with new capabilities

---

## Dependencies

- honcho-ai SDK
- self-hosted Honcho stack (Postgres + Redis)
- Hermes Agent (already have)
- Hermes-LCM
- Hermes Control Interface (optional)

---

## Risks / Notes

1. **Honcho race condition bug** — async writeback can silently lose conclusions. Use sync writeback or monitor.
2. **Token costs** — Honcho runs dialectic inference on every conversation. Cost depends on message volume.
3. **Russell still needs instruction at session start** — Honcho helps but the brain/*.md files are still the source of truth for what Russell should focus on.
4. **This doesn't replace the brain files** — it makes Russell remember what happened between sessions, not what his goals are.

---

## Next Steps

1. Clone and test elkimek/honcho-self-hosted on the Zo server
2. Connect to Russell Tuna (existing Hermes instance)
3. Verify session continuity works
4. Add LCM layer for measurement
5. Consider the Control Interface dashboard