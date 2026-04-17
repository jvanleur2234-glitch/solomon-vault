#!/usr/bin/env python3
"""Auto-summary generator for Telegram sessions."""

import json
import sys
import argparse
from datetime import datetime


def parse_conversation(messages):
    """Extract structured info from conversation messages."""
    if not messages:
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "topics": [],
            "decisions": [],
            "code": [],
            "problems": [],
            "unresolved": [],
            "followup": [],
        }

    topics = []
    decisions = []
    code = []
    problems = []
    unresolved = []
    followup = []

    for msg in messages:
        role = msg.get("role", "")
        content = msg.get("content", "")
        if not content:
            continue

        lines = content.split("\n")
        for line in lines:
            line = line.strip()
            lower = line.lower()

            if lower.startswith("**decision:") or lower.startswith("decision:"):
                decisions.append(line.split(":", 1)[-1].strip().lstrip("**").rstrip("**"))
            elif lower.startswith("**problem:") or lower.startswith("problem:"):
                problems.append(line.split(":", 1)[-1].strip().lstrip("**").rstrip("**"))
            elif lower.startswith("**unresolved:") or lower.startswith("unresolved:"):
                unresolved.append(line.split(":", 1)[-1].strip().lstrip("**").rstrip("**"))
            elif lower.startswith("**follow-up:") or lower.startswith("follow-up:") or lower.startswith("**followup:"):
                followup.append(line.split(":", 1)[-1].strip().lstrip("**").rstrip("**"))
            elif "```" in line or "file '" in line or "file '" in line.lower():
                code.append(content)
                break
            elif any(kw in lower for kw in ["created", "modified", "built", "wrote", "generated", "implemented"]):
                if len(line) > 10 and len(line) < 200:
                    code.append(line)

        if not topics and role == "user":
            topics.append(content[:100])

    return {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "topics": topics,
        "decisions": decisions,
        "code": code[:5],
        "problems": problems,
        "unresolved": unresolved,
        "followup": followup,
    }


def generate_summary(data):
    """Format data into a markdown summary."""
    md = f"""## Telegram Session Summary

**Date:** {data['date']}

---

### Key Decisions
"""
    if data["decisions"]:
        for d in data["decisions"]:
            md += f"- {d}\n"
    else:
        md += "_No formal decisions recorded_\n"

    md += "\n### Code Created/Modified\n"
    if data["code"]:
        for c in data["code"]:
            md += f"- {c}\n"
    else:
        md += "_No code changes recorded_\n"

    md += "\n### Problems Solved\n"
    if data["problems"]:
        for p in data["problems"]:
            md += f"- {p}\n"
    else:
        md += "_No problems solved this session_\n"

    md += "\n### Unresolved Issues\n"
    if data["unresolved"]:
        for u in data["unresolved"]:
            md += f"- {u}\n"
    else:
        md += "_No unresolved issues_\n"

    md += "\n### Follow-up Needed\n"
    if data["followup"]:
        for f in data["followup"]:
            md += f"- {f}\n"
    else:
        md += "_No follow-up required_\n"

    return md


def main():
    parser = argparse.ArgumentParser(description="Auto-summary for Telegram sessions")
    parser.add_argument("--conversation", help='JSON array of messages, e.g. \'[{"role":"user","content":"hi"}]\'')
    args = parser.parse_args()

    messages = []
    if args.conversation:
        try:
            messages = json.loads(args.conversation)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        try:
            incoming = sys.stdin.read()
            if incoming.strip():
                messages = json.loads(incoming)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON from stdin: {e}", file=sys.stderr)
            sys.exit(1)

    data = parse_conversation(messages)
    print(generate_summary(data))


if __name__ == "__main__":
    main()
