# RD_REPORT: Clawe

**Repository:** https://github.com/getclawe/clawe  
**Stars:** 719 | **Forks:** 84 | **License:** AGPL-3.0  
**Last Updated:** Feb 22, 2026  
**Type:** Multi-agent coordination system (Trello for AI agents)

---

## What It Does

Clawe is a multi-agent coordination system powered by OpenClaw. It lets you deploy a team of AI agents with distinct roles, personalities, and scheduled heartbeats. Each agent has its own workspace, and they coordinate through a Kanban-style task board with a web dashboard.

Key components:
- **squadhub**: Gateway that runs all agents
- **watcher**: Notification delivery + cron scheduling
- **clawe**: Web dashboard (squad status, task board, agent chat)
- **Convex**: Backend database for agents, tasks, notifications, activities

Pre-configured agents: 🦞 Clawe (Squad Lead), ✍️ Inky (Content Editor), 🎨 Pixel (Designer), 🔍 Scout (SEO)

---

## How It Compares to What We Have

**vs. Solomon OS (Hermes):**  
- Hermes is a single 24/7 AI agent with full business context, integrated into Telegram
- Clawe is a multi-agent team with cron-based scheduling and a web dashboard
- Clawe has no Telegram integration built-in (requires OpenClaw setup)

**vs. Mercury:**  
- Mercury focuses on cost-controlled research and shell security
- Clawe focuses on team coordination and task management
- Different architectures entirely

---

## What We'd Use It For

1. **Multi-agent task delegation** — Instead of one agent handling everything, split work across specialized agents (content, SEO, design)
2. **Scheduled automation** — Heartbeat-based agents that wake up on cron to check for work
3. **Task board for AI agents** — Kanban-style task management where agents claim and complete tasks
4. **Team dashboard** — Web UI to monitor all agent activity in one place

---

## Integration Notes

- Requires Docker + Docker Compose
- Needs Convex account (free tier works)
- API keys managed via UI (Anthropic, OpenAI)
- AGPL-3.0 license — must release modifications if distributing

---

## Recommendation: INTEGRATE

**Why:** Clawe fills a gap in Solomon OS — structured multi-agent task coordination with a proper dashboard. It could become the backend task queue for Hermes, with agents waking on schedules to process work.

**Action:** 
1. Clone to `/home/workspace/Clawe/`
2. Run the Docker setup
3. Configure 4 agents matching Solomon OS workflows (sales, research, content, support)
4. Sync with Hermes via shared files or API

This is a FORGE-worthy addition — the architecture aligns well with Solomon OS needs.