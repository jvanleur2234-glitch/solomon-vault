# RD Report: Google ADK 2.0 + google/skills

**Date:** 2026-05-19  
**Source:** https://x.com/i/status/2056721811480719553 (Santiago @svpino)  
**Type:** Framework / Agent Toolkit  

---

## What It Is

Google released two big things around Google I/O 2026:

### 1. google/adk-python — Agent Development Kit 2.0
- **19.7k stars**, 3.4k forks, v2.0.0 released today
- Open-source Python framework for building AI agents
- Key features:
  - **Workflow Runtime**: graph-based execution engine with routing, loops, fan-out/fan-in, retry, state management, human-in-the-loop
  - **Task API**: structured agent-to-agent delegation with multi-turn task mode
  - Code-first, Python 3.11+, `pip install google-adk`
- Supports Gemini models, extensible to other LLMs

### 2. google/skills — Agent Skills library
- **10k stars**, 763 forks
- Open format for giving agents capabilities on Google Cloud products
- Skills for: Gemini API, BigQuery, Cloud Run, Cloud SQL, Firebase, GKE, etc.
- Install via `npx skills add google/skills`

### The "library of end-to-end examples" claim
The X post said Google published "an entire library of highly sophisticated, end-to-end agent examples." The actual repos above are developer frameworks/tools, not a collection of pre-built agent examples. There's likely an "Agent Garden" component in Google Cloud's enterprise agent platform, but the main claim somewhat overstates what's actually in these public repos. Still significant.

---

## How It Compares to JCPaid Stack

| Aspect | JCPaid Stack | Google ADK |
|--------|--------------|-------------|
| **Purpose** | Business AI orchestration | Developer framework for agents |
| **Agents** | 147 agents (The Agency), multi-bot coordination | Single/multi-agent dev kit |
| **Memory** | here.now (10GB permanent) | Ephemeral session memory |
| **Business logic** | JCPaid Bus, fleet dispatch, personas | Code-first, generic |
| **Target user** | Non-technical biz owners | Developers |
| **Deployment** | Zo Computer, Solomon OS | Cloud Run, Vertex AI |

Google ADK is a **developer tool** — you write Python code to build agents. JCPaid is a **business operating system** — no code required, pre-built agents and workflows. Different audience entirely.

---

## Competitive Analysis

**Threat to JCPaid?** LOW. Google's ADK targets developers building custom agents. JCPaid targets people who want AI to run their business without writing code. The skill gap is enormous.

**Inspiration / Integration opportunities?** WORTH NOTING:
- The ADK workflow engine (graph-based with routing/loops/retry) is architecturally similar to what JCPaid Bus could use for complex orchestration
- The Task API for agent-to-agent delegation is conceptually similar to Solomon Bus messaging
- google/skills format (compact agent-first docs for specific tech) is similar to Hermes skill format

---

## Strategic Takeaway

Google is entering the agent framework space in force (ADK 2.0 drops today at I/O). This validates that multi-agent orchestration is the direction the industry is going. But their tool requires developers — it doesn't compete with JCPaid's no-code business AI positioning.

**However:** The ADK's workflow engine architecture is worth studying for future JCPaid Bus enhancements. The graph-based execution model with routing, loops, and retry is exactly the kind of capability that could make JCPaid Bus much more powerful.

---

## Recommendation

**INTEGRATE** — Not the ADK itself (wrong architecture for our use case), but study its workflow patterns. Clone the repo, study the workflow runtime implementation, and consider whether JCPaid Bus could adopt similar graph-based execution for complex business workflows.

Also worth watching: **google/adk-samples** (referenced in ADK docs) for examples of multi-agent patterns we could replicate in The Agency.

**Action:** Clone google/adk-python and google/skills to workspace for reference. Add to brain/Services.md.