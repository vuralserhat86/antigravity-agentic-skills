---
name: agents_md
router_kit: AIKit
description: AGENTS.md dosyaları oluşturma, monorepo yapılandırma ve agent instruction yönetimi rehberi.
metadata:
  skillport:
    category: development
    tags: [agents, agents md, algorithms, artificial intelligence, automation, chatbots, cognitive services, deep learning, embeddings, frameworks, generative ai, inference, large language models, llm, machine learning, model fine-tuning, natural language processing, neural networks, nlp, openai, prompt engineering, rag, retrieval augmented generation, tools, vector databases, workflow automation]      - conventions
---

# 🤖 AGENTS.md

> Agent instruction ve conventions dosyaları oluşturma rehberi.

---

## 📋 AGENTS.md Nedir?

AGENTS.md, AI coding assistant'ların proje özelinde kurallara uymasını sağlayan convention dosyasıdır.

### Kullanım Alanları
- Proje spesifik kurallar
- Kod stili conventions
- Dizin yapısı açıklamaları
- Yasaklı pattern'ler
- Önerilen yaklaşımlar

---

## 📁 Root AGENTS.md Template

```markdown
# AGENTS.md

Bu proje için AI assistant kuralları.

## Proje Genel Bakış
[Projenin kısa açıklaması]

## Tech Stack
- Framework: Next.js 15
- Language: TypeScript
- Styling: Tailwind CSS
- Database: PostgreSQL

## Dizin Yapısı
\`\`\`
src/
├── app/           # Next.js App Router pages
├── components/    # React components
├── lib/           # Utility functions
├── hooks/         # Custom React hooks
└── types/         # TypeScript types
\`\`\`

## Kod Conventions

### Naming
- Components: PascalCase (`UserProfile.tsx`)
- Hooks: camelCase with `use` prefix (`useAuth.ts`)
- Utils: camelCase (`formatDate.ts`)

### Imports
- Absolute imports: `@/components/...`
- Group order: React > External > Internal > Types

## Yasaklar
- ❌ `any` type kullanma
- ❌ `console.log` production'da
- ❌ Inline styles

## Tercih Edilenler
- ✅ Server Components (default)
- ✅ Zod validation
- ✅ Error boundaries
```

---

## 📂 Nested AGENTS.md (Modül Bazlı)

### src/components/AGENTS.md
```markdown
# Components Conventions

## Component Yapısı
\`\`\`tsx
// 1. Imports
// 2. Types
// 3. Component
// 4. Export
\`\`\`

## Props
- Interface ile tanımla
- `Props` suffix kullan

## Styling
- Tailwind class'ları kullan
- `cn()` utility ile merge
```

### src/api/AGENTS.md
```markdown
# API Conventions

## Endpoint Yapısı
- RESTful naming
- Versioning: `/api/v1/`

## Error Handling
- Consistent error response format
- HTTP status codes doğru kullan
```

---

## 🗺️ Feature Map

```markdown
## Feature: User Authentication

### Paths
- Entry: `src/app/(auth)/login/page.tsx`
- API: `src/app/api/auth/[...nextauth]/route.ts`
- Components: `src/components/auth/`
- Hooks: `src/hooks/useAuth.ts`

### Tests
- Unit: `__tests__/auth/`
- E2E: `e2e/auth.spec.ts`

### Docs
- `docs/auth.md`
```

---

## 🔄 Monorepo Yapısı

```markdown
# Monorepo AGENTS.md

## Packages
| Package | Path | Purpose |
|---------|------|---------|
| @acme/web | apps/web | Next.js frontend |
| @acme/api | apps/api | Express backend |
| @acme/ui | packages/ui | Shared components |
| @acme/utils | packages/utils | Shared utilities |

## Cross-Package Rules
- UI components: `@acme/ui` kullan
- Utils: `@acme/utils` kullan
- Duplicate code yasak
```

---

*AGENTS.md v1.0 - Convention Over Configuration*
