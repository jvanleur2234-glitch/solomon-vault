# Per-Agent Brain Architecture

**Date:** April 19, 2026
**Inspired by:** Isaak Freeman's connectomics thesis — every neuron has a synapse map, every agent skill needs a brain map.

---

## The Core Insight

**Not one brain for all agents. One brain PER agent/skill.**

Just like the human brain:
- Motor cortex handles movement
- Visual cortex handles sight
- Hippocampus handles memory
- Each is specialized, but they share a common substrate

Each Solomon OS agent/skill gets its own persistent memory directory:
```
solomon-vault/brains/
  russell-tuna/       ← personal AI memory
  hermes/             ← skills agent brain
  solomon-bus/        ← message queue brain
  solomon-guardian/   ← security agent brain
  solomon-air/        ← VoIP agent brain
  solomon-browser/    ← browser agent brain
  icarus/             ← cross-agent memory broker
  evolver/            ← self-improvement brain
  [skill-name]/       ← each skill gets its own brain
```

## What Each Agent Brain Contains

### Per-agent brain structure
```
brain/
  memory/
    hot/          ← current session (ephemeral)
    cold/         ← lessons learned (persistent)
      lessons/    ← verified learnings
      staging/    ← unverified, pending confirmation
    shared/       ← cross-agent learnings (read-only)
    identity.md   ← who this agent is, purpose, values
  skills/         ← skill-specific memory
  context/        ← current task context
  history/        ← past interactions log
  cache/          ← vector embeddings of all above
```

### Cross-agent memory (Icarus)
```
icarus/
  shared-memory/   ← things all agents know
  handoff/        ← what this agent learned for others
  receive/        ← what other agents learned for this one
```

## The Memory Protocol

### Write (after each interaction)
1. Agent completes task
2. Write result to `brain/memory/cold/lessons/[task-type].md`
3. If uncertain, write to `brain/memory/cold/staging/`
4. Publish key learnings to Icarus shared memory

### Read (at session start)
1. Agent loads identity (`brain/identity.md`)
2. Load recent cold memories (`brain/memory/cold/lessons/`)
3. Check Icarus for cross-agent learnings
4. Load task-specific context from `brain/context/`

### Evolver Integration
Each agent brain has an Evolver loop:
- Weekly: review lessons → promote staging to verified
- Monthly: extract patterns → update identity
- Quarterly: cross-agent audit → shared pool update

## Implementation Priority

1. **Russell Tuna brain** — highest value, most usage
2. **Hermes skills brain** — impacts all skill execution
3. **Icarus shared memory** — connects all brains
4. **Solomon Bus brain** — message queue learning
5. **Skill-level brains** — each major skill

## Brain Files for Russell Tuna (First Implementation)

```
solomon-vault/brains/russell-tuna/
  identity.md          ← "I am Russell Tuna, personal AI assistant..."
  memory/
    hot/              ← current session state
    cold/
      lessons/        ← verified task learnings
      staging/       ← pending confirmations
    shared/          ← cross-agent learnings
  context/
    active-tasks.md  ← what's currently working on
    recent-wins.md   ← what worked recently
  history/
    sessions/        ← session logs
    patterns/         ← recurring task patterns
```

## The Grand Vision

Every skill, every agent, every worker — all with persistent memory that:
- Survives restarts
- Compounds over time
- Specializes to their domain
- Shares learnings with siblings
- Never loses context

This IS the Second Brain. Not one brain. A society of specialized brains.

---

*Build spec inspired by connectomics thesis — pdf.isaak.net/thesis*
