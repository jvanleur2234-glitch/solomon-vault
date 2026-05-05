# RD Report: WithOneAI CLI — 250+ Platform Integration Layer

**Source:** x.com/tom_doerr/status/2051408052016808054 (59 likes)
**GitHub:** github.com/withoneai/cli — MIT
**Date:** 2026-05-04

## What It Is

CLI tool that gives AI agents authenticated access to 250+ platforms through a single interface. No API keys, no OAuth flows, no request formats to memorize. One `one add <platform>` command and the agent is connected.

## Key Features

- **250+ platform integrations** — Gmail, Slack, Shopify, HubSpot, Stripe, Notion, and everything else
- **Unified action interface** — Search actions, read docs, execute across any platform with one command structure
- **MCP server auto-installed** — Tools become available to any MCP-compatible agent automatically
- **Multi-step flows** — Chain actions across platforms into reusable workflows
- **Browser auth or API key** — User picks authentication method
- **Per-directory or global** — Works for multi-tenant scenarios

## Pricing

Free tier available. NPM package: `@withone/cli`. Node.js 18+ required.

## For JCPaid

**CRITICAL INTEGRATION.** This is exactly what JCPaid's client delivery layer needs. Instead of building separate integrations for each platform per client, JCPaid agents use WithOneAI CLI as a unified integration layer.

```
JCPaid Agent (Hermes)
    ↓
WithOneAI CLI → 250+ platforms
    ↓
Stripe, Gmail, Notion, HubSpot, etc.
```

**Savings:** Building each integration separately would take weeks. WithOneAI = hours.

## For Hermes

Install as skill: `npx @withone/cli@latest init`. After init, agent has MCP tools for all connected platforms.

## Recommendation

**FORGE IMMEDIATELY.** Clone to /home/workspace/withone-cli/. Integrate as the platform integration layer for JCPaid client agents.

## Status

✅ Cloned to /home/workspace/cli/
