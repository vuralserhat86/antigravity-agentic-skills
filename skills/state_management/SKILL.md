---
name: state_management
router_kit: FullStackKit
description: React/Vue/Nextjs uygulamalarında veri akışı, Context API, Redux ve Zustand.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - data-flow
---

# 🧩 State Management

> Uygulama verisinin (Store) öngörülebilir ve performanslı yönetimi.

---

*State Management v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Redux Style Guide](https://redux.js.org/style-guide/style-guide) & [Zustand Documentation](https://docs.pmnd.rs/zustand/getting-started/introduction)

### Aşama 1: Strategy Selection
- [ ] **Local vs Global**: Veriyi sadece bir bileşen mi kullanıyor (Local) yoksa tüm uygulama mı (Global)?
- [ ] **Library**: İhtiyaca göre `Context API` (Dahili), `Zustand` (Hafif/Hızlı) veya `Redux Toolkit` (Kurumsal/Karmaşık) seç.

### Aşama 2: Architecture & Setup
- [ ] **Stores/Slices**: Veriyi mantıksal parçalara (User, Auth, Products) ayırarak store'ları kur.
- [ ] **Immutability**: State güncellenirken her zaman yeni bir obje dön (Mutasyondan kaçın).
- [ ] **Selectors**: Bileşenlerin sadece ihtiyaç duyduğu veriyi dinlemesini (Re-render optimizasyonu) sağla.

### Aşama 3: Side Effects & Performance
- [ ] **Async Actions**: API çağrılarını ve asenkron işleri (Thunk/Actions) store içinde yönet.
- [ ] **Persistence**: Gerekirse state'in bir kısmını `localStorage` veya `sessionStorage` üzerinde sakla (Hydration).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | "Prop Drilling" (Veriyi 5 kat aşağı taşıma) yaşanıyor mu? |
| 2 | State güncellendiğinde gereksiz bileşenler re-render oluyor mu? |
| 3 | State temizliği (Cleanup) sayfa geçişlerinde yapılıyor mu? |
