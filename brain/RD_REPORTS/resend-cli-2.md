# RD Report: Resend CLI 2.0

**URL:** https://x.com/zenorocha/status/2044412765830627402
**Date:** April 15, 2026
**Researcher:** Zo (Telegram)
**Priority:** 🟡 Worthwhile — clear use case, fits email pipeline

---

## What It Is

Resend is an email API platform (by Zeno Rocha, creator of React Email). CLI 2.0 ships:
- **Send emails using local React files** (`.tsx` / `.jsx`) — React Email templates locally, sent via CLI
- **Automations and events** — multi-step workflows against your own data, terminal-based
- **Webhook listening** — `resend listen` for inbound webhooks
- **Built-in Skills for AI agents** — AI agents can invoke Resend actions directly

---

## How It Works

```bash
# Send an email from a React file
resend emails:send --from you@domain.com --react ./email.tsx

# Create an automation
resend automations:create

# Listen for webhooks
resend listen
```

Resend handles delivery, templates, and analytics. CLI is the new interface (no web dashboard required).

---

## How It Compares to What We Have

| Capability | Solomon OS | Resend CLI 2.0 |
|---|---|---|
| Email sending | Gmail API (Zo) | ✅ Better deliverability, React templates |
| Transactional email | ❌ Not set up | ✅ Built-in |
| Email automations | Manual / rule-based | ✅ CLI workflow builder |
| Webhook receiver | Zo Space API route | ✅ `resend listen` built-in |
| AI agent integration | Zo API + Tools | ✅ Native "Skills" for agents |

---

## What We'd Use It For

1. **Professional outbound email** — Better deliverability than Gmail. Could replace Zo's `send_email_to_user` for cold outreach, client comms, invoices.
2. **Email automation pipelines** — Multi-step sequences triggered by Solomon Bus events.
3. **Webhook-driven alerts** — `resend listen` as a lightweight receiver instead of spinning up a Zo Space route.
4. **AI agent email actions** — Russell Tuna / Hermes could use Resend Skills to send emails autonomously.

---

## Risks / Caveats

- **Requires Resend account + API key** — add to secrets
- **We already have Gmail** — marginal value unless we're sending high volume or need better deliverability
- **Not a fit for real-time Telegram alerts** — Resend is email, not push

---

## Recommendation

**SKILL** — not urgent, but worth installing the CLI and testing. Could replace Gmail for outbound professional email (invoices, client outreach). Add to Hermes as a skill if we ever need professional-grade email sending at scale.

Install: `npm install -g resend`

---
*Last updated: April 15, 2026*