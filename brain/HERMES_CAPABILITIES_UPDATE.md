## SkillClaw Integration (April 21, 2026)
- **Repo:** github.com/AMAP-ML/SkillClaw (4.2K stars, MIT)
- **Location:** /home/workspace/SkillClaw/
- **What it does:** Local proxy that intercepts Hermes → LLM requests, records sessions, evolves skills in background. Skills auto-deduplicate, auto-improve, cross-pollinate across sessions.
- **Integration status:** Cloned + installed. Client proxy + evolve server ready. Hermes config backup created. Setup pending (interactive).
- **Spec:** `solomon-vault/brain/SKILLCLAW_HERMES_INTEGRATION.md`
- **For Solomon OS:** Wire into Hermes S1/S2/S3 → skills auto-evolve across all agent sessions. Multi-agent unified skill library.

## Phantom Self-Evolution (April 21, 2026)
- **Repo:** github.com/ghostwright/phantom (1.27K stars, Apache 2.0)
- **Location:** /home/workspace/phantom/
- **What it does:** AI coworker with its own computer. 27K lines TS, 822 tests, v0.18.2. Self-evolution engine: 6-step Observe→Critique→Delta→Validate→Apply→Consolidate loop.
- **Key patterns integrated into Solomon OS:**
  - solomon-evolution/evolution.py — 6-step pipeline
  - solomon-config/ — constitution, persona, user-profile, domain-knowledge, strategies/
  - Phantom uses Sonnet 4.6 as cross-model judge (avoids self-enhancement bias)
- **Spec:** `solomon-vault/brain/PHANTOM_SELF_EVOLUTION_INTEGRATION.md`