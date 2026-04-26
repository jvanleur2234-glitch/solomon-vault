# RD Report: AI Planning Framework for LLM-Based Web Agents

## What It Is
**Paper**: "AI Planning Framework for LLM-Based Web Agents" by Orit Shahnovsky and Rotem Dror (University of Haifa)
**arXiv**: https://arxiv.org/pdf/2603.12710
**Platform**: Academic research paper (March 2026)
**Stars**: N/A (research paper, not a repo)

## Core Content
The paper formally treats web tasks as sequential decision-making processes and introduces a taxonomy that maps modern LLM-agent architectures to traditional planning paradigms:

| Agent Type | Maps To | How It Works |
|---|---|---|
| **Step-by-Step** | Breadth-First Search (BFS) | Generates implicit candidate actions, evaluates one at a time, prioritizes immediate state feedback over long-term planning |
| **Tree Search** | Best-First Tree Search | Maintains explicit search tree, uses value function V(s) to score and expand most promising nodes |
| **Full-Plan-in-Advance** | Depth-First Search (DFS) | Generates complete planned trajectory before execution, strictly follows the plan (replans on divergence) |

## Key Findings

1. **Step-by-step agents**: 38.41% overall success rate, but align more closely with human gold trajectories
2. **Full-Plan-in-Advance agents**: 89% element accuracy (technical measure), but less human-aligned
3. **Core problem**: Agents can perform well in controlled demos but struggle when tasks become complex or unpredictable
4. **Deeper limitation**: Current AI systems are limited not just by knowledge but by how they plan and execute decisions over time

## Failure Modes Identified
- **Context drift**: Over many steps, the original goal falls out of memory (Step-by-step agents are most susceptible)
- **Incoherent task decomposition**: Agent fails to break task into coherent multi-step actions
- **Misread intent**: Produces a plan that executes flawlessly toward the wrong goal (all three strategies share this assumption flaw)

## Evaluation Metrics Introduced (5 Novel Metrics)
Beyond binary success/failure — assesses trajectory quality:
1. Recovery Rate
2. Trajectory Efficiency
3. Plan Coherence
4. Action Validity
5. Goal Alignment

## What We'd Use It For

**1. Solomon OS / Russell Tuna architecture decisions**
- The taxonomy gives us a principled way to choose agent planning strategies for different task types
- Full-Plan-in-Advance (DFS) could work for well-defined, predictable workflows; Step-by-step (BFS) for open-ended exploration

**2. Evaluating agent reliability**
- The 5 novel metrics go beyond pass/fail — useful for reporting to clients on Solomon OS task quality
- Could incorporate into Solomon Guardian's agent evaluation layer

**3. Understanding demo-vs-production gap**
- Explains why AI agents look impressive in demos but fail in real-world use — critical for client expectation setting
- The "30% misbehaviour floor" mentioned in the thread aligns with this

**4. Agent design patterns**
- Tree Search approach (multi-step lookahead with value function) could improve Solomon Bus job execution reliability
- Context drift resistance = Full-Plan-in-Advance with plan-as-external-memory pattern

## Relevance to Our Stack

**Direct overlap with**: planning-with-files (Manus-style 3-file planning), gnhf iteration engine, ML-Master HCC

**Complements**: agentarmor-studio (8-layer security), hermes-agent architecture

**The assumption flaw** (misread intent → wrong goal) is critical for Solomon Guardian — needs a validation layer before execution

## Comparison to What We Have

Currently Solomon OS / Russell Tuna appears to use Step-by-step reasoning (react to each prompt). The Full-Plan-in-Advance pattern with plan-as-external-memory would resist context drift better for long-horizon tasks.

The paper validates our direction: we need metrics beyond success/fail, and planning strategy choice matters for reliability.

## Recommendation

**Category**: INTEGRATE

**Action items**:
1. Study Section 3.2 (Full-Plan-in-Advance implementation) for Solomon Bus architecture
2. Adopt the 5 evaluation metrics for Solomon Guardian quality reporting
3. Add "plan-as-external-memory" pattern to Russell Tuna for context drift resistance
4. The assumption flaw (correct goal understanding at step 0) = new Guardian validation gate

**Priority**: Medium — foundational research, not immediately actionable but structurally important

## Sources
- https://arxiv.org/pdf/2603.12710
- https://x.com/i/status/2048086413917540391 (thread by @ZabihullahAtal)