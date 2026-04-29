# Free Tier Compounding Strategy

> Use multiple AI services' free tiers simultaneously to build a full autonomous business — without paying for a single agent.

---

## The Core Insight

Each AI platform gives away free credits to acquire users. If you sign up for ALL of them and cycle through their free tiers, you get:
- **Bud.app**: 100k free credits (AI worker with phone/SMS/Telegram/browser)
- **NVIDIA NIM**: Free tier models (microsoft/phi-4-mini, nemotron, kosmos-2)
- **Google AI**: Jules (coding agent) + Gemini CLI + 1000 AI credits/month
- **OpenRouter**: Free tier credits for 100+ models
- **OpenAI**: Free tier limits on o1, GPT-4o
- **Anthropic**: Free tier for Claude
- **Groq**: Free tier with Llama, Mixtral, Gemma
- **Cerebras**: Free tier with Llama
- **Lemuria**: Free tier models

**Combined**: hundreds of dollars worth of AI capability per month, zero cost.

---

## The Compounding Loop

```
Step 1: Sign up for all free tiers
       ↓
Step 2: Each agent does one task → reports back
       ↓
Step 3: Rotate to next free tier when limit hit
       ↓
Step 4: Use earnings to fund paid tiers for unlimited
```

---

## Platforms to Sign Up For (Free Tier)

### 1. Bud.app (bud.app)
- **What**: AI Human Emulator — has its own phone, Telegram, browser, computer
- **Free**: 100k credits on signup
- **Bonus**: Comment on their X posts for extra credits
- **Best for**: Research tasks, report writing, web browsing, SMS/Telegram coordination
- **Signup**: bud.app — no payment required for trial

### 2. NVIDIA NIM (integrate.api.nvidia.com)
- **What**: Enterprise-grade models via API — free tier available
- **Free models**: microsoft/phi-4-mini-instruct, nemotron, kosmos-2, microsoft/phi-3.5-moe-instruct
- **Best for**: Fast inference, cost-effective completion, domain-specific tasks
- **Already connected**: Russell Tuna uses this

### 3. Google AI (ai.google.com)
- **What**: Jules (coding agent), Gemini CLI, Project Mariner (browser agent)
- **Free**: 1000 AI credits/month on AI Pro tier (costs $19/month but often free trial)
- **Best for**: Code generation, debugging, full-stack development
- **Alternative**: Use Google AI Studio free tier for Gemini models

### 4. Groq (console.groq.com)
- **What**: Fast inference API with free tier
- **Free models**: llama-3.1-70b-versatile, llama-3.3-70b-versatile, mixtral-8x7b-32768
- **Best for**: High-speed completion, bulk tasks
- **Signup**: console.groq.com — free API key

### 5. Cerebras (cerebras.ai)
- **What**: Fastest inference available — wafer-scale AI
- **Free**: Llama models via API
- **Best for**: Rapid completion when speed matters
- **Signup**: cerebras.ai — free tier available

### 6. OpenRouter (openrouter.ai)
- **What**: Unified API for 100+ models from OpenAI, Anthropic, Meta, Google, etc.
- **Free tier**: $1-5 free credits on signup, occasional free model access
- **Best for**: Accessing models that aren't on other free tiers
- **Signup**: openrouter.ai — free tier available

### 7. Lemuria (lemuria.ai)
- **What**: New free-tier model provider
- **Signup**: lemuria.ai

### 8. Huginn (self-hosted)
- **What**: Open-source autonomous agent (Apache 2.0)
- **Cost**: Free to run on your own server
- **Best for**: Continuous monitoring, scheduled tasks, web scraping
- **Already**: Cloned to /home/workspace/solomon-huginn

### 9. Heliport (if available)
- **What**: Distribute computing for AI
- **Signup**: Check their site

---

## The Compounding System Architecture

```
SOLOMON OS (Orchestrator)
├── Russell Tuna (Telegram) → NVIDIA NIM (nemotron/phi-4)
├── Hermes (Skills) → Huginn (self-hosted, free)
├── Bud.app agents (free credits, rotating) → Research & reports
├── Groq API (free tier) → Fast completion
├── Cerebras API (free tier) → Speed-critical tasks
├── Google Jules (free tier) → Code generation
└── OpenRouter (free credits) → Model diversity
```

---

## How to Execute This

### Phase 1: Sign Up (Today)
1. Go to bud.app → sign up → get 100k free credits
2. Go to console.groq.com → get free API key
3. Go to cerebras.ai → get free API key
4. Go to openrouter.ai → sign up for free tier
5. Go to ai.google.com → try Jules (free tier)
6. Comment on @budapp posts for bonus credits

### Phase 2: Route Tasks by Strength
- **Bud.app**: Research tasks, report writing, web browsing, SMS coordination
- **Russell Tuna (NVIDIA NIM)**: Telegram conversations, complex reasoning
- **Groq**: Bulk fast tasks (summarization, extraction, classification)
- **Cerebras**: Speed-critical completions
- **Jules (Google)**: Code generation, debugging, full-stack dev
- **Huginn (self-hosted)**: Continuous monitoring, scheduled scraping

### Phase 3: Compound Earnings
- Use CashClaw services to earn money
- Put earnings into Bud.app paid tier ($25/month Pro) for unlimited
- Scale paid tiers as revenue grows

---

## What This Means for Solomon OS

Solomon OS becomes the **orchestrator** that routes tasks to whichever free-tier agent is best suited — and when one hits its limit, it rotates to the next.

This is how you run a full AI business on zero budget while you sleep.

---

*Last updated: April 29, 2026*
*Status: PHASE 1 — SIGNUP IN PROGRESS*