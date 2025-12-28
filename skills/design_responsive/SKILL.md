---
name: design_responsive
router_kit: FullStackKit
description: Breakpoints, fluid typography, container queries ve modern CSS features.
metadata:
  skillport:
    category: design
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, design responsive, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - design-components
---

# 📱 Design Responsive

> Responsive tasarım ve modern CSS özellikleri.

---

## 📐 1. Breakpoints

### Standard
```
Mobile:       0 - 639px
Tablet SM:    640 - 767px
Tablet:       768 - 1023px
Desktop:      1024 - 1439px
Wide:         1440px+
```

### Tailwind Mapping
```
sm:  640px
md:  768px
lg:  1024px
xl:  1280px
2xl: 1536px
```

---

## 🔤 2. Fluid Typography

```css
:root {
  --fluid-sm: clamp(0.875rem, 0.8rem + 0.35vw, 1rem);
  --fluid-base: clamp(1rem, 0.9rem + 0.5vw, 1.125rem);
  --fluid-lg: clamp(1.25rem, 1rem + 1vw, 1.5rem);
  --fluid-xl: clamp(1.5rem, 1.2rem + 1.5vw, 2rem);
  --fluid-2xl: clamp(2rem, 1.5rem + 2.5vw, 3rem);
}
```

---

## 📦 3. Container System

| Device | Max-Width | Padding |
|--------|-----------|---------|
| Mobile | 100% | 16px |
| Tablet | 768px | 24px |
| Desktop | 1200px | 32px |
| Wide | 1440px | 48px |

---

## 🎯 4. Container Queries

```css
.card-container {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card-content {
    display: grid;
    grid-template-columns: 1fr 2fr;
  }
}
```

---

## ⚙️ 5. User Preferences

```css
/* Dark mode */
@media (prefers-color-scheme: dark) { }

/* Reduced motion */
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; }
}

/* High contrast */
@media (prefers-contrast: high) { }
```

---

## 📋 6. Grid Columns

| Device | Columns | Gutter |
|--------|---------|--------|
| Mobile | 4 | 16px |
| Tablet | 8 | 16px |
| Desktop | 12 | 24px |

---

## 🔗 İlgili Skill'ler
- `design-tokens` - Base values
- `design-patterns` - Hierarchy, animations

---

*Design Responsive v1.0*
