# JCPaid × The Agency × Hermes × Paperclip — Integration Spec

**Date:** 2026-04-30  
**Status:** BOOTSTRAPPED

---

## WHAT WE BUILT

### The Full Stack

```
JCPaid Control Layer (you)
├── The Agency (147 agents, coordination)
├── Hermes Agent (execution engine, v0.11.0)
└── Paperclip (company workspaces, runtime)
```

### How Each Layer Works

| Layer | Tool | Role |
|---|---|---|
| **Coordination** | The Agency | Hires/manages 147 agents, assigns tasks, reviews work |
| **Execution** | Hermes Agent | Runs the actual work inside each company |
| **Workspace** | Paperclip | Company memory/history where work happens |
| **Control** | JCPaid (you) | Monitor all clients, control what agents do |

---

## THE WORKFLOW

```
Client signs up → JCPaid creates company in Paperclip → 
The Agency assigns agents → Hermes executes work → 
Paperclip stores results → You monitor from dashboard
```

### Real Example (HVAC Client)

1. **Client onboarding:** Create "EZ Heating & Cooling" company in Paperclip
2. **Agent assignment:** The Agency hires seo-specialist, lead-gen, sales-rep agents for that company
3. **Work execution:** Hermes Agent runs seo-audit task inside the EZ Heating workspace
4. **Results:** Paperclip stores the audit report, The Agency logs the completion
5. **Monitoring:** You see all activity from JCPaid dashboard

---

## THE AGENCY AGENTS WE USE

From the 147 agents, these are the most valuable for JCPaid clients:

### For Any Client
- **researcher** — Background research on competitors, market, prospects
- **writer** — Emails, proposals, blog posts, social content
- **designer** — Ads, social media graphics, brand materials
- **accountant** — Financial tracking, invoicing, expense reports
- **qa** — Quality assurance on all AI-generated work

### For Marketing Clients
- **seo-specialist** — SEO audits, keyword research, optimization
- **content-strategist** — Content calendars, blog strategy
- **social-media-manager** — Post scheduling, engagement, growth

### For Sales Clients
- **sales-rep** — Lead qualification, follow-up sequences
- **outreach-agent** — Cold emails, LinkedIn messages, SMS

### For Operations
- **project-manager** — Task coordination, deadline tracking
- **data-analyst** — Reports, metrics, performance tracking

---

## HERMES INTEGRATION

Hermes runs inside each Paperclip company as the executor:

```bash
# Start Hermes inside a Paperclip company workspace
cd /home/workspace/paperclip
hermes gateway run

# Hermes delegates work to The Agency agents via ISCP
```

### Key Hermes Features We Use

1. **Delegate tool** — Assigns tasks to The Agency agents
2. **Memory** — Stores company history, client preferences, past work
3. **Skills registry** — 1,223 skills available for any task
4. **Multi-provider** — Claude, GPT-4, Groq, Kimi, Ollama, etc.

---

## PAPERCLIP INTEGRATION

Paperclip provides the company workspace structure:

```bash
# Each client = one Paperclip company
# Each agent = one Hermes session inside that company
```

### Company Structure

```
paperclip/companies/
├── ez-heating-cooling/     # Client company
│   ├── agents/             # The Agency agents
│   ├── hermes/             # Hermes execution state
│   ├── memory/             # Company knowledge base
│   └── outputs/            # Generated reports, proposals
└── another-client/
    └── ...
```

---

## CONNECTING THE AGENCY TO HERMES

### Step 1: Register Hermes as an Agency tool

```bash
cd /home/workspace/jcpaid
./agency/tools/agent-define --name hermes-executor --role execution
```

### Step 2: Configure The Agency to use Hermes

In `agency/config/agency.yaml`:

```yaml
execution:
  engine: hermes
  gateway: http://127.0.0.1:8642
  api_key: ${HERMES_API_KEY}
```

### Step 3: Add Paperclip as company memory

```bash
# Each company gets a Paperclip workspace
paperclip company create --name "EZ Heating & Cooling"
```

---

## WHAT THIS ENABLES

### For JCPaid (us)
- 147 pre-built agents = 147 service offerings
- Each agent IS a deliverable we can sell
- Agents work 24/7, no salary, no benefits
- Full audit trail via The Agency's receipt system

### For Clients
- Own AI company staffed with specialized agents
- Work done in their company workspace (Paperclip)
- Professional dashboard to monitor activity
- No AI slop — quality gate via The Agency review system

### For Joseph
- Control everything from one dashboard
- Add clients without hiring humans
- Scale to unlimited clients (no infrastructure headaches)
- Own the relationship, pocket the margin

---

## NEXT STEPS

1. [ ] Configure Hermes gateway for The Agency
2. [ ] Create first company workspace in Paperclip (test with EZ Heating)
3. [ ] Assign The Agency agents to the test company
4. [ ] Run first end-to-end task (SEO audit)
5. [ ] Build JCPaid monitoring dashboard
6. [ ] Get first paying client

---

## FILES CREATED

- `/home/workspace/jcpaid/` — The Agency bootstrap (334 files)
- `/home/workspace/hermes-agent/` — Hermes Agent repo
- `/home/workspace/paperclip/` — Paperclip repo
- `/home/workspace/hermes-workspace/` — Hermes Workspace (port 3002)
- `/home/workspace/the-agency/` — The Agency source