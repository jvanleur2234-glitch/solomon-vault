# RD Report: OASIS — 1 Million AI Agent Social Media Simulator

**URL:** https://github.com/camel-ai/oasis  
**License:** Apache 2.0  
**Stars:** 4.4K | **Forks:** 482  
**Paper:** arxiv.org/abs/2411.11581

## What It Is
Scalable open-source social media simulator running up to 1 MILLION LLM agents on platforms like Twitter and Reddit. Each agent has realistic profiles, can perform 23 actions (follow, comment, repost, create post, like, search, etc.), and the environment includes interest-based + hot-score recommendation algorithms that mirror real platform dynamics.

## Architecture
- Built on CAMEL framework (camel-ai.org)
- Python 99.9%
- Database-backed simulation (SQLite)
- Supports both Twitter and Reddit environments
- Agent profiles generated from real user data (JSON)
- Token consumption: 100 agents per timestep ≈ 335K input + 16.7K output tokens (Qwen-turbo)

## Key Features
- **Scale:** 1M agents — comparable to real-world platforms
- **23 action types:** LIKE_POST, CREATE_POST, COMMENT, REPOST, FOLLOW, MUTE, SEARCH, TREND, etc.
- **Recommendation systems:** Interest-based + hot-score algorithms
- **Multi-modal support** (in progress)
- **Electronic mall** on Reddit for buying/selling in simulation
- **Group chats** and messaging
- **Interview action** for asking agents specific questions

## Token Economics (Qwen pricing as of 2024-12-14)
| Model | 100 Agents | 1,000 Agents | 10,000 Agents |
|-------|-----------|-------------|--------------|
| qwen-plus | ¥0.027 | ¥0.27 | ¥2.68 |
| qwen-max | ¥0.72 | ¥7.72 | ¥77.17 |

## Relevance to JCPaid / Solomon OS

### FORGE — interesting but not immediately actionable
OASIS is primarily a research platform. However:

1. **Agent behavior testing** — Before launching real campaigns, test messaging/viral patterns in simulation. What content spreads? What triggers polarization?
2. **Social engineering at scale** — If you're doing outreach or influence campaigns for clients, OASIS models group dynamics accurately
3. **Multi-agent architecture reference** — The CAMEL-based agent graph structure (LLMAction, ManualAction, agent profiles) is a solid reference for Solomon OS agent design
4. **JackConnect positioning** — "Want to test how your real estate content spreads before posting? We simulate 100K agents first." Novel consulting angle

### Caveats
- Research tool, not a product — significant work to turn into a service
- Token costs scale fast with agent count
- No commercial licensing story yet
- Python-only, no web interface out of the box

## Recommendation
SKIP for now — too research-heavy. But bookmark: if JCPaid pivots toward social simulation services (e.g., testing marketing campaigns in silico before launch), OASIS becomes the technical backbone.

**Watch:** Camel-AI's broader ecosystem — they have camel (20K+ stars), oasis, and several other agent frameworks that are trending.

---
*Created: 2026-04-20 | Priority: normal | Source: GitHub URL shared via Telegram*