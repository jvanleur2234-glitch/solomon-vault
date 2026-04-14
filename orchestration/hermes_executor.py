"""
Hermes Executor — spawns Hermes agents for development/code tasks.
Hermes = hosted agent system with 94 skills at /home/workspace/hermes-skills/.
"""

import os
import subprocess
import logging
from typing import Optional

log = logging.getLogger("solomon.hermes")

HERMES_SKILLS_DIR = "/home/workspace/hermes-skills"


def list_skills() -> list[dict]:
    """List all available Hermes skills."""
    skills = []
    if not os.path.exists(HERMES_SKILLS_DIR):
        return skills

    for entry in os.scandir(HERMES_SKILLS_DIR):
        if entry.is_dir() and entry.name != "__pycache__":
            skill_dir = entry.path
            readme = os.path.join(skill_dir, "README.md")
            desc = ""
            if os.path.exists(readme):
                with open(readme) as f:
                    desc = f.read()[:200].strip()
            skills.append({
                "name": entry.name,
                "path": skill_dir,
                "description": desc
            })
    return skills


def find_skill(task_keywords: list[str]) -> Optional[dict]:
    """Find the best Hermes skill for a task based on keywords."""
    skills = list_skills()
    task_text = " ".join(task_keywords).lower()

    best_match = None
    best_score = 0

    for skill in skills:
        skill_text = (skill["name"] + " " + skill["description"]).lower()
        score = sum(1 for kw in task_keywords if kw.lower() in skill_text)
        if score > best_score:
            best_score = score
            best_match = skill

    return best_match if best_score > 0 else None


async def execute_task(
    url: str,
    task_description: str,
    skill_name: Optional[str] = None,
) -> str:
    """
    Execute a task using Hermes.

    If skill_name is provided, use that skill.
    Otherwise, auto-detect the best skill from task_description.
    """
    task_keywords = task_description.lower().split()
    skill = None

    if skill_name:
        # Find specified skill
        skills = list_skills()
        for s in skills:
            if s["name"] == skill_name:
                skill = s
                break
    else:
        # Auto-detect
        skill = find_skill(task_keywords)

    if not skill:
        return (
            "No matching Hermes skill found for this task.\n"
            f"Task: {task_description}\n"
            f"URL: {url}\n"
            "Consider using the browser executor instead."
        )

    # Build the Hermes command
    # Hermes CLI: hermes run --skill <name> --task <task>
    try:
        cmd = [
            "hermes", "run",
            "--skill", skill["name"],
            "--task", f"{task_description} --url {url}"
        ]

        log.info(f"Running Hermes: {' '.join(cmd)}")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120,
            cwd="/home/workspace"
        )

        if result.returncode == 0:
            output = result.stdout or "Task completed successfully."
            log.info(f"Hermes task success: {skill['name']}")
            return f"*Hermes Skill: {skill['name']}*\n\n{output}"
        else:
            log.error(f"Hermes error: {result.stderr}")
            return f"Hermes error: {result.stderr[:500]}"

    except subprocess.TimeoutExpired:
        return "Hermes task timed out after 120 seconds."
    except FileNotFoundError:
        return "Hermes CLI not found. Is Hermes installed?"
    except Exception as e:
        log.error(f"Hermes executor error: {e}")
        return f"ERROR: {e}"


if __name__ == "__main__":
    skills = list_skills()
    print(f"Found {len(skills)} Hermes skills:")
    for s in skills[:10]:
        print(f"  - {s['name']}: {s['description'][:60]}")
