#!/usr/bin/env python3
"""
Browser Skill Replay - Execute recorded skills using agent-browser
"""

import json
import sys
import time
import re
import subprocess
import argparse
from pathlib import Path
from urllib.parse import urlparse

SKILLS_DIR = Path("/home/workspace/Skills/browser-recorder/skills")

def load_skill(name):
    path = SKILLS_DIR / f"{name}.json"
    if not path.exists():
        # Try removing .json if user included it
        path = SKILLS_DIR / f"{name.replace('.json','')}.json"
    if not path.exists():
        print(f"❌ Skill '{name}' not found in {SKILLS_DIR}")
        print(f"   Available: {[p.stem for p in SKILLS_DIR.glob('*.json')]}")
        sys.exit(1)
    with open(path) as f:
        return json.load(f)

def substitute_params(text, params):
    """Replace {{param}} placeholders with actual values."""
    if not text:
        return text
    result = str(text)
    for key, value in params.items():
        result = result.replace(f"{{{{{key}}}}}", str(value))
    return result

def run_command(cmd):
    """Run agent-browser command, return output."""
    result = subprocess.run(
        ["agent-browser"] + cmd.split(),
        capture_output=True, text=True, timeout=30
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode

def replay_skill(skill_name, params=None, dry_run=False):
    """Replay a recorded skill with parameters."""
    skill = load_skill(skill_name)
    params = params or {}
    
    # Substitute variables from skill into params
    variables = skill.get("variables", {})
    for key, val in variables.items():
        if key not in params:
            params[key] = val
    
    print(f"\n🎬 Replaying skill: {skill['name']}")
    print(f"   Steps: {len(skill['steps'])}")
    print(f"   Params: {params}\n")
    
    # Check browser connection
    _, stderr, code = run_command("get url")
    if code != 0 or not _:
        print("❌ Browser not connected. Run: agent-browser connect --port 9222")
        sys.exit(1)
    
    current_url = _.strip()
    if current_url and "empty" not in current_url.lower():
        print(f"   Current page: {current_url}")
    
    for i, step in enumerate(skill["steps"], 1):
        action = step.get("action")
        selector = substitute_params(step.get("selector", ""), params)
        value = substitute_params(step.get("value"), params)
        description = step.get("description", "")
        
        print(f"  {i}. {action} → {selector} {f'= {value}' if value else ''}")
        if description:
            print(f"     └ {description}")
        
        if dry_run:
            print(f"     [DRY RUN - skipping]")
            continue
        
        # Execute based on action type
        if action == "navigate":
            run_command(f"open {selector}")
            time.sleep(2)
            
        elif action == "click":
            output, err, _ = run_command(f"click {selector}")
            if err:
                print(f"     ⚠️ {err[:100]}")
            time.sleep(1)
            
        elif action in ("type", "fill"):
            run_command(f'fill {selector} "{value}"')
            time.sleep(0.5)
            
        elif action == "select":
            run_command(f"select {selector} {value}")
            time.sleep(0.5)
            
        elif action == "press":
            run_command(f"press {selector}")
            time.sleep(0.5)
            
        elif action == "wait":
            time.sleep(int(selector) if selector.isdigit() else 2)
            
        else:
            print(f"     ⚠️ Unknown action: {action}")
        
        time.sleep(0.5)
    
    print(f"\n✅ Replay complete!")

def list_skills():
    """List all available skills."""
    skills = list(SKILLS_DIR.glob("*.json"))
    if not skills:
        print("No skills recorded yet.")
        print(f"   Record one: python3 record.py start --name my-skill")
        return
    
    print(f"\n📋 Recorded Skills ({len(skills)}):\n")
    for p in skills:
        with open(p) as f:
            s = json.load(f)
        created = s.get("created", "unknown")[:10]
        steps = s.get("metadata", {}).get("total_steps", len(s.get("steps", [])))
        print(f"   {p.stem}")
        print(f"     Created: {created} | Steps: {steps}")
        if s.get("trigger"):
            print(f"     Trigger: {s['trigger']}")
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Browser Skill Replay")
    parser.add_argument("skill", nargs="?", help="Skill name to replay")
    parser.add_argument("--params", "-p", help="Parameters as key=value,key=value")
    parser.add_argument("--dry-run", "-n", action="store_true", help="Show steps without executing")
    parser.add_argument("--list", "-l", action="store_true", help="List all skills")
    
    args = parser.parse_args()
    
    if args.list or (not args.skill):
        list_skills()
    else:
        params = {}
        if args.params:
            for pair in args.params.split(","):
                if "=" in pair:
                    k, v = pair.split("=", 1)
                    params[k.strip()] = v.strip()
        
        replay_skill(args.skill, params, dry_run=args.dry_run)
