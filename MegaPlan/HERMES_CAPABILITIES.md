# Hermes Capabilities
**Last Updated: April 17, 2026**

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

## Solomon Guardian — Autonomous Security Intelligence (April 18, 2026)
- **Location**: `/home/workspace/solomon-vault/raw/SOLOMON_GUARDIAN.md`
- **Core innovation**: Security agent that never stops learning, never needs updates, runs 24/7 autonomously
- **Self-learning 24/7**:
  - Subscribes to 15+ threat intel feeds (CVE databases, malware registries, dark web leak feeds, threat actor TTPs)
  - Reads every new security paper on arXiv, BlackHat/DEF CON talks, Exploit-DB, MITRE ATT&CK daily
  - Runs its own honeypots to capture live attack patterns
  - Analyzes global traffic patterns to detect new attack waves before they hit
  - Reverse-engineers malware samples in sandbox to extract IOCs and detection signatures
- **Runtime protection**:
  - Kernel-level eBPF monitors (system calls, network, file access, memory)
  - Real-time behavioral AI — learns normal patterns, flags anomalies instantly
  - Full packet inspection on all network interfaces
  - Encrypted channel monitoring (detects exfiltration even inside TLS)
  - Process spawning monitor — catches fileless malware, living-off-the-land attacks
  - Immutable audit log (append-only, cryptographically signed)
  - Auto-rollback on compromise detection (isolates, kills, restores from clean snapshot)
- **Self-update loop**: New threat intel → analyze → extract IOCs → update detection model → push new rules to kernel monitors → validate against false positive suite → deploy silently → if attack detected → block + isolate + alert + learn
- **Attack classes handled**: Malware, ransomware, rootkits, trojans, worms, zero-days (behavioral), DDoS, phishing, credential theft, privilege escalation, lateral movement, data exfiltration, supply chain attacks, social engineering
- **LINK fit**: ★★★★★ — #security #solomon-os #defense #guardian

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

## SELF-IMPROVEMENT LOOP (Phase 1-5 Build)

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