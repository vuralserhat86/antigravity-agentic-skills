---
name: design_components
router_kit: FullStackKit
description: Reusable UI bileşen tasarımı, Radix UI, Headless UI ve Shadcn/ui kullanımı. ⚠️ UI kodlarken kullan. Stil sistemleri için → tailwind-mastery veya vanilla-css.
metadata:
  skillport:
    category: design
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, design components, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - ui-kit
---

# 🧩 Design Components

> Yeniden kullanılabilir ve erişilebilir UI bileşenleri geliştirme.

---

*Design Components v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Component-Driven Development](https://www.componentdriven.org/)

### Aşama 1: Decomposition (Parçalarına Ayır)
- [ ] **Atoms**: En küçük yapıları (Button, Input, Text) belirle.
- [ ] **Molecules**: Atomlardan oluşan grupları (SearchBox, Card) oluştur.

### Aşama 2: Headless & Accessibility
- [ ] **Primitives**: `Radix UI` veya `Headless UI` gibi erişilebilir temel kütüphaneleri seç.
- [ ] **Shadcn/UI**: Modern ve özelleştirilebilir bileşen şablonlarını entegre et.

### Aşama 3: Prop Design & Composition
- [ ] **Props**: Bileşenin esnekliği için doğru interface/type tanımlarını yap.
- [ ] **Composition**: "Compound Component" pattern'ı ile karmaşık UI'ları yönet.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Bileşen bağımsız olarak çalışabiliyor mu (Isolated)? |
| 2 | Klavye navigasyonu ve Ekran Okuyucu uyumlu mu? |
| 3 | Stil yönetimi (Tailwind vb.) tutarlı mı? |
