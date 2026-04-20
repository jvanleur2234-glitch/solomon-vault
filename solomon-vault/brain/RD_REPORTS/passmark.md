# RD Report: Passmark — AI Playwright Regression Testing Library

**Date:** 2026-04-20  
**Source:** [X @bug0inc](https://x.com/bug0inc/status/2045886906953781408)  
**Stars:** 374 | **License:** FSL-1.1-Apache-2.0  
**Recommendation:** INTEGRATE (architecture patterns, not code — FSL license)

---

## What It Is

Passmark = Playwright + AI that writes and executes browser regression tests from natural language. No selectors to maintain. No test prompts to update when the UI changes. The AI adapts.

**Stack:** TypeScript, Playwright, Redis, Claude + Gemini (or any AI gateway)

---

## How It Works

### Core Flow
```
Step Request → Cache Check → AI Execution → Cache Result → Assertions
                                    ↓              ↓
                              miss          fail (auto-heal)
```

1. **Cache check** — Redis stores successful step executions keyed by `userFlow + step.description`
2. **Cache hit** → execute directly, no AI call
3. **Cache miss** → AI executes the step via Playwright
4. **Success** → cache the result
5. **Cached step fails** → auto-heal: re-run via AI, update cache

### Multi-Model Assertions
```
Assertion runs Claude + Gemini in parallel
    ↓
If they agree → pass
If they disagree → arbiter model (Gemini 3.1 Pro) decides
```
Consensus-based = no false positives from single-model bias.

---

## Key Architecture Patterns

### 1. Redis Step Caching
- Only single-step AI executions are cached (multi-step flows vary too much)
- Bypassed on Playwright retries (fresh run = fresh data)
- Key insight: **cache by intent, not by selector** — same natural language description = same action

### 2. Auto-Healing on Cache Failure
```
cached_step fails
    → re-invoke AI with same step description
    → new result replaces cached result
    → next run uses the fixed action
```
No stale selectors. No manual test updates.

### 3. Multi-Model Consensus
```typescript
// Two models run the same assertion simultaneously
// Third model (arbiter) breaks ties
const result = await assert({
  page,
  assertion: "Dashboard shows 3 active projects",
  expect,
});
```

### 4. Placeholder System
```
{{run.email}}        → random email per test
{{run.dynamicEmail}} → shared across runSteps with same executionId
{{email.otp:...}}    → extract from received email
{{data.key}}         → stored in Redis per project
```

### 5. AI Gateway Abstraction
```typescript
configure({
  ai: { gateway: "vercel" | "openrouter" | "cloudflare" | "none" }
});
```
Swap providers without changing test code. Currently supports Vercel AI Gateway, OpenRouter, Cloudflare AI Gateway, or direct provider SDKs.

---

## For Solomon OS / Clicky

**Direct overlap with the browser-recorder skill:**
- browser-recorder records walkthroughs (actions + verification)
- Passmark executes AI-driven tests with auto-healing
- Together: **Clicky = browser-recorder recording + Passmark playback engine**

### What to Adopt

| Passmark Pattern | Clicky Application |
|-----------------|-------------------|
| Redis step caching | Cache walkthrough steps keyed by flow+step intent |
| Auto-healing on fail | Re-try failed steps with same description, update .clicky |
| Claude+Gemini consensus | Dual-model verification of walkthrough completion |
| AI Gateway abstraction | Swap Ollama/Groq/OpenRouter without changing walkthrough code |
| Email placeholder system | For walkthroughs that require email verification |

### What NOT to Copy (FSL License)
- Source code directly — FSL-1.1-Apache-2.0 has use restrictions
- Architecture patterns are fine to adopt independently

### Implementation Path
1. Clone to `/home/workspace/Skills/passmark/` for pattern reference
2. Add Redis caching layer to `play.py`
3. Add multi-model verification to `verify.py`
4. Adopt placeholder system for walkthrough params

---

## Strategic Fit

| Dimension | Score | Notes |
|-----------|-------|-------|
| **JCPaid / Solomon OS** | ★★★★☆ | Core regression testing for Solomon Browser |
| **Clicky walkthrough player** | ★★★★★ | Playback engine already designed this way |
| **JackConnect** | ★★★☆☆ | Regression test client flows before deploying |
| **Solomon Browser** | ★★★★☆ | Auto-healing = self-healing browser |
| **License risk** | ★★☆☆☆ | FSL — adopt patterns, don't copy code |

---

## Status

- **Queued:** task_queue.json entry added
- **Next step:** Clone to `/home/workspace/Skills/passmark/` for pattern study
- **See also:** `browser-recorder` skill (recording layer), `clicky` skill (playback layer)

*Last updated: 2026-04-20*