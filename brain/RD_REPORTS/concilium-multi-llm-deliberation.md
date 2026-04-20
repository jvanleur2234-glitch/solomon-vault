# RD Report: Concilium (matiasdaloia/concilium)

## What It Is
Open-source multi-LLM deliberation platform that runs several AI agents in parallel, has them anonymously peer-review each other, and synthesizes a single superior answer. CLI + Electron desktop app, MIT licensed.

## License & Stars
- **License:** MIT
- **Stars:** Not polled yet; active development

## Key Capabilities
- **Parallel execution** → anonymous cross-review → consensus-based ranking → synthesized final result
- **Blind peer review**: agents evaluate each other's work without knowing who wrote it
- **Chairman synthesis**: model synthesizes final answer from juror reviews
- **CLI and Electron desktop** interfaces; programmatic API via `@concilium/cli`
- **Local-first**: data stays on machine
- **Multiple backends**: OpenRouter API key for jurors/synthesis

## Relevance to Solomon OS
- **Multi-agent deliberation (Council of High Intelligence competitor)**: Ready-made deliberation system
- **Self-improvement**: Peer review mechanism → agents can evaluate each other's outputs
- **Security**: Anonymous review prevents bias in security audits
- **Skill frameworks**: Could integrate as a Hermes skill for critical decision-making

## Decision
**SKILL** — Fork to `jvanleur2234-glitch/concilium`. Add to HERMES_CAPABILITIES.md under multi-agent deliberation.

## Notes
- Direct competitor to our Council of High Intelligence concept
- Anonymous peer review is novel — good for unbiased security review
- Node.js based = easy to integrate with existing JS/TS tooling