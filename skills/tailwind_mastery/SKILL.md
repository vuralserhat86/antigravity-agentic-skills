---
name: tailwind_mastery
router_kit: AIKit
description: Tailwind CSS v4, design tokens, responsive patterns ve utility-first CSS best practices.
metadata:
  skillport:
    category: design
    tags: [agents, algorithms, artificial intelligence, automation, chatbots, cognitive services, deep learning, embeddings, frameworks, generative ai, inference, large language models, llm, machine learning, model fine-tuning, natural language processing, neural networks, nlp, openai, prompt engineering, rag, retrieval augmented generation, tailwind mastery, tools, vector databases, workflow automation]      - responsive
---

# 🎨 Tailwind Mastery

> Tailwind CSS v4 ve utility-first CSS best practices rehberi.

---

## 📋 İçindekiler

1. [Tailwind v4 Yenilikleri](#1-tailwind-v4-yenilikleri)
2. [Design System](#2-design-system)
3. [Responsive Patterns](#3-responsive-patterns)
4. [Component Patterns](#4-component-patterns)
5. [Dark Mode](#5-dark-mode)
6. [Performance](#6-performance)

---

## 1. Tailwind v4 Yenilikleri

### CSS-First Configuration
```css
/* app.css */
@import "tailwindcss";

@theme {
  --color-primary: #3b82f6;
  --color-secondary: #10b981;
  --font-display: "Inter", sans-serif;
  --spacing-128: 32rem;
}
```

### Otomatik Content Detection
```css
/* v4'te content config'e gerek yok */
/* Otomatik olarak tüm dosyalar taranır */
```

### Native CSS Features
```css
/* Container Queries */
@container (min-width: 400px) {
  .card { /* styles */ }
}

/* v4 utility */
<div class="@container">
  <div class="@md:flex">...</div>
</div>
```

---

## 2. Design System

### Spacing Scale
```html
<!-- 4px base (0.25rem) -->
<div class="p-1">  <!-- 4px -->
<div class="p-2">  <!-- 8px -->
<div class="p-4">  <!-- 16px -->
<div class="p-8">  <!-- 32px -->
<div class="p-16"> <!-- 64px -->
```

### Typography Scale
```html
<h1 class="text-4xl font-bold"><!-- 36px -->
<h2 class="text-3xl font-semibold"><!-- 30px -->
<h3 class="text-2xl font-medium"><!-- 24px -->
<p class="text-base"><!-- 16px -->
<small class="text-sm"><!-- 14px -->
```

### Color System
```html
<!-- Primary palette -->
<div class="bg-blue-500 hover:bg-blue-600">
<div class="text-blue-700 dark:text-blue-300">

<!-- Semantic colors -->
<div class="bg-success"> <!-- Custom -->
<div class="text-error">
```

### Custom Theme
```css
@theme {
  /* Colors */
  --color-brand-50: #eff6ff;
  --color-brand-500: #3b82f6;
  --color-brand-900: #1e3a8a;
  
  /* Typography */
  --font-sans: "Inter", system-ui, sans-serif;
  --font-mono: "Fira Code", monospace;
  
  /* Shadows */
  --shadow-soft: 0 2px 15px -3px rgb(0 0 0 / 0.1);
}
```

---

## 3. Responsive Patterns

### Breakpoints
```html
<!-- Mobile first -->
<div class="
  w-full          /* base: mobile */
  md:w-1/2        /* 768px+ */
  lg:w-1/3        /* 1024px+ */
  xl:w-1/4        /* 1280px+ */
  2xl:w-1/5       /* 1536px+ */
">
```

### Responsive Grid
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>
```

### Responsive Typography
```html
<h1 class="text-2xl md:text-4xl lg:text-6xl font-bold">
  Responsive Title
</h1>
```

### Hide/Show
```html
<div class="hidden md:block">Desktop only</div>
<div class="md:hidden">Mobile only</div>
```

---

## 4. Component Patterns

### Card
```html
<div class="
  bg-white dark:bg-gray-800
  rounded-2xl
  shadow-lg hover:shadow-xl
  transition-shadow duration-300
  p-6
  border border-gray-100 dark:border-gray-700
">
  <h3 class="text-lg font-semibold">Title</h3>
  <p class="text-gray-600 dark:text-gray-300 mt-2">Content</p>
</div>
```

### Button Variants
```html
<!-- Primary -->
<button class="
  bg-blue-600 hover:bg-blue-700
  text-white font-medium
  px-6 py-3 rounded-lg
  transition-colors
  focus:ring-2 focus:ring-blue-500 focus:ring-offset-2
">
  Primary
</button>

<!-- Secondary -->
<button class="
  bg-gray-100 hover:bg-gray-200
  text-gray-900 font-medium
  px-6 py-3 rounded-lg
  transition-colors
">
  Secondary
</button>

<!-- Outline -->
<button class="
  border-2 border-blue-600
  text-blue-600 hover:bg-blue-50
  font-medium px-6 py-3 rounded-lg
  transition-colors
">
  Outline
</button>
```

### Input
```html
<input class="
  w-full px-4 py-3
  border border-gray-300 rounded-lg
  focus:ring-2 focus:ring-blue-500 focus:border-blue-500
  outline-none transition
  placeholder:text-gray-400
" placeholder="Enter text...">
```

### Flex Patterns
```html
<!-- Center -->
<div class="flex items-center justify-center min-h-screen">

<!-- Space between -->
<div class="flex items-center justify-between">

<!-- Stack (vertical) -->
<div class="flex flex-col gap-4">
```

---

## 5. Dark Mode

### Class Strategy
```html
<!-- html'e class ekle -->
<html class="dark">

<!-- Component -->
<div class="bg-white dark:bg-gray-900 text-gray-900 dark:text-white">
```

### System Preference
```javascript
// tailwind.config.js (v3) veya @media (v4)
if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
  document.documentElement.classList.add('dark');
}
```

### Toggle Implementation
```javascript
function toggleDarkMode() {
  document.documentElement.classList.toggle('dark');
  localStorage.theme = document.documentElement.classList.contains('dark') 
    ? 'dark' : 'light';
}
```

---

## 6. Performance

### Purge Optimization
```css
/* v4: Otomatik - sadece kullanılan class'lar bundle'a dahil */
```

### Avoid Dynamic Classes
```html
<!-- ❌ YANLIŞ: Dinamik class purge edilebilir -->
<div class={`text-${color}-500`}>

<!-- ✅ DOĞRU: Tam class adı -->
<div class={color === 'red' ? 'text-red-500' : 'text-blue-500'}>
```

### Safelist (Gerekirse)
```javascript
// tailwind.config.js
module.exports = {
  safelist: [
    'bg-red-500',
    'bg-green-500',
    { pattern: /^bg-(red|green|blue)-/ },
  ],
};
```

### Production Build
```bash
# Minified CSS
NODE_ENV=production npx tailwindcss -i input.css -o output.css --minify
```

---

## 🎯 Quick Reference

### Spacing: `p-{n}`, `m-{n}`, `gap-{n}`
### Sizing: `w-{n}`, `h-{n}`, `size-{n}`
### Flex: `flex`, `items-center`, `justify-between`
### Grid: `grid`, `grid-cols-{n}`, `gap-{n}`
### Text: `text-{size}`, `font-{weight}`, `text-{color}`
### Border: `border`, `border-{n}`, `rounded-{size}`
### Shadow: `shadow`, `shadow-{size}`
### Transition: `transition`, `duration-{ms}`, `ease-{type}`

---

*Tailwind Mastery v1.0 - Tailwind CSS v4 Best Practices*
