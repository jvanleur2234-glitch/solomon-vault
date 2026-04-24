# R&D Report: useSend

**URL:** https://github.com/usesend/useSend  
**Date Saved:** 2026-04-24  
**Stars:** 4.2k | **Forks:** 361 | **License:** AGPL-3.0  
**Status:** Active (v1.9.2, Mar 22 2026)

---

## What it is

Open source email sending infrastructure. Like Resend/SendGrid/Postmark but self-hostable. Uses AWS SES under the hood but provides a full dashboard + API layer on top.

## Tech Stack

Next.js, Prisma, Tailwind, shadcn/ui, NextAuth.js, tRPC, Hono (public API), Redis (queue)

## Key Features

- Add domains, transactional mails, marketing/bulk emails
- REST API + SMTP support
- Dashboard with delivered/opened/clicked/bounced analytics
- Schedule API, webhook support, inbound email
- BYO AWS credentials (bring your own SES)
- Self-hostable with Docker
- Email editor (tiptap + jsx-email + maily.to inspired)

## Relevance to Solomon OS

**Potential use:** Could replace Resend as the email sending layer for Solomon OS client outreach, invoice reminders, etc. Self-hostable = no per-email costs, just AWS SES costs.

**Not immediately needed:** We already have Resend integrated. But if we ever want to self-host email sending to cut costs or own the infrastructure, useSend is a solid option.

**Comparison to what we have:**
- Current: Resend (managed, API-based, ~$20/mo for decent volume)
- useSend: Self-hosted, AGPL, requires AWS SES + self-management

## Recommendation

**SKILL** — Worth noting as a cost-saving option if we ever hit Resend pricing limits or want a fully self-hosted email stack for clients. Not urgent. Keep in the back pocket.

Watch for: v2 release (they're in beta and building fast — 62 releases already)