---
name: mcp_builder
router_kit: FullStackKit
description: MCP (Model Context Protocol) server oluşturma, FastMCP/TypeScript SDK kullanımı ve API entegrasyonu rehberi.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, mcp builder, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - server
---

# 🔌 MCP Builder

> MCP server oluşturma ve API entegrasyonu rehberi.

---

## 📋 MCP Nedir?

Model Context Protocol (MCP), LLM'lerin dış servislerle etkileşim kurmasını sağlayan standart bir protokoldür.

### Kullanım Alanları
- API entegrasyonları
- Veritabanı bağlantıları
- Dosya sistemi erişimi
- Harici servis çağrıları

---

## 🐍 Python (FastMCP)

### Kurulum
```bash
pip install fastmcp
```

### Basit Server
```python
from fastmcp import FastMCP

mcp = FastMCP("my-server")

@mcp.tool()
def hello(name: str) -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

### Resource Ekleme
```python
@mcp.resource("config://app")
def get_config() -> str:
    """Get application configuration."""
    return json.dumps({"version": "1.0"})
```

---

## 📘 TypeScript (MCP SDK)

### Kurulum
```bash
npm install @modelcontextprotocol/sdk
```

### Server Oluşturma
```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new McpServer({
  name: "my-server",
  version: "1.0.0",
});

server.tool("hello", { name: "string" }, async ({ name }) => {
  return { content: [{ type: "text", text: `Hello, ${name}!` }] };
});

const transport = new StdioServerTransport();
await server.connect(transport);
```

---

## ⚙️ Yapılandırma

### mcp_config.json
```json
{
  "mcpServers": {
    "my-server": {
      "command": "python",
      "args": ["path/to/server.py"],
      "env": {
        "API_KEY": "your-key"
      }
    }
  }
}
```

---

## 🎯 Best Practices

1. **Tool naming**: Açıklayıcı, lowercase, hyphen-separated
2. **Descriptions**: Her tool için detaylı docstring
3. **Error handling**: Try-catch ile hata yönetimi
4. **Type hints**: Parametre tipleri belirt
5. **Validation**: Input validation yap

---

*MCP Builder v1.0*
