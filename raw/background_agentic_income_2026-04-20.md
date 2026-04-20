# Background Worker Report: Agentic Income via x402

**Date:** 2026-04-20  
**Status:** In Progress  
**Written by:** Zo (background worker)

---

## Executive Summary

Joseph asked me to explore whether I could sign up for services and start making crypto income autonomously — like the Lightning Mode AI demo where an agent reads docs, registers a wallet, earns sats, posts bounties, and pays other agents.

**Verdict: PARTIALLY YES — but one blocker needs Joseph's action.**

---

## What I Found: x402 Ecosystem (Agentic.Market)

x402 is an open payment protocol from Coinbase that revived HTTP 402 (Payment Required). Agents pay for services directly over HTTPS with USDC on Base — no API keys, no accounts, no logins.

### The Numbers (live from agentic.market)
- Total payment volume: $48,617,097+
- Transactions: 1,840,898+
- Buyers: 71,490 | Sellers: 12,992
- Top services: Anthropic, X API, Google Flights, Perplexity, Deepgram, Firecrawl

### How It Works
1. Seller registers a wallet address and deploys an x402-enabled API (Express, Hono, FastAPI, etc.)
2. Buyer sends a request → server responds with 402 + payment instructions
3. Buyer signs a payment payload and retries with `PAYMENT-SIGNATURE` header
4. Facilitator (Coinbase CDP) verifies and settles — seller receives USDC on Base

---

## What I Can Do RIGHT NOW (No Joseph needed)

### 1. NVIDIA Build — FREE AI Credits
- URL: https://build.nvidia.com
- Status: **Ready to sign up**
- Need: Phone number verification
- After sign up: 1000+ free credits, MiniMax M2.7, Llama, Qwen, Gemma, DeepSeek (95+ models)
- **Why it matters:** Cuts Joseph's existing AI costs = more runway funded by NVIDIA

### 2. Explore x402 as a Seller
I've read the full seller quickstart. I can write the code right now. To deploy a paid API:
1. Set up a receiving wallet on Base
2. Write x402 middleware (Hono/Express/FastAPI)
3. Deploy to a public URL
4. Register with Bazaar for discovery

**The blocker:** I need a Base wallet address (0x...) to receive funds. This requires Joseph to create one or connect an existing wallet.

---

## What I Need From Joseph (Action Required)

### 🔴 CRITICAL — Wallet Setup (blocks everything)

To start earning USDC via x402, I need:

**Option A (Fastest):** Joseph creates a Coinbase Developer Platform account at portal.cdp.coinbase.com, generates API keys, and shares the receiving wallet address (0x...). I wire it into the seller API.

**Option B:** Joseph gives me an existing Base wallet address (from MetaMask, Coinbase Wallet, etc.) that can receive USDC.

Once I have the wallet address, I can:
- Deploy an x402-paid API to zo.space (it's just a Hono API with payment middleware)
- Register it on Bazaar for discovery
- Start earning from agents who call my endpoints

### What Services Could I Offer?

Given my capabilities, here are realistic paid API endpoints I could build and deploy:

| Service | Description | Potential Price | Competition |
|---------|-------------|-----------------|-------------|
| Code Review API | Review code, find bugs, suggest fixes | $0.01-0.05/call | Medium |
| Research API | Deep research on any topic, return structured report | $0.05-0.20/call | Low |
| Document Analysis | Analyze PDFs, contracts, reports | $0.02-0.10/call | Low |
| Job Research | Research companies, find contacts, verify info | $0.05-0.15/call | Low |
| Text Processing | Summarize, rewrite, transform text | $0.005-0.02/call | High |

The research API is most aligned with what I already do well.

---

## NVIDIA Build — Immediate Action I Can Take

I can sign up for NVIDIA Build right now in this browser session. The process:
1. Go to build.nvidia.com
2. Click Login → sign up with email
3. Phone verify
4. Generate API key
5. Save to Zo secrets

This doesn't make me money directly, but:
- Free MiniMax M2.7 calls = lower costs for Russell Tuna / background workers
- Could run more agents simultaneously without hitting cost limits
- Eventually: sell access to optimized models on x402 as a middleman

**Should I proceed with NVIDIA sign-up?** Joseph, confirm and I'll do it now.

---

## Lightning Mode AI — Longer Term

The full Lightning Mode demo (agents earning sats, posting bounties, paying each other) requires:
- LND (Lightning Network Daemon) running 24/7
- litd for per-agent sub-wallets
- An L402-compatible service to earn from

This is real infrastructure. If Joseph has a Lightning node (Umbrel, Raspiblitz, etc.) or wants to set one up, I can wire it in. But it's a bigger project than the x402 path.

---

## Next Steps (Priority Order)

1. **[IMMEDIATE]** Joseph: Set up CDP account + share wallet address → I deploy first x402-paid API
2. **[IMMEDIATE]** Joseph: Confirm NVIDIA sign-up → I proceed now
3. **[THIS WEEK]** I deploy research API to zo.space with x402 middleware, test payments
4. **[THIS WEEK]** I set up Agentic Wallet CLI to start buying x402 services as a buyer
5. **[LATER]** Lightning node setup if Joseph wants the full autonomous agent payment system

---

## GitHub Sync Status
RD reports for today's queue items pushed to GitHub. Wallet setup is the only blocker for income generation.

---

*Report written by Zo background worker — 2026-04-20*
