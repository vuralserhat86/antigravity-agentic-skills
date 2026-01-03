---
name: state_management
router_kit: FullStackKit
description: React state yönetimi stratejileri - Local state, Context API, Redux Toolkit ve Zustand.
metadata:
  skillport:
    category: frontend
    tags: [architecture, automation, best practices, cleanup, coding, collaboration, compliance, context api, debugging, development, documentation, efficiency, frontend, git, maintainability, optimization, performance, productivity, programming, quality assurance, react state, redux, refactoring, scalability, software engineering, standards, state management, state management_1, testing, typescript, utilities, version control, workflow, zustand]      - client-side-react
---

# 📦 State Management

> Veri akışını yönetme, tutarlılık sağlama ve performanslı state stratejileri.

---

## 📐 State Hiyerarşisi

### 1. Local State (`useState`)
Gereksiz render'ları önlemek için state'i her zaman "en yakın" (Leaf) component'te tut.

### 2. Lifted State
Aynı veriye ihtiyaç duyan kardeş component'’ler varsa, state'i ortak parent'a taşı.

### 3. Global State
Uygulamanın geneli (Auth, Theme, Cart) için merkezi bir store kullan.
- **Tavsiye**: Zustand (Basitlik için) veya Redux Toolkit (Karmaşıklık için).

---

## 🛠️ Zustand Example

```typescript
import { create } from 'zustand'

const useCartStore = create((set) => ({
  count: 0,
  inc: () => set((state) => ({ count: state.count + 1 })),
  dec: () => set((state) => ({ count: state.count - 1 })),
}))
```

---

## 🔧 Workflow

> **Kaynak:** [React State Management (Official)](https://react.dev/learn/managing-state) & [Zustand Documentation](https://docs.pmnd.rs/zustand/getting-started/introduction)

### Aşama 1: Tool Selection & Data Audit
- [ ] **State Triage**: Verinin kapsamını belirle: Local (Component), Remote (Server/Cache) mi yoksa Global (App) mi?
- [ ] **Tooling**: Sunucu verisi için `React Query`, basit global state için `Zustand`, karmaşık logic için `Redux Toolkit` seç.
- [ ] **Schema Definition**: State objesinin şemasını ve TypeScript arayüzlerini (`Interfaces`) tanımla.

### Aşama 2: Implementation & Selectors
- [ ] **Store Setup**: Store'u modüler parçalara (Slices) bölerek yönetilebilirliği artır.
- [ ] **Selectors**: State içinden sadece gerekli parçayı (`useStore(state => state.count)`) çekerek gereksiz render'ları önle.
- [ ] **Persistence**: Gerekiyorsa state'i `localStorage` (Zustand persist) ile kalıcı hale getir.

### Aşama 3: Performance & Debugging
- [ ] **DevTools**: Redux veya Zustand DevTools kullanarak action'ları ve state değişimlerini izle.
- [ ] **Memory Audit**: Store içinde devasa veriler (örn: tüm log listesi) tutmaktan kaçın, sadece görünür veriyi tut.
- [ ] **Edge Cases**: State sıfırlama (Logout case), race conditions ve error state'leri test et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Sunucu verisi (Server State) global store içinde mi? (Olmamalı, React Query kullan). |
| 2 | Component'ler sadece ihtiyacı olan state parçasına mı abone? |
| 3 | State güncellemeleri "Immutable" (değişmez) kurallarına uyuyor mu? |

---

*State Management v1.1 - Enhanced*
