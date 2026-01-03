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

## 📋 Ne Zaman Kullanılır?

| Kullan | Kullanma |
|--------|----------|
| Multi-component UI | Basit HTML |
| State management | Static content |
| Routing gerekli | Tek sayfa |
| shadcn components | Vanilla CSS |

---

## 🔧 Temel Yapı

```tsx
import React, { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Card } from '@/components/ui/card';

export default function App() {
  const [count, setCount] = useState(0);
  
  return (
    <Card className="p-6">
      <h1 className="text-2xl font-bold">Counter: {count}</h1>
      <Button onClick={() => setCount(c => c + 1)}>
        Increment
      </Button>
    </Card>
  );
}
```

---

## 🎯 shadcn/ui Components

### Sık Kullanılanlar
```tsx
// Button
<Button variant="default|destructive|outline|secondary|ghost|link">
  Click me
</Button>

// Card
<Card>
  <CardHeader>
    <CardTitle>Title</CardTitle>
    <CardDescription>Description</CardDescription>
  </CardHeader>
  <CardContent>Content</CardContent>
  <CardFooter>Footer</CardFooter>
</Card>

// Input
<Input placeholder="Enter text..." />

// Dialog
<Dialog>
  <DialogTrigger>Open</DialogTrigger>
  <DialogContent>
    <DialogHeader>
      <DialogTitle>Title</DialogTitle>
    </DialogHeader>
  </DialogContent>
</Dialog>
```

---

## 🎨 Tailwind Patterns

### Layout
```tsx
// Centered
<div className="flex items-center justify-center min-h-screen">

// Grid
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">

// Stack
<div className="flex flex-col gap-4">
```

### Responsive
```tsx
<div className="
  text-sm md:text-base lg:text-lg
  p-4 md:p-6 lg:p-8
  w-full md:w-1/2 lg:w-1/3
">
```

---

## ⚡ State Patterns

```tsx
// Local state
const [data, setData] = useState([]);

// Form state
const [form, setForm] = useState({
  name: '',
  email: ''
});

// Controlled input
<Input 
  value={form.name}
  onChange={e => setForm({...form, name: e.target.value})}
/>
```

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

---
*Web Artifacts Builder v1.5 - With Workflow*
