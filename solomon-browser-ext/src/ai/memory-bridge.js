// Memory Bridge — manages Solomon browser memory
// Stores: page visits, interactions, learnings, extracted content

export class MemoryBridge {
  constructor() {
    this.storageKey = 'solomon_memory';
    this.maxItems = 500;
  }

  async store(content, metadata = {}) {
    const memory = await this.getAll();
    
    memory.unshift({
      id: this.generateId(),
      content,
      metadata,
      timestamp: Date.now(),
      type: metadata.type || 'memory'
    });

    // Trim to max size
    while (memory.length > this.maxItems) {
      memory.pop();
    }

    await this.save(memory);
    return true;
  }

  async retrieve(query, limit = 20) {
    const memory = await this.getAll();
    
    if (!query) {
      return memory.slice(0, limit);
    }

    // Simple text search
    const queryLower = query.toLowerCase();
    const results = memory.filter(item => {
      const text = (item.content + ' ' + JSON.stringify(item.metadata)).toLowerCase();
      return text.includes(queryLower);
    });

    return results.slice(0, limit);
  }

  async getAll() {
    return new Promise((resolve) => {
      chrome.storage.local.get([this.storageKey], (data) => {
        resolve(data[this.storageKey] || []);
      });
    });
  }

  async save(memory) {
    return new Promise((resolve) => {
      chrome.storage.local.set({ [this.storageKey]: memory }, resolve);
    });
  }

  generateId() {
    return `mem_${Date.now()}_${Math.random().toString(36).slice(2, 9)}`;
  }

  async clear() {
    return new Promise((resolve) => {
      chrome.storage.local.remove([this.storageKey], resolve);
    });
  }
}
