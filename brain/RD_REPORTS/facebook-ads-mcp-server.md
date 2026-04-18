# RD_REPORT: facebook-ads-mcp-server

**Repository:** https://github.com/gomarble-ai/facebook-ads-mcp-server  
**Stars:** ~not tracked (archestra.ai badge only)  
**License:** MIT  
**Language/Stack:** Python, FastMCP, requests  

---

## What It Does

MCP server that wraps the **Facebook/Meta Graph API v22.0** into Model Context Protocol tools. Lets any MCP-compatible AI client (Claude Desktop, Cursor, etc.) query and manage Facebook ad accounts, campaigns, ad sets, ads, creatives, and insights — with automatic pagination.

### Available Tools

| Tool | What It Does |
|------|-------------|
| `list_ad_accounts` | Lists all ad accounts linked to the token (auto-paginated) |
| `get_details_of_ad_account` | Account fields: name, balance, spend, status, currency, etc. |
| `get_campaign_by_id` | Single campaign details |
| `get_campaigns_by_adaccount` | All campaigns in an account (paginated, filterable) |
| `get_adset_by_id` / `get_adsets_by_adaccount` / `get_adsets_by_campaign` | Ad set read operations |
| `get_ad_by_id` / `get_ads_by_adaccount` / `get_ads_by_campaign` / `get_ads_by_adset` | Ad read operations |
| `get_ad_creative_by_id` / `get_ad_creatives_by_ad_id` | Creative details |
| `get_adaccount_insights` | Performance insights at account level (impressions, spend, CPC, CPM, conversions, etc.) |
| `get_campaign_insights` / `get_adset_insights` / `get_ad_insights` | Nested performance insights |
| `get_activities_by_adaccount` / `get_activities_by_adset` | Change history / audit log |
| `fetch_pagination_url` | Manual pagination follow-through |

### Authentication

`--fb-token YOUR_META_ACCESS_TOKEN` as a command-line argument.

### Architecture

- `FastMCP` server (`mcp` package, >=1.6.0)
- `requests` for Graph API calls
- Token cached in memory after first read
- Pagination handled via `paging.next` URLs
- Fields/filtering params JSON-encoded as Meta API requires

---

## What We'd Use It For

**TikTok UGC Distribution Agency** — when Russell Tuna manages client ad accounts, he needs to pull performance data (spend, CPC, conversions) to report back or optimize. This gives Hermes a direct line into Facebook/Meta Ads data.

**AI White-Collar Staffing Agency** — businesses hiring Russell Tuna as an AI worker could grant him API access; he reads their ad performance and produces optimization reports. The staffing agency takes a cut.

**AI Tools Affiliate Site (Real Estate)** — if any Facebook ad campaigns are being run for the affiliate content, Hermes could track their performance autonomously.

---

## How It Compares to What We Have

- **No existing Facebook/Meta Ads integration** in Solomon OS. This is net new capability.
- Hermes has a skills registry — this would be a new **MCP-based skill** added to Hermes.
- Zo already has a Facebook integration listed in channels but it appears to be for posting/messaging, not ads analytics. This is a different API surface entirely.

---

## Integration Path

1. Install on Zo: `pip install -r requirements.txt` + `pip install mcp>=1.6.0`
2. Save Meta Access Token to [Settings > Advanced](/?t=settings&s=advanced) as `META_ACCESS_TOKEN`
3. Add to Hermes as a new MCP skill: `facebook-ads-mcp-server`
4. Russell Tuna can then call `get_adaccount_insights`, `get_campaign_insights`, etc. via Hermes Router

---

## Recommendation

**FORGE → SKILL** (integrate into Hermes as a permanent capability)

MIT license, clean code, no proprietary lock-in. Natural fit for the AI Staffing Agency playbook — Russell Tuna reading client ad performance data and producing reports is exactly the kind of white-collar work this business is built to deliver.

**Priority:** 🟡 Worthwhile — add after the core Hermes MCP router is stable.