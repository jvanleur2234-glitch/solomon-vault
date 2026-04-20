# RD Report: BC-250 Mining Board

**Date:** 2026-04-20  
**Source:** [X @omarsar0](https://x.com/omarsar0/status/2045886906953781408)  
**Type:** rd-research

## What It Is

**Repo:** [mothenjoyer69/bc250-documentation](https://github.com/mothenjoyer69/bc250-documentation) — 459 stars, AGPL-3.0  
**What it is:** Documentation for ASRock/AMD BC-250 mining boards being repurposed as desktop PCs. These are former crypto mining rigs now sold cheaply (people who bought them for mining lost money). The board uses a PS5-derived AMD APU.

## Hardware Specs

- **CPU:** AMD BC250 APU ("Ariel") — 6x Zen 2 cores @ 3.49GHz (cut-down PS5 SoC)
- **GPU:** 24CU RDNA2 iGPU ("cyan-skillfish") — PS5 has 36CUs
- **Memory:** 16GB GDDR6 shared (CPU/GPU split configurable via firmware)
- **TDP:** 220W
- **Ports:** 1x M.2 NVMe, 1x GbE, 2x USB 2.0, 2x USB 3.0, DisplayPort
- **Price:** Now cheap on resale market (~$50-100)

## Bitcoin Mining — Does It Work?

**No.** SHA-256 ASICs (Antminer S21+ at 200+ TH/s) have dominated BTC mining since 2015. GPU mining (even RDNA2) produces maybe 1-2 GH/s — orders of magnitude too slow. You would spend more on electricity than you'd earn in BTC.

## What IS Interesting

### 1. RDNA2 GPU Compute
24 CUs = usable for:
- Local AI inference (Ollama on GPU)
- Stable Diffusion / image generation
- Video encoding (FFmpeg VAAPI)
- Parallel compute tasks

### 2. Budget Solomon OS Worker Nodes
A farm of BC-250 boards = cheap distributed compute layer:
- Each board: 6 CPU cores + 24 GPU CUs + 16GB GDDR6
- Run Ollama or SD inference locally
- No cloud dependency
- Privacy-first

### 3. Be Like You! OS Hardware Target
These boards (~$50-100 each) are perfect hardware targets for Be Like You! OS:
- Linux runs well (Fedora/Bazzite)
- Modified firmware exposes GPU settings
- GPU governor available (oberon-governor)
- Can overclock with `vc` clock control

## Technical Notes

- Linux support: Almost perfect with Mesa 25.1
- Windows: No GPU drivers (won't ever happen)
- Flashing modified firmware: Required to change GDDR6 allocation (default 4GB/12GB split → 512MB for desktop use)
- Hardware programmer recommended for flashing (CH347 or Raspberry Pi Pico)
- lm-sensors works with nct6683 driver

## Recommendation

**SKIP** for Bitcoin mining (economically unviable)  
**INTERESTING** for budget Solomon OS / Be Like You! OS compute nodes

**LINK fit:** ★★★☆☆ — hardware for distributed AI compute layer

## Next Steps (If Interested)

1. Acquire BC-250 board(s) on resale market (~$50-100 each)
2. Flash modified firmware (enable GPU settings, 512MB VRAM for desktop)
3. Install Fedora/Bazzite Linux
4. Install oberon-governor + Mesa 25.1
5. Install Ollama with GPU support
6. Connect to Solomon Bus as worker nodes

---

*Last updated: 2026-04-20*