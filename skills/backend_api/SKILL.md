---
name: backend_api
router_kit: FullStackKit
description: REST uygulama, validation, security headers, auth patterns. ⚠️ Kod yazarken kullan. API tasarımı/GraphQL için → api-design.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, backend api, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - backend-database
---

# 🌐 Backend API

> REST API tasarımı ve güvenlik best practices.

---

*Backend API v1.2 - Verified*

## 🔄 Workflow

> **Kaynak:** [Node.js Best Practices (Goldberg)](https://github.com/goldbergyoni/nodebestpractices#-2-metrics-and-logging)

### Aşama 1: Interface Design (Contract First)
- [ ] **Specs**: OpenAPI (Swagger) veya Zod şeması ile input/output tanımla.
- [ ] **Roadmap**: Endpoint listesini ve HTTP metodlarını belirle.

### Aşama 2: Layered Implementation
- [ ] **Controller**: Sadece HTTP request/response yönet, business logic yazma.
- [ ] **Service**: Tüm iş mantığını buraya koy (Reusable).
- [ ] **DAL**: Veritabanı erişimini soyutla.

### Aşama 3: Security & Hardening
- [ ] **Middleware**: Helmet, Rate Limiter ve CORS ayarlarını yap.
- [ ] **Validation**: Gelen her veriyi (Body, Query, Params) Zod ile doğrula.
- [ ] **Error**: Global Error Handler kur ve user-friendly mesaj dön.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | API dokümantasyonu koddan önce mi hazırlandı? |
| 2 | Controller dosyasında hiç SQL/ORM kodu var mı? (Olmamalı) |
| 3 | 500 hatası dönünce stack trace gizleniyor mu? |
