# RD Report: Council — Multi-Agent Discussion System

**Fork:** `jvanleur2234-glitch/council-fresh` | **Original:** `dubs3c/council` | **License:** MIT | **Stars:** ~700 | **Lang:** Python

## What It Is
Python-based multi-agent discussion system for structured debate and consensus. Default personas: Architect (systems design), Critic (devil's advocate), AppSec Specialist (implementation realism). Moderator synthesizes final report.

## Key Capabilities
- 4-phase workflow: Proposal → Debate → Early Consensus Check → Moderator Synthesis
- Distinct agent personas with configurable LLMs per agent
- Markdown report generation with full transcript
- Approval round and final consensus output
- YAML-based persona configuration
- OpenAI-compatible provider support

## Relevance to Solomon OS
- **Multi-Agent Deliberation:** Strong fit for Council of High Intelligence
- **Security:** AppSec persona directly relevant to Hermes security scanning
- **Skill Framework:** Personas as configurable Hermite skills

## Threat Analysis
- MIT licensed, actively maintained
- Structured debate is well-suited for security review workflows

## Integration Path
```
SKILL: council-debate → multi-agent security review for Hermes
USE CASE: Architecture reviews, security discussions, design decisions
```

**Recommendation:** FORGE — Fork as Hermes council skill with security focus.
