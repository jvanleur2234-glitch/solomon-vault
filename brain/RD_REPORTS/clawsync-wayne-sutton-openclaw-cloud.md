# RD Report: ClawSync by Wayne Sutton — Direct Competitor Analysis

**Date:** 2026-05-01
**Type:** Competitor Product — DIRECT OVERLAP
**Recommendation:** SKILL — clone, study architecture, steal Soul Document pattern

---

## What It Is

**ClawSync** = OpenClaw for the cloud. A multi-agent AI platform built on Convex, with a clean React UI and full enterprise feature set. MIT license. Author: Wayne Sutton (@waynesutton).

5-month-old repo with impressive feature velocity.

---

## Core Architecture

```
Frontend: React + Vite (src/)
Backend: Convex (convex/)
Database: Convex native (real-time, auto-migration)
Auth: WorkOS AuthKit (planned), SyncBoard password hash
Storage: Convex native OR Cloudflare R2 (optional)
AI Providers: Anthropic, OpenAI, xAI (Grok), OpenRouter
Memory: Supermemory AI (persistent cross-session)
Browser: Stagehand (browser automation)
Scraping: Firecrawl (durable caching)
```

---

## Feature Breakdown

### Multi-Agent System
- Multiple agents simultaneously
- Each with independent: config, skills, MCP servers, memory
- Agent Controls: auto-run, pause, restart, single task, think-to-continue
- Agent-to-Agent communication and delegation

### Soul Documents
- Shared personality documents
- Can power one OR many agents
- This is the equivalent of our SOUL.md pattern — key differentiator for JCPaid personas

### SyncBoard Admin
- Private dashboard (password-protected)
- Manage agents, souls, skills, integrations
- X (Twitter) config panel
- Media/file manager
- Stagehand browser automation
- Firecrawl scraping
- AI Analytics with weekly cron
- Research projects
- Supermemory config

### Public Chat UI
- Real-time streaming
- Agent selector
- Landing page with tweets + activity feed

### Skills System
- Template skills (pre-built patterns)
- Webhook skills (API integrations)
- Code skills (custom convex/agent/skills/)
- Marketplace for external registries

### Channel Integrations
- Telegram, Discord, WhatsApp, Slack, Email
- X (Twitter) — read, reply, post, auto-reply mentions

### Memory & Research
- Supermemory integration (persistent cross-session)
- Agent Research — competitive, topic, real-time X research
- Weekly AI analytics with anomaly detection

### Design System
- Geist fonts (Vercel)
- Token-based CSS (`src/styles/tokens.css`)
- Key tokens: `--bg-primary: #f3f3f3`, `--bg-secondary: #ececec`, `--interactive: #ea5b26`

---

## Competitive Analysis

| Feature | ClawSync | JCPaid (ours) |
|---------|----------|---------------|
| Backend | Convex (real-time SaaS) | Hermes + here.now |
| Memory | Supermemory (cloud) | here.now (permanent, local) |
| Desktop | None | holaOS desktop |
| Skills | Template/webhook/code | Hermes 1,223 skills |
| Price | Unknown | Flat $299/mo |
| License | MIT | MIT |
| Channels | Telegram/Discord/WhatsApp/Slack/Email | Same |
| Browser | Stagehand | Browserclaw |

**Our advantages:**
- here.now = permanent memory (not cloud-dependent)
- holaOS desktop = clients see their AI running like a real PC
- Flat $299 (no per-feature pricing)
- Hermes 1,223 skills already installed

**Their advantages:**
- Convex = real-time, zero-config backend deployment
- More polished UI out of the box
- Agent-to-agent communication built-in
- Weekly analytics cron already working

---

## Soul Document Architecture (KEY STEAL)

ClawSync's "Soul Documents" = SOUL.md pattern but:
- Stored in Convex database (not filesystem)
- Can be shared across multiple agents
- Editable via SyncBoard UI
- Powers agent personality without code changes

**For JCPaid:** This is the same as our SOUL.md → personas pattern. We can:
1. Store SOUL.md in here.now (permanent) instead of Convex (cloud)
2. Push Soul Documents to clients' holaOS desktops
3. Make personality editable via web dashboard

---

## What To Steal

1. **Soul Document architecture** → SOUL.md as shared personas for JCPaid
2. **Analytics cron pattern** → weekly report generation for client dashboards
3. **Agent Controls UI** → run/pause/restart/think-to-continue for JCPaid fleet
4. **SyncBoard layout** → admin dashboard pattern for client management
5. **tokens.css system** → Geist font + color tokens for JCPaid frontend

---

## License

MIT — full freedom to study, fork, adapt.

---

## Links

- Repo: https://github.com/waynesutton/clawsync
- Convex backend: `convex/` directory
- Frontend: `src/` directory
- Design tokens: `src/styles/tokens.css`
- Default soul: `content/soul.md`
