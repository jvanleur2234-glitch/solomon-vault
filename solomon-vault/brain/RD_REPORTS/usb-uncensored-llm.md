# R&D Report: USB Uncensored LLM

## What It Is
Zero-install portable local AI environment. Runs from USB drive or SSD. Cross-platform (Windows/Mac/Linux/Android). Air-gapped. Models run locally, no internet needed after setup.

## Key Specs
- Storage: USB 3.0+ flash or SSD, 8GB minimum (16GB recommended)
- RAM: 8GB for 2B/4B models, 16GB for 9B/12B models
- Models: Gemma 2 2B abliterated, Gemma 4 4B heretic, Qwen 3.5 9B uncensored + custom GGUF
- Stack: Ollama engine + custom Python HTTP server + dark mode UI
- LAN access: serves AI on WiFi network, access from phone/tablet

## JCPaid Fit: ★★★★★

### USB Distribution Model
This is EXACTLY how JCPaid/Solomon OS gets distributed:
1. USB drive with Solomon OS pre-installed
2. Plug into any PC/Mac/Linux box
3. Runs entirely locally — no cloud, no internet needed
4. Air-gapped = truly private
5. Cross-platform

### Business Angles

**Angle 1 — USB Stick Business**
- Sell pre-loaded USB drives with Solomon OS
- $99 for USB drive + 1 year subscription
- $199 for USB drive + lifetime license
- Target: tradespeople, privacy-conscious professionals
- No internet required = works in warehouses, job sites, rural areas

**Angle 2 — SMB Network Appliance**
- Solomon OS plugs into their network via Ethernet
- Serves AI to all computers on the LAN
- No per-seat cloud subscription
- One-time hardware purchase + $49/mo support
- Target: plumbing, HVAC, electrical, contracting companies
- Local invoice AI, job management AI, customer lookup AI

**Angle 3 — Trades Training USB**
- USB loaded with Solomon OS + trade-specific skills
- Plumbers: code lookup, permit questions, video tutorials
- Electricians: NEC code lookup, troubleshooting guides
- HVAC: refrigerant charts, diagnostic flows
- Sell $49 USB + $19/mo skill updates

## What We'd Build
Add to USB-Uncensored-LLM structure:
```
[Solomon OS USB]
├── Windows/      # Solomon OS installer for Windows
├── Mac/          # Solomon OS installer for Mac  
├── Linux/        # Solomon OS installer for Linux
├── Android/      # Termux version for Android
└── Shared/
    ├── bin/     # Ollama + Solomon OS binaries
    ├── models/  # Pre-loaded GGUF models
    ├── skills/  # Hermes skills library
    └── solomon/  # Solomon OS core (Hermes, Russell Tuna, Icarus, Evolver)
```

## Next Steps
1. Fork this repo ✅ (done)
2. Add Solomon OS Windows/Mac/Linux installers
3. Pre-load best Ollama models
4. Build trade-specific skill packs
5. Create USB stick product listing

## RD Report
- Forked: jvanleur2234-glitch/USB-Uncensored-LLM
- Location: /home/workspace/USB-Uncensored-LLM/
- Added to HERMES_CAPABILITIES.md
