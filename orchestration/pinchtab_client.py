"""
PinchTab HTTP API client for Solomon OS orchestration layer.
Base URL: http://localhost:9888, Auth: Bearer solomon123
"""

import httpx
import time
from typing import Optional

BASE_URL = "http://localhost:9888"
TOKEN = "solomon123"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


class PinchTabClient:
    def __init__(self, base_url: str = BASE_URL, token: str = TOKEN):
        self.base_url = base_url.rstrip("/")
        self.token = token
        self.instance_port: Optional[int] = None
        self.instance_id: Optional[str] = None

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    def start_instance(self, mode: str = "headless") -> dict:
        """Start a new browser instance. Returns {id, port, status}."""
        with httpx.Client(base_url=self.base_url, headers=self._headers(), timeout=30) as client:
            resp = client.post("/instances/start", json={"mode": mode})
            resp.raise_for_status()
            data = resp.json()
            self.instance_id = data["id"]
            self.instance_port = int(data["port"])
            # Wait for instance to be ready
            for _ in range(10):
                time.sleep(1)
                status = self.instance_status(self.instance_id)
                if status.get("status") == "running":
                    break
            return data

    def stop_instance(self, instance_id: str) -> dict:
        """Stop a browser instance."""
        with httpx.Client(base_url=self.base_url, headers=self._headers(), timeout=10) as client:
            resp = client.post(f"/instances/{instance_id}/stop")
            resp.raise_for_status()
            return resp.json()

    def instance_status(self, instance_id: str) -> dict:
        """Get instance status."""
        with httpx.Client(base_url=self.base_url, headers=self._headers(), timeout=10) as client:
            resp = client.get(f"/instances/{instance_id}")
            resp.raise_for_status()
            return resp.json()

    def navigate(self, url: str) -> dict:
        """Navigate to URL in the active instance. Returns {tabId, title, url}."""
        if not self.instance_port:
            raise RuntimeError("No instance running. Call start_instance() first.")
        with httpx.Client(base_url=self.base_url, headers=self._headers(), timeout=30) as client:
            resp = client.post(f"/{self.instance_port}/navigate", json={"url": url})
            resp.raise_for_status()
            return resp.json()

    def snapshot(self, filter_mode: str = "interactive") -> dict:
        """Get accessibility tree snapshot. filter=interactive|all|text."""
        if not self.instance_port:
            raise RuntimeError("No instance running.")
        with httpx.Client(base_url=self.base_url, headers=self._headers(), timeout=15) as client:
            resp = client.get(f"/{self.instance_port}/snapshot?filter={filter_mode}")
            resp.raise_for_status()
            return resp.json()

    def action(self, kind: str, ref: str, value: Optional[str] = None) -> dict:
        """Execute an action: click, type, fill, press, scroll, hover, select."""
        body = {"kind": kind, "ref": ref}
        if value is not None:
            body["value"] = value
        if not self.instance_port:
            raise RuntimeError("No instance running.")
        with httpx.Client(base_url=self.base_url, headers=self._headers(), timeout=15) as client:
            resp = client.post(f"/{self.instance_port}/action", json=body)
            resp.raise_for_status()
            return resp.json()

    def screenshot(self) -> bytes:
        """Take a screenshot. Returns raw PNG bytes."""
        if not self.instance_port:
            raise RuntimeError("No instance running.")
        with httpx.Client(base_url=self.base_url, headers=self._headers(), timeout=15) as client:
            resp = client.get(f"/{self.instance_port}/screenshot")
            resp.raise_for_status()
            return resp.content

    def list_tabs(self) -> dict:
        """List all tabs across instances."""
        with httpx.Client(base_url=self.base_url, headers=self._headers(), timeout=10) as client:
            resp = client.get("/tabs")
            resp.raise_for_status()
            return resp.json()

    def close(self):
        """Stop the current instance if running."""
        if self.instance_id:
            try:
                self.stop_instance(self.instance_id)
            except Exception:
                pass
            self.instance_id = None
            self.instance_port = None


if __name__ == "__main__":
    import json

    client = PinchTabClient()
    print("Starting instance...")
    inst = client.start_instance()
    print(json.dumps(inst, indent=2))

    print("\nNavigating to example.com...")
    nav = client.navigate("https://example.com")
    print(json.dumps(nav, indent=2))

    print("\nTaking snapshot...")
    snap = client.snapshot()
    print(json.dumps(snap, indent=2))

    print("\nStopping instance...")
    stop = client.close()
    print(json.dumps(stop, indent=2))
