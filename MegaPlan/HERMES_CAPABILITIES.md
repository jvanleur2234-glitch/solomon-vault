# Hermes Capabilities
**Last Updated: April 17, 2026**

## JCPaid Universal Self-Improvement Loop (April 18, 2026)

The same adversarial loop from Solomon Guardian applies to ALL of JCPaid:

**5 Loops, 1 Infrastructure:**

| Loop | What it tracks | What improves |
|------|---------------|---------------|
| Business Growth | Client acquisition, pricing, channels | Revenue compounding |
| Content Creation | Views, clicks, watch time, CTAs | Content performance |
| Sales Outreach | Open rates, reply rates, close rates | Close rate improving |
| Product Building | Feature usage, errors, build speed | Build velocity |
| Strategy | Win/loss on initiatives, prediction accuracy | Prediction accuracy |

**Technical layer powers all 5:**
Icarus (shared memory) → Evolver (analyzes patterns) → Hermes (applies fixes) → agentic-stack (graduates lessons) → All loops compound together

**Full doc:** `solomon-vault/brain/SELF_IMPROVEMENT_LOOP.md`
- **Location:** `/home/workspace/solomon-vault/brain/SELF_IMPROVEMENT_LOOP.md`

---

## JCPaid Pre-Install Stack (April 18, 2026)

The philosophy: JCPaid = Best of breed pre-installed + AI layer + user makes it their own. The default experience is already better than most people's current setup. Then customize from there.

**Reference catalog:** https://selfh.st/apps/ — self-hosted alternatives directory by Ethan Sholly. Use license filters to find MIT/Apache/AGPL options for pre-install batch.

### The Pre-Install Batch

**Communication:**
- Matrix/Element — E2E encrypted messaging, bridges to Telegram/Signal
- Jitsi — video calls, no Zoom needed

**File & Docs:**
- NextCloud — Google Drive replacement, self-hosted
- CollabOS or OnlyOffice — collaborative docs/spreadsheets/slides

**Passwords & Security:**
- Vaultwarden — Bitwarden-compatible, lightweight, runs on $5 VPS

**VPN & Networking:**
- WireGuard — modern VPN protocol, kernel-level, very fast
- Tailscale — zero-config VPN mesh, works through NATs

**AI Layer (Solomon OS on top):**
- Ollama — local LLM inference, free, no API costs
- browser-harness — self-healing browser automation for AI agents
- Paseo — cross-device AI agent control from phone

**Email:**
- Thunderbird — full email client, IMAP/SMTP
- Resend API — send emails via API, 3K free/month

**Calendar & Tasks:**
- Cal.com — Calendly alternative, self-hosted, open source

**Notes & Knowledge:**
- Obsidian — local-first markdown notes
- Cabinet — git-backed KB with AI agents + Kanban

**Video:**
- Jitsi Meet — self-hosted video conferencing
- PeerTube — YouTube alternative, federated

### License Priority
MIT > Apache 2.0 > AGPL > GPL. Avoid GPL for SaaS-like products (share-alike传染). AGPL fine for internal tooling. MIT/Apache are always safe.

### Build Approach
1. Pick one category (e.g. passwords/VPN) and build a one-command installer
2. Test on a fresh VM to verify it works
3. Layer in the AI automation for that category
4. Repeat for each category
5. Package as a JCPaid OS image

## Agency Agents — 810K Stars AI Employee Templates (April 18, 2026)
- **Repo:** github.com/msitarzewski/agency-agents — 810K stars, MIT License
- **Cloned:** /home/workspace/agency-agents/ (full repo, 21 categories, 140+ roles)
- **Key templates copied:** brain/AGENT_TEMPLATES/ (10 highest-value roles for AI Staffing Agency)
- **What it does:** 147 specialized AI agents across 12 divisions (engineering, design, marketing, sales, product, QA, support, etc.) — each with full personality, workflow, success metrics, and production-ready deliverables. Works with Claude Code, Cursor, Gemini CLI, Windsurf, OpenCode.
- **Business fit:** DIRECT — these are the exact "AI workers" businesses hire from an AI staffing agency. Map client needs → select right agent template → Russell Tuna /fork delivers the work.
- **For AI Staffing Agency:** `sales-outbound-strategist` for lead gen, `marketing-seo-specialist` for SEO work, `sales-account-strategist` for upsells, `support-support-responder` for customer service, etc.
- **Next step:** Build Telegram Role Selector so clients can pick an AI worker by name/need
- **LINK fit:** ★★★★★ — #ai-staffing #ready-to-deploy #business-revenue

## agentic-stack (April 17, 2026)
- **Repo:** codejunkie99/agentic-stack — 1.7K stars, MIT
- **Forked:** jvanleur2234-glitch/solomon-os-agentic-stack
- **What it does:** Portable `.agent/` folder with 4 memory layers (working/episodic/semantic/personal), progressive skill loading, host-agent review protocol (graduate.py/reject.py), adapters for Claude Code/Cursor/Windsurf/Hermes/OpenCode/OpenClient
- **KEY PATTERN:** Host agent reviews AI-generated lessons. No unattended reasoning. No provider lock-in.
- **LINK fit:** ★★★★★ — #memory #self-improvement #hermes #solomon-os

## Anything Analyzer (April 17, 2026)
- **Repo:** Mouseww/anything-analyzer — MIT license
- **Forked:** jvanleur2234-glitch/anything-analyzer
- **What it does:** All-in-one packet capture (CDP browser + MITM proxy) + AI auto-analysis (API reverse, security audit, JS crypto extraction). Built with Electron + React + Python MITM + MCP server
- **Use for:** Reverse engineer any app/website API → build integrations → resell access. Protocol analysis as a service.
- **LINK fit:** ★★★★★ — #protocols #integrations #revenue

## egregore (April 17, 2026)
- **Repo:** egregore-xyz/egregore — shared mind for AI teams
- **What it does:** Team AI that remembers everything across sessions. Shared episodic + semantic memory across all agents.
- **Use for:** Multi-agent teams that need shared context. Every agent contributes to a common knowledge base.
- **LINK fit:** ★★★★☆ — #multi-agent #shared-memory

## production-saas-starter (April 17, 2026)
- **Repo:** moasq/production-saas-starter — Next.js 16 + Go 1.25 B2B SaaS
- **Forked:** jvanleur2234-glitch/solomon-production-saas-starter
- **What it does:** Enterprise SaaS boilerplate: Next.js 16, Go Gin, PostgreSQL+pgvector, Docker, Stytch auth, Polar.sh billing, RAG pipeline
- **Use for:** Spin up paid B2B SaaS in days. Stytch B2B SSO + Polar.sh = full billing stack
- **LINK fit:** ★★★★☆ — #saas #starter #revenue

## Runline — 188 API Plugins for AI Agents (April 17, 2026)
- **Repo:** Michaelliv/runline — npm package
- **Installed:** `npm install -g runline`
- **What it does:** JavaScript sandbox (QuickJS WASM) that gives agents safe execution of 188 API plugins. Plugins run outside sandbox with full Node.js access. `runline exec 'return await stripe.customer.list()'`
- **Plugins:** github, stripe, hubspot, salesforce, airtable, notion, linear, slack, sendgrid, twilio, shopify, clickup, jira, close, bullhorn + 178 more
- **Russell Tuna Integration:** `/runline` command added to russell_bot.py — any of 188 API actions via Telegram
- **Use for:** API actions without writing integration code. Every API = one JS line.
- **LINK fit:** ★★★★★ — #integrations #ai-staffing #plugins

## CloudBrowser (April 17, 2026)
- **Location:** jack-connect/cloud-browser/
- **What it does:** Hyperbrowser equivalent — AI-controlled browser with Playwright CDP + Ollama agentic reasoning. Create session → submit task → get results. Local-only, no API keys.
- **For JackConnect:** Browser AI that can navigate MLS, CRM, email for real estate agents
- **Status:** API server ready on port 9876

## Cabinet (April 17, 2026)
- **Location:** jack-connect/cabinet/
- **What it does:** AI-first startup OS — knowledge base + AI agents + scheduled jobs + Kanban boards. Git-backed history. Self-hosted. Drop HTML apps in any folder.
- **For JackConnect:** Jack's personal AI team brain — all agents, all memory, all work in one place

## Cognee Memory Layer (April 17, 2026)
- **Location:** jack-connect/cognee/
- **What it does:** Structured memory for LLMs — graph + vector search over any data. Pipeline: add text/files/tables → cognify → search
- **For JackConnect:** Long-term memory for Jack's real estate business — client history, deal notes, market data

## Watch Once Engine (April 17, 2026)
- **Location:** jack-connect/watch-once/
- **What it does:** Record a workflow once → AI extracts the steps → generates autoMate script → permanent automation
- **For JackConnect:** "Watch once, automate forever" — Jack does CMA once → system learns → never manually again

## JackConnect Dashboard (April 17, 2026)
- **Location:** jack-connect/jack-dashboard/
- **What it does:** Homepage替代方案 — 50+ service widgets (Ollama, Pinecone, Home Assistant, Plex, etc.)
- **For JackConnect:** Jack's personal ops dashboard — one URL, everything he needs to run his AI team

## Facebook Ads MCP Server (April 17, 2026)
- **Repo:** gomarble-ai/facebook-ads-mcp-server — MIT license
- **Cloned:** /home/.z/workspaces/con_d8HQ6zgAf8q434AC/facebook-ads-mcp-server/
- **Forked:** jvanleur2234-glitch/facebook-ads-mcp-server
- **What it does:** MCP server wrapping Meta Graph API v22.0. Tools: list_ad_accounts, get_adaccount_insights, get_campaign_insights, get_adset_insights, get_ad_insights, get_activities, + full CRUD on campaigns/ad sets/ads/creatives.
- **Authentication:** `--fb-token YOUR_META_ACCESS_TOKEN`
- **For Solomon OS:** Russell Tuna reads client ad performance data → optimization reports for AI Staffing Agency. Hermes can pull Facebook Ads data directly via MCP router.
- **LINK fit:** ★★★★☆ — #facebook-ads #meta #insights #analytics #ai-staffing

## AI-penetration-testing — OWASP LLM Top 10 Toolkit (April 18, 2026)
- **Repo:** github.com/Mr-Infect/AI-penetration-testing — 195 stars, Ethical Hacking License
- **Forked:** jvanleur2234-glitch/AI-penetration-testing
- **What it is:** AI/ML/LLM pentesting toolkit. OWASP LLM Top 10 vulnerability framework (prompt injection, data exfil, supply chain, poisoning, prompt leakage, vector attacks, etc.).
- **JCPaid fit:** PERFECT for Solomon Guardian. OWASP LLM Top 10 = the vulnerability checklist the Guardian tests against. Red team techniques from this repo directly feed the Guardian Attack Team.
- **Status:** Forked ✅ — RD report: `solomon-vault/brain/RD_REPORTS/ai-pentest.md`

## SOLOMON GUARDIAN — Full Self-Defense + Self-Improvement Loop (Wired April 18, 2026)

The complete adversarial loop — all pieces now connected:

```
AI-pentest (Red Team methodology)
         ↓
Guardian Attack Team (detects vulnerabilities)
         ↓
Icarus (shared memory, cross-agent signal)
         ↓
Evolver (scans error logs → Gene selection → GEP prompt)
         ↓
Hermes (applies fix, review mode)
         ↓
agentic-stack (graduate/reject)
         ↓
Solomon Bus → push update to all agents
         ↓
Next attack = harder to breach
```

**Key integrations:**
- AI-pentest OWASP LLM Top 10 → Guardian vulnerability checklist
- Evolver Gene library → automatic fix generation
- Icarus → shared memory layer across all Solomon OS agents
- Guardian log (append-only, cryptographically signed) → audit trail + rollback
- **Self-update loop:** New threat intel → analyze → extract IOCs → update detection → validate → deploy → block + isolate + alert + learn
- **Attack classes handled:** Malware, ransomware, rootkits, trojans, worms, zero-days (behavioral), DDoS, phishing, credential theft, privilege escalation, lateral move, LLM prompt injection, vector store attacks, model poisoning
- **Status:** Full loop operational. Evolver + Icarus + AI-pentest + agentic-stack all wired in.

## Be Like You! OS — Mobile OS Built on Solomon OS (April 18, 2026)
- **Full architecture**: `/home/workspace/BE_LIKE_YOU_OS.md`
- **Three-layer stack**:
  - Layer 1: vPhone OS — LineageOS fork + VoIP (Linphone/SIP/WebRTC) + Solomon Air as dialer + AI launcher
  - Layer 2: Solomon OS Platform embedded on-device (Solomon Air + JackConnect + Hermes + Solomon Bus + Ollama)
  - Layer 3: Be Like You! Tube — human-only video platform (AI content PROHIBITED)
- **Solomon Guardian** embedded at kernel level of the OS
- **Build path**: Phase 1 (Android APK with root — months 1-3) → Phase 2 (LineageOS ROM fork — months 4-9) → Phase 3 (video platform — Year 2)
- **Revenue**: Carrier pre-install ($2-5/device) + enterprise ($50/device/year) + Solomon OS platform ($9/mo) + Be Like You! Tube (40% ad rev + PPV)
- **What makes it revolutionary**: AI IS the interface — no app grid, chat with your phone. Free global calling via VoIP. Solomon Guardian security built in.
- **vphone-cli reference**: github.com/Lakr233/vphone-cli — virtual phone provisioning via SIP/VoIP
- **LINK fit**: ★★★★★ — #mobile-os #solomon-os #open-source #voip #security

## SDR Cellular Network — Private Cell Network (April 18, 2026)

**Concept:** Build your own low-cost private cellular network. No carrier fees, no government eavesdropping.

**What it enables:**
- Private 2G/3G/4G cell tower
- SMS/calls within your network
- Complete privacy from carriers and governments
- Runs on SDR hardware ($20 USB dongle)

**Why it matters for JCPaid:**
- Solomon OS / Be Like You! OS = privacy-first AI phone OS
- SDR cellular = the ultimate privacy moat
- Users can have their OWN cell network, completely off-grid

**For Be Like You! OS:**
- Layer between vPhone VoIP and carrier independence
- When combined with Tor/mesh networking = truly untraceable communication
- This is the endgame for the "free global calling" vision

**What we'd need to add:**
- OpenBTS or YateBTS (open source BTS software)
- USRP or RTL-SDR hardware
- VoIP gateway integration

**Privacy moat:** Being your own carrier = no cell carrier surveillance, no SIM tracking, no IMSI catcher vulnerability.

## Be Like You! OS — N.O.M.A.D. Fork (April 19, 2026)
- **Repo:** github.com/jvanleur2234-glitch/be-like-you-nomad (Apache 2.0)
- **Forked from:** Crosstalk-Solutions/project-nomad (13K stars)
- **What it is:** Project N.O.M.A.D. + Solomon OS integrated as a Docker sidecar. One Postgres database replaces Redis, RabbitMQ, Elasticsearch, Pinecone, Snowflake.
- **Components added to N.O.M.A.D.:**
  - Hermes agent (agent brain)
  - Russell Tuna (Telegram AI)
  - Icarus (cross-agent memory layer)
  - Evolver (self-improvement engine)
  - Solomon Bus (job queue via Postgres SKIP LOCKED)
  - Solomon Air (VoIP + SDR)
  - Solomon Guardian (security monitor)
  - Solomon Browser (AI browser agent)
  - Full-text search (Postgres TSvector + GIN)
  - Vector search (Postgres pg_vector)
- **Architecture:** N.O.M.A.D. Command Center (existing) + Solomon OS sidecar (new Docker containers)
- **Unified Postgres schema:** All agents share ONE database. Functions: `dequeue_job()`, `find_similar_memories()`, `search_knowledge()`, `queue_stats()`
- **Status:** Forked, pushed to GitHub. Ready to build the integration spec.
- **Full spec:** `be-like-you-nomad/SPEC.md`
- **Docker compose:** `be-like-you-nomad/solomon/docker-compose.yaml`
- **Postgres schema:** `be-like-you-nomad/solomon/postgres-schema.sql`

## Project N.O.M.A.D. — Offline Knowledge Server (April 18, 2026)

**Concept:** Build your own offline knowledge server. No internet required.

**What it enables:**
- Offline access to all your knowledge base, documents, and tools
- Complete independence from the internet
- Runs on a local server ($20 Raspberry Pi)

**Why it matters for JCPaid:**
- Solomon OS / Be Like You! OS = privacy-first AI phone OS
- N.O.M.A.D. = the ultimate offline moat
- Users can have their OWN knowledge base, completely off-grid

**For Be Like You! OS:**
- Layer between vPhone VoIP and carrier independence
- When combined with Tor/mesh networking = truly untraceable communication
- This is the endgame for the "free global calling" vision

**What we'd need to add:**
- OpenBTS or YateBTS (open source BTS software)
- USRP or RTL-SDR hardware
- VoIP gateway integration

**Privacy moat:** Being your own carrier = no cell carrier surveillance, no SIM tracking, no IMSI catcher vulnerability.

## ClawLess — Browser-Based AI Agent Runtime (April 18, 2026)

**Concept:** Run AI agents directly in the browser, no server required.

**What it enables:**
- AI agents that work on any device, anywhere
- No need for a server or internet connection
- Runs on a local browser tab

**Why it matters for JCPaid:**
- Solomon OS / Be Like You! OS = privacy-first AI phone OS
- ClawLess = the ultimate offline moat
- Users can have their OWN knowledge base, completely off-grid

**For Be Like You! OS:**
- Layer between vPhone VoIP and carrier independence
- When combined with Tor/mesh networking = truly untraceable communication
- This is the endgame for the "free global calling" vision

**What we'd need to add:**
- OpenBTS or YateBTS (open source BTS software)
- USRP or RTL-SDR hardware
- VoIP gateway integration

**Privacy moat:** Being your own carrier = no cell carrier surveillance, no SIM tracking, no IMSI catcher vulnerability.

## SELF-IMPROVEMENT LOOP — FULLY WIRED (April 19, 2026)

All 4 layers + execution engines now connected:

### The Complete Self-Improvement Loop

```
Guardian detects attack (eBPF, behavioral AI, threat intel feeds)
        ↓
Icarus fabric_write (attack signal → all agents instantly)
        ↓
Evolver scans error logs → selects matching Gene (fix template)
        ↓
Evolver emits GEP prompt → applies fix to source code/config
        ↓
Human-in-loop review mode (--review flag, whitelist-only, 180s timeout)
        ↓
Approved → deployed. Rejected → logged for manual review.
        ↓
agentic-stack graduates/rejects the lesson (graduate.py/reject.py)
        ↓
Icarus fabric_write (fix deployed → system-wide immunity update)
        ↓
Next interaction = smarter from all past mistakes
```

### Component Roles

| Component | Role |
|-----------|------|
| **Guardian** | Attack Team (probes) + Defense Team (responds) — runs 24/7 adversarial loop |
| **Icarus** | Cross-agent shared memory — one agent learns it, every agent recalls it |
| **Evolver** | Self-evolution engine — scans logs, selects Gene, emits GEP, applies fix |
| **agentic-stack** | Lesson review protocol — graduate.py approves, reject.py flags for rework |
| **Hermes** | Applies fixes, runs skills, reports outcomes |
| **Solomon Vault brain/** | COLD + Identity layers (where lessons are permanently stored) |

### Safety
- Evolver `--review` mode: human-in-loop holds every change
- Whitelist-only commands (no rm -rf, no chmod 777)
- 180s timeout per fix
- Reviewer gets: error description, Gene used, GEP prompt, diff preview
- agentic-stack final review before lesson is promoted to verified pattern

### Quality Gates
- Unverified → stage in `cold/staging/` until 2+ confirmations OR explicit user approval
- Verified → promote to `cold/lessons/` (permanent immunity)
- Shared pool → anonymized techniques + anti-patterns for cross-user learning

### Build Status
| Layer | Status |
|-------|--------|
| HOT (current session state) | ✅ Per-user directories at `solomon-vault/users/{user-id}/` |
| COLD (lessons learned) | ✅ Solomon Vault brain/ + Icarus fabric/ |
| Shared (anonymized pool) | ✅ `solomon-vault/shared/` |
| Identity (who user is) | ✅ Solomon Vault brain/NORTH_STAR.md |
| Evolver (Gene selection + GEP) | ✅ Forked, RD report, HERMES_CAPABILITIES.md |
| Icarus (cross-agent memory) | ✅ Forked, RD report, HERMES_CAPABILITIES.md |
| agentic-stack (lesson review) | ✅ Forked, HERMES_CAPABILITIES.md |
| Guardian (adversarial loop) | ✅ SOLOMON_GUARDIAN.md v2 with Evolver/Icarus wired in |
| Sunday Self-Review Agent | ✅ Weekly audit loop |

---

### Build Phases

Solomon OS has a continuous self-improvement architecture across 4 layers:

### The 4 Memory Layers
| Layer | What | Scope | Latency |
|-------|------|-------|---------|
| HOT | Current session state | Per-user | Sync (fast) |
| COLD | Lessons learned, verified patterns | Per-user | Async |
| Shared | Anonymized techniques + anti-patterns | Cross-user | Read-only |
| Identity | Who the user is (soul, values, goals) | Per-user | Slow-changing |

### The Self-Improvement Cycle (every interaction)
1. **Respond** — use HOT + Identity context
2. **Log result** — what happened
3. **Evaluate** — did it work?
4. **Update** — reinforce success / diagnose failure
5. **Propagate** — if shareable, anonymize and add to shared pool
6. **Compound** — next session smarter from all past sessions

### Build Phases
- **Phase 1 (WEEKS 1-2):** Per-user memory directories, context loader, session summarizer
- **Phase 2 (WEEKS 2-3):** Feedback signal capture (explicit + implicit), quality gates
- **Phase 3 (WEEKS 3-5):** Cross-user knowledge sharing with anonymization layer
- **Phase 4 (WEEKS 4-6):** Identity evolution with drift detection
- **Phase 5 (ONGOING):** Continuous compounding — daily review, weekly audit, monthly deep-dive

### Privacy Model
- Users CAN share: techniques, workflow patterns, tool configs, anti-patterns (all anonymized)
- Users CANNOT share: conversations, client data, raw memory files
- Users can OPT-OUT of shared pool contributions
- Users can revoke contributions at any time

### Shared Knowledge Pool
Location: `/home/workspace/solomon-vault/shared/`
- `techniques/` — what works (anonymized success patterns)
- `anti-patterns/` — what fails (anonymized failed approaches)
- `insights/` — platform-level aggregate patterns (cohort-level, not individual)

### Quality Gates
- New learning → requires 2+ confirmations OR explicit user approval before promoting to verified lesson
- Unverified → stage in `cold/staging/` until confirmed
- Verified → promote to `cold/lessons/`

### Existing Foundations
- Solomon Vault brain/ → maps to COLD + Identity layers ✅
- GBrain patterns → feedback + entity detection ✅
- Sunday Self-Review Agent → weekly audit loop ✅
- Per-user brain files → HOT + COLD needed (per-user directories at `solomon-vault/users/{user-id}/`) 🔨
- Shared technique registry → needs building 🔨
- Anonymization layer → needs building 🔨

## Supported Model Providers

| Provider | Env Var | Model | Status |
|----------|---------|-------|--------|
| Ollama | (local) | qwen3:1.7b, llama3.2 | ✅ |
| OpenAI | `OPENAI_API_KEY` | GPT-4o, GPT-4o-mini | ✅ |
| NVIDIA | `NVIDIA_API_KEY` | minimax-m2.5 via build.nvidia.com | ✅ |

## JCPaid Pre-Install Philosophy (April 18, 2026)
> JCPaid = Best of breed pre-installed + AI layer + user makes it their own

### Core Stack
The stack to pre-install in every JCPaid/Solomon OS build:

**Communication**
- Matrix/Element — E2E encrypted messaging, bridge to Telegram/Signal
- Jitsi — video calls, no Zoom needed

**File & Docs**
- NextCloud — Google Drive replacement, self-hosted
- CollabOS or OnlyOffice — Docs/sheets/slides, not Google's

**Password & Secrets**
- Vaultwarden — Bitwarden server, 1Password replacement

**VPN**
- WireGuard — modern, fast, killswitch
- Mysterium Node — decentralized VPN (pre-forked at /home/workspace/node)

**AI Layer**
- Ollama — local LLM, already running ✅
- browser-harness — self-healing browser harness (forked: jvanleur2234-glitch/browser-harness)
- Paseo — cross-device Russell Tuna control (forked: jvanleur2234-glitch/paseo)

**Email**
- Thunderbird + self-hosted SMTP (or Resend API)

**Calendar/Tasks**
- Cal.com — Calendly replacement, self-hosted

**Notes/KB**
- Obsidian — local-first notes
- Cabinet — AI knowledge base (already in jack-connect/)

**Philosophy:** Ship it so good out of the box — everything works, everything talks to each other, Solomon OS AI manages it all — that the default experience is already better than most people's current setup. Then customize from there.

**Reference catalog:** https://selfh.st/apps/ — self-hosted alternatives directory by Ethan Sholly. Use license filters to find MIT/Apache/AGPL options for pre-install batch.

## Icarus Hermes Plugin (April 18, 2026)
- **Repos:** github.com/esaradev/icarus-daedalus (249 stars, MIT) + github.com/esaradev/icarus-plugin (51 stars, MIT)
- **Forked:** jvanleur2234-glitch/icarus-daedalus + jvanleur2234-glitch/icarus-plugin
- **What it does:** Shared memory layer for Hermes agents — one agent learns it, every agent recalls it. Self-building wiki, memory maintenance with quality scoring/auto-archival, training data export for fine-tuning replacement models. Markdown + YAML frontmatter in ~/fabric/, no database. Hot/Warm/Cold tiering with auto-curation.
- **For Solomon OS:** Fills the #1 gap — shared cross-agent memory. Zo learns something → Russell Tuna recalls it. Cross-platform (Telegram ↔ CLI). Self-improving (every decision logged → training data → fine-tuned model).
- **Priority:** HIGH — Install as shared memory layer for ALL Solomon OS agents.
- **Full RD report:** `solomon-vault/brain/RD_REPORTS/icarus.md`

## Evolver — GEP Self-Evolution Engine (April 18, 2026)
- **Repo:** github.com/EvoMap/evolver — 5K stars, GPL-3.0
- **Forked:** jvanleur2234-glitch/evolver
- **What it does:** Self-evolution engine. Scans error logs → selects matching Gene (fix template) → emits GEP prompt → applies fix. Safe: whitelist-only commands, 180s timeout, human-in-loop review mode.
- **JCPaid fit:** ★★★★★ — CRITICAL. This IS the self-improvement engine Solomon OS was missing.
- **Full loop:** Guardian detects attack → Icarus shares signal → Evolver scans → selects Gene → GEP prompt → Hermes applies fix → review mode approves.
- **Strategies:** balanced / innovate / harden / repair-only
- **Install:** `cd evolver && npm install && node index.js --review`
- **Full RD report:** `solomon-vault/brain/RD_REPORTS/evolver.md`

## Mano-P 1.0 — Vision-Based GUI Agent (April 18, 2026)
- **Repo:** github.com/Mininglamp-AI/Mano-P (281 stars, MIT)
- **Forked:** jvanleur2234-glitch/Mano-P
- **What it does:** Pure-vision GUI-VLA agent. Takes screenshot → understands UI → executes actions (click, type, scroll, drag). No APIs, no DOM, no browser dependency — works on ANY desktop app.
- **Key specs:** 58.2% OSWorld success rate, runs quantized 4B at 476 tokens/s on M4 Pro, zero data leaves device
- **Why it matters:** Solves the cross-desktop problem that OpenClaw/Hermes/browser-harness all have. Can automate ANY app on screen.
- **Limitation:** macOS only (M4 required) — Windows/Linux in progress
- **For JCPaid:** HIGH fit for JackConnect — real estate agents use desktop CRMs/MLS daily. Fork and watch.
- **For Be Like You! OS:** HIGH — vision-based automation works on any device
- **Full RD report:** `solomon-vault/brain/RD_REPORTS/mano-p.md`

## Hermes xurl Skill — Official X API CLI (April 18, 2026)
- **PR:** NousResearch/hermes-agent#12303 — merged TODAY
- **xurl:** github.com/xdevplatform/xurl — official X API CLI by Chris Park et al. (740 stars, v1.0.3)
- **Installed:** xurl binary on this server at /usr/local/bin/xurl ✅
- **What changed:** Old `xitter` skill (Infatoshi/x-cli, OAuth 1.0a, 5 env vars, single account) replaced with `xurl` (OAuth 2.0 PKCE + 1.0a, auto-refresh, multi-app/multi-user, DMs+media+streaming+raw v2)
- **Key improvements:**
  - Official — maintained by X dev platform, not 3rd party
  - OAuth 2.0 PKCE with auto-refresh tokens
  - Multi-account support (multiple X apps/users)
  - Credentials stored in `~/.xurl` managed by xurl itself — no manual env var juggling
  - Larger API surface: DMs, follows, blocks, mutes, media upload, streaming, raw v2 endpoints, webhooks
  - Better agent-safety guardrails (forbidden flags list, no `--verbose` in agent mode, never-read-`~/.xurl` rule)
- **Hermes fit:** Replace our existing xitter-based X skill with this. Full X API access (posts, DMs, search, media) wrapped in Hermes SKILL.md conventions.
- **Install xurl:** `curl -fsSL https://raw.githubusercontent.com/xdevplatform/xurl/main/install.sh | bash`
- **Full RD report:** `solomon-vault/brain/RD_REPORTS/hermes-xurl.md`