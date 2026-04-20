# RD Report: 1Panel — VPS Control Panel with Native AI Agents

**Date:** 2026-04-20
**Source:** [GitHub 1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel) — 35.1K stars, GPL-3.0
**Task:** 1panel-001

---

## What It Is

**1Panel** = Modern, open-source VPS control panel with **native AI agent support built in**. The only control panel with Ollama + OpenClaw agents running in the dashboard. 2M+ users worldwide.

**One-line install:**
```bash
bash -c "$(curl -sSL https://resource.1panel.pro/v2/quick_start.sh)"
```

**Stack:** Go 65.5% + Vue 34.5% — modern, actively developed (5,003 commits)

---

## Why This Changes Everything

| | 1Panel | cPanel | Plesk | aaPanel | Webmin |
|--|--|--|--|--|--|
| Free & open source | ✅ | ❌ | ❌ | Partial | ✅ |
| **Native AI agent runtime** | ✅ | ❌ | ❌ | ❌ | ❌ |
| One-click app marketplace | ✅ 165+ | ❌ | ❌ | ✅ | ❌ |
| Modern UI (post-2020) | ✅ | ❌ | ❌ | Partial | ❌ |
| Docker management | ✅ | ❌ | ❌ | ❌ | ❌ |

**Key features:**
- AI Agent Runtime: Ollama + OpenClaw agents from dashboard
- One-click website + SSL + domain binding
- 165+ app marketplace (Nextcloud, Bitwarden, Umami, NocoBase)
- Docker container management (visual UI)
- Firewall, fail2ban, WAF, audit logs
- Backup to AWS S3 / Cloudflare R2 / local

**Pro Edition ($80/yr):** Unlimited AI agents, multi-node, custom branding

---

## Atlas OS Bundle Strategy — THIS IS THE ANSWER

The Atlas OS bundle strategy said: "Find a server management layer we can bundle." **1Panel IS that layer.**

Instead of building our own VPS control panel from scratch, we bundle 1Panel + Solomon OS together:

```
Customer installs 1Panel (one command)
        ↓
1Panel auto-installs Solomon OS as a managed service
        ↓
1Panel dashboard = Solomon OS control panel
        ↓
AI agents (Ollama + OpenClaw) run alongside our agents
        ↓
JackConnect is a 1Panel app in the marketplace
        ↓
Every 1Panel user = potential Solomon OS customer
```

---

## Recommendation

**FORGE — CRITICAL PRIORITY**

This is the missing piece for the Atlas OS bundle strategy. Clone: `git clone https://github.com/1Panel-dev/1Panel /home/workspace/1panel/`

**Actions:**
1. Clone 1Panel ✅
2. Write integration spec for `1panel + solomon-os`
3. Create `1panel-skill` in Hermes
4. Pitch: "Solomon OS is the AI layer for 1Panel"

---

## Link Fit

★★★★★ — #vps-control-panel #ai-agents #atlas-bundle #self-hosted #hermes #solomon-air

*Last updated: 2026-04-20*