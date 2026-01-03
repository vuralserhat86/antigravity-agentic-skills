---
name: playwright_testing
router_kit: FullStackKit
description: Playwright ile modern E2E testleri, UI otomasyonu ve görsel regresyon testleri.
metadata:
  skillport:
    category: testing
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, playwright testing, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - e2e-testing
---

# 🎭 Playwright Testing

> Hızlı, güvenilir ve modern tarayıcı otomasyonu ve E2E testleri.

---

*Playwright Testing v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Playwright Best Practices](https://playwright.dev/docs/best-practices) & [Checkly Guide](https://www.checklyhq.com/learn/playwright/)

### Aşama 1: Setup & Architecture
- [ ] **VS Code Extension**: Testleri doğrudan IDE'den çalıştır ve debug et (`Show Trace` özelliği).
- [ ] **Fixtures**: Ortak setup (Login, Data seed) işlemleri için `test.beforeEach` yerine Custom Fixtures kullan.
- [ ] **Auth**: `storageState` kullanarak login işlemini sadece bir kez yap ve durumu paylaş.

### Aşama 2: Writing Resilient Tests
- [ ] **Locators**: `page.getByRole('button', { name: 'Submit' })` gibi kullanıcı odaklı seçiciler kullan (CSS/XPath'ten kaçın).
- [ ] **Assertions**: Web-first assertions kullan (`await expect(locator).toBeVisible()`). Asla manuel `wait` koyma.
- [ ] **Network**: API çağrılarını mock'lamak veya spy yapmak için `page.route` kullan (Hız ve izolasyon için).

### Aşama 3: Debugging & CI
- [ ] **UI Mode**: `--ui` bayrağı ile testleri çalıştır, timeline üzerinde DOM snapshotlarını incele.
- [ ] **Trace Viewer**: CI'da patlayan testler için `trace: 'on-first-retry'` ayarını aç.
- [ ] **Sharding**: Testleri CI üzerinde paralel çalıştırmak için shard özelliğini kullan.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Testler birbirinden izole mi? (Biri diğerinin verisini bozmuyor mu?) |
| 2 | Hard-coded `waitForTimeout(5000)` var mı? (Varsa hemen sil). |
| 3 | Görsel regresyon testleri (Snapshot) farklı OS'lerde tutarlı mı? (Docker kullan). |
