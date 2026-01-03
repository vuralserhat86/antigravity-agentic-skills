---
name: backend_core
router_kit: FullStackKit
description: Node.js/TypeScript temel prensipler, proje yapısı ve TypeScript strict mode kuralları.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, backend core, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - backend-database
---

# 🔧 Backend Core

> Node.js/TypeScript temel prensipler ve proje yapısı.

---

*Backend Core v1.2 - Verified*

## 🔄 Workflow

> **Kaynak:** [Node.js Best Practices - Project Structure](https://github.com/goldbergyoni/nodebestpractices#-1-project-structure-practices)

### Aşama 1: Foundation (Structure)
- [ ] **Components**: Klasörleri teknik role göre değil (controllers, models), bileşene göre ayır (components/user, components/order).
- [ ] **Config**: `dotenv` ve `envalid` (veya Zod) ile ortam değişkenlerini tip güvenli hale getir.
- [ ] **Entry**: Uygulamayı `app.ts` (setup) ve `server.ts` (listen) olarak ayır.

### Aşama 2: Core Utilities
- [ ] **Logger**: `console.log` yerine `winston` veya `pino` kur.
- [ ] **Async Wrapper**: Promise rejection'ları yakalamak için global handler veya wrapper kullan.
- [ ] **Linter**: ESLint ve Prettier ayarlarını CI pipeline'a bağla.

### Aşama 3: Hardening
- [ ] **Graceful Shutdown**: SIGTERM/SIGINT sinyallerini dinle ve bağlantıları nazikçe kapat.
- [ ] **Health Check**: `/health` endpoint'i ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Yeni bir özellik eklerken 5 farklı klasöre dokunmak gerekiyor mu? (Gerekmemeli -> Component based) |
| 2 | `.env` dosyası commit edilmiş mi? (Edilmemeli) |
| 3 | Uygulama çökünce process otomatik restart oluyor mu? (PM2/Docker) |
