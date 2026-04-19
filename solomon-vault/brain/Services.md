# Services.md — Solomon OS Agent Services

*What each agent does, how to access them, and what they own.*

---

## Agent Roster

| Agent | Role | Platform | Status |
|-------|------|----------|--------|
| Zo (CEO) | Orchestration, building, strategy | Zo Computer | ✅ Active |
| Russell Tuna | Client comms, Telegram, outreach | t.me/RussellTunaBot | ✅ Active |
| Hermes | Execution layer — skills, tools | localhost:3101 | ✅ Active |
| CashClaw | SEO audits, lead generation, cold email | CLI | ✅ Built |
| JackConnect | First client agent — real estate | Custom | 🔨 In progress |
| Clicky | Watch-once workflow automation | Planned | 📋 Not started |
| Solomon Bus | Inter-agent communication | Bus daemon | ✅ Active |
| Job Runner | Persistent background jobs | Daemon | ✅ Active |

## Show Me The Money Skills (14 Business Skills)

Russell Tuna and Hermes can invoke these via `/money <skill-name>`:

| Skill | What It Does |
|-------|-------------|
| money-outreach | Cold email campaigns, B2B lead generation, sales sequences |
| money-ops | 24/7 autonomous ops, scheduling, business health scoring |
| money-finance | Revenue tracking, Stripe integration, financial reports |
| money-content | Blog posts, landing pages, email sequences, video scripts |
| money-seo | SEO audits, keyword research, GEO (AI search optimization) |
| money-ads | Google/Meta ad campaigns, spend optimization, ROAS |
| money-social | X/Twitter, LinkedIn, Reddit, Product Hunt posting |
| money-strategy | Business model stress test, pricing, GTM, competitive analysis |
| money-discover | Market research, ICP building, competitive benchmarking |
| money-product | Build + deploy MVP, Stripe payments, QA testing |
| money-quality | Code review, pre-launch QA, security audit |
| money-diagnose | Socratic business diagnosis — find WHY you're stuck |
| money-show-me | Main entry point — routes to the right skill |

---

## How to Invoke Each Agent

### Russell Tuna (Telegram)
- **Access:** t.me/RussellTunaBot
- **Commands:** `/start`, `/fork [task]`, `/help`
- **Use for:** Client-facing conversations, outreach, content posting

### Hermes (CLI)
- **Access:** `hermes --help`
- **Skills registry:** `/home/workspace/hermes-skills/`
- **Use for:** Execution tasks, tool runs, builds

### CashClaw (CLI)
- **Access:** `cashclaw audit --url <url> --tier <tier>`
- **Use for:** SEO audits, lead generation, cold email delivery
- **Billing:** Stripe integration via CLI

### JackConnect (Custom Agent)
- **Owner:** Jack Vanleur (first paying client)
- **Use for:** Real estate agent workflows — listings, follow-ups, lead intake, CMA
- **Status:** Built April 11, needs packaging for commercial sale

### Clicky (Planned)
- **Concept:** Watch Joseph do something once → record → turn into permanent workflow
- **Use for:** Democratizing workflow creation — show the AI one time, it automates forever
- **Status:** Not started — pending Phase 1

---

## Service Health Checks

```bash
# All services
cat /home/workspace/.agent/status/services.json

# Individual checks
curl -s localhost:3101/health  # Hermes
curl -s localhost:11434/api/tags  # Ollama
```

---

## Adding a New Service

1. Document the service in this file
2. Add to the agent roster table above
3. Create a health check entry in `/home/workspace/.agent/status/monitor.sh`
4. If external: register as a user service via Zo dashboard
5. Update SHARED_KNOWLEDGE.md with any new capabilities

---
## SOLOMON RING — Private Security Camera System (Local-First)

**Concept:** Privacy-first doorbell/camera security system. No cloud. No big tech. Own your footage.

**Problem it solves:**
- Ring, Nest, Arlo = all cloud-dependent. Companies can be hacked, comply with warrants, sell data.
- Solomon Ring puts all processing + storage LOCAL on a Solomon NAS or home server.

**Core features:**
- Hardware: ESP32-CAM +-compatible board running Solomon OS agent
- Local AI processing: detection, face recognition, package recognition ON DEVICE
- No outbound connections — camera only talks to local Solomon NAS
- Encrypted storage (Solomon Guardian layer)
- Solomon OS manages all cameras as agent endpoints
- Real-time alerts via Solomon Air (local push, no third party)
- App in Solomon OS to view live feed + recorded clips
- Motion zones, scheduling, sensitivity — all local config

**Architecture:**
```
ESP32-CAM (Solomon Agent) ←→ Local Network ←→ Solomon NAS (storage + AI)
                                                  ↑
                                         Solomon OS (control plane)
                                                  ↓
                                    Solomon Air (alerts to phone)
```

**Open source advantage:**
- Anyone can build Solomon Ring hardware
- Community-contributed detection models (train on your own face data, locally)
- App marketplace for specialized detection agents

**Privacy moat:** Footage NEVER leaves the home network. Even if someone hacks "Solomon" company, there's nothing to access — all data is local.

