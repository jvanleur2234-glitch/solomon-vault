# SkillClaw → Hermes Integration Spec

*Date:* 2026-04-21
*Source:* https://github.com/AMAP-ML/SkillClaw
*Purpose:* Wire SkillClaw into Hermes skills registry for collective skill evolution

---

## What SkillClaw Does

SkillClaw sits between Hermes and the LLM API as a local proxy:
- **Client proxy** intercepts Hermes → LLM requests, records sessions
- **Evolve server** reads sessions from shared storage, evolves skills, writes back to `~/.hermes/skills`
- Skills auto-deduplicate, auto-improve, cross-pollinate across sessions

## Architecture

```
Hermes Agent
    │
    ▼
~/.hermes/config.yaml → SkillClaw Proxy (port 30000)
    │
    ├── Session captured → shared storage (local/S3/OSS)
    │
    ▼
skillclaw-evolve-server
    │
    ├── workflow engine: Summarize → Aggregate → Execute
    └── agent engine: OpenClaw-driven workspace
    │
    ▼
~/.hermes/skills/ (evolved SKILL.md files)
    │
    ▼
Hermes picks up evolved skills next session
```

## Integration Steps

1. Install SkillClaw:
```bash
cd /home/workspace/SkillClaw
bash scripts/install_skillclaw.sh
source .venv/bin/activate
```

2. Setup with Hermes integration:
```bash
skillclaw setup
# → Choose "hermes" for CLI agent
# → Proxy port: 30000 (default)
# → Local shared storage: ~/.skillclaw/local-share
```

3. SkillClaw rewrites `~/.hermes/config.yaml` to point Hermes at SkillClaw proxy

4. Start client proxy:
```bash
skillclaw start --daemon
skillclaw status
```

5. Start evolve server (local, single-user):
```bash
skillclaw-evolve-server --use-skillclaw-config --interval 300 --port 8787
```

6. Verify:
```bash
hermes chat -Q -m skillclaw-model -q "Reply with exactly HERMES_SKILLCLAW_OK"
curl http://127.0.0.1:30000/healthz
```

## For Solomon OS Multi-Agent

Each agent (Zo, Russell Tuna, Hermes S1/S2/S3) can run its own SkillClaw client pointing at same shared storage → skills unify across all agents.

## Status
- [x] Cloned to /home/workspace/SkillClaw/
- [ ] Hermes integration pending
- [ ] Evolve server startup pending