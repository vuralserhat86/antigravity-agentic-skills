---
name: vue_expert
router_kit: FullStackKit
description: Vue 3 Composition API, Pinia, Nuxt 3 ve Vite optimizasyonu.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, vue expert, web development]      - vue-mastery
---

# 🟢 Vue Expert

> Reactive, performanslı ve ölçeklenebilir Vue.js uygulamaları geliştirme.

---

*Vue Expert v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Vue 3 Documentation (Composition API)](https://vuejs.org/guide/extras/composition-api-faq.html) & [Vue 3.5 New Features](https://blog.vuejs.org/posts/vue-3-5)

### Aşama 1: Logical Modeling & State
- [ ] **Ref vs Reactive**: Nesne hiyerarşisine göre `ref` veya `reactive` seçimini yap (3.5+ destructuring dostu ref kullanımı).
- [ ] **Composable Design**: Tekrar eden mantığı (Logic) `useX` formatında composable'lara taşı.
- [ ] **Store Architecture**: Global state gereksinimleri için Pinia store yapılarını (`defineStore`) kur.

### Aşama 2: Component Architecture
- [ ] **Script Setup**: `<script setup lang="ts">` kullanarak en optimize ve kısa syntax'ı uygula.
- [ ] **Prop/Emit Definition**: `defineProps` ve `defineEmits` ile tip güvenliğini (TypeScript) en üst seviyede tut.
- [ ] **Efficient Watchers**: Yan etkileri (Side effects) yönetmek için `watch` veya `watchEffect` kullan, temizlik işlemlerini (onUnmounted) unutma.

### Aşama 3: Performance & Tooling
- [ ] **Scoped Styling**: CSS çakışmalarını önlemek için `<style scoped>` kullan veya Tailwind entegrasyonu yap.
- [ ] **SSR Alignment**: Nuxt 3 projelerinde `OnMounted` dışındaki DOM erişimlerinden kaçın.
- [ ] **Reactivity Audit**: Gereksiz re-render'ları önlemek için `computed` kullanımını maksimize et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `shallowRef` veya `markRaw` ile performans optimizasyonu yapıldı mı? |
| 2 | Component interface'leri (Props/Slots) dökümante edildi mi? |
| 3 | Reactivity Proxy sınırları gözetildi mi? (Doğrudan destructuring kontrolü) |
