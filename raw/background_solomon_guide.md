# Background — Solomon Guide Build

Generated: 2026-04-10T18:49:04.687036

## Services Status
{
  "hermes-webapi": "not responding on 8642",
  "ollama": "not responding on 11434"
}

## Workspace (20 files)
--full-page
9router
AGENTS.md
AI_ARSENAL.md
AiToEarn
Aperant
Articles
Atomic-Chat
AxiomVoice
Busin
Business
Business-Ideas
CLI-Anything
CLI-Anything-WEB
COHE_DESIGN.md
Chelsea.vanleur.txt
CodeMachine-CLI
DeepTutor
Default
EdgeClaw

## Key Findings

- SPEC loaded: 5783 chars
- Hermes WebAPI check: <urlopen error [Errno 99] Cannot assign requested address>
- DeepTutor context.py preview: """
Unified Context
===============

A single data object that flows through the orchestrator into every
tool / capability / plugin invocation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Attachment:
    """A file or image attached to the user message."""

    type: str  # "image" | "file" | "pdf"
    url: str = ""
    base64: str = ""
    filename: str = ""
    mime_type: str = ""


@dataclass
class UnifiedContext:

- Clicky OverlayWindow preview: //
//  OverlayWindow.swift
//  leanring-buddy
//
//  System-wide transparent overlay window for blue glowing cursor.
//  One OverlayWindow is created per screen so the cursor buddy
//  seamlessly follows the cursor across multiple monitors.
//

import AppKit
import AVFoundation
import SwiftUI

class OverlayWindow: NSWindow {
    init(screen: NSScreen) {
        // Create window covering entire screen
        super.init(
            contentRect: screen.frame,
            styleMask: .borderless,
 
- VoxCPM2: not installed — needs pip install voxcpm
- google-ads-copilot ARCHITECTURE: # Google Ads Copilot — Architecture

## The Big Picture

Google Ads Copilot is an AI agent that compounds learning over time. It reads search behavior, maps intent, surfaces waste, and proposes precise corrective actions — all grounded in real account data.

Not a dashboard replacement. Not a bid optimizer. A strategist with memory.

### Architecture: Read → Draft → Apply

```
┌───────────────────

## Next Steps

1. Install VoxCPM2: `pip install voxcpm`
2. Test Hermes WebAPI cursor tag response
3. Build memory consolidation layer (DeepTutor pattern)
4. Connect Clicky overlay to Hermes

## Google Ads Copilot — Forked

Forked: TheMattBerman/google-ads-copilot
Stars: growing fast (alpha, builder preview)
Key insight: Intent-first, not bid-first. Memory compounds across sessions.
Architecture: Read → Draft → Apply (3 layers, draft-staged, human-in-loop)
Skills: 15 analytical skills + apply layer
Workspace memory: intent-map.md, queries.md, negatives.md, learnings.md

This is a GREAT model for Solomon Guide memory system — same "session compounds" pattern.
