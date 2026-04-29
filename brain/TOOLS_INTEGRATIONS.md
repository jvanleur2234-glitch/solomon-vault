# Bud.app — AI Agent with Full Computer

**What it is:** Bud (formerly Orchids) is a proprietary AI agent platform that rebranded April 2026. Described as "the first agent with a full computer."

**Key capabilities:**
- Own phone number (SMS)
- Own Telegram account (operates autonomously)
- Full browser for web navigation
- Storage, compute, memory
- File creation/editing
- Connects to Slack, Notion, external tools
- Learns custom skills
- Uses YOUR API keys at cost (ChatGPT, Claude, GitHub Copilot, Gemini)

**Business model:** SaaS — no GitHub, proprietary closed source. 7-figure ARR since September 2025.

**Strategic insight:** Bud's model of giving an AI its own phone number + Telegram account + browser is the exact architecture Solomon OS should replicate. This is the "AI Human Emulator" pattern — the agent lives in your phone's messages, not a chat box.

**Can we use it?**
- Fork: ❌ No (proprietary)
- Replicate: ✅ Yes (build same architecture: phone number + Telegram bot + browser + storage)
- Integrate via holaOS MCP: ✅ Yes (Bud could be added as an MCP server if they expose one)

---

# holaOS MCP Connectors

**Already built-in:** holaOS has first-class MCP support via `workspace.yaml` and the Bridge SDK (`@holaboss/bridge`).

**How to connect our agents:**
1. Add to `workspace.yaml` under `mcp_registry.servers`
2. Use Bridge SDK for runtime integration
3. Tool names get prefixed with `app_id.` (e.g., `hermes.execute_skill`)

**Files to reference:**
- `/workspace/docs/content/docs/concepts/agent-harness/mcp-support.mdx`
- `/workspace/docs/content/docs/build/apps/mcp-tools.mdx`
- `/workspace/docs/content/docs/build/apps/bridge-sdk.mdx`

**For Hermes:** Add as MCP server — our 94+ skills become callable from holaOS runtime
**For Paperclip:** Add as MCP server — agent orchestration available to holaOS workspace

---

# Space Agent

Research needed — Joseph mentioned it. Possible candidates:
- Google Vertex AI Agent Space (enterprise, GCP)
- KTern.AI Agent Space (SAP-focused)
- "Boost Space" no-code agent builder

Need Joseph to clarify which Space Agent he means.