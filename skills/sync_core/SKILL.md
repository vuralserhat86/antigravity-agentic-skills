---
name: sync_core
router_kit: FullStackKit
description: Multi-file sync - atomic changes, dependency tracking ve conflict resolution.
metadata:
  skillport:
    category: development
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, sync core, testing, utilities, version control, workflow]      - refactoring-patterns
---

# 🔄 Sync Core

> Multi-file synchronization ve atomic changes.

---

## 📋 Atomic Change Principle

```markdown
Birden fazla dosya değişikliği gerektiğinde:
1. Tüm değişiklikleri önceden planla
2. Sıralı değişiklik yap
3. Her adımda build/test çalıştır
4. Tek commit'te birleştir
```

---

## 🔗 Dependency Tracking

```typescript
// Değişiklik yapmadan önce etkilenen dosyaları bul
// import/export chain'i takip et

// file-a.ts
export const API_URL = 'https://api.example.com';

// file-b.ts
import { API_URL } from './file-a';

// Değişiklik: API_URL → Tüm import'ları güncelle
```

---

## ⚠️ Change Order

```
1. Types/Interfaces (önce)
2. Utils/Helpers
3. Services
4. Components (son)
```

---

## ✅ Checklist

- [ ] Tüm dosyalar belirlendi
- [ ] Sıralama doğru
- [ ] Her adımda test
- [ ] Tek commit

---

*Sync Core v1.0*
