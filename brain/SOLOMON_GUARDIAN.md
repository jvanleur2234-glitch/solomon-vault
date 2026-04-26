# Solomon Guardian — Goal Validation Gate

*Integrated from: AI Planning Framework for LLM-Based Web Agents (arXiv:2603.12710)*
*Created: April 26, 2026*

---

## Purpose

The #1 failure mode in LLM-based agents is **misread intent** — perfect execution toward the WRONG goal.

Solomon Guardian is the gate that sits before ANY task execution. It answers one question: **"Do I understand what the user actually wants?"**

---

## The Guardian Validation Flow

```
USER INPUT
    ↓
[Step 0: Parse Intent]
    ↓
[Step 0.5: Confirm Intent] ← Guardian Gate
    ↓
[Step 1: Execute Task]
    ↓
[Step N: Validate Output Against Original Goal]
    ↓
DELIVER
```

---

## Step 0 — Parse Intent

When a task comes in, the agent:
1. Reads the raw request
2. Identifies: What is the END STATE the user wants?
3. Identifies: What does success look like?
4. Identifies: Are there any constraints or preferences?

Output: One sentence describing the goal. Example: "User wants a cold email sequence for 50 real estate agents in Chicago, casual tone, focused on listing appointments."

---

## Step 0.5 — Confirm Intent (THE GATE)

**The agent repeats back the goal in its own words:**

"Alright, so I understand you want me to create a cold email sequence for 50 Chicago real estate agents. The emails should be casual in tone and focused on booking listing appointments. You'll review them before any go out. Is that right?"

**User confirms or corrects → Task proceeds**
**User corrects → Update understanding → Re-confirm**

---

## Step N — Output Validation

After task completion, before delivering:
1. Re-read original goal statement
2. Ask: Does this output actually serve that goal?
3. If no: discard output and restart from Step 0

---

## Why This Gate Exists

| Failure Mode | Without Guardian | With Guardian |
|---|---|---|
| Misread intent | Perfect email for wrong ICP | Goal confirmed before writing |
| Context drift | Original goal lost in step 15 | Plan-as-external-memory keeps goal |
| Scope creep | Task balloons beyond original ask | Guardian stops at confirmed scope |
| Wrong metric | Optimize wrong KPI | Goal alignment metric enforced |

---

## Implementation

Every Hermes skill execution and Russell Tuna response passes through:

```python
def guardian_gate(task_description, user_confirmation_required=True):
    # Step 0: Parse intent
    parsed_goal = parse_intent(task_description)
    
    # Step 0.5: Confirm (if required)
    if user_confirmation_required:
        confirmed_goal = confirm_with_user(parsed_goal)
        if not confirmed_goal:
            return {"status": "blocked", "reason": "user_correction"}
    else:
        confirmed_goal = parsed_goal  # Trust but verify mode
    
    # Step N: Output validation function
    def validate_output(output):
        return output_serves_goal(output, confirmed_goal)
    
    return {"status": "cleared", "goal": confirmed_goal, "validate": validate_output}
```

---

## Guardian Status

This is an ARCHITECTURAL PATTERN — not a separate service. 
Every agent in Solomon OS implements the Guardian Gate in their own execution flow.