---
name: zustand_state
router_kit: FullStackKit
description: Zustand ile modern React state yönetimi - store creation, slices, persistence ve middleware.
metadata:
  skillport:
    category: frontend
    tags: [architecture, automation, best practices, cleanup, coding, collaboration, compliance, debugging, development, documentation, efficiency, frontend, git, maintainability, optimization, performance, productivity, programming, quality assurance, react state, refactoring, scalability, software engineering, standards, state management, testing, typescript, utilities, version control, workflow, zustand, zustand state_1]      - client-side-react
---

# 📦 Zustand State Management

> Küçük, hızlı ve ölçeklenebilir React state yönetimi rehberi.

---

## 🚀 Store Creation

### Basic Store
```typescript
import { create } from 'zustand'

const useStore = create((set) => ({
  count: 0,
  inc: () => set((state) => ({ count: state.count + 1 })),
  reset: () => set({ count: 0 }),
}))

// Usage
const count = useStore((state) => state.count)
const inc = useStore((state) => state.inc)
```

### With TypeScript
```typescript
interface BearState {
  bears: number
  increase: (by: number) => void
}

const useStore = create<BearState>()((set) => ({
  bears: 0,
  increase: (by) => set((state) => ({ bears: state.bears + by })),
}))
```

---

## 🧩 Middleware & Persistence

- **Persist**: State'i localStorage veya sessionStorage'da tutma.
- **Devtools**: Redux DevTools ile entegrasyon.
- **Immer**: Mutable update syntax kullanımı.

---

## 🔧 Workflow

> **Kaynak:** [Zustand v5.0 Official Documentation](https://zustand-demo.pmnd.rs/) & [Next.js Hydration Patterns](https://zustand.docs.pmnd.rs/guides/nextjs)

### Aşama 1: Store Definition & Types
- [ ] **Model Selection**: State ve Action yapılarını içeren TypeScript interface'lerini belirle.
- [ ] **Curry Initialization**: `create<T>()()` syntax'ını kullanarak store'u başlat.
- [ ] **Middleware Selection**: İhtiyaca göre `persist` (localStorage) veya `devtools` katmanlarını ekle.

### Aşama 2: React Integration & Slices
- [ ] **Atomic Slices**: Büyük store'ları `StateCreator` kullanarak atomik dilimlere ayır.
- [ ] **Selector Strategy**: Bileşenlerin sadece kullandığı state dilimine abone olmasını (`useStore(state => state.X)`) sağla.
- [ ] **Shallow Audit**: Birden fazla değer seçerken gereksiz render'ları önlemek için `shallow` kullan.

### Aşama 3: Persistence & Hydration
- [ ] **Hydration Guard**: Next.js projelerinde `_hasHydrated` flag pattern'i ile SSR uyumluluğunu sağla.
- [ ] **Storage Config**: Hassas veriler için `sessionStorage` veya özel şifreli storage konfigürasyonunu yap.
- [ ] **Action Logging**: Hata ayıklama sürecinde aksiyon isimlerini (`counter/increase`) devtools ile izle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `set` metodu içerisinde doğrudan mutasyon yapıldı mı? (İllegal!) |
| 2 | Component içinde selector yerine doğrudan destructuring yapıldı mı? |
| 3 | Persist storage key'i benzersiz mi? |

---

*Zustand State v1.1 - Enhanced*
