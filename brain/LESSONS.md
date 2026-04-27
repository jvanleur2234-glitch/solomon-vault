# LESSONS.md — Solomon OS Failure Moat

> Every failure, every correction, every surprise — captured here so we never make the same mistake twice.
> Auto-distilled from `lessons.jsonl` when that pipeline is live. Until then: manually maintained.

---

## Seed Lessons — Solomon OS Specific

### Webhook & Key Redaction
- **NEVER push raw secrets to GitHub.** Stripe keys (`sk_live_*`), webhook secrets (`whsec_*`), bot tokens, API keys — always redact before any file hits a repo.
  - Pattern: `sed -i 's/sk_live_[A-Za-z0-9]*/[STRIPE_KEY]/g; s/whsec_[A-Za-z0-9]*/[WEBHOOK_SECRET]/g' $FILE`
- Save third-party secrets to [Settings > Advanced](/?t=settings&s=advanced) as named environment variables. Read from `process.env.SECRET_NAME` in scripts. Never hardcode.

### Telegram Context Continuity
- At the START of every Telegram session: read `SOLOMON_OS.md`, then explicitly surface the last session's unresolved items before diving in. Joseph should never have to paste context manually.
- After EVERY Telegram session: save a session summary to `solomon-vault/raw/telegram_SUMMARY_YYYY-MM-DD.md`. Include: date, key decisions, code created/modified, problems solved, unresolved issues, follow-up needed.

### Hermes Skill Additions
- Any time a new skill, tool, repo, or capability is added to Hermes Agent — update `solomon-vault/brain/HERMES_CAPABILITIES.md` immediately. Don't wait.
- When cloning a new repo into the workspace, log it in `HERMES_CAPABILITIES.md` under the relevant section.

### GitHub Sync After Every Session
- After every session (especially Telegram): run `/home/workspace/.agent/sync-to-github.sh` to push brain files. This keeps all Zo instances in sync.
- Also update `zo-excellence-package/SHARED_KNOWLEDGE.md` with session decisions and builds.

### Background Workers Must Be Tracked
- When launching a bg worker (via `bg:*` or `background:*`): immediately save PID + expected output path to `solomon-vault/raw/bg_workers_tracking.json`.
- If a bg worker has been running > 2 hours without output, investigate and report status to Joseph via Telegram.

### Service Health on Failure
- When a service fails, run `service_doctor` before restarting, updating, or replacing it. First diagnosis, then action.
- On crash loops: restart_space_server before creating new services.

### Pipeline Before Pitching
- Before reaching out to any prospective client: run a full CashClaw audit on their site first.Lead with audit findings, not a generic pitch.
- Before writing cold email copy: confirm their site, find their pain points via social/Google, personalize at least one line.

### Sunday Self-Review
- Every Sunday the Sunday Self-Review Agent runs. Maintain: `telegram_SUMMARY` files in `raw/`, failed experiments logged in `zo-foam`, AGENTS.md current.
- Keep `raw/` folders clean — summaries are reference material, not scratch space.

### Zo Space Route Safety
- Before replacing the homepage (`/`) or any existing public route: inspect what exists first. Never overwrite without confirming.
- For significant visual changes: use `agent-browser` to preview on localhost:3099 before surfacing to Joseph.

### Queue Task Analysis First
- When Joseph sends `queue:<URL>`: always analyze (read the repo, watch the video, scrape the article) BEFORE adding to the queue. Tell him if it's worth it, what it does, how it compares, what we'd use it for.
- Then add to queue with your analysis attached.

---

## Auto-Distillation (Future)

When the full lesson pipeline is live, these sections will be auto-populated from `lessons.jsonl`:
- `## Failures Logged`
- `## Corrections Received`
- `## Patterns Distilled`

---

*Last updated: April 27, 2026*