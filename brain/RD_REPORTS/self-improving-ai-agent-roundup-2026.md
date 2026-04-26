# RD Report: Self-Improving AI Agent Roundup (2026)

## Summary
Multiple self-improving agent repos found this session. All MIT/Apache licensed.

### xmaks82/self-improving-agent
**Stars:** High | **Forked:** yes
- 16 interconnected agents forming self-improvement pipeline
- Feedback → Analyzer → Versioner → new system prompt (v1→v2→v3)
- Multi-provider: Groq, SambaNova, Cerebras, OpenRouter, Zhipu, Claude via OAuth
- 6-layer Bash safety, read-before-edit, permission controls, secret scanning

### Shreyas-Gowda26/self-improving-agent (fork of above)
Same architecture + MCP integration + 11 built-in tools + human-in-the-loop (diff preview, confirm, dry run)

### inngest/inngest-self-learning-agent
**Forked:** yes
- Durable AI agent with think/act/observe loop
- Self-learning prompts: A/B test prompt variants, weighted traffic, automated evaluation
- Guardrails: prevents prompt copying scoring criteria
- Multi-channel: Slack, Telegram

### theprint/nfh-self-improvement-loop
- Minimal adversarial framework
- Generator proposes change, separate Evaluator judges (separation of duties)
- One change per cycle, no rationale disclosed to evaluator
- Automatic rollback on failure

### soulfir/miguel
- Self-modifying within Docker sandbox
- Sub-agents: Coder, Researcher, Analyst
- Auto-commit + push after validation

## Solomon OS fit
**FORGE** — self-improving prompts are core to Hermes evolution loop. Multi-provider fallback (free LLMs) enables Solomon OS agents to run cheaply. NFH separation of generator/evaluator = key security pattern for preventing prompt injection.

## Action
Deep-read xmaks82's VersionerAgent for Hermes prompt evolution.
