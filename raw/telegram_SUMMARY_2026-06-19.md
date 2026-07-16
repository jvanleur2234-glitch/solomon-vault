# Telegram Session Summary — 2026-06-19

## Date: June 19, 2026

## Topics

### Hermes Agent v0.17 "The Reach Release" (https://x.com/i/status/2068059162349916542)

- Source: X post by Hermes Agent community
- Released June 19, 2026 (today)
- 1,475 commits, ~800 PRs, 245 contributors since v0.16.0
- GitHub: https://github.com/NousResearch/hermes-agent/releases/tag/v2026.6.19
- **Current local install: v0.14.0 — we are 3 versions behind**

#### Most relevant changes for Solomon OS:
1. **Background subagents** — `delegate_task(background=true)` returns handle, re-enters conversation when done. Replaces our synchronous /bg: handler.
2. **Automation Blueprints** — natural-language automations, no cron syntax. Renders on all surfaces. Replaces our rrule-heavy create_agent calls.
3. **`image_generate` editing** — unified image tool, replaces separate edit_image backend.
4. **Skills Hub overhaul** — connected hubs, security scan, full previews. Replaces manual SKILL.md editing.
5. **Curator prune default-on** — stale skills cleaned automatically, zero tokens on routine curation.
6. **Multi-profile multiplex in dashboard** — one gateway for all profiles.

#### Decisions made:
- Saved full RD report at `solomon-vault/brain/RD_REPORTS/hermes-v0.17-reach-release.md`
- Updated `/home/workspace/MegaPlan/HERMES_CAPABILITIES.md` (was last updated 2026-05-13, ~5 weeks stale)
- Created `~/.hermes/plugins/` and `osagnent/` backup of HERMES_CAPABILITIES.md at HERMES_CAPABILITIES.md.bak.2026-06-19

#### Pending:
- Run `hermes update --yes` when Joseph approves — update is ready but not auto-run.
- Migrate our 10 `create_agent` calls to Automation Blueprints post-update.
- Wire our `/bg:` rule to use Hermes native `delegate_task(background=true)` post-update.
- Adopt Skills Hub workflow (browser) instead of manual SKILL.md editing.

## Key Decisions
- Did NOT auto-run `hermes update --yes` — Joseph hasn't approved the update yet.
- Saved session summary.
- Updated HERMES_CAPABILITIES.md per user rule (Hermes additions require file update).

## Unresolved
- Joseph to approve running `hermes update --yes` to jump from v0.14 → v0.17.
- Whether to do the update in-place or sandbox-snapshot first (high churn: 1,693 files changed).

## Code Created / Modified
- `solomon-vault/brain/RD_REPORTS/hermes-v0.17-reach-release.md` (NEW)
- `MegaPlan/HERMES_CAPABILITIES.md` (REWRITTEN — was 5 weeks stale)
- `MegaPlan/HERMES_CAPABILITIES.md.bak.2026-06-19` (NEW — backup of pre-update state)
- `solomon-vault/raw/telegram_SUMMARY_2026-06-19.md` (NEW)
