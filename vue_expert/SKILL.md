---
name: vue_expert
router_kit: FullStackKit
description: Vue 3 (Composition API), Pinia, Vue Router ve Vite ekosistemi uzmanlığı.
metadata:
  skillport:
    category: frontend
    tags: [architecture, automation, best practices, cleanup, coaching, coding, collaboration, compliance, debugging, deployment, design patterns, development, documentation, efficiency, frontend, git, maintainability, optimization, performance, pinia, productivity, programming, project management, quality assurance, refactoring, scalability, software engineering, standards, testing, typescript, utilities, version control, vue expert_1, vue.js, vuejs, workflow]      - client-side-react
---

# 🟢 Vue Expert

> Vue 3 + Composition API ile reaktif ve performanslı ön yüz uygulamaları.

---

## 🏗️ Core Patterns

### Composition API (`<script setup>`)
```vue
<script setup>
import { ref, onMounted } from 'vue'

const count = ref(0)
const increment = () => count.value++

onMounted(() => console.log('Mounted!'))
</script>

<template>
  <button @click="increment">{{ count }}</button>
</template>
```

### Pinia (State Management)
```typescript
export const useAuthStore = defineStore('auth', {
  state: () => ({ user: null }),
  actions: {
    async login() { /* ... */ }
  }
})
```

---

## ⚡ Performance Optimization

- **`v-once` & `v-memo`**: Gereksiz update'leri engelleme.
- **`defineAsyncComponent`**: Route bazlı code splitting.
- **`shallowRef`**: Büyük ve derin objelerin reaktivite maliyetini düşürme.

---

## 🔧 Workflow

> **Kaynak:** [Vue.js Official Documentation](https://vuejs.org/guide/introduction.html) & [Pinia Documentation](https://pinia.vuejs.org/)

### Aşama 1: Component Design & Setup
- [ ] **Structure**: `script setup` ve Composition API standartlarına uy. Logic'leri `Composables` klasörüne taşı (Reusability).
- [ ] **Props/Emits**: `defineProps` ve `defineEmits` ile componentler arası iletişimi tip güvenli (TS) olarak tanımla.
- [ ] **Lifecycle**: Hooks (`onMounted`, `onUpdated` vb.) kullanımını minimize et, reaktiviteyi (`watch`, `computed`) tercih et.

### Aşama 2: Routing & State
- [ ] **Router**: Nested routes ve Navigation Guards (Auth kontrolü için) kurulumunu yap.
- [ ] **Pinia**: Global state'i modüler store'lara böl. State'i doğrudan mutasyona uğratmak (Actions dışı) yerine action kullanımını zorunlu tut.
- [ ] **Transitions**: Kullanıcı deneyimi için `<Transition>` ve `<Suspense>` bileşenlerini kullan.

### Aşama 3: Quality & Performance
- [ ] **TypeScript**: Tüm componentleri TS ile sarmala (Volar eklentisi desteği ile).
- [ ] **Testing**: `Vitest` ve `Vue Test Utils` ile component logic'lerini test et.
- [ ] **DevTools**: Vue DevTools ile "Reactivity Tracking" yap ve darboğazları bul.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `ref` vs `reactive` seçimi doğru yapıldı mı? (Primitive vs Object). |
| 2 | Gereksiz `watch` kullanımı (Performance killer) var mı? |
| 3 | `template` içinde çok ağır logic var mı? (Computed'a taşınmalı). |

---

*Vue Expert v1.1 - Enhanced*
