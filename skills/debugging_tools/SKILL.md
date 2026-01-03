---
name: debugging_tools
router_kit: FullStackKit
description: Chrome DevTools, VS Code Debugger ve Proxy araçları kullanımı.
metadata:
  skillport:
    category: quality
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging tools, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - browser-tools
---

# 🛠️ Debugging Tools

> Modern hata ayıklama araçlarının etkin kullanımı.

---

*Debugging Tools v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Chrome DevTools Documentation](https://developer.chrome.com/docs/devtools/)

### Aşama 1: Browser Debugging (DevTools)
- [ ] **Inspect**: Element/Network/Console tablarını kullanarak sorunu lokalize et.
- [ ] **Breakpoints**: `debugger;` veya DevTools UI üzerinden satır bazlı duraklama noktaları koy.
- [ ] **Network Audit**: API isteklerinin payload ve header yapılarını incele.

### Aşama 2: IDE & Server Debugging
- [ ] **VS Code Debug**: `launch.json` yapılandırması ile Node.js veya Browser tarafını IDE üzerinden debug et.
- [ ] **Watch**: Değişkenlerin anlık değerlerini takip listesine ekle.

### Aşama 3: Proxy & Advanced Tools
- [ ] **Charles/Fiddler**: Network trafiğini yakalamak ve manipüle etmek için proxy araçlarını kullan.
- [ ] **React DevTools**: Bileşen ağacı ve state/props değişimlerini izle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Breakpoint çalışıyor mu? |
| 2     | Network isteği 4xx/5xx mi dönüyor? |
| 3     | State değişimi UI'ya yansıyor mu? |
