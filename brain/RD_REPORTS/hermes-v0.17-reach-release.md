# RD Report: Hermes Agent v0.17 "The Reach Release"

**Date:** 2026-06-19
**Source:** https://x.com/i/status/2068059162349916542
**GitHub:** https://github.com/NousResearch/hermes-agent/releases/tag/v2026.6.19
**Version:** v0.17.0 (v2026.6.19)
**Released:** June 19, 2026
**Since v0.16.0:** ~1,475 commits · ~800 PRs · 1,693 files changed · 235K+ insertions · 245 contributors
**Stars:** 198K (up from 189K at v0.16.0)
**Current local install:** v0.14.0 — **we are 3 versions behind**
**Verdict:** **UPDATE + INTEGRATE** — massive drop, affects Solomon OS directly.

---

## What Changed Since v0.14.0

### v0.15 → v0.17 highlights (3 releases):

**Two new channels:**
- **iMessage via Photon** — no Mac relay needed, replaces BlueBubbles
- **Raft agent network** — wake-channel bridge, Hermes as agent on Raft.build

**Desktop app (v0.17):**
- Rebindable shortcuts, OS notifications, live subagent watch-windows
- Composer model selector, per-model presets
- Install any VS Code Marketplace theme
- Resizable terminal pane, RTL/bidi auto-detect

**Background subagents** — `delegate_task(background=true)` — runs in background, returns handle, full result re-enters conversation when done. **This is the /loop primitive we were missing.**

**Image editing** — `image_generate` now edits existing images (not just create). Make logo blue, remove background, turn sketch into render. Same tool, same pattern as `video_generate`.

**Automation Blueprints** — pick automation by name, Hermes asks for what it needs. No cron syntax. Renders natively on every surface (dashboard, CLI, TUI, messenger, docs). One definition, all surfaces.

**Cursor's Composer via xAI Grok subscription** — `grok-composer-2.5-fast` in OAuth picker. 200k context. If you have xAI Grok, you can now use Composer's coding speed with Hermes's loop.

**Full dashboard profile builder** — pick model, skills, MCP servers in browser. Multi-profile switcher, machine-wide view.

**Skills Hub overhaul** — connected hubs, Featured section, full previews, security scan on each skill.

**`memory` tool atomic batch ops** — model can free space + add entries in one call. No more fragile multi-turn dance.

**Dashboard secure login** — all token-required endpoints return 401 behind OAuth. WS auth uses dashboard token. Safer `public_url`.

**Official WhatsApp Business Cloud API** — alongside Baileys bridge. First-party, no QR-scanning bridge process.

**Rich Telegram** — Bot API 10.1 rich messages, better formatting, native markup.

**Curator cost optimization** — skill curator now prunes stale skills by default, no LLM consolidation unless opted in. **Zero tokens on routine curation.**

### Specific changes that affect us:

| Feature | What it solves for us | Priority |
|---|---|---|
| Background subagents | Our /bg: handler — was synchronous. Now native async delegation | 🔴 High |
| Automation Blueprints | Cron syntax painful — natural language works | 🔴 High |
| `image_generate` editing | Our edit_image usage — unified tool, no separate backend | 🟡 Medium |
| Skills Hub security scan | Skill vetting — pre-install audit | 🟡 Medium |
| `memory` atomic ops | PLUR memory ops — fewer failed multi-turn updates | 🟡 Medium |
| Curator cost: prune default-on | Our scheduled agents burning tokens on curation — free by default | 🟢 Lower |
| Rich Telegram | Better Telegram message rendering | 🟢 Lower |
| Multi-profile multiplex | One gateway for all profiles — less process overhead | 🟢 Lower |

---

## Action Plan

### 1. Update Hermes (priority: this week)
```
hermes update --yes
hermes doctor
```
We're 3 versions behind. Update is straightforward.

### 2. Adopt `delegate_task(background=true)` for our /bg: handler
- Currently we use /zo/ask API to spawn background Zo sessions
- v0.17 native async delegation = same model, less round-trip
- Hook into bg: rule so first attempts use Hermes native, fall back to /zo/ask

### 3. Migrate scheduled agents to Automation Blueprints
- Currently all 10 of our `create_agent` calls have cron-style rrules
- Convert to blueprints: natural-language prompts + intent, Hermes generates schedule
- Less brittle when model wants to change time/frequency

### 4. Enable curator prune (free, default-on in v0.17)
- Our `curator.consolidate: false` already saves tokens
- New prune-by-default means stale skills get cleaned automatically

### 5. Use Skills Hub dashboard browser
- Stop manually editing SKILL.md files
- Browse/install from trusted hubs (OpenAI, Anthropic, HuggingFace, NVIDIA)
- Security scan on each install

---

## Risks

- **v0.16 broke some legacy config paths** — check our `~/.hermes/config.yaml` after update
- **v0.17 changes `write_mode` tri-state → `write_approval` boolean** — default off, but check our plugins
- **New Telegram DM topic anchor requirement** — already noted in v0.16 changes, may affect our topic-aware delivery
- **Cron per-job profile support was reverted** — if we were relying on per-job profile, that path is gone

---

## Status

⏳ Pending user decision on update timing. Ready to run `hermes update --yes` when Joseph gives the go.
