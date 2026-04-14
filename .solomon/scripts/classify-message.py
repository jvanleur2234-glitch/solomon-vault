#!/usr/bin/env python3
"""Classify user messages and inject routing hints for Solomon OS."""
import json
import sys
import re

SIGNALS = {
    "lead": {
        "patterns": ["found a lead", "new prospect", "potential client", "someone wants", "interested in", "got a lead", "leads are", "cold call", "warm lead", "referral from", "HYRVE job", "marketplace job"],
        "hint": "LEAD detected — consider using /capture-lead or creating a lead note in work/leads/"
    },
    "client": {
        "patterns": ["signed a client", "new client", "client onboarding", "client name is", "working with", "paid client", "first client"],
        "hint": "CLIENT detected — consider using /new-client or creating a client note in org/clients/"
    },
    "win": {
        "patterns": ["first dollar", "got paid", "revenue", "made money", "closed deal", "won the", "got a testimonial", "case study", "referral", "testimonial from"],
        "hint": "WIN detected — consider using /capture-win or adding to perf/brag/"
    },
    "decision": {
        "patterns": ["decided to", "decision:", "going with", "chose to", "the call is", "we're going", "let's go with", "agreed on"],
        "hint": "DECISION detected — consider creating a Decision Record and updating brain/Key Decisions.md"
    },
    "incident": {
        "patterns": ["service is down", "error:", "not working", "crashed", "outage", "failed to", "can't connect", "broken"],
        "hint": "INCIDENT detected — consider creating an incident note in work/incidents/ and updating brain/Services.md"
    },
    "idea": {
        "patterns": ["new idea:", "what if we", "could do a", "business idea", "revenue stream", "product idea", "service idea", "monetize"],
        "hint": "IDEA detected — consider adding to brain/Business Ideas.md"
    },
    "service": {
        "patterns": ["deployed", "running at", "installed", "set up", "configured", "port", "localhost:", "service is"],
        "hint": "SERVICE detected — consider updating brain/Services.md with the new service info"
    },
    "telegram": {
        "patterns": ["telegram", "dm me", "message on telegram", "t.me/", "@"],
        "hint": "TELEGRAM signal — Russell Tuna bot may be relevant"
    }
}

def classify(prompt: str) -> list[str]:
    p = prompt.lower()
    hints = []
    for signal_type, data in SIGNALS.items():
        for pattern in data["patterns"]:
            if re.search(r'\b' + re.escape(pattern) + r'\b', p):
                hints.append(data["hint"])
                break
    return hints

def main():
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)
    
    prompt = input_data.get("prompt", "")
    if not prompt:
        sys.exit(0)
    
    hints = classify(prompt)
    if hints:
        output = {
            "hookSpecificOutput": {
                "additionalContext": (
                    "Content classification hints (act on these if relevant to Solomon OS):\n"
                    + "\n".join(f"- {h}" for h in hints)
                    + "\n\nRemember: use /capture-lead, /capture-win, /new-client, or create notes in the right folders."
                )
            }
        }
        json.dump(output, sys.stdout)
        sys.stdout.flush()
        sys.exit(0)

if __name__ == "__main__":
    main()
