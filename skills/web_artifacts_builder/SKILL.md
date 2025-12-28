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

---

*Web Artifacts Builder v1.0*
