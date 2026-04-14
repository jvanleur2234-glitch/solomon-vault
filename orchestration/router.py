"""
Solomon OS — Orchestration Router
Decides: analyze | browser | hermes | russell
"""

import re
from typing import Literal

# URL patterns that suggest specific agents
AGENT_URL_PATTERNS = {
    "github": "hermes",
    "gitlab": "hermes",
    "linear": "hermes",
    "notion": "hermes",
    "slack": "hermes",
    "discord": "hermes",
    "shopify": "hermes",
    "stripe": "hermes",
    "twitter.com": "russell",
    "x.com": "russell",
    "linkedin.com": "russell",
    "tiktok.com": "russell",
    "instagram.com": "russell",
    "youtube.com": "russell",
}

# Keywords that suggest browser action
BROWSER_KEYWORDS = {
    "login", "signin", "click", "fill", "submit", "browse", "scrape",
    "extract", "download", "upload", "post", "comment", "reply"
}

# Keywords that suggest Hermes skills
HERMES_KEYWORDS = {
    "code", "git", "repo", "file", "edit", "write", "debug", "deploy",
    "database", "api", "script", "build", "test", "search code"
}

# Keywords that suggest Russell (social/content)
RUSSELL_KEYWORDS = {
    "tweet", "post", "reply", "dm", "follow", "like", "retweet",
    "linkedin", "write post", "social", "content", "comment"
}


def classify_url(url: str, task_desc: str = "") -> Literal["analyze", "browser", "hermes", "russell"]:
    """
    Decide which execution path to take for a URL + task.
    Returns: analyze | browser | hermes | russell
    """
    combined = (url + " " + task_desc).lower()

    # Check for Hermes keywords
    if any(k in combined for k in HERMES_KEYWORDS):
        return "hermes"

    # Check for Russell keywords
    if any(k in combined for k in RUSSELL_KEYWORDS):
        return "russell"

    # Check for browser keywords
    if any(k in combined for k in BROWSER_KEYWORDS):
        return "browser"

    # Check URL patterns
    for pattern, agent in AGENT_URL_PATTERNS.items():
        if pattern in url.lower():
            return agent

    # Default: analyze first (safe)
    return "analyze"


def route(url: str, task_desc: str = "") -> dict:
    """
    Returns routing decision with reasoning and recommended action.
    """
    decision = classify_url(url, task_desc)

    explanations = {
        "analyze": "No specific agent needed — snapshot + summarize the page",
        "browser": "Browser action requested — use PinchTab to interact with page",
        "hermes": "Development task detected — route to Hermes agent",
        "russell": "Social/content task detected — route to Russell Tuna",
    }

    return {
        "decision": decision,
        "reason": explanations[decision],
        "url": url,
        "task": task_desc,
    }


if __name__ == "__main__":
    test_cases = [
        ("https://github.com/facebook/react", "search for useState usage"),
        ("https://twitter.com/elonmusk/status/123", "like and reply with hello"),
        ("https://shopify.com/admin", "add a new product"),
        ("https://example.com", "just browsing"),
        ("https://notion.so/workspace", "create a new page"),
    ]

    for url, task in test_cases:
        r = route(url, task)
        print(f"URL: {url}")
        print(f"Task: {task}")
        print(f"Decision: {r['decision']} — {r['reason']}\n")
