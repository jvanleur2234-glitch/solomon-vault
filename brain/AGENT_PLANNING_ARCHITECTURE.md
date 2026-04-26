# Agent Planning Architecture — Solomon OS Integration

*Source: AI Planning Framework for LLM-Based Web Agents (arXiv:2603.12710)*
*Integrated: April 26, 2026*

---

## The Three Planning Strategies

Every agent task can be executed in one of three modes. Solomon OS now explicitly chooses based on task type:

| Strategy | Maps To | Best For | Reliability |
|---|---|---|---|
| **Step-by-Step** | BFS | Open-ended exploration, first-time tasks, learning | 38.41% success but most human-aligned |
| **Tree Search** | Best-First | Multi-path decision problems,权衡 tradeoffs | Moderate, value-function dependent |
| **Full-Plan-in-Advance** | DFS | Well-defined repeatable workflows, production tasks | 89% element accuracy |

---

## Integration Points

### 1. Solomon Bus → Full-Plan-in-Advance (DFS)

**Problem:** Job Runner executes multi-step jobs but has no explicit plan. Long jobs drift from original intent.

**Fix:** Solomon Bus job intake now:
1. Accepts task description
2. Generates complete planned trajectory BEFORE execution
3. Validates plan coherence
4. Executes strictly following plan
5. Replans on divergence (deviation detected)

**Implementation:** `brain/SOLOMON_GUARDIAN.md` contains the validation layer.

---

### 2. Solomon Guardian — Goal Validation Gate

**Critical insight from the paper:** The #1 failure mode is **misread intent** — perfect execution toward the WRONG goal.

Solomon Guardian now validates BEFORE any task execution:

```
Step 0: Guardian Validation Gate
├── Parse: What is the user actually asking for?
├── Confirm: Repeat back the goal in my own words
├── Wait: User confirms or corrects
└── Only then: Pass to execution layer
```

This single gate eliminates the most common failure mode.

---

### 3. The 5 Quality Metrics (Solomon Guardian Reporting)

Beyond pass/fail — Solomon OS now tracks:

| Metric | What It Measures |
|---|---|
| **Recovery Rate** | % of failures where agent self-corrected and completed |
| **Trajectory Efficiency** | Actual steps vs. optimal steps ratio |
| **Plan Coherence** | Does each step logically follow the previous? |
| **Action Validity** | Are actions legal/possible in the target system? |
| **Goal Alignment** | Does final output match original intent? |

**Use case:** Client-facing quality reports showing WHY a task failed and what the system is doing about it.

---

### 4. Plan-as-External-Memory (Context Drift Prevention)

**Problem:** Step-by-step agents lose the original goal after 10-20 steps. Context window fills up.

**Fix:** For long-horizon tasks (>5 steps):

```
At task start:
1. Write plan to /tmp/solomon_plan_<task_id>.md
2. Agent reads this file at EACH step, not from context
3. At step N, agent asks: Does my current action still serve the plan?
4. If no: abort and re-validate at Guardian Gate
```

This makes any task resumable and prevents context drift.

---

### 5. Strategy Selection Heuristic

When Solomon Bus receives a new job, it auto-selects strategy:

```
if (task is well-defined AND repeatable):
    → Full-Plan-in-Advance (DFS)
elif (task has known success criteria AND time-constrained):
    → Tree Search (Best-First)
else:
    → Step-by-Step (BFS) with Guardian validation
```

---

## Architecture Files

- **Guardian Gate:** `brain/SOLOMON_GUARDIAN.md` — validates goal before execution
- **Metrics:** `brain/AGENT_METRICS.md` — 5 quality metrics implementation
- **Plan Memory:** `brain/PLAN_MEMORY.md` — plan-as-external-memory pattern

---

## Source

https://arxiv.org/pdf/2603.12710