---
description: "Check status of all live services in Solomon OS."
---
Check live service status for Solomon OS:

1. Read `brain/Services.md` for known services
2. Run health checks on:
   - Russell Tuna bot (telegram ping)
   - MoneyPrinterTurbo (localhost:8080)
   - Ollama (localhost:11434)
   - Solomon Bus (check PID)
3. Report status table:
   - Service name
   - Status (LIVE/DOWN/DEGRADED)
   - Response time or error
4. Update `brain/Services.md` with check results + timestamp
