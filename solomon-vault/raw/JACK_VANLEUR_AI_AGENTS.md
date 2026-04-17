# JACK VANLEUR — AI AGENT SUITE
## Alpine Real Estate × Solomon OS | Sioux Falls Market

**Built:** April 11, 2026  
**Status:** PLANNING COMPLETE — READY TO BUILD  
**Contact:** jack@thinkalpine.com | 605.940.1578

---

## WHO IS JACK VANLEUR

**Profile:** Designated Broker, Alpine Real Estate Companies, Sioux Falls, SD
**Experience:** 13+ years real estate brokerage
**Background:** Business (Finance, Marketing, Entrepreneurial Management) from Creighton University  
**Alpine Tenure:** Joined October 2022; previously Hegg REALTORS (2020-2022)  
**Previous Career:** Account management + financial reporting  
**Personal:** Married to Meghan, two sons (Bennett, Cohan). Outdoors: hunting, fishing, baseball  
**Location:** Brandon, SD native, serves Sioux Falls market  
**Specialty:** Likely investment property (Alpine's investment fund focus)

---

## ALpine Real Estate Companies Overview

**Structure:**
- Alpine Property Management: 700+ units, in-house maintenance
- Alpine Real Estate: residential + commercial brokerage
- Alpine Construction & Development
- Alpine Capital (investment funds, 6 funds, $40M+ total project value)
- Alpine Staging & Design

**Markets Served:** Sioux Falls, SD + surrounding communities  
**Brokerage Model:** Full-service (transaction coordination available)

---

## WHAT JACK DOES DAILY (Real Estate Agent Workflow)

### Pre-Transaction (Lead Generation & Nurturing)
- Respond to new leads within 5 minutes (Zillow, Realtor.com, website)
- Follow up with past clients and sphere of influence
- CRM updates and contact notes
- Market analysis for pricing conversations
- Geo-farming and farm area monitoring
- Schedule showings and open houses

### Active Transaction
- Show properties to buyers
- Write and negotiate offers
- Coordinate inspections, appraisals, title, escrow
- Draft and review contracts
- Update clients on transaction progress
- Ensure compliance and document completion
- Troubleshooting delays and contingencies

### Post-Transaction
- Client anniversary and birthday outreach
- Referral requests from satisfied clients
- Database nurturing for future deals
- Investment client reporting (given Alpine Capital)

---

## THE AI AGENT SUITE FOR JACK

### 7 AI EMPLOYEES (1 Supervisor + 6 Specialists)

---

### 1. 🕵️ PROSPECTOR — Lead Intake & Qualification
**What it does:**
- Reads emails, texts, form submissions, website inquiries
- Qualifies leads: budget, timeline, motivation, property type
- Scores lead hotness (1-10)
- Updates CRM automatically
- Schedules follow-up tasks
- Alerts Jack to urgent leads via Telegram

**Jack's specific triggers:**
- "I need to buy/sell a house in Sioux Falls"
- Budget range, timeline, property preferences
- Investment property interest → flag for Alpine Capital

**Output:** Qualified lead card sent to Jack via Telegram

---

### 2. 🔍 PROPERTY MATCHMAKER — Buyer/Seller Matching
**What it does:**
- Maintains live Sioux Falls inventory understanding
- Matches buyers to properties based on criteria
- Alerts Jack when new listings match his active buyers
- For sellers: pulls comps, recommends pricing
- Tracks showing feedback to refine matches

**Jack's Sioux Falls inventory knowledge:**
- Neighborhoods: Tea, Harrisburg, Brandon, SE Sioux Falls, NW
- Price ranges Jack handles: ~$200K-$2M+
- Investment properties for Alpine Capital clients

**Output:** Property match cards via Telegram with link to listing

---

### 3. 📋 TRANSACTION COORDINATOR — Deal Tracker
**What it does:**
- Builds timeline from accepted offer to close
- Tracks all contingencies and deadlines
- Sends daily priority alerts
- Drafts buyer/seller/agent communications
- Flags risks before they become emergencies
- Maintains deal status board

**For Jack's active deals:**
- Inspection → appraisal → contingency deadlines
- Title and escrow coordination
- Closing date reminders

**Output:** Daily digest at 7 AM via Telegram

---

### 4. 📰 MARKET INTELLIGENCE — Farm Monitor
**What it does:**
- Monitors Alpine listing alerts
- Tracks new listings in Jack's farm areas
- Watches price reductions and relistings
- Alerts on competitor activity
- Analyzes market trends for client presentations
- Tracks DOM, price/sqft trends in target neighborhoods

**Jack's farm areas:** Sioux Falls metro (SE, NW, Tea, Harrisburg, Brandon)

**Output:** Weekly market report via Telegram

---

### 5. 💌 CLIENT NOURISHER — Relationship Manager
**What it does:**
- Tracks all contacts in CRM with important dates
- Sends birthday, anniversary, holiday messages (personalized by AI)
- Nurtures past clients with market updates
- Identifies referral opportunities
- Sends automated check-ins at 30/60/90 days post-close

**Jack's SOI (Sphere of Influence):**
- Past clients
- Family and friends
- Baseball community
- Creighton alumni network
- Outdoor enthusiast community (hunting/fishing)

**Output:** Nurture tasks queued automatically, sent via Telegram for approval

---

### 6. ✍️ MARKETING COORDINATOR — Content Creator
**What it does:**
- Writes listing descriptions from property details
- Creates social media posts (Facebook, Instagram, LinkedIn)
- Generates CMA reports for seller conversations
- Writes follow-up emails and text templates
- Creates property flyers and email campaigns
- Video script outlines for property tours

**For Alpine listings:**
- Professional listing descriptions
- Social posts for new listings
- "Just Sold" announcements
- Investment opportunity summaries for Alpine Capital

**Output:** Draft content via Telegram for Jack to approve/post

---

### 7. 📊 INVESTMENT ANALYST — Property Math
**What it does:**
- Analyzes investment property deals (cap rate, cash-on-cash, DSCR)
- Compares properties for investors
- Models renovation scenarios (BRRRR analysis)
- Tracks Alpine Capital fund performance
- Generates investor reports

**For Jack's investment clients:**
- Off-market deal analysis
- Rehab cost estimation
- Rental income projections
- Exit strategy modeling (hold vs. flip)

**Output:** Deal analysis cards via Telegram

---

### 🤖 SUPERINTENDENT — Jack's AI Supervisor
**What it does:**
- Orchestrates all 6 specialist agents
- Daily briefing at 7 AM
- Priority ranking for the day
- Decision support: "Client wants to put in offer — here's the data"
- Learns Jack's preferences over time
- Escalates only what needs Jack's attention
- Coordinates between agents when tasks cross domains

**Interface:** Telegram direct message to Jack

---

## HOW THEY WORK TOGETHER

```
SUPERINTENDENT
│
├── Morning Briefing (7 AM) ── daily priorities
│
├── PROSPECTOR ───────────────────────┐
│   (qualifies leads, scores hotness)  │ If investment lead
│                                      ↓
├── PROPERTY MATCHMAKER ─────── INVESTMENT ANALYST
│   (matches buyers/sellers)       (deal math)
│
├── TRANSACTION COORDINATOR ───────────────┐
│   (tracks deadlines, drafts comms)       │
│                                           ↓
├── MARKET INTELLIGENCE ←─── MARKETING COORDINATOR
│   (monitors farm)        (creates content)
│
└── CLIENT NOURISHER ───────────────────────┘
    (relationship follow-up, referrals)
```

---

## TECHNICAL ARCHITECTURE

### Stack
- **Brain:** Hermes (skills: real estate, market analysis, writing)
- **Communication:** Russell Tuna (Telegram messages to Jack)
- **Browser:** PinchTab (web browsing, MLS access, property research)
- **LLM:** Ollama qwen3:1.7b (local, free inference)
- **Memory:** Solomon Vault (all client data, deal history, preferences)
- **Skills:** 7 custom skills written in Hermes format

### Skills to Build
1. `prospector-re` — Lead qualification + CRM update
2. `property-matcher-re` — Sioux Falls MLS matching + comps
3. `transaction-coordinator-re` — Deal tracking + timeline management
4. `market-intelligence-re` — Farm monitoring + alerts
5. `client-nurturer-re` — Contact nurturing + referral triggers
6. `marketing-coordinator-re` — Listing copy + social content
7. `investment-analyst-re` — Deal math + investor reports

### Data Sources for Jack
- Alpine listings (thinkalpine.com)
- MLS data (Sioux Falls area via IDX)
- Zillow, Realtor.com for market data
- Jack's Gmail (email inquiries)
- CRM data from Solomon Vault
- Alpine Capital fund data (investment clients)

---

## WHAT TO BUILD FIRST

### Phase 1: Core Stack (This Week)
1. PinchTab running ✅ (done)
2. Hermes skills for real estate
3. Superintendent agent (daily briefing)
4. Prospector + Property Matcher (lead flow)
5. Transaction Coordinator (deal tracking)

### Phase 2: Client Flow (Week 2)
6. Client Nourisher (SOI management)
7. Market Intelligence (farm monitoring)
8. Marketing Coordinator (content)

### Phase 3: Investment Vertical (Week 3)
9. Investment Analyst (for Alpine Capital clients)

---

## WHY THIS WORKS FOR JACK

**Current problem:** Jack is a top producer but there's only one of him. AI handles the admin so he focuses on:
- Client relationships (what he does best)
- Negotiations and closings (where he makes money)
- Investment deal sourcing (Alpine Capital)

**Time saved:** 10-15 hrs/week on admin work  
**Revenue potential:** Never miss a lead, more deals through better follow-up  
**Competitive advantage:** No other Sioux Falls agent has this

---

## PRICING FOR JACK (Proof of Concept)

**Setup:** Free (already built on Solomon OS)  
**Monthly subscription:** $99/mo (uses existing stack)  
**Goal:** 3-month proof → expand to all Alpine agents

**Success metrics:**
- Lead response time: 5 min → 30 seconds
- Deals closed: +2-3 in first quarter
- Client satisfaction: no dropped balls