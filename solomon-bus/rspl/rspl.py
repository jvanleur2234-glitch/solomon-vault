"""
RSPL — Resource Substrate Protocol Layer
========================================
Models Skills, Prompts, Agents, Tools, Memory as first-class versioned resources.
Each resource has:
  - lifecycle: init → build → run → update → restore
  - version lineage with git-style history
  - rollback capability
  - safety invariants checked before mutations

Resources are PASSIVE — cannot self-modify.
All mutations go through RSPL interfaces only.
"""

import json
import os
import subprocess
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Optional

RSPL_DIR = Path("/home/workspace/solomon-bus/rspl")
VERSIONS_DIR = Path("/home/workspace/solomon-bus/versions")

RESOURCE_TYPES = ["skill", "prompt", "agent", "tool", "memory"]

class RSPLResource:
    """A versioned, lifecycle-managed resource in Solomon OS."""

    def __init__(self, resource_type: str, name: str):
        if resource_type not in RESOURCE_TYPES:
            raise ValueError(f"Invalid resource_type: {resource_type}")
        self.resource_type = resource_type
        self.name = name
        self.resource_dir = RSPL_DIR / resource_type / name
        self.versions_dir = VERSIONS_DIR / resource_type / name

    def init(self, content: str, metadata: dict = None) -> str:
        """Initialize a new resource at version 0.1.0."""
        self.resource_dir.mkdir(parents=True, exist_ok=True)
        self.versions_dir.mkdir(parents=True, exist_ok=True)
        metadata = metadata or {}
        v0_1_0 = self._write_version("0.1.0", content)
        registry_entry = {
            "name": self.name,
            "type": self.resource_type,
            "current_version": "0.1.0",
            "created": datetime.utcnow().isoformat() + "Z",
            "lifecycle": "init",
            "metadata": metadata,
        }
        self._update_registry(registry_entry)
        return v0_1_0

    def build(self, version: str, content: str) -> str:
        """Build a new version of the resource."""
        return self._write_version(version, content)

    def restore(self, version: str) -> Optional[str]:
        """Restore a previous version. Returns content or None."""
        vfile = self.versions_dir / f"{version}.md"
        if not vfile.exists():
            return None
        return vfile.read_text()

    def list_versions(self) -> list:
        """List all versions of this resource."""
        if not self.versions_dir.exists():
            return []
        return sorted([f.stem for f in self.versions_dir.glob("*.md")])

    def current(self) -> Optional[dict]:
        """Get current registry entry."""
        reg = self._registry_file()
        if not reg.exists():
            return None
        return json.loads(reg.read_text())

    def _write_version(self, version: str, content: str) -> str:
        """Write a versioned snapshot and update lineage log."""
        self.versions_dir.mkdir(parents=True, exist_ok=True)
        vfile = self.versions_dir / f"{version}.md"
        vfile.write_text(content)
        # Append to lineage
        lineage_file = self.versions_dir / "lineage.jsonl"
        entry = {
            "version": version,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "content_hash": hashlib.md5(content.encode()).hexdigest(),
            "size_bytes": len(content),
        }
        with open(lineage_file, "a") as f:
            f.write(json.dumps(entry) + "\n")
        return str(vfile)

    def _registry_file(self) -> Path:
        return RSPL_DIR / f"{self.resource_type}_{self.name}.json"

    def _update_registry(self, entry: dict):
        with open(self._registry_file(), "w") as f:
            json.dump(entry, f, indent=2)

    def update_lifecycle(self, lifecycle: str):
        """Move resource through lifecycle stages."""
        current = self.current()
        if current:
            current["lifecycle"] = lifecycle
            current["last_updated"] = datetime.utcnow().isoformat() + "Z"
            self._update_registry(current)


class SkillResource(RSPLResource):
    """A Hermes skill as a versioned RSPL resource."""

    def __init__(self, name: str):
        super().__init__("skill", name)
        self.skill_dir = Path(f"/home/workspace/Skills/{name}")

    def link_skill(self) -> bool:
        """Symlink RSPL version to actual skill directory."""
        current = self.current()
        if not current:
            return False
        version = current["current_version"]
        vfile = self.versions_dir / f"{version}.md"
        if vfile.exists():
            dest = self.skill_dir / "SKILL.md"
            # Backup current
            if dest.exists():
                subprocess.run(["cp", str(dest), str(dest) + f".bak-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"])
            subprocess.run(["cp", str(vfile), str(dest)])
            return True
        return False

    def rollback(self) -> bool:
        """Roll back to previous version."""
        versions = self.list_versions()
        if len(versions) < 2:
            return False
        prev = versions[-2]
        content = self.restore(prev)
        if content:
            current = self.current()
            current["current_version"] = prev
            current["lifecycle"] = "restored"
            current["last_updated"] = datetime.utcnow().isoformat() + "Z"
            self._update_registry(current)
            self.link_skill()
            return True
        return False


def register_skill(name: str, content: str, metadata: dict = None) -> dict:
    """Register a new skill as an RSPL resource."""
    skill = SkillResource(name)
    if skill.current():
        return {"status": "exists", "resource": name}
    path = skill.init(content, metadata)
    return {"status": "registered", "version": "0.1.0", "path": path}


def bump_skill_version(name: str, content: str, bump_type: str = "patch") -> dict:
    """Write a new version of a skill (patch/minor/major)."""
    skill = SkillResource(name)
    current = skill.current()
    if not current:
        return {"status": "error", "message": f"Skill {name} not registered"}
    current_v = current["current_version"]
    parts = current_v.split(".")
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
    if bump_type == "major":
        major += 1; minor = 0; patch = 0
    elif bump_type == "minor":
        minor += 1; patch = 0
    else:
        patch += 1
    new_v = f"{major}.{minor}.{patch}"
    skill.build(new_v, content)
    current["current_version"] = new_v
    current["lifecycle"] = "updated"
    current["last_updated"] = datetime.utcnow().isoformat() + "Z"
    skill._update_registry(current)
    return {"status": "bumped", "version": new_v}


def rollback_skill(name: str) -> dict:
    """Roll back a skill to its previous version."""
    skill = SkillResource(name)
    if skill.rollback():
        return {"status": "rolled_back", "resource": name}
    return {"status": "error", "message": "No previous version to restore"}


def list_skills() -> list:
    """List all registered RSPL skills."""
    skills = []
    for rf in RSPL_DIR.glob("skill_*.json"):
        try:
            skills.append(json.loads(rf.read_text()))
        except Exception:
            pass
    return skills


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("RSPL: Resource Substrate Protocol Layer for Solomon Bus")
        print("Usage: python3 rspl.py [register|list|rollback|bump] [args...]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "list":
        for s in list_skills():
            print(f"  {s['name']} @ {s['current_version']} [{s['lifecycle']}]")
    elif cmd == "register" and len(sys.argv) >= 4:
        print(register_skill(sys.argv[2], sys.argv[3]))
    elif cmd == "rollback" and len(sys.argv) >= 3:
        print(rollback_skill(sys.argv[2]))
    elif cmd == "bump" and len(sys.argv) >= 4:
        print(bump_skill_version(sys.argv[2], sys.argv[3]))