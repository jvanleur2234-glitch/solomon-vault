# RD Report: agent-tower-plugin vs owlex

## Both Found in Same Search: "multi-agent deliberation"

## agent-tower-plugin
- **What**: Claude Code plugin for multi-agent deliberation (council, debate, deliberate modes)
- **License**: MIT
- **Status**: Already forked as `jvanleur2234-glitch/agent-tower-plugin`
- **Key Difference**: Runs agents locally via Claude Code/Codex/Gemini CLIs
- **Modes**: Council (parallel → anonymous ranking → chairman synthesis), Debate (2 agents + judge), Deliberate (producer/reviewer loop)

## owlex
- **What**: MCP server enabling external model council deliberation
- **License**: MIT
- **Status**: Forked as `jvanleur2234-glitch/owlex`
- **Key Difference**: External model integration ( Codex, Gemini, OpenCode, ClaudeOR, AiChat) via council API
- **Deliberation**: 2 rounds with critique/revision, specialist roles, team presets

## Synergy for Solomon OS
Both can serve Hermes as validation layers:
1. `agent-tower-plugin`: Internal Claude Code debate for coding decisions
2. `owlex`: External multi-model validation for business/strategy decisions

Together they form a complete "Council of High Intelligence" stack.

## Recommendation
Keep both forks. Create Hermes skill wrapper that routes:
- Code review → agent-tower-plugin
- Business decisions → owlex
