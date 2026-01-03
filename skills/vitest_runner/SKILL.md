---
name: vitest_runner
router_kit: QualityKit
description: Vitest ile hızlı unit ve component testleri, mocking ve coverage.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, vitest runner, workflow]      - test-speed
---

# ⚡ Vitest Runner

> Vite ekosistemi için optimize edilmiş, ultra hızlı test koşucu.

---

*Vitest Runner v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Vitest Documentation](https://vitest.dev/guide/) & [Testing Library - React with Vitest](https://testing-library.com/docs/react-testing-library/setup#vitest)

### Aşama 1: Environment & Setup
- [ ] **Config**: `vitest.config.ts` (veya `vite.config.ts`) içinde test ortamını (jsdom/node) ve coverage ayarlarını yapılandır.
- [ ] **Globals**: Dashboardsız kullanım için `globals: true` ayarını kontrol et (Örn: `describe`, `it`, `expect` otomatik gelsin).

### Aşama 2: Writing & Mocking
- [ ] **TestSuite**: `describe` ve `it/test` bloklarıyla senaryoları yapılandır.
- [ ] **Mocking**: `vi.mock()` ile dış bağımlılıkları ve `vi.fn()` ile fonksiyon casuslarını (Spies) oluştur.
- [ ] **Async Testing**: `await` ve `waitFor` kullanarak asenkron durumları test et.

### Aşama 3: Analysis & Optimization
- [ ] **Coverage**: `vitest run --coverage` ile kod kapsamını (v8 veya istanbul) raporla.
- [ ] **UI Mode**: Testleri görsel olarak takip etmek için `vitest --ui` kullan.
- [ ] **Performance**: `parallel` ve `threads` ayarlarıyla test çalıştırma süresini optimize et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Testler "Clean Up" (Örn: `afterEach(cleanup)`) yapıyor mu? |
| 2 | "Snapshots"lar güncel ve anlamlı mı? |
| 3 | Hangi modda (jsdom vs node) çalışıldığı doğru mu? |
