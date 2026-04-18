#!/usr/bin/env python3
"""
Browser Recorder - CDP-based browser event capture
Connects to Chrome via Chrome DevTools Protocol to record user actions as skills.
"""

import json
import sys
import time
import socket
import threading
import argparse
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

try:
    import websocket
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "websocket-client", "-q"])
    import websocket

SKILLS_DIR = Path("/home/workspace/Skills/browser-recorder/skills")
SKILLS_DIR.mkdir(parents=True, exist_ok=True)

class BrowserRecorder:
    def __init__(self, port=9222, skill_name=None):
        self.port = port
        self.skill_name = skill_name
        self.ws = None
        self.msg_id = 0
        self.recording = []
        self.recording_lock = threading.Lock()
        self.current_url = ""
        self.running = False
        
    def ws_connect(self):
        """Connect to Chrome DevTools Protocol WebSocket."""
        ws_url = f"ws://localhost:{self.port}/devtools/page/target-{self.port}"
        try:
            # Try to get the correct target
            import http.client
            conn = http.client.HTTPConnection("localhost", self.port)
            conn.request("GET", "/json")
            resp = json.loads(conn.getresponse().read())
            if resp:
                ws_url = resp[0].get("webSocketDebuggerUrl", ws_url)
        except Exception:
            pass
        
        self.ws = websocket.create_connection(ws_url, suppress=True)
        self.running = True
        
    def send(self, method, params=None):
        """Send CDP command and return response."""
        self.msg_id += 1
        msg = {"id": self.msg_id, "method": method}
        if params:
            msg["params"] = params
        self.ws.send(json.dumps(msg))
        
        while True:
            resp = json.loads(self.ws.recv())
            if resp.get("id") == self.msg_id:
                return resp.get("result", {})
    
    def enable_events(self):
        """Enable all DOM/Input/Network event collection."""
        self.send("DOM.enable")
        self.send("Input.enable")
        self.send("Page.enable")
        self.send("Network.enable")
        
    def get_selector(self, node_id):
        """Build a CSS selector for a DOM node."""
        try:
            result = self.send("DOM.getPath", {"nodeId": node_id})
            return result.get("path", f"node#{node_id}")
        except:
            return f"node#{node_id}"
    
    def record_step(self, action, selector, value=None, description=""):
        """Add a recorded step to the buffer."""
        step = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "selector": selector,
            "description": description
        }
        if value is not None:
            step["value"] = value
            
        with self.recording_lock:
            self.recording.append(step)
            
        print(f"  📝 Recorded: {action} → {selector} {f'= {value}' if value else ''}")
    
    def handle_event(self, method, params):
        """Handle incoming CDP events."""
        with self.recording_lock:
            if not self.recording and method not in ("Page.frameNavigated", "DOM.documentUpdated"):
                return
        
        if method == "Page.frameNavigated":
            frame = params.get("frame", {})
            url = frame.get("url", "")
            if url and url != self.current_url:
                self.current_url = url
                self.record_step("navigate", url, description=f"Navigated to {urlparse(url).netloc}")
                
        elif method == "Input.dispatchMouseEvent":
            pass  # Mouse events handled by click generation
                
        elif method == "DOM.characterDataModified":
            pass  # Text changes
            
        elif method == "Input.dispatchKeyEvent" and params.get("type") == "keyDown":
            pass  # Keystrokes handled separately
    
    def listen_events(self):
        """Listen for CDP events in background thread."""
        while self.running:
            try:
                msg = json.loads(self.ws.recv())
                if "method" in msg:
                    threading.Thread(
                        target=self.handle_event,
                        args=(msg["method"], msg.get("params", {})),
                        daemon=True
                    ).start()
            except Exception as e:
                if self.running:
                    print(f"Listener error: {e}")
                break
    
    def start(self, url=None):
        """Start recording session."""
        print(f"\n🎬 Browser Recorder started on port {self.port}")
        print(f"   Skill: {self.skill_name}")
        print(f"   Skills saved to: {SKILLS_DIR}")
        print("\n   Performing actions in your browser now...")
        print("   Press Ctrl+C to stop and save.\n")
        
        self.ws_connect()
        self.enable_events()
        
        if url:
            print(f"   Navigating to: {url}")
            self.send("Page.navigate", {"url": url})
            time.sleep(2)
        
        # Start event listener thread
        listener = threading.Thread(target=self.listen_events, daemon=True)
        listener.start()
        
        # Also poll for DOM changes
        last_html = ""
        while self.running:
            time.sleep(1)
            try:
                doc = self.send("DOM.getDocument", {"depth": 0})
                # Don't hammer DOM - just watch
            except:
                pass
    
    def stop(self):
        """Stop recording and save skill file."""
        self.running = False
        print(f"\n\n💾 Saving skill '{self.skill_name}'...")
        
        if not self.recording:
            print("   No actions recorded.")
            return
        
        skill = {
            "name": self.skill_name,
            "created": datetime.now().isoformat(),
            "steps": self.recording,
            "metadata": {
                "total_steps": len(self.recording),
                "recorded_from": self.current_url
            }
        }
        
        path = SKILLS_DIR / f"{self.skill_name}.json"
        with open(path, "w") as f:
            json.dump(skill, f, indent=2)
        
        print(f"   ✅ Saved {len(self.recording)} steps → {path}")
        print(f"\n   To replay: python3 replay.py {self.skill_name}")
        
        if self.ws:
            self.ws.close()
        
        return skill


def find_chrome_port():
    """Try to find an active Chrome debugging port."""
    for port in [9222, 9333, 9444, 9555]:
        try:
            import http.client
            conn = http.client.HTTPConnection("localhost", port, timeout=1)
            conn.request("GET", "/json")
            resp = conn.getresponse()
            if resp.status == 200:
                return port
        except:
            continue
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Browser Recorder - CDP event capture")
    parser.add_argument("action", choices=["start", "stop", "status"], help="Action to perform")
    parser.add_argument("--name", "-n", help="Skill name")
    parser.add_argument("--port", "-p", type=int, default=9222, help="CDP port")
    parser.add_argument("--url", "-u", help="Starting URL")
    
    args = parser.parse_args()
    
    if args.action == "start":
        port = find_chrome_port() or args.port
        name = args.name or input("Skill name: ").strip().replace(" ", "-").lower()
        
        if not name:
            print("Error: skill name required")
            sys.exit(1)
        
        recorder = BrowserRecorder(port=port, skill_name=name)
        try:
            recorder.start(url=args.url)
        except KeyboardInterrupt:
            recorder.stop()
            
    elif args.action == "status":
        port = find_chrome_port()
        if port:
            print(f"✅ Chrome found on port {port}")
        else:
            print("❌ Chrome DevTools not found. Start Chrome with:")
            print("   chrome --remote-debugging-port=9222")
