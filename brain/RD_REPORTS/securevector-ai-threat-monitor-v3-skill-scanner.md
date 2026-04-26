# securevector-ai-threat-monitor — On-Premise AI Security Layer

**Fork:** Already forked  
**License:** MIT  
**Latest:** v3.2.0

## What It Is
An on-premise security solution that sits between AI agents and LLM providers to detect and block prompt injections, tool abuse, and data leaks in real-time. Supports multiple providers (OpenAI, Claude, Anthropic, Ollama) via a multi-provider proxy.

## Key Features
- **Real-time threat detection** on requests and responses
- **Tool permission controls** to prevent unauthorized agent actions
- **Cost tracking** with per-agent spend monitoring + global daily budgets
- **Skill Scanner (v3.2.0)**: static agent-skill analysis with optional AI review
- **Skill Scan Policy Engine**: risk scoring, trusted publishers, allow/block rules
- **Local operation**: no data leaves your environment
- Runs as Python package or full app

## Why It Matters for Solomon OS
- **Hermes security layer** — could complement AgentArmor Studio
- Skill Scanner directly addresses the OWASP LLM01 prompt injection risk
- On-premise model fits Solomon OS self-hosted architecture
- Policy engine (allow/block rules) could be a Hermes SKILL

## Comparison to AgentArmor Studio
| Feature | SecureVector | AgentArmor Studio |
|---|---|---|
| Skill scanning | ✅ v3.2.0 | ✅ 8-layer |
| Real-time guard | ✅ | ✅ |
| Policy engine | ✅ allow/block | ? |
| Cost tracking | ✅ | ❌ |
| Local-only | ✅ | ? |
| MIT licensed | ✅ | ✅ |

## Verdict
**INTEGRATE** — The Skill Scanner + Policy Engine in v3.2.0 is directly relevant to Hermes security. Study for potential Hermes skill install verification.