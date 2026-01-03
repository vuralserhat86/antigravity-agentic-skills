---
name: typescript_advanced
router_kit: FullStackKit
description: TypeScript advanced types, generics, utility types ve strict type checking rehberi.
metadata:
  skillport:
    category: engineering
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, maintainability, optimization, performance, productivity, programming, quality assurance, refactoring, software engineering, standards, testing, typescript, typescript advanced_1, utilities, version control, workflow]      - javascript-mastery
---

# 🔷 TypeScript Advanced

> Tip güvenliği (Type Safety) ve ileri seviye TypeScript pratikleri.

---

## 🚀 Advanced Types

### Generics
```typescript
function getFirst<T>(arr: T[]): T | undefined {
  return arr[0];
}

const num = getFirst<number>([1, 2, 3]); // number | undefined
```

### Utility Types
- `Partial<T>`: Tüm özellikleri opsiyonel yapar.
- `Required<T>`: Tüm özellikleri zorunlu yapar.
- `Readonly<T>`: Özellikleri değiştirilemez yapar.
- `Pick<T, K>`: Belirli özellikleri seçer.
- `Omit<T, K>`: Belirli özellikleri çıkarır.

---

## 🛠️ Mapping & Conditional Types

### Conditional Types
```typescript
type IsString<T> = T extends string ? true : false;
type A = IsString<string>; // true
type B = IsString<number>; // false
```

### Mapped Types
```typescript
type Optional<T> = {
  [P in keyof T]?: T[P];
};
```

---

## 🔧 Workflow

> **Kaynak:** [TypeScript Deep Dive](https://basarat.gitbook.io/typescript/) & [Official TypeScript Documentation](https://www.typescriptlang.org/docs/)

### Aşama 1: Strict Configuration
- [ ] **Config**: `tsconfig.json` içinde `strict: true`, `noImplicitAny: true` ve `exactOptionalPropertyTypes: true` ayarlarını aktif et.
- [ ] **Path Aliases**: Karmaşık import yollarını önlemek için `paths` (örn: `@/*`) ayarlarını yap.
- [ ] **Check CI**: `tsc --noEmit` komutunu CI/CD sürecine hata yakalayıcı olarak ekle.

### Aşama 2: Strategic Typing
- [ ] **Inference over Annotation**: TypeScript'in otomatik tip çıkarımı (Inference) yapabildiği yerlerde gereksiz tip tanımlamalarından kaçın.
- [ ] **Union & Discriminated Unions**: State veya Type kontrollerinde `type Action = { type: 'save' } | { type: 'delete' }` gibi yapıları kullan.
- [ ] **Generics**: Yeniden kullanılabilir (Reusable) bileşen ve fonksiyonlarda `Generic` tiplerle esnekliği sağla.

### Aşama 3: Verification & Refinement
- [ ] **Opaque Types**: Primitive tipleri birbirinden ayırmak için "Branded Types" (örn: `type UserId = string & { __brand: 'User' }`) kullan.
- [ ] **Assertion vs Guard**: `as` (Assertion) kullanımını minimize et, yerine `is` (Type Guard) fonksiyonlarını tercih et.
- [ ] **Performance**: Çok karmaşık conditional type'ların IDE performansını düşürüp düşürmediğini kontrol et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Kodda `any` kullanımı var mı? (Asla olmamalı!). |
| 2 | Opsiyonel alanlar (`?`) null/undefined kontrolleriyle korunuyor mu? |
| 3 | Third-party kütüphanelerin `@types` paketleri eksik mi? |

---

*TypeScript Advanced v1.1 - Enhanced*
