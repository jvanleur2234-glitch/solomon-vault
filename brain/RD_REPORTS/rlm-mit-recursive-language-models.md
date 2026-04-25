# RD Report: Recursive Language Models (RLMs)
**Date:** 2026-04-24  
**Source:** https://x.com/iam_elias1/status/2047606354714808426  
**Paper:** arXiv:2512.24601 | **GitHub:** alexzhang13/rlm  
**Status:** 🔴 CRITICAL — New AI Paradigm

---

## What It Is

RLMs are a task-agnostic inference paradigm that treats long prompts as **external variables** rather than context to be memorized. Instead of cramming documents into a model's context window, you store them outside the model and give the model tools to navigate them.

**Core insight (so obvious it hurts):** Stop putting the document IN the AI's memory. Store it as a Python variable outside. Let the AI write code to search, navigate, and read the parts it needs.

This is exactly how a human expert works with a 10,000-page archive — they don't memorize it, they know how to find what they need.

---

## The Problem It Solves

### Context Rot
The more you pack into a context window, the worse the model performs on things already inside it. Facts blur, middle information vanishes. Massive context windows didn't solve this — they made it worse.

### RAG's Fundamental Flaws
- Retriever guesses which chunks matter BEFORE the AI reads anything
- If the retriever guesses wrong (and it does constantly), the AI never sees what it needed
- Chunking destroys relationships between distant paragraphs
- Full picture gets shredded; AI reassembles blindfolded

### The Numbers
- Standard frontier models on hard long-context benchmarks: near-zero
- GPT-5 on complex code history beyond 75K tokens: couldn't solve 10%
- RLMs on same benchmarks: solved, with double-digit gains
- Successfully handles up to **10M tokens** (100x beyond native context)
- Cost per query: comparable or cheaper than massive context calls

---

## How It Works — Technical Deep Dive

### Architecture Overview

```
User: rlm.completion(prompt)
 │
 ▼
RLM (depth=0)
 ├─ Spawn LMHandler (TCP server, auto port)
 ├─ Create LocalREPL (in-process exec() namespace)
 ├─ Iterate:
 │   a. Send message history → LM backend → get response
 │   b. Extract ```repl``` code blocks from response
 │   c. Execute code in LocalREPL
 │   d. Append stdout/stderr to message history
 │   e. Repeat until FINAL_VAR / limits exceeded
 └─ Tear down handler and environment
```

### Three Core Components

**1. RLM** (`rlm/core/rlm.py`) — the main loop that drives iteration
**2. LMHandler** (`rlm/core/lm_handler.py`) — per-completion TCP server that routes LM API calls
**3. LocalREPL** (`rlm/environments/local_repl.py`) — Python execution environment where model-generated code runs

### The Key Innovation: Code Execution Inside the Loop

The model generates Python code, not just text. The code runs in a REPL that has:
- `llm_query()` — plain LM call (no iteration, just prompt→text)
- `rlm_query()` — spawns a child RLM (recursive, full iteration)
- `FINAL_VAR()` — marks a variable as the final answer
- Custom tools (user-provided functions)

**Example from the quickstart:** The model is given 50,000 lines of random text with a secret number buried in it. It writes code to search the text, find the line, extract the number — without ever "reading" all 50K lines into context.

### Recursive Sub-Calls (The "Recursive" in RLM)

When `rlm_query()` is called from inside the REPL:
- Spawns a **child RLM** with its own handler + REPL
- Child runs its own iteration loop
- Can spawn its own grandchildren up to `max_depth`
- At `max_depth`, falls back to plain `llm_query()`

```
max_depth=3

RLM (depth=0)
 └─ rlm_query() → child RLM (depth=1)
     └─ rlm_query() → child RLM (depth=2)
         └─ rlm_query() → plain LM call (depth=3 >= max_depth, no REPL)
```

Each depth can use a different (cheaper/faster) model via `other_backends`.

### Namespace Layout in the REPL

```
globals:
├── __builtins__ → _SAFE_BUILTINS (eval/exec/input removed)
├── llm_query()         → plain LM call via handler
├── llm_query_batched() → batched plain LM calls
├── rlm_query()         → recursive RLM sub-call
├── rlm_query_batched() → batched recursive sub-calls
├── FINAL_VAR()         → mark a variable as the final answer
├── SHOW_VARS()         → list user-created variables
└── <custom_tools>      → user-provided callable tools

locals (accumulates user variables):
├── context             → alias for context_0
├── context_0           → first context payload
├── context_1, …        → additional contexts (persistent mode)
├── history             → conversation history
└── <user variables>    → anything created by model code
```

### Code Execution Is In-Process

LocalREPL executes model-generated code via Python's `exec()` — NOT a subprocess. This means:
- **Fast**: No process spawn overhead
- **Persistent namespace**: Variables created in one code block persist in the next
- **Soft sandbox**: Dangerous builtins removed, but not a security boundary (not for untrusted code)

For isolation, there are cloud sandbox options: Docker, Modal, Prime Intellect, Daytona, E2B.

---

## What the Code Provides

### Install
```bash
pip install rlms
```

### Basic Usage
```python
from rlm import RLM

rlm = RLM(
    backend="openai",
    backend_kwargs={"model_name": "gpt-5-nano"},
    verbose=True,
)

result = rlm.completion(
    "The context contains ~50k lines of random text with a single line "
    "matching the pattern SECRET_NUMBER=<digits>. Find and return ONLY the "
    f"numeric value.\n\n{haystack}"
)

print(result.response)
```

### With Custom Tools
```python
def fetch_stock_price(symbol: str) -> dict:
    # ...mock data...
    return prices.get(symbol.upper(), {"error": "not found"})

rlm = RLM(
    backend="openai",
    custom_tools={
        "fetch_stock_price": {
            "tool": fetch_stock_price,
            "description": "Fetch current stock price for a symbol",
        },
    },
)

result = rlm.completion("What's the price of AAPL?")
```

### Environment Options
- `local` (default) — in-process exec(), same Python interpreter
- `docker` — separate Docker container
- `modal` — Modal Sandboxes (cloud)
- `prime` — Prime Intellect Sandboxes (beta, slow)
- `daytona`, `e2b` — other cloud sandbox options

---

## Comparison with Hermes/Solomon OS

### What Hermes Already Has
- Agentic loop with tool use
- File system access
- Code execution (likely sandboxed)
- Sub-agent spawning (?)
- Long context handling via standard RAG

### What RLMs Add That Hermes Doesn't Have

| Capability | Hermes (likely) | RLM |
|---|---|---|
| Iterative REPL-driven code execution | ❓ | ✅ Core mechanism |
| Recursive sub-agents (RLM spawning RLM) | ❓ | ✅ Native |
| Context stored as external variable | ❌ RAG / in-context | ✅ |
| Model writes code to navigate documents | ❌ | ✅ |
| Handles 10M+ tokens | ❌ | ✅ |
| Trajectory logging + visualizer | ❌ | ✅ Built-in |

### Key Question: Does Hermes Already Do This?
The SOLOMON_OS.md describes a 24/7 AI agent with workspace awareness, command execution, and job management. If Hermes already has an iterative loop where the model can spawn sub-tasks and use tools, RLM's key contribution is the specific pattern of:
1. Storing large context as external variables (not in prompt)
2. Giving the model code execution tools to navigate those variables
3. Recursive sub-agents with depth-based routing

---

## Integration Possibilities for Solomon OS

### Option A: Add RLM as a Hermes Capability
- Install `pip install rlms` in the Hermes environment
- Create an RLM wrapper tool that Hermes can call for long-context tasks
- The agent would use RLM when it needs to process large files/workspaces
- Custom tools could expose Solomon OS services (file search, job status, etc.)

### Option B: Study the Pattern and Implement Natively
- RLM's core insight is simple enough to implement without the library
- Store workspace files as external variables
- Give the agent code execution + search tools
- Track recursion depth for sub-agent spawning

### Option C: Use as Evaluation Benchmark
- Clone the repo, run the benchmarks
- Measure Hermes against RLM on the same long-context tasks
- Identify where Hermes falls short

---

## Risks and Caveats

1. **Security**: In-process exec() with `__builtins__` restriction is soft sandbox only. Not for untrusted code.
2. **Beta sandboxes**: Prime Intellect sandboxes are marked beta with slow runtimes.
3. **Skepticism valid**: Critics say it's "just RAG with recursive re-reading" and that context drift compounds. The paper's results are strong but the debate is ongoing.
4. **Post-training required for best results**: RLM-Qwen3-8B (the post-trained version) outperforms baseline significantly. Using RLM with a non-fine-tuned model may be less impressive.
5. **Depth tradeoffs**: Each recursive level costs more. max_depth=1 is cheap; max_depth=3+ adds significant latency and cost.

---

## Recommendation: FORGE

RLMs are worth integrating into Hermes as a **first-class capability**. The pattern is clean, the library is well-engineered, and the use case (large workspace navigation) is exactly what Solomon OS needs.

**Next steps:**
1. Install `rlms` in the Hermes environment
2. Create an RLM-powered file search tool that Hermes can call
3. Expose Solomon OS services (job queue, client data, workspace files) as custom_tools
4. Test against large workspace (e.g., all of `/home/workspace`) to verify 10M token handling
5. Consider whether recursive depth=2+ provides value over depth=1 for Solomon OS tasks

**Watch:** Whether the Prime Intellect "agents managing context over weeks/months" vision materializes — that's the long-term version of this idea and directly relevant to a 24/7 autonomous agent.

---

## Sources
- https://arxiv.org/abs/2512.24601 — Paper
- https://github.com/alexzhang13/rlm — Code
- https://x.com/iam_elias1/status/2047606354714808426 — Viral thread