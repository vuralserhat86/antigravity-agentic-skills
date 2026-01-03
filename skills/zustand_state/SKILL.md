---
name: zustand_state
router_kit: FullStackKit
description: React uygulamalarında Zustand ile minimalist ve performanslı state yönetimi.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development, zustand state]      - lightweight-state
---

# 🐻 Zustand State

> Hızlı, minimalist ve öngörülebilir state yönetimi.

---

*Zustand State v2.0 - With Workflow*

## 🔄 Workflow

> **Kaynak:** [Zustand v5.0 Official Documentation](https://zustand-demo.pmnd.rs/) & [Next.js Hydration Patterns](https://zustand.docs.pmnd.rs/guides/nextjs)

### Aşama 1: Store Definition & Types
- [ ] **Model Selection**: State ve Action yapılarını içeren TypeScript interface'lerini belirle.
- [ ] **Curry Initialization**: `create<T>()()` (double parentheses) syntax'ını kullanarak store'u başlat.
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
| 2 | Component içinde selector yerine doğrudan destructuring yapıldı mı? (Performans riski!) |
| 3 | Persist storage key'i benzersiz (Unique) mi? |
