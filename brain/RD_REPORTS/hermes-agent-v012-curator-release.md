# RD Report: Hermes Agent v0.12.0 "The Curator Release"

**Date:** 2026-04-30
**Type:** Open Source AI Agent Framework Update
**Recommendation:** INTEGRATE — Multi-profile dashboard patterns for JCPaid + update Hermes capabilities

---

## What It Is

Hermes Agent v0.12.0 — "The Curator Release" — dropped April 30, 2026 by Nous Research. Major new features:

- **Profiles Dashboard** — Web UI for managing multiple agent configurations (create/rename/delete)
- **SOUL.md in-browser editing** — edit agent identity/personality directly in the UI
- **Profile REST API** — programmatic profile management
- **i18n Chinese support** — internationalization
- **Bug fixes + test coverage** — stability improvements

**Engagement:** 933 likes, 139K views on main announcement. Community actively building on it.

---

## Notable: Human + AI Pair Programming PR

@VinceZcrikl contributed a PR that shipped in this release. His workflow:
- He described requirements (natural language)
- Hermes wrote the code AND unit tests
- He reviewed and iterated
- Hermes continued until it was ready

This is JCPaid's service model in miniature — a human directing an AI that does the execution. Directly relevant to positioning.

---

## How It Compares to What We Have

| Feature | Hermes v0.12.0 | JCPaid needed |
|---|---|---|
| Multi-profile management | ✅ Web UI dashboard | ✅ Build for clients |
| SOUL.md editing in UI | ✅ In-browser | ✅ Client dashboard |
| Per-profile configuration | ✅ Create/rename/delete | ✅ 147 agents per client |
| REST API for profiles | ✅ | ✅ Client automation |
| i18n | ✅ Chinese | Needed for scale |

---

## What We'd Use It For

1. **Profiles dashboard as JCPaid client portal template** — Hermes just proved the UX. We replicate the pattern for client AI employee management.

2. **SOUL.md live editing** — clients choose their AI employee personality via UI, not raw files. Critical for non-technical customers.

3. **The "human describes + AI builds" pattern** — position JCPaid as the service that makes this work reliably for business clients, not just developers.

---

## Integration Points

- Update `HERMES_CAPABILITIES.md` with v0.12.0 feature list
- Clone Profile dashboard pattern for `solomon-vault/brain/JCPaid_DASHBOARD_SPEC.md`
- The 147 Agency agents each need profile management

---

## Competitive Note

HermesOS (competitor, launched ~April 29) charges $9.99-$19.99/mo with crypto requirement. Hermes Agent (open source, Nous Research) just added Profiles — free, self-hosted, no crypto. The gap between "cloud AI agent" and "self-hosted AI agent" is closing fast. JCPaid's differentiation: flat $299/mo, no crypto, holaOS desktop integration, here.now permanent memory.

**Status:** RD Complete — INTEGRATE