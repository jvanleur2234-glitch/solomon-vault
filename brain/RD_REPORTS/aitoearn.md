# RD Report: AiToEarn

**Repository:** yikart/AiToEarn  
**Stars:** ~12,300  
**License:** MIT  
**Language:** TypeScript  
**Tech Stack:** Node.js 20, Nx monorepo, Next.js frontend, pnpm

---

## What It Is

AiToEarn is an open-source AI agent for content marketing — create, publish, engage, and monetize across 14 platforms from one dashboard. Positioned as a free alternative to Hootsuite ($99/mo), Buffer ($100/mo), and Later ($80/mo).

**4 Core Agents:**
- **Monetize** — CPS/CPE/CPM payment models for brand deals
- **Publish** — One-click distribution to Douyin, Rednote, TikTok, YouTube, Facebook, Instagram, Threads, X, Pinterest, LinkedIn, WeChat, Bilibili, Kuaishou
- **Engage** — Browser extension auto-likes, follows, generates AI replies, detects buying signals ("link please", "how to buy")
- **Create** — AI content generation via Grok, Veo, Seedance, Kling, Hailuo, Sora, Pika, Runway, Flux; batch mode for matrix accounts

**Key Features:**
- "All In Agent" auto-generates and publishes content autonomously
- Trend Radar for viral content detection
- Calendar scheduler across all platforms
- MCP protocol support (Claude, Cursor compatible)
- OpenClaw plugin for earning tasks inside OpenClaw
- Docker one-click deploy
- International (aitoearn.ai) and China (aitoearn.cn) versions

---

## What We'd Use It For

1. **Content distribution for JCPaid** — Push AI-generated POD designs to social platforms automatically
2. **Engagement automation** — Detect buying signals on posts about niches we serve (Golden Retriever, HVAC, fishing)
3. **Solomon OS integration** — MCP tool for Russell Tuna / Hermes to access cross-platform publishing
4. **Client service layer** — Offer "AI social media manager" as a $199/mo upsell to POD clients

---

## Competitive Analysis

| Feature | AiToEarn | Hootsuite | Buffer |
|---|---|---|---|
| Price | Free (self-host) | $99/mo | $100/mo |
| AI content generation | ✅ | ❌ | ❌ |
| AI replies/comments | ✅ | ❌ | ❌ |
| Buying signal detection | ✅ | ❌ | ❌ |
| MCP/Claude integration | ✅ | ❌ | ❌ |
| Open-source | ✅ | ❌ | ❌ |

---

## Integration with JCPaid

**Where it fits:**
```
JCPaid Stack:
├── here.now        → Long-term memory
├── Solomon Bus     → Task queue
├── The Agency      → 147 AI agents
├── Hermes          → 1,223 skills execution
└── AiToEarn        → CROSS-PLATFORM CONTENT DISTRIBUTION [NEW]
```

**What we'd gain:**
- Publish POD designs to 14 platforms automatically
- Detect buying signals on niche communities
- Free alternative to $99-100/mo social tools
- MCP tool for Claude/Russell Tuna integration

---

## Recommendation

**SKILL** — Add as a skill in Hermes/Solomon OS

This directly addresses the "automated income" goal by:
1. Removing manual social posting work from JCPaid workflow
2. Providing free cross-platform distribution (saves $99-297/mo vs Hootsuite/Buffer/Later)
3. Detecting buying signals we can convert into sales
4. Layering on top of AI design generation (osagnent-vault) → AiToEarn publish pipeline

**Next steps:**
1. Write AiToEarn skill for Hermes
2. Docker deploy on Zo server
3. Connect to osagnent-vault design pipeline
4. Add "social distribution" tier to JCPaid pricing

---

**Built:** 2026-05-14  
**Research:** Full repo clone + README analysis
