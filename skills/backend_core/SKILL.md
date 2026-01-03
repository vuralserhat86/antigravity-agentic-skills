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

## 📋 1. Kapsam

| Alan | Teknoloji |
|------|-----------|
| Runtime | Node.js 20+ (LTS) |
| Dil | TypeScript (Strict) |
| Framework | NestJS, Fastify, Express |

---

## ⚙️ 2. TypeScript Strict Mode

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noImplicitReturns": true
  }
}
```

### `any` Yasak
```typescript
// ❌ YANLIŞ
function process(data: any) { }

// ✅ DOĞRU
function process(data: DataPayload) { }

// Bilinmeyen için unknown kullan
function parse(input: unknown) { }
```

---

## 📁 3. Proje Yapısı (Feature-First)

```
src/
├── modules/
│   ├── auth/
│   │   ├── auth.controller.ts
│   │   ├── auth.service.ts
│   │   ├── auth.repository.ts
│   │   └── auth.dto.ts
│   └── users/
├── shared/
│   ├── middleware/
│   ├── guards/
│   └── utils/
├── infrastructure/
│   ├── database/
│   ├── cache/
│   └── logger/
├── config/
└── main.ts
```

---

## 🔐 4. Environment Variables

```typescript
import { z } from 'zod';

const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production', 'test']),
  PORT: z.string().transform(Number),
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
});

export const env = envSchema.parse(process.env);
```

---

## 🔗 İlgili Skill'ler
- `backend-api` - REST/GraphQL tasarımı
- `backend-database` - DB patterns, caching

---

- `backend-database` - DB patterns, caching

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
