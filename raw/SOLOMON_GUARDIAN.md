# CYBER GUARDIAN OS — ARCHITECTURE v2

## PURPOSE
Guardian is Solomon OS's autonomous defensive AI — protects all systems 24/7, detects threats, responds in real-time, and self-improves endlessly.

## 🔴 CORE INNOVATION — ADVERSARIAL SELF-IMPROVEMENT LOOP

The Guardian runs TWO parallel teams at all times:

**DEFENSE TEAM** — Protects, detects, responds, hardens
**ATTACK TEAM** — Constantly penetrates, exploits, breaks, reports

The ONLY rule: **Attackers must win.** If a vulnerability is found, the system learns from it, patches it, and hardens. The attack team NEVER stops. Loop never ends.

---

## ADVERSARIAL CYCLE (runs 24/7, no human intervention)

1. **Attacker probes** — Find new vulnerability, zero-day, misconfiguration, or logic flaw
2. **Attacker exploits** — Gains access, escalates privileges, moves laterally, exfiltrates data, or disrupts service
3. **Attack registers** — Alert fired with full context: vector, payload, root cause, impact
4. **Guardian learns** — New rule created, patch deployed, model retrained on attack signature
5. **Defense strengthens** — System is now immune to that attack vector
6. **Attacker adapts** — Finds new vector the Guardian hasn't seen
7. **Loop repeats** — Forever. No finish line.

---

## ATTACK TEAM MODULES

### Recon Agent
- Port scans, DNS enumeration, service fingerprinting, OSINT on infrastructure
- Maps the attack surface continuously
- Tools: nmap, masscan, amass, subfinder, shodan, curl banners

### Exploit Agent
- Attempts known exploits against discovered services
- Tests for OWASP Top 10, CVEs with available PoCs
- Brute forces authentication (SSH, HTTP, API endpoints)
- Tools: metasploit, sqlmap, commix, social-engineer-toolkit, hydra

### Vulnerability Research Agent
- Fuzzes inputs, finds logic flaws, identifies zero-days
- Tests for race conditions, injection attacks, authentication bypasses
- Analyzes patch diffs of open-source dependencies for backdoors

### Red Team Agent
- Simulates real adversary TTPs (Mitre ATT&CK)
- Phishing via SMTP server, credential harvesting
- Lateral movement via discovered credentials
- Data exfiltration simulations

### Living Off the Land Agent
- Uses only built-in system tools (LOLbins)
- Tests if defenders can detect basic system abuse
- Fileless malware simulation

---

## DEFENSE TEAM MODULES

### Hardening Agent
- Applies patches, locks down configs, removes unnecessary services
- Enforces MFA, rotates credentials, tightens firewall rules
- Implements least-privilege access controls

### Detection Agent
- SIEM rules, YARA signatures, behavioral ML anomaly detection
- eBPF kernel monitors, file integrity monitoring
- Network traffic analysis, DNS tunneling detection

### Response Agent
- Isolates compromised systems automatically
- Kills malicious processes, blocks IPs, revokes sessions
- Prevents lateral movement in real-time

### Forensics Agent
- Analyzes successful breaches for root cause
- Generates attack timeline, impact assessment
- Extracts IOCs for threat intel

### Threat Intel Agent
- Aggregates indicators from all successful attacks
- Enriches with VirusTotal, AlienVault OTX, Shodan
- Generates actionable signatures for detection

---

## SELF-IMPROVEMENT ENGINE

After EVERY successful attack:
1. Full debrief: what happened, how it was exploited, what failed
2. Root cause analysis — was it a config, a code bug, a logic flaw, a missing patch?
3. Fix deployed automatically within minutes
4. Detection rule created for that exact attack pattern
5. Attack team briefed: that vector is now closed, find another
6. Defense team briefed: new baseline, stay alert for variants
7. Cycle count incremented — system gets harder to breach over time

---

## EVOLVER INTEGRATION — GEP Self-Evolution Engine

**Repo:** github.com/EvoMap/evolver (5K stars, GPL-3.0)
**Forked:** jvanleur2234-glitch/evolver
**Install:** `cd evolver && npm install && node index.js --review`

### The Full Self-Improvement Loop (Wired)

```
Guardian detects attack (eBPF, behavioral AI, threat intel feeds)
        ↓
Icarus shared memory (signal shared across ALL agents instantly)
        ↓
Evolver scans error logs → selects matching Gene (fix template)
        ↓
Evolver emits GEP prompt → applies fix to source code/config
        ↓
Human-in-loop review mode (review flag = true, whitelist-only, 180s timeout)
        ↓
Approved → deployed. Rejected → logged for manual review.
        ↓
agentic-stack graduates/rejects the lesson (graduate.py/reject.py)
        ↓
Next interaction = smarter from all past mistakes
```

### How Each Piece Fits

| Component | Role in Guardian Loop |
|-----------|----------------------|
| **Guardian Attack Team** | Probes → finds vulnerability → fires alert |
| **Guardian Defense Team** | Responds → hardens → logs root cause |
| **Icarus** (icarus-daedalus) | Shares attack signal across ALL agents instantly |
| **Evolver** (5K stars, GEP) | Scans logs → selects Gene → emits GEP → applies fix |
| **agentic-stack** | Reviews AI-generated lessons, graduates verified patterns |
| **Hermes** | Applies fixes, runs skills, reports outcomes |

### Evolver Gene Selection (How It Works)
- Gene = fix template mapped to error pattern
- Evolver reads error class → finds matching Gene → generates GEP prompt
- GEP prompt = natural language description of the fix needed
- Fix applied to codebase → review mode holds it until human approves
- Approved = deployed. System is now immune to that vector.

### Safety
- `--review` flag = human-in-loop holds every change
- Whitelist-only commands (no rm -rf, no chmod 777)
- 180s timeout per fix
- Reviewer gets: error description, Gene used, GEP prompt, diff preview

### Integration Commands

```bash
# Start Evolver in review mode
cd /home/workspace/evolver && node index.js --review

# Wire Icarus → Evolver
echo "export EVOLVER_ENABLED=true" >> ~/.solomon/env

# Test the loop end-to-end
hermes --test self-improvement-loop
```

---

## ICARUS INTEGRATION — Cross-Agent Shared Memory

**Repos:** 
- github.com/esaradev/icarus-daedalus (249 stars, MIT) 
- github.com/esaradev/icarus-plugin (51 stars, MIT)
**Forked:** jvanleur2234-glitch/icarus-daedalus + jvanleur2234-glitch/icarus-plugin

### How Icarus Powers the Loop

```
Guardian detects attack → Icarus fabric_write (attack signal)
        ↓
All agents read the attack signal → Hermes, Russell Tuna, every agent knows
        ↓
Evolver scans → sees the attack signal → selects Gene
        ↓
Fix applied → Icarus fabric_write (fix deployed, new detection rule)
        ↓
All agents read the fix → system-wide immunity update
```

### Fabric Commands (How Agents Talk)

```bash
# Guardian writes attack signal
fabric_write guardian hot attack "DETECTED: SQL injection vector in /api/users"

# All agents read
fabric_read hermes hot

# Evolver searches for matching Gene
fabric_search "SQL injection"

# Fix deployed — write to cold (permanent lesson)
fabric_write evolver cold fix "SQL injection → parameterized queries deployed"
```

### Memory Tiers (Auto-Curation)
- **Hot** (< 24h): Active attacks, live threats
- **Warm** (1-7 days): Recent fixes, lessons in validation
- **Cold** (> 7 days): Verified permanent immunity

---

## GOVERNANCE

- **The ONE rule**: Attackers must always win eventually — that is the point
- **Speed requirement**: Fix must be deployed before next attack cycle (typically < 5 minutes)
- **Transparency**: Every attack logged publicly, every fix documented
- **Zero vanity**: If no attacks are succeeding, the attack team is not trying hard enough
- **Learning priority**: Every vulnerability discovered becomes a permanent immunity

---

## STACK

- Ollama (local LLMs for attack/reasoning)
- Python agents with tool access (nmap, metasploit, yara, ebpf, etc.)
- Evolver — self-evolution engine (scans, Gene selection, GEP prompts)
- Icarus — shared memory across all agents (fabric_write/read/search)
- agentic-stack — lesson review protocol (graduate.py/reject.py)
- PostgreSQL audit log
- Redis task queue
- Prometheus + Grafana dashboards
- eBPF for kernel-level monitoring
- AppArmor / SELinux profiles
- Crowdstrike-style behavioral AI detection

---

*Last updated: April 19, 2026 — Evolver + Icarus wired into the self-improvement loop*
