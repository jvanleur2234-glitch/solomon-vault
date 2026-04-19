// SelfSync Client — connects to selfsync server for cross-device bookmark/password sync
// GitHub: loyalpartner/selfsync
// Self-hosted Chrome Sync alternative — no Google required

export class SelfSync {
  constructor() {
    this.serverUrl = null; // Configured in options page
    this.apiKey = null;    // Configured in options page
  }

  async configure() {
    return new Promise((resolve) => {
      chrome.storage.sync.get(['selfsync_url', 'selfsync_key'], (data) => {
        this.serverUrl = data.selfsync_url || 'http://localhost:3991';
        this.apiKey = data.selfsync_key || '';
        resolve({ url: this.serverUrl, key: this.apiKey ? '***' : 'not set' });
      });
    });
  }

  async push(data) {
    await this.configure();
    
    if (!this.serverUrl) {
      console.log('[SelfSync] Not configured — skipping push');
      return false;
    }

    try {
      const response = await fetch(`${this.serverUrl}/sync`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          ...(this.apiKey ? { 'Authorization': `Bearer ${this.apiKey}` } : {})
        },
        body: JSON.stringify({
          data,
          timestamp: Date.now(),
          device: await this.getDeviceId()
        })
      });
      
      return response.ok;
    } catch (e) {
      console.error('[SelfSync] Push failed:', e);
      return false;
    }
  }

  async pull() {
    await this.configure();
    
    if (!this.serverUrl) {
      return null;
    }

    try {
      const response = await fetch(`${this.serverUrl}/sync`, {
        method: 'GET',
        headers: {
          ...(this.apiKey ? { 'Authorization': `Bearer ${this.apiKey}` } : {})
        }
      });
      
      if (!response.ok) return null;
      
      const result = await response.json();
      return result.data;
    } catch (e) {
      console.error('[SelfSync] Pull failed:', e);
      return null;
    }
  }

  async getDeviceId() {
    return new Promise((resolve) => {
      chrome.storage.local.get(['device_id'], (data) => {
        if (data.device_id) {
          resolve(data.device_id);
        } else {
          const id = 'dev_' + Math.random().toString(36).slice(2, 11);
          chrome.storage.local.set({ device_id: id });
          resolve(id);
        }
      });
    });
  }
}
