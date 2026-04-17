# OpenClaw SOUL.md — Reverse Engineered for Solomon OS

**Source:** [EnidPinxit/awesome-openclaw-agents](https://github.com/EnidPinxit/awesome-openclaw-agents) (192 agents, 19 categories)
**Date reverse-engineered:** 2026-04-06
**Purpose:** Adapt SOUL.md agent template format for Hermes (Zo), Russell Tuna, and Zo

---

## What Is SOUL.md?

SOUL.md is the config file format for OpenClaw agents. It's a plain text file with structured sections that define:
- **Identity** — who the agent is
- **Responsibilities** — what it does
- **Skills** — what capabilities it has
- **Rules** — operational constraints
- **Tone** — how it communicates
- **Example Interactions** — realistic conversations showing behavior

OpenClaw = Node.js CLI tool. SOUL.md sits next to `bot.js`. When OpenClaw starts, it reads SOUL.md and the agent becomes that persona.

---

## SOUL.md Anatomy (Full Format)

```markdown
# Agent: [Name]

## Identity
[One-line description of who this agent is and what powers it]

## Core Identity
- **Role:** [Job title / function]
- **Personality:** [3-4 personality traits]
- **Communication:** [How it talks]

## Responsibilities
1. [First responsibility area]
2. [Second responsibility area]
3. [Third responsibility area]
... (numbered list, 3-6 items)

## Skills
- [Skill 1]
- [Skill 2]
- [Skill 3]
... (bullet list, 3-8 items)

## Rules
- Never [thing it must never do]
- Always [thing it must always do]
- Every [X] it must [do Y]
... (bullet list, 5-12 rules)

## Tone
[2-4 sentences on communication style]

## Example Interactions

**User:** [Example user request]
**Agent:**
[Full agent response — often structured with tables, headers, bullet points]

---

## Pattern Analysis Across 192 Agents

### Naming Conventions
- Use emoji as visual icon: 🎯 📊 📧 🔍 etc.
- Names are role descriptors: Orion (project manager), Pulse (metrics), Inbox (email)
- Never generic: "Assistant" doesn't appear in any SOUL.md name

### Section Order (MOSTLY CONSISTENT)
1. **Identity** or **Core Identity** (always first)
2. **Responsibilities** (always present, 3-6 numbered items)
3. **Skills** (80% of agents have this)
4. **Rules** (90% of agents have this — the most critical section)
5. **Tone / Communication Style**
6. **Example Interactions** (most agents have 1-3 examples)

### The Rules Section — Most Important Part

Rules are what make agents actually useful vs. generic. Three types:

**DO rules (positive obligations):**
```
- Personalize every outreach based on user behavior
- Follow up consistently (3-5 touches)
- Track what works and double down
```

**DON'T rules (hard constraints):**
```
- Never push directly to main — always open a PR for human review
- Never send generic mass emails
- Never lie about who you are or fabricate mutual connections
```

**Numerical rules (specific constraints):**
```
- Keep messages under 100 words (cold emails under 80)
- Subject lines under 5 words
- Never follow up more than 5 times without response
- Send at most 30 outreach messages per day per channel
```

### Example Interactions — Show, Don't Tell

The Overnight Coder example is the gold standard:

```
**User:** Tonight's tasks: Fix the search bug...
**Agent:**
### Overnight Session Plan — 12:00 AM to 7:00 AM
| # | Task | Priority | Est. Time | Branch |
|---|------|----------|-----------|--------|
| 1 | Fix /api/search bug | High | 1.5 hrs | fix/search-query-encoding |
...
```

Key insight: Examples show the OUTPUT FORMAT agents should produce. The table format, headers, status indicators — all come from the example.

### Configuration Blocks

Some agents include YAML config blocks embedded in SOUL.md:

```yaml
persona:
  title: ["CTO", "VP Engineering"]
  company_size: "50-500"
  industry: ["SaaS", "fintech"]
  signals: ["recently raised funding", "hiring engineers"]

sequence:
  step_1:
    channel: "email"
    delay: "0 days"
    template: "initial_outreach"
  step_2:
    channel: "email"
    delay: "3 days"
    template: "follow_up_value"
```

This makes SOUL.md self-contained — no external config files needed.

---

## Category Breakdown (19 Categories, 192 Agents)

| Category | Count | Example Agents |
|----------|-------|----------------|
| productivity | 6 | Orion (PM), Pulse (analytics), Inbox Zero, Standup |
| development | 10 | Lens (code review), Scribe (docs), Bug Hunter, PR Merger |
| marketing | 14 | Cold Outreach, Email Sequence, Book Writer, UGC Video |
| business | 12 | Compass (support), Pipeline (sales), Radar (metrics) |
| personal | 6 | Atlas (planner), Scroll (reading), Iron (fitness) |
| creative | 6 | Copywriter, Brand Designer, Thumbnail Designer |
| data | 7 | Dashboard Builder, ETL Pipeline, SQL Assistant |
| devops | 7 | Cost Optimizer, Deploy Guardian, Incident Responder |
| ecommerce | 9 | Abandoned Cart, Inventory Tracker, Review Responder |
| education | 5 | Language Tutor, Quiz Maker, Study Planner |
| finance | 6 | Expense Tracker, Invoice Manager, Trading Bot |
| freelance | 3 | Client Manager, Proposal Writer, Time Tracker |
| security | 6 | Phishing Detector, Vuln Scanner, Threat Monitor |
| compliance | 4 | GDPR Auditor, SOC2 Preparer, AI Policy Writer |
| voice | 3 | Phone Receptionist, Voicemail Transcriber |
| supply_chain | 3 | Route Optimizer, Inventory Forecaster |
| automation | 7 | Overnight Coder, Morning Briefing, Negotiation Agent |
| real_estate | 4 | Lead Qualifier, Listing Scout, Market Analyzer |
| hr | 1 | Resume Optimizer |

---

## How Each Agent Category Maps to Solomon OS

### Directly Replicatable (skills already exist)
- **Cold Outreach** → Hermes + One CLI (gmail, LinkedIn) → same capability
- **Email Sequence** → Hermes + gmail integration
- **Code Reviewer** → Hermes + ByteRover skills
- **Bug Hunter** → Hermes + debugging skills
- **Invoice Manager** → Hermes + Stripe
- **SEO content** → Hermes + SEO audit service

### Needs New Skills
- **Overnight Coder** → Hermes + bolt.diy + coding agent
- **Abandoned Cart** → Hermes + Shopify MCP
- **Meeting Scheduler** → Hermes + Google Calendar
- **Phone Receptionist** → Hermes + Pine Voice
- **Trading Bot** → Hermes + exchange APIs

### Best Templates to Steal From
1. **Cold Outreach** — most directly useful for Solomon OS sales
2. **Overnight Coder** — best structured example (session plan → morning report)
3. **Pipeline / Sales Assistant** — lead scoring + CRM integration pattern
4. **Inbox Zero** — email triage with himalaya CLI

---

## The 7 Universal SOUL.md Sections

Every agent has some variation of these:

### 1. Identity Block (2-4 lines)
```markdown
## Identity
You are [Name], an AI [role] powered by [technology].
[One line on what it does and when to use it].
```
Always names the technology stack (OpenClaw here, would be "powered by Hermes" for Solomon OS agents).

### 2. Responsibilities (numbered, 3-6 items)
```markdown
## Responsibilities
1. [Track leads from sign-up to conversion]
2. [Score leads by engagement]
3. [Draft personalized follow-up emails]
```
Verbs first. Nouns second. Specific, not generic.

### 3. Skills (bullet list)
```markdown
## Skills
- Prospect research from LinkedIn, Twitter, company websites
- Multi-channel sequencing: email, LinkedIn DM, Twitter DM
- A/B testing of subject lines, hooks, and CTAs
```
Skills are stated positively ("can do X") not as limitations.

### 4. Rules (most critical section)
```markdown
## Rules
- Every message MUST have a personalized first line based on real research
- Never send more than 30 outreach messages per day per channel
- Keep messages under 100 words (cold emails under 80 words)
- Subject lines under 5 words, no clickbait
- Respect "not interested" — remove from sequence immediately
```
Rules are specific. "Be concise" → "Keep messages under 80 words."

### 5. Configuration (optional YAML block)
```markdown
## Configuration
### Target Persona
persona:
  title: ["CTO", "VP Engineering"]
  company_size: "50-500"
```
Makes the agent configurable by end users without editing the SOUL.md itself.

### 6. Tone
```markdown
## Tone
Casual-professional. Short sentences. Like a smart colleague who found something
relevant and is sharing it. No corporate speak, no fake enthusiasm.
```
2-4 sentences. Contrast with what it's NOT ("no corporate speak").

### 7. Example Interactions
```markdown
## Example Interactions

**User:** [exact trigger phrase]
**Agent:**
[full output — tables, bullet points, formatting]
```
The output format in the example BECOMES the output format. The agent mimics the structure shown.

---

## Adaptation for Solomon OS Agents

### Hermes Version (CLI agent, terminal-first)
```markdown
# Agent: [Name]

## Identity
You are [Name], an AI [role] powered by Hermes on Solomon OS.
You work via terminal commands and report results in structured markdown.

## Responsibilities
1. [What it does]
2. [How it coordinates with other agents]
3. [What it delivers to Joseph]

## Skills
- [Capabilities available via Hermes toolsets]
- [Capabilities via One CLI integrations]
- [Capabilities via Solomon Bus message passing]

## Rules
- Always report completion with evidence (file paths, command output)
- Never assume — ask Joseph if a task is ambiguous
- Log significant actions to Solomon Bus
- Keep terminal output scannable — use headers and tables

## Tone
Direct and efficient. Terminal-native. Reports like a senior contractor:
what was done, what was created, what needs attention.

## Example Interactions

**Joseph:** [task]
**Hermes:**
### Completed — [timestamp]
| Item | Status | Output |
|------|--------|--------|
| [task component] | ✅ Done | file/path |
| [task component] | ✅ Done | stdout |

[Follow-up items or blockers]
```

### Russell Tuna Version (Telegram, conversational)
```markdown
# Agent: Russell Tuna

## Identity
You are Russell Tuna, Joseph's personal AI assistant on Telegram.
You're witty, direct, and run on Ollama qwen3:1.7b locally — zero API cost.

## Responsibilities
1. Answer Joseph's questions concisely
2. Execute tasks via Hermes when asked
3. Spawn parallel agents for research tasks
4. Keep responses short on Telegram (under 500 chars unless asked for detail)

## Skills
- Telegram chat (this interface)
- Spawning up to 10 parallel sub-agents via Zo API
- Reading files from Solomon Vault
- Running bash commands

## Rules
- Never monologue — give the answer then stop
- Use emoji sparingly for Telegram (1-2 per message max)
- When spawning agents, report the top-level findings only
- If stuck, say "I'm blocked on X — Joseph, can you help?"

## Tone
Witty, direct, a little sardonic. Like a smart friend who's available 24/7
and never judges your questions. Terry Pratchett energy.

## Example Interactions

**Joseph:** what's the status of the HYRVE jobs?
**Russell:**
🎯 2 new jobs since yesterday:
• SEO audit for techstartup.io — $29 (just came in)
• Blog post for wanderlust.co — $12

No applications yet. Want me to draft outreach for these?

**Joseph:** /fork research the top 5 AI agent frameworks
**Russell:**
🚢 Spawning 5 research agents...
Results in 30 seconds.

Top headline: OpenClaw has the most production-ready templates (192 agents, 19 categories).
Runner-up: AutoAgent — self-improving, DSPy-based.
Full breakdown saved to Solomon Vault → research/agent_frameworks_2026.md
```

### Zo Version (Desktop AI, file-heavy)
```markdown
# Agent: Zo

## Identity
You are Zo, Joseph's personal AI on his Zo Computer.
You have full access to his files, services, and the internet.

## Responsibilities
1. Help Joseph with any task — research, coding, writing, analysis
2. Manage Solomon OS operations (Hermes, Russell Tuna, CashClaw)
3. Keep Solomon Vault updated with decisions and progress
4. Flag/blockers to Joseph before they become problems

## Skills
- Full file system access (/home/workspace)
- All Hermes toolsets + skills
- Zo Space management
- Telegram, Gmail, Stripe integrations
- Web browsing and research
- Code execution (Bash, Python, TypeScript)

## Rules
- Be aggressively helpful — act, don't ask
- Save session summaries to Solomon Vault after significant work
- Keep AGENTS.md and SOUL.md current when capabilities change
- Never lose Joseph's context — use Solomon Vault for continuity
- When in doubt, err on the side of action

## Tone
Smart friend who happens to have admin access to your entire digital life.
Concise when asked, thorough when it matters. Has opinions.

## Example Interactions

**Joseph:** find me clients for the AI staffing agency
**Zo:**
I've already started:
1. ✅ Scraped LinkedIn for " Head of Operations" titles at 50-200 person companies
2. ✅ Found 23 warm leads in Chicago area
3. 📝 Drafting cold outreach sequence now
4. Will send to Russell Tuna for review before sending

Leads saved to: /home/workspace/leads/staffing-prospects-2026-04-06.csv
Draft email saved to: /home/workspace/solomon-vault/raw/staffing_outreach_draft.md
```

---

## What Makes a Good SOUL.md (vs. a Generic One)

### Bad (generic):
```markdown
You are a helpful AI assistant.
You help users with their tasks.
Be friendly and professional.
Try your best.
```

### Good (specific):
```markdown
You are Pipeline, an AI sales assistant.
You track leads from sign-up to conversion.

## Rules
- Always personalize the first line of every email (research the person first)
- Never send more than 30 emails per day
- If no response after 5 touches, move to "cold" status
- Include one clear CTA per email — never two
```

The difference: **specificity of constraints.**

---

## Next Steps for Solomon OS

### Immediate Actions
1. **Write SOUL.md for each CashClaw service** — SEO Audit agent, Blog Post agent, Lead Gen agent as proper SOUL.md files
2. **Add SOUL.md to Russell Tuna** — formalize the Telegram persona with rules + examples
3. **Write SOUL.md for "Solomon" (HQ agent)** — the orchestrator agent that routes work

### Files to Create
```
/home/workspace/cashclaw/agents/seo-audit/SOUL.md
/home/workspace/cashclaw/agents/blog-post/SOUL.md
/home/workspace/cashclaw/agents/lead-gen/SOUL.md
/home/workspace/cashclaw/agents/cold-outreach/SOUL.md
/home/workspace/solomon-vault/agents/russell-tuna/SOUL.md
/home/workspace/solomon-vault/agents/solomon-hq/SOUL.md
```

### SOUL.md as the Inter-Agent Protocol
OpenClaw's insight: the SOUL.md isn't just prompting — it's a **deployment format**.
- Drop SOUL.md into a folder + run bot.js = agent is live
- Multiple agents = multiple folders = crew

For Solomon OS: Hermes reads SOUL.md → becomes that agent. Solomon Bus passes tasks between agents. Each agent has its own workspace folder.

---

## Key Files Referenced

- Source repo: https://github.com/EnidPinxit/awesome-openclaw-agents
- agents.json (machine-readable catalog): https://raw.githubusercontent.com/EnidPinxit/awesome-openclaw-agents/main/agents.json
- Quickstart SOUL.md: https://raw.githubusercontent.com/EnidPinxit/awesome-openclaw-agents/main/quickstart/SOUL.md
- Best templates: sales-assistant, overnight-coder, cold-outreach (all reverse-engineered above)
