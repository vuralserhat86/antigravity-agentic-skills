---
name: tailwind_mastery
router_kit: FullStackKit
description: Tailwind CSS ileri seviye kullanım, JIT engine, custom theme ve mimari pratikler.
metadata:
  skillport:
    category: frontend
    tags: [architecture, automation, best practices, cleanup, coaching, coding, collaboration, compliance, css, design, design patterns, development, documentation, efficiency, frontend, git, maintainability, optimization, performance, productivity, programming, quality assurance, scalability, software engineering, standards, tailwind css, tailwind mastery_1, tailwindcss, testing, ui/ux, utilities, version control, web development, workflow]      - utility-first-css
---

# 🎨 Tailwind Mastery

> Utility-first CSS ile hızlı, tutarlı ve modern UI geliştirme rehberi.

---

## 🏗️ Core Concepts

### 1. Utility-First
Sınırsız CSS dosyası yazmak yerine, önceden tanımlı class'ları (`flex`, `pt-4`, `text-blue-500`) birleştirerek tasarım oluşturma.

### 2. Design Tokens
Renk, spacing ve yazı tiplerini merkezi `tailwind.config.js` üzerinden yönetme.
```javascript
theme: {
  extend: {
    colors: {
      'brand': '#5c6ac4',
    }
  }
}
```

### 3. JIT (Just-In-Time)
Sadece kullanılan class'ları compile ederek devasa CSS dosyalarından kurtulma. `top-[117px]` gibi arbitrary value desteği.

---

## 🛠️ Advanced Patterns

### Conditional Classes (clsx / tailwind-merge)
```javascript
import { clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

const buttonClasses = twMerge(clsx(
  'p-4 bg-blue-500',
  isActive && 'bg-green-500',
  className
));
```

---

## 🔧 Workflow

> **Kaynak:** [Tailwind CSS Documentation](https://tailwindcss.com/docs) & [Refactoring UI (Adam Wathan)](https://refactoringui.com/)

### Aşama 1: Foundation & Theme Setup
- [ ] **Config**: `tailwind.config.ts` içinde markaya özel renk paletini, fontları ve breakpointleri tanımla.
- [ ] **Plugins**: `@tailwindcss/typography` ve `@tailwindcss/forms` gibi resmi eklentileri ihtiyaca göre kur.
- [ ] **Directives**: `globals.css` içinde `@tailwind base`, `@tailwind components`, `@tailwind utilities` komutlarını ekle.

### Aşama 2: Component Patterns
- [ ] **Abstraction**: Çok sık tekrarlanan yapılar (örn: Primary Button) için `@apply` yerine modern Framework component'lerini (React/Vue/etc.) tercih et.
- [ ] **Variants**: `hover:`, `focus:`, `dark:` ve `active:` gibi state varyantlarını sistematik uygula.
- [ ] **Arbitrary Values**: Özel değer gerektiren yerlerde (`h-[calc(100vh-80px)]`) köşeli parantez syntax'ını kullan.

### Aşama 3: Optimization & Audit
- [ ] **Merging**: `tailwind-merge` kullanarak çakışan class'ların (örn: `p-2` vs `p-4`) düzgün ezilmesini sağla.
- [ ] **IntelliSense**: VS Code Tailwind CSS IntelliSense eklentisiyle class isimlerini ve renk önizlemelerini doğrula.
- [ ] **Purging**: Production build'da kullanılmayan CSS'in tamamen atıldığını döküman boyutundan (max 50-100kb) teyit et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Kod içinde "arbitrary values" (`[...]`) aşırıya kaçtı mı? (Config'e taşınmalı). |
| 2 | Component'ler içinde class karmaşası (Class soup) okunabilirliği bozuyor mu? |
| 3 | Responsive prefix'leri (`md:`, `lg:`) hiyerarşik olarak doğru mu? |

---

*Tailwind Mastery v1.1 - Enhanced*
