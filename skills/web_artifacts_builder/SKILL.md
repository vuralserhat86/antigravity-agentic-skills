---
name: web_artifacts_builder
router_kit: FullStackKit
description: React, Tailwind, shadcn/ui ile karmaşık web artifacts oluşturma rehberi.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web artifacts builder, web development]      - artifacts
---

# 🎨 Web Artifacts Builder

> React/Tailwind/shadcn ile karmaşık UI artifacts rehberi.

---

*Web Artifacts Builder v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [shadcn/ui Documentation](https://ui.shadcn.com/docs) & [Modern React Development Patterns (2025)](https://react.dev/learn)

### Aşama 1: Component Definition & Setup
- [ ] **Primitive Selection**: shadcn/ui kütüphanesinden gerekli temel bileşenleri (`npx shadcn-ui@latest add ...`) projeye dahil et.
- [ ] **Type Mapping**: Props ve state yapılarını TypeScript interface'leri ile tanımlayarak tip güvenliğini sağla.
- [ ] **Atomic Composition**: Büyük UI yapılarını daha küçük, yönetilebilir alt bileşenlere (Sub-components) ayır.

### Aşama 2: Styling & Interactions
- [ ] **Tailwind Orchestration**: Responsive tasarım ve etkileşim (Hover, Active) durumlarını Tailwind class'ları ile kurgula.
- [ ] **State Flow**: Karmaşık etkileşimler için `useState` veya `useReducer` ile veri akışını yönet.
- [ ] **Accessibility (A11y)**: Bileşenlerin klavye navigasyonu ve ekran okuyucu uyumluluğunu (ARIA tags) kontrol et.

### Aşama 3: Polish & Export
- [ ] **Animation & Motion**: Kullanıcı deneyimini artırmak için `framer-motion` veya CSS transitions ekle.
- [ ] **Light/Dark Sync**: Renklerin her iki modda da doğru kontrast oranına sahip olduğunu doğrula.
- [ ] **Performance Audit**: Gereksiz re-render'ları saptamak için bileşenleri profilleyerek optimize et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Bileşenler mobil cihazlarda doğru render ediliyor mu? |
| 2 | shadcn bileşenleri projenin tasarım diline (Theme) uygun mu? |
| 3 | State güncellemeleri sırasında yan etkiler (Side effects) doğru yönetiliyor mu? |
