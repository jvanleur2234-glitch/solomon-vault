// Hermes Client — connects to Solomon OS AI layer from the browser extension
// Routes to Zo AI (via /zo/ask API) or local Ollama

export class HermesClient {
  constructor() {
    this.endpoint = 'https://api.zo.computer/zo/ask';
    this.model = 'vercel:minimax/minimax-m2.7';
    this.localEndpoint = 'http://localhost:11434/api/generate';
  }

  async think(prompt, context = {}) {
    const mode = context.mode || 'balanced';
    
    // Build system prompt based on mode
    const systemPrompt = this.getSystemPrompt(mode);
    
    // Construct full prompt with context
    const fullPrompt = this.buildPrompt(prompt, context, systemPrompt);
    
    // Try local first (Ollama), fall back to cloud
    try {
      const localResult = await this.tryLocal(fullPrompt);
      if (localResult) return localResult;
    } catch (e) {
      console.log('[Hermes] Local unavailable, falling back to cloud');
    }
    
    return this.callCloud(fullPrompt);
  }

  getSystemPrompt(mode) {
    const base = 'You are Solomon, an AI assistant embedded in a browser extension. ';
    
    switch (mode) {
      case 'fast':
        return base + 'Give concise, direct answers. 1-3 sentences max.';
      case 'deep':
        return base + 'Think deeply about this. Consider multiple angles, implications, and edge cases. Show your reasoning. Be thorough.';
      default:
        return base + 'Provide a balanced response — informative but not overly long.';
    }
  }

  buildPrompt(prompt, context, systemPrompt) {
    let full = systemPrompt + '\n\n';
    
    if (context.page) {
      full += `Current page context:\n`;
      if (context.page.title) full += `Title: ${context.page.title}\n`;
      if (context.page.url) full += `URL: ${context.page.url}\n`;
      if (context.page.h1) full += `Heading: ${context.page.h1}\n`;
      if (context.page.text) full += `Page text: ${context.page.text.slice(0, 1000)}\n`;
      full += '\n';
    }
    
    full += `User question: ${prompt}`;
    return full;
  }

  async tryLocal(prompt) {
    const response = await fetch(this.localEndpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'llama3.2',
        prompt: prompt,
        stream: false,
        options: { temperature: 0.7 }
      })
    });
    
    if (!response.ok) throw new Error('Local unavailable');
    
    const data = await response.json();
    return data.response;
  }

  async callCloud(prompt) {
    const response = await fetch(this.endpoint, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${await this.getToken()}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        input: prompt,
        model_name: this.model
      })
    });
    
    if (!response.ok) throw new Error('Cloud API failed');
    
    const data = await response.json();
    return data.output;
  }

  async getToken() {
    // In a real extension this would use proper OAuth or extension-specific auth
    // For now, read from storage
    return new Promise((resolve) => {
      chrome.storage.local.get(['zo_token'], (data) => {
        resolve(data.zo_token || process.env.ZO_CLIENT_IDENTITY_TOKEN || '');
      });
    });
  }
}
