# RD_REPORT: TRINITY — An Evolved LLM Coordinator (Sakana AI)

## What It Is
**TRINITY** — A multi-agent AI coordination system where a lightweight evolved coordinator orchestrates a diverse pool of specialized state-of-the-art models. Published as a conference paper at **ICLR 2026**.

The coordinator (<20K learnable params) dynamically assigns one of three roles to an LLM at each reasoning step:
1. **Thinker** — Devises high-level strategies, analyzes current state
2. **Worker** — Executes concrete problem-solving steps
3. **Verifier** — Evaluates if the current solution is complete and correct

86.2% pass@1 on LiveCodeBench at time of publication. Zero-shot transferred to 4 unseen tasks (AIME, BigCodeBench, MT-Bench, GPQA), surpassing every individual constituent model including GPT-5 and Gemini 2.5-Pro.

## What We'd Use It For

1. **Hermes Agent internal architecture** — The Thinker/Worker/Verifier tri-role pattern maps directly to how Solomon OS could structure multi-agent reasoning loops
2. **Russell Tuna task routing** — Evolved coordinator concept for routing client requests to specialized sub-agents
3. **Sakana Fugu product study** — Sakana's commercial multi-agent product is built on TRINITY; studying the paper informs our competitive positioning
4. **Evolutionary training exploration** — If we ever need to fine-tune a coordinator, the paper reveals that gradient-based methods fail here and evolutionary algorithms succeed

## Comparison to What We Have
- **vs Agentrail / agency-agents**: Agentrail is a TypeScript agent harness with mailboxing + Docker isolation. TRINITY is about coordinating *multiple LLMs* as specialized roles within one reasoning trace. Different layer entirely (TRINITY is coordination, Agentrail is orchestration infrastructure).
- **vs Solomon OS multi-agent concept**: Solomon OS has the concept of specialized agents (Russell Tuna, Russell Tuna R&D). TRINITY provides the actual mechanism — an evolved coordinator that dynamically assigns roles across models. Complementary.
- **vs cass-memory system**: cass-memory is about persisting procedural memory across sessions. TRINITY is about multi-turn reasoning with role specialization. Different concerns.

## Key Technical Insights
- **Why evolutionary algorithms?** Traditional REINFORCE gradients failed due to low signal-to-noise ratio (binary rewards, weak parameter coupling). Imitation learning (SFT) was ruled out due to cost of multi-turn label generation. Evolutionary algorithms handle tight, high-dimensional coordination problems that gradient methods cannot.
- **Coordinator design**: Uses hidden states of a compact language model + small routing head. Only ~20K params total.
- **Training data**: They evolved the coordinator on a set of coordination tasks, optimizing for successful multi-turn problem resolution.

## Risks
- Paper is recent (ICLR 2026); implementation details may evolve
- Sakana AI is a commercial entity with products; competitive Intelligence gathering is valid but should not replicate their proprietary systems
- MIT/arxiv means open to study; commercial use of their findings needs legal review

## Recommendation: **FORGE**

**Rationale:** This is a genuine new AI paradigm paper (multi-agent coordination via evolved coordinator). The <20K param coordinator achieving SOTA by dynamically orchestrating frontier models is a fundamentally different approach than single-model scaling. 

**Next Steps:**
1. Read the full paper at arxiv.org/abs/2512.04695
2. Map the tri-role pattern (Thinker/Worker/Verifier) onto our existing agent designs
3. Add to competitive landscape in HERMES_CAPABILITIES.md and SOLOMON_OS.md
4. Consider: could we implement a lightweight coordinator for Solomon OS using a small fine-tuned model with role-routing?
