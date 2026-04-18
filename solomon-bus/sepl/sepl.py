"""
SEPL — Self-Evolution Protocol Layer
=====================================
Closed-loop control system for Solomon Bus.
Turns reactive agents into self-improving workers.

The loop:
  1. Reflect (ρ)   → Analyze failure traces → generate failure hypotheses
  2. Select (σ)    → Translate hypotheses → candidate modifications
  3. Improve (ι)   → Apply mutations → candidate state
  4. Evaluate (ε)   → Test against objectives + safety invariants
  5. Commit (κ)    → Conditional acceptance; rollback on failure

Each iteration is traceable, reversible, auditable.
"""

import json
import os
import hashlib
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional

SEPL_DIR = Path("/home/workspace/solomon-bus/sepl")
LOGS_DIR = SEPL_DIR / "logs"
LOOPS_DIR = SEPL_DIR / "loops"
HYPOTHESES_DIR = SEPL_DIR / "hypotheses"
SAFETY_DIR = SEPL_DIR / "safety"

LOGS_DIR.mkdir(parents=True, exist_ok=True)
LOOPS_DIR.mkdir(parents=True, exist_ok=True)
HYPOTHESES_DIR.mkdir(parents=True, exist_ok=True)
SAFETY_DIR.mkdir(parents=True, exist_ok=True)


class SEPLLoop:
    """A single SEPL execution loop for a given task."""

    def __init__(self, task_id: str, task_description: str, context: dict = None):
        self.task_id = task_id
        self.task_description = task_description
        self.context = context or {}
        self.loop_dir = LOOPS_DIR / task_id
        self.loop_dir.mkdir(parents=True, exist_ok=True)
        self.iteration = 0
        self.hypotheses = []
        self.candidates = []
        self.failed = False
        self.converged = False

    def log_phase(self, phase: str, data: dict):
        """Log output of each phase to the loop trace."""
        log_file = self.loop_dir / f"phase_{phase}_{self.iteration}.json"
        with open(log_file, "w") as f:
            json.dump({
                "phase": phase,
                "iteration": self.iteration,
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "data": data,
            }, f, indent=2)

    def reflect(self, failure_trace: str) -> list:
        """Phase 1 — Reflect: analyze failure → generate hypotheses."""
        self.iteration += 1
        # Generate failure hypotheses from trace
        hypotheses = self._generate_hypotheses(failure_trace)
        self.hypotheses = hypotheses
        self.log_phase("reflect", {"failure_trace": failure_trace, "hypotheses": hypotheses})
        return hypotheses

    def _generate_hypotheses(self, trace: str) -> list:
        """Generate failure hypotheses from a failure trace."""
        hypotheses = []
        trace_lower = trace.lower()
        # Pattern-based hypothesis generation
        if "timeout" in trace_lower or "took too long" in trace_lower:
            hypotheses.append({
                "id": f"H{self.iteration}-1",
                "type": "performance",
                "hypothesis": "Task exceeds time budget — need faster model or simpler approach",
                "confidence": 0.7,
                "fix_candidate": "switch_to_faster_model_or_simplify_task"
            })
        if "not found" in trace_lower or "missing" in trace_lower or "404" in trace_lower:
            hypotheses.append({
                "id": f"H{self.iteration}-2",
                "type": "data",
                "hypothesis": "Required resource is missing — need to add fallback or create resource",
                "confidence": 0.85,
                "fix_candidate": "add_fallback_or_create_resource"
            })
        if "permission" in trace_lower or "denied" in trace_lower or "unauthorized" in trace_lower:
            hypotheses.append({
                "id": f"H{self.iteration}-3",
                "type": "auth",
                "hypothesis": "Authentication or permission failure — need to refresh credentials",
                "confidence": 0.9,
                "fix_candidate": "refresh_credentials_or_use_different_auth"
            })
        if "invalid" in trace_lower or "malformed" in trace_lower:
            hypotheses.append({
                "id": f"H{self.iteration}-4",
                "type": "validation",
                "hypothesis": "Input validation failure — need to sanitize or add checks",
                "confidence": 0.8,
                "fix_candidate": "add_input_sanitization"
            })
        if "rate limit" in trace_lower or "throttle" in trace_lower:
            hypotheses.append({
                "id": f"H{self.iteration}-5",
                "type": "rate_limit",
                "hypothesis": "API rate limit hit — need backoff or queue task",
                "confidence": 0.95,
                "fix_candidate": "add_backoff_retry_with_queue"
            })
        # Default fallback hypothesis
        if not hypotheses:
            hypotheses.append({
                "id": f"H{self.iteration}-default",
                "type": "unknown",
                "hypothesis": "Unclassified failure — need more diagnostic info",
                "confidence": 0.3,
                "fix_candidate": "gather_more_diagnostics"
            })
        return hypotheses

    def select(self, hypotheses: list) -> list:
        """Phase 2 — Select: choose top 3 fix candidates."""
        # Sort by confidence descending
        sorted_h = sorted(hypotheses, key=lambda h: h.get("confidence", 0), reverse=True)
        top3 = sorted_h[:3]
        self.candidates = [
            {"hypothesis": h, "selected": True, "rank": i+1}
            for i, h in enumerate(top3)
        ]
        self.log_phase("select", {"candidates": self.candidates})
        return self.candidates

    def improve(self, skill_name: str, candidate: dict, new_content: str) -> str:
        """Phase 3 — Improve: apply mutation to skill, store as candidate."""
        # Import RSPL to write candidate version
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent / "rspl"))
        from rspl import bump_skill_version, SkillResource

        skill = SkillResource(skill_name)
        current = skill.current()
        if not current:
            return f"Error: skill {skill_name} not registered in RSPL"

        # Write as candidate version (patch bump, alpha tag)
        base_v = current["current_version"]
        candidate_v = f"{base_v}a"  # alpha candidate
        skill.build(candidate_v, new_content)
        self.log_phase("improve", {
            "skill": skill_name,
            "candidate_version": candidate_v,
            "hypothesis_id": candidate["hypothesis"]["id"],
            "content_hash": hashlib.md5(new_content.encode()).hexdigest()
        })
        return candidate_v

    def evaluate(self, skill_name: str, candidate_version: str, test_cases: list = None) -> dict:
        """Phase 4 — Evaluate: run tests + safety invariants."""
        # Load candidate
        skill_dir = Path("/home/workspace/solomon-bus/versions/skill") / skill_name
        candidate_file = skill_dir / f"{candidate_version}.md"
        if not candidate_file.exists():
            return {"passed": False, "reason": "candidate not found"}

        content = candidate_file.read_text()
        results = {
            "passed": True,
            "tests_run": 0,
            "tests_passed": 0,
            "safety_passed": True,
            "issues": []
        }

        # Run safety checks
        safety_issues = self._check_safety(content, skill_name)
        if safety_issues:
            results["safety_passed"] = False
            results["issues"].extend(safety_issues)
            results["passed"] = False

        # Run test cases if provided
        if test_cases:
            for tc in test_cases:
                results["tests_run"] += 1
                if self._run_test(content, tc):
                    results["tests_passed"] += 1
                else:
                    results["passed"] = False
                    results["issues"].append(f"Test failed: {tc['name']}")

        self.log_phase("evaluate", results)
        return results

    def _check_safety(self, content: str, skill_name: str) -> list:
        """Run safety invariants on skill content."""
        issues = []
        content_lower = content.lower()
        dangerous_patterns = [
            ("rm -rf /", "Shell injection: dangerous rm command"),
            ("eval(", "Code injection: eval usage"),
            ("os.system(", "Code injection: os.system usage"),
            ("subprocess.call(", "Code injection: subprocess.call"),
            ("DELETE FROM", "SQL injection: raw DELETE without sanitization"),
            ("password = ", "Hardcoded password detected"),
            ("api_key = ", "Hardcoded API key detected"),
            ("os.environ[", "Direct env access — prefer secrets manager"),
        ]
        for pattern, reason in dangerous_patterns:
            if pattern.lower() in content_lower:
                issues.append(f"Safety: {reason}")
        # Skill-specific checks
        if skill_name == "auto-skill-router":
            if "exec(" in content or "eval(" in content:
                issues.append("Safety: skill-router cannot contain dynamic code execution")
        return issues

    def _run_test(self, content: str, test_case: dict) -> bool:
        """Run a test case against skill content."""
        # Simple pattern matching for now
        test_type = test_case.get("type", "keyword")
        if test_type == "keyword":
            return test_case.get("expected", "") in content
        elif test_type == "not_contains":
            return test_case.get("forbidden", "") not in content
        return True

    def commit(self, skill_name: str, candidate_version: str, evaluation_result: dict) -> dict:
        """Phase 5 — Commit: deploy candidate or rollback."""
        # Local import to avoid circular deps
        import sys
        sys.path.insert(0, str(Path(__file__).parent.parent / "rspl"))
        from rspl import bump_skill_version, SkillResource

        if not evaluation_result.get("passed", False):
            # Rollback: mark candidate as rejected, keep current version
            self.failed = True
            self.log_phase("commit", {
                "action": "rejected",
                "reason": evaluation_result.get("issues", ["evaluation failed"]),
                "skill": skill_name,
                "candidate": candidate_version
            })
            return {
                "action": "rejected",
                "reason": evaluation_result.get("issues"),
                "rolled_back": True
            }

        # Deploy candidate — write production version
        current = SkillResource(skill_name).current()
        prod_version = current["current_version"].split("a")[0] if "a" in candidate_version else candidate_version
        # Bump to next patch
        parts = prod_version.split(".")
        prod_version = f"{parts[0]}.{parts[1]}.{int(parts[2])+1}"
        bump_skill_version(skill_name, candidate_version, "patch")
        self.log_phase("commit", {
            "action": "deployed",
            "skill": skill_name,
            "version": prod_version
        })
        self.converged = True
        return {"action": "deployed", "version": prod_version}

    def run_full(self, task_id: str, failure_trace: str, skill_name: str,
                 new_content: str, test_cases: list = None) -> dict:
        """Run the full SEPL loop end-to-end."""
        loop = SEPLLoop(task_id, task_id)
        hypotheses = loop.reflect(failure_trace)
        candidates = loop.select(hypotheses)
        if not candidates:
            return {"status": "no_candidates", "hypotheses": []}
        candidate_v = loop.improve(skill_name, candidates[0], new_content)
        eval_result = loop.evaluate(skill_name, candidate_v, test_cases)
        commit_result = loop.commit(skill_name, candidate_v, eval_result)
        return {
            "task_id": task_id,
            "iteration": loop.iteration,
            "hypotheses": hypotheses,
            "candidate_version": candidate_v,
            "evaluation": eval_result,
            "commit": commit_result
        }


def log_failure(failure_type: str, skill_name: str, trace: str, context: dict = None) -> str:
    """Log a failure event to the SEPL failure log."""
    failure_id = hashlib.md5(f"{failure_type}{skill_name}{datetime.utcnow().isoformat()}".encode()).hexdigest()[:12]
    entry = {
        "id": failure_id,
        "failure_type": failure_type,
        "skill_name": skill_name,
        "trace": trace,
        "context": context or {},
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "sepl_task_id": f"sepl_{failure_id}"
    }
    log_file = LOGS_DIR / f"{failure_type}_{datetime.utcnow().strftime('%Y-%m-%d')}.jsonl"
    with open(log_file, "a") as f:
        f.write(json.dumps(entry) + "\n")
    return entry["sepl_task_id"]


def load_safety_invariants(skill_type: str = None) -> dict:
    """Load safety invariants for skill type."""
    inv_file = SAFETY_DIR / "invariants.json"
    if not inv_file.exists():
        return {}
    invariants = json.loads(inv_file.read_text())
    if skill_type:
        return invariants.get(skill_type, {})
    return invariants


def check_safety(content: str, skill_type: str) -> tuple:
    """Standalone safety check. Returns (passed, issues)."""
    loop = SEPLLoop("safety_check", "safety_check")
    issues = loop._check_safety(content, skill_type or "generic")
    return len(issues) == 0, issues


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("SEPL: Self-Evolution Protocol Layer for Solomon Bus")
        print("Usage: python3 sepl.py [log_failure|run_loop|check_safety] [args...]")
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "log_failure" and len(sys.argv) >= 4:
        print(log_failure(sys.argv[2], sys.argv[3], sys.argv[4]))
    elif cmd == "check_safety" and len(sys.argv) >= 3:
        content = sys.argv[3]
        passed, issues = check_safety(content, sys.argv[2] if len(sys.argv) > 2 else "generic")
        print(f"Safety: {'PASS' if passed else 'FAIL'}")
        for issue in issues:
            print(f"  - {issue}")