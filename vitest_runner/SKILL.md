---
name: vitest_runner
router_kit: FullStackKit
description: Vitest ile hızlı unit test, mocking, coverage ve Vite entegrasyonu.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, cleanup, coding, collaboration, compliance, debugging, development, documentation, efficiency, git, maintainability, optimization, performance, productivity, programming, quality assurance, software engineering, standards, testing, unit testing, utilities, version control, vitest, vitest runner_1, vite, workflow]      - testing-tools
---

# ⚡ Vitest Runner

> Vite tabanlı projeler için ultra hızlı ve modern test koşucu rehberi.

---

## 🚀 Setup & Config

### Kurulum
```bash
npm install -D vitest
```

### vitest.config.ts
```typescript
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    globals: true,
    environment: 'happy-dom', // UI testleri için
  },
})
```

---

## 🛠️ Key Features

### 1. In-Source Testing
Kodu ve testi aynı dosyada tutma (Küçük utility'ler için).
```typescript
export const add = (a: number, b: number) => a + b

if (import.meta.vitest) {
  const { it, expect } = import.meta.vitest
  it('adds two numbers', () => {
    expect(add(1, 2)).toBe(3)
  })
}
```

### 2. Fast Mocking (vi)
```typescript
const spy = vi.fn()
vi.mock('./module', () => ({
  getData: () => 'mocked'
}))
```

---

## 🔧 Workflow

> **Kaynak:** [Vitest Documentation](https://vitest.dev/guide/) & [Vite Guide](https://vitejs.dev/)

### Aşama 1: Environment & Config
- [ ] **Setup**: `vitest` paketini kur ve `npm test` script'ini ekle.
- [ ] **Environment**: Proje tipine göre `node`, `jsdom` veya `happy-dom` seçimini yap.
- [ ] **Globals**: `globals: true` ile her dosyada `import { describe... }` zorunluluğunu kaldır (Opsiyonel).

### Aşama 2: Unit & Component Testing
- [ ] **Writing**: `describe/it` hiyerarşisiyle testleri yaz. Edge case'leri (`null`, `empty`, `throws`) unutma.
- [ ] **Mocking**: `vi.mock` veya `vi.spyOn` kullanarak harici bağımlılıkları (API, DB) izole et.
- [ ] **Watch Mode**: Geliştirme sırasında `vitest` watch mode'un (Hızlı HMR) avantajını kullan.

### Aşama 3: Coverage & Benchmarking
- [ ] **Coverage**: `c8` veya `istanbul` kullanarak coverage raporlarını üret (`vitest run --coverage`).
- [ ] **UI Mode**: Gelişmiş dökümantasyon ve görsel analiz için `vitest --ui` modunu kullan.
- [ ] **CI Integration**: GitHub Actions veya benzeri platformlarda testlerin otomatik çalışmasını sağla.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Test dosyaları `__tests__` veya `.test.ts` formatında mı? |
| 2 | Mock'lanan modüller her testten sonra `vi.clearAllMocks()` ile sıfırlanıyor mu? |
| 3 | Coverage %80 üzerinde mi? |

---

*Vitest Runner v1.1 - Enhanced*
