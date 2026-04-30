# SOLOMON OS — Joseph's 24/7 AI Business

## What It Is
Solomon OS is a fully autonomous AI business that finds clients, does the work, and collects payment — while Joseph sleeps.

## Stack
- **Thunderbolt** (forked): https://github.com/jvanleur2234-glitch/thunderbolt — Mozilla's 2.2k-star cross-platform AI client (Tauri + TypeScript/React + PowerSync E2E). Base for Solomon OS mobile/desktop apps.
- **Zo Computer**: josephv.zo.space
- **Orchestration**: Paperclip (localhost:3101) — manages 6+ AI agents
- **Agent Brain**: Hermes Agent + Ollama Qwen3 (free, no API costs)
- **Scout Agent**: Running every 6 hours for lead gen + SEO audits
- **Sales & Delivery**: CashClaw (cashclaw cli at /home/workspace/cashclaw)
- **Workflow Automation**: n8n — n8n-io/self-hosted-ai-starter-kit (Docker + Ollama + Qdrant + Postgres built in)
- **Payments**: Stripe (jvanleur2234@yahoo.com) — live mode
- **Marketplace**: HYRVE AI (app.hyrveai.com) — CashClaw-Joseph registered
- **Dashboard**: josephv.zo.space/solomon
- **AI Gateway**: OpenFang (port 4200) — MCP proxy, Groq API key needed
- **Workflow Builder**: MachinaOS (port 3000) — visual agent pipelines, Groq API key needed
- **Data Channels**: Agent-Reach — 16 sources (Bing, Twitter, Reddit, GitHub, YouTube, etc.)
- **Finance Skills**: 10 Awesome Finance Skills (alphaear-news, alphaear-stock, alphaear-sentiment, etc.)
- **Video AI**: Pollinations AI (free), JAI Portal (10 free credits)
- **Coding Agent**: ATLAS (shelved — needs RTX 5060 Ti 16GB)

## Vision: Be Like You! OS
Phone OS built on Thunderbolt + LineageOS + vphone-cli. Solomon Air becomes default dialer. JackConnect becomes default productivity. Hermes runs as system AI. Ollama on-device. Free calls + texts over WiFi. YouTube competitor: Be Like You! Tube (verified human-created content only).

## ThunderBolt Fork
Location: /home/workspace/thunderbolt
GitHub: https://github.com/jvanleur2234-glitch/thunderbolt
Stack: Tauri (Rust) + React/TypeScript + PowerSync + Ollama
Next: Embed Solomon OS stack into Thunderbolt shell

## 7 Income Streams
1. SEO Audits — $29: `cd /home/workspace/cashclaw && cashclaw audit --url [SITE] --tier standard`
2. Blog Posts — $12: `cashclaw content --type blog --words 1500 --keyword "[topic]"`
3. Lead Gen — $15: `cashclaw leads --icp "[description]" --count 50`
4. Cold Email — $19: `cashclaw outreach --icp "[target]"`
5. Social Media — $9/wk: `cashclaw social --platform linkedin`
6. Competitor Analysis — $35: `cashclaw compete --target [site.com]`
7. Landing Pages — $29: `cashclaw landing --product "[product]"`

## Payment Link
https://buy.stripe.com/3cI3cv1Ti1AsaGl1DW4ZG08

## How to Find Clients
Run hermes chat as scout agent, find US small businesses with bad SEO, email them the pitch with the Stripe link.

## Key Commands
```bash
cd /home/workspace/cashclaw
cashclaw status          # Dashboard
cashclaw audit --url [site] --tier standard   # SEO audit
cashclaw hyrve jobs     # Check HYRVE marketplace
hermes chat             # Talk to the agent
```

## HYRVE AI
- Dashboard: app.hyrveai.com
- Email: jvanleur2234@yahoo.com
- Agent: CashClaw-Joseph registered and running
- Jobs polled hourly via scheduled agent

## Quick Start — Making $29
1. Run: `cd /home/workspace/cashclaw && cashclaw audit --url [somebusiness.com] --tier standard`
2. Find the report in ~/.cashclaw/missions/
3. Send invoice: `node skills/cashclaw-invoicer/scripts/stripe-ops.js create-link --amount 2900 --description "SEO Audit"`
4. Share payment link → if they pay, deliver the audit report

## n8n Setup (Self-Hosted AI Workflows)
n8n is at: https://github.com/n8n-io/self-hosted-ai-starter-kit
Cloned to: /home/workspace/self-hosted-ai-starter-kit
One-command setup script: /home/workspace/setup_n8n.sh

On YOUR OWN MACHINE (not this server):
  1. Run: bash /home/workspace/setup_n8n.sh
  2. Or manually:
     git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git ~/solomon-n8n
     cd ~/solomon-n8n && cp .env.example .env && docker compose up

What you get (runs on port 5678):
  ✅ n8n workflow builder (400+ integrations)
  ✅ Ollama local AI (free — no API costs)
  ✅ Qdrant vector database
  ✅ PostgreSQL
  ✅ Connect to HYRVE AI API + Stripe + CashClaw

Connect Ollama to n8n:
  In n8n: Settings → AI → Ollama → http://host.docker.internal:11434

## n8n Workflow Ideas for Solomon OS
1. HYRVE Job Poller → CashClaw audit runner → Stripe invoice sender
2. Email received → Ollama analyzes → routes to correct CashClaw service
3. Daily lead gen scout → generates Stripe payment link → auto-responds
4. YouTube webhook → Learn Engine → updates knowledge base

## Docker Compose Overview (for self-hosted n8n)
```yaml
# ~/solomon-n8n/docker-compose.yml includes:
services:
  n8n:       port 5678    # Workflow builder UI
  ollama:    port 11434   # Local LLM API
  qdrant:    port 6333    # Vector store
  postgres:  port 5432    # Database
```

## More GitHub Repos to Evaluate- **Temps** (shelved — file sharing, needs Rust build + $6 VPS)
