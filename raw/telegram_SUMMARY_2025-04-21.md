# Telegram Session Summary — 2025-04-21

**Key decisions made:**

1. **Product name:** SolomonOS — the entire product. JackConnect was just a temporary name from earlier conversation. The app is for real estate agents starting with Jack (brother in Sioux Falls, SD) as beta tester.

2. **Architecture:** Codebase must be structured generically with a config/verticals system that can flip between verticals (RE, restaurant, plumbing, etc.) with minimal friction.

3. **Messaging platform:** DECISION A+B — Start building a WhatsApp-style messaging app but also use Telegram as an immediate notification hub. Spin up a background worker to lead this project independently.

4. **LLM:** Start with Ollama + llama3.2:1b. BitNet slot reserved for later.

5. **Build order:** 
   - Start with generic SolomonOS framework 
   - Inject RE/real estate vertical config for Jack
   - Build the messaging platform in parallel via background worker

6. **Background worker:** I'm spinning up a dedicated agent (either from me or Hermes) to lead the entire messaging platform project. That agent owns the full build.

**Current state:**
- Tauri app scaffold exists at `/home/workspace/jack-connect/`
- SPEC.md exists but needs to be rewritten for SolomonOS
- Need to restructure the Rust backend around SolomonOS architecture
- Need to create a verticals/config system

**Next step:** 
- Wait for Joseph to confirm Zo is restarted (DM me back)
- Then start building SolomonOS framework immediately

**Open items:**
- Need to figure out how to spin up the background worker for messaging app
- Need to decide exact tech stack for the messaging app
- Need to decide what "WhatsApp-style" means precisely (real-time chat, E2E encryption, push notifications, etc.)

**Files modified:**
- /home/workspace/jack-connect/desktop-app/src-tauri/src/main.rs (read, no changes yet)
- /home/workspace/jack-connect/SPEC.md (exists, needs rewrite)