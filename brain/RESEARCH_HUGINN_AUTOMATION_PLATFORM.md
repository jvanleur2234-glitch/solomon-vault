# Huginn — Self-Hosted AI Automation Platform

## Source
- GitHub: https://github.com/huginn/huginn
- Fork: jvanleur2234-glitch/solomon-huginn
- Stars: 24k+ ⭐
- License: MIT
- Language: Ruby on Rails

## What It Is
Open-source event-driven automation platform. Self-hosted alternative to Make.com/Zapier.
Been active since 2013 — battle-tested, production-grade.

## Core Components
- **Agents** — Event consumers/producers. 30+ built-in types.
- **Scenarios** — Workflows linking agents together (like Zapier Zaps)
- **Credentials** — OAuth/API key storage
- **Webhook receiver** — Inbound webhooks as triggers
- **Web UI** — Visual workflow builder

## Built-in Agents (high-value for Solomon OS)
| Agent | Solomon OS Use |
|-------|--------------|
| Website Agent | Scrape any page on a schedule |
| HTTP Agent | Call APIs (RENU API, Stripe, etc.) |
| Email Agent | Send emails via SMTP |
| Slack Agent | Post to Slack channels |
| Twitter Agent | Post tweets, monitor mentions |
| RSS Agent | Monitor RSS feeds |
| JQ Agent | Transform JSON data |
| Trigger Agent | Fire when conditions met |
| Liquid Agent | Template processing |
| Webhook Agent | Receive webhooks |

## Solomon OS Fit
**Score: 9/10**

This directly replaces the crude Solomon Bus JSON file queue. We should:
1. Fork Huginn → `solomon-huginn`
2. Add our Memary memory layer as a new Agent type
3. Replace Job Runner + Bus with Huginn scenarios
4. Expose via Solomon OS web UI

## Status
CLONED — INTEGRATE