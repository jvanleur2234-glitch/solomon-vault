# JCPaid × The Agency × HermesOS

**Purpose:** Multi-client AI employee agency. One Hermes handles all clients. Clients use holaOS as their dashboard.

**The Stack:**
- `holaOS/` — Client desktop app (open agent OS)
- `agency-framework/` — The Agency 147 AI agents + fleet dispatch
- `hermes-workspace/` — Hermes Agent v0.11.0 execution layer
- `the-agency/` — Source framework (MIT licensed)
- `here.now/` — Per-client memory (10GB, permanent)

**How it works:**
```
Client PC (holaOS) ← → Hermes (one instance, all clients) ← → here.now memory
                                              ↑
                                    The Agency (147 agents, one-per-task)
```

**Pricing:**
- $299/mo per client (1 Hermes = infinite clients)
- Cost: ~$0 (CPU already paid)
- here.now: $5/mo per client for extra storage

**Deployment:**
```bash
hermes gateway run  # Port 8642
# holaOS connects via WebSocket
```

**Competitive positioning vs HermesOS:**
- HermesOS: $9.99-$19.99/mo, crypto/token required, cloud-only
- JCPaid: $299/mo flat, no crypto, client owns their data + here.now memory
- We win on: simplicity, permanence, no token speculation