# JCPaid × The Agency × Hermes

**Purpose:** Multi-client AI employee agency using The Agency framework + Hermes execution + Paperclip companies.

**Stack:**
- `agency-framework/` — The Agency 147 AI agents, fleet dispatch system
- `hermes-workspace/` — Hermes Agent v0.11.0 execution layer
- `paperclip/` — Company generator (real estate, HVAC templates)
- `the-agency/` — Source framework (MIT licensed)

---

## Key Files

| File | Purpose |
|------|---------|
| `AGENCY_README.md` | Original Agency framework docs |
| `agency-framework/agency/tools/` | 50+ CLI tools (dispatch, health, agent-create) |
| `agency-framework/.claude/skills/` | 147 AI agent skills |
| `agency-framework/.claude/commands/` | Agent commands |
| `agency-framework/agency/agents/` | Agent class definitions |

---

## Deployment

```bash
cd /home/workspace/jcpaid
hermes gateway run  # Port 8642
open http://127.0.0.1:3002  # Hermes Workspace
```

---

## Adding New Client

1. Create company with Paperclip
2. Register client in JCPaid dashboard
3. Provision Hermes agent per client
4. Configure API keys per client

---

## Pricing

- $299/mo per client (first 5 clients = $1,495/mo)
- Cost: ~$0 (CPU already paid)
- No per-user SaaS fees