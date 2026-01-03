---
name: design_components
router_kit: FullStackKit
description: Tasarımın koda aktarılması, atomik tasarım, variant yapıları ve accessibility (A11y) standartları.
metadata:
  skillport:
    category: design
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, design components, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - design-tokens
---

# 🏗️ Design Components

> Komponent bazlı tasarım ve geliştirme rehberi.

---

## 📐 Atomic Design Hierarchy

1. **Atoms**: Labels, inputs, buttons (en küçük birimler).
2. **Molecules**: Form fields, card headers (atomların birleşimi).
3. **Organisms**: Navigation bars, product grids (kompleks yapılar).
4. **Templates**: Page layouts (iskelet).
5. **Pages**: Final screens (içerik dolu).

---

## 🎨 Component Anatomy

```typescript
interface ButtonProps {
  variant: 'primary' | 'secondary' | 'ghost';
  size: 'sm' | 'md' | 'lg';
  isDisabled?: boolean;
  isLoading?: boolean;
  leftIcon?: React.ReactNode;
}
```

---

## ♿ Accessibility (A11y) Basics

- **Aria Labels**: `aria-label="Kapat"`
- **Roles**: `role="button"`, `role="tabpanel"`
- **keyboard Navigation**: `tabIndex={0}`, `onKeyDown` handlers.
- **Contrast**: Metin ve arka plan kontrastı (min 4.5:1).

---

*Design Components v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Brad Frost - Atomic Design](https://atomicdesign.bradfrost.com/) & [Radix UI Design System](https://www.radix-ui.com/)

### Aşama 1: Component Specs & Tokens
- [ ] **Audit**: Figma dosyasındaki spacing, typography ve color token'larını belirle.
- [ ] **Hierarchy**: Tasarımı Atom, Molecule ve Organism seviyelerine böl.
- [ ] **States**: Hover, Focus, Disabled ve Loading durumlarını tanımla.

### Aşama 2: Implementation & Variants
- [ ] **Base Logic**: Komponentin temel HTML yapısını ve `Props` arayüzünü (TypeScript) oluştur.
- [ ] **Variant Creation**: `Tailwind` veya `CVA` (Class Variance Authority) kullanarak variant yapılarını kur.
- [ ] **Visual Consistency**: Padding ve gap değerlerinin hiyerarşiye uygunluğunu kontrol et.

### Aşama 3: Testing & Documentation
- [ ] **Visual Testing**: Komponentin farklı tarayıcılarda ve viewports'larda görsel bütünlüğünü test et (Storybook).
- [ ] **Unit Testing**: Etkileşimli komponentler (Dropdown, Modal) için logic testleri yaz.
- [ ] **Handoff**: Tasarımın geliştiriciye aktarımı için dokümantasyonu (Design-to-Code) güncelle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Komponent tek bir sorumluluğa (Single Responsibility) sahip mi? |
| 2 | Tüm variant'lar merkezi bir `tokens` dosyasından mı besleniyor? |
| 3 | Screen reader testleri başarılı mı? |

---
*Design Components v1.5 - With Workflow*
