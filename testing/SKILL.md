---
name: testing
router_kit: FullStackKit
description: Kapsamlı test stratejileri ve modern test araçları. Unit, integration, e2e ve visual testing.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - quality-assurance
---

# 🧪 Testing & Quality Assurance

> Yazılım kalitesini sağlamak için sistematik test yaklaşımları ve modern otomaston araçları.

---

## 🏗️ Test Piramidi (Standartlar)

- **Unit Tests**: En taban ve en çok olan. Fonksiyonel birimler. (Jest, Vitest).
- **Integration Tests**: Servisler arası etkileşim. (Supertest, MSW).
- **E2E Tests**: Tam kullanıcı akışı. (Playwright, Cypress).

---

## 🛠️ Modern Tooling (2025)

| Kategori | Araçlar |
|----------|---------|
| **Unit/Logic** | Vitest, Jest |
| **Component/UI** | React Testing Library |
| **E2E / Visual** | Playwright, Chromatic |
| **API Mocking** | Mock Service Worker (MSW) |

---

## 🧪 Snippets

### Unit Test (Vitest)
```typescript
it('should calculate discount correctly', () => {
  expect(calculateDiscount(100, 20)).toBe(80);
});
```

### E2E Test (Playwright)
```javascript
test('user logs in', async ({ page }) => {
  await page.goto('/login');
  await page.fill('#user', 'admin');
  await page.click('button');
  await expect(page).toHaveURL('/dashboard');
});
```

---

## 🔧 Workflow

> **Kaynak:** [Spotify's Testing Pyramid](https://engineering.atspotify.com/2018/01/testing-of-microservices/) & [Playwright Best Practices](https://playwright.dev/docs/best-practices)

### Aşama 1: Strategy & Test Plan
- [ ] **Define Coverage**: Kritik kullanıcı akışlarını ve test gerektiren logic'leri belirle.
- [ ] **Choose Level**: Test piramidine göre (Unit -> Integration -> E2E) doğru test seviyesini seç.
- [ ] **Env Setup**: Vitest veya Playwright ortamını yapılandır, gerekli mock'ları hazırla.

### Aşama 2: Implementation & Interaction
- [ ] **Unit Tests**: Fonksiyonları ve UI bileşenlerini izole (Stub/Mock kullanarak) test et.
- [ ] **Integration Flows**: Servislerin ve veritabanı/API katmanının uyumunu doğrula.
- [ ] **E2E Scenarios**: Playwright ile gerçek tarayıcı üzerinde "Login -> Checkout" gibi tam akışları simüle et.

### Aşama 3: Verification & CI/CD
- [ ] **Coverage Audit**: Test kapsamını (Line/Branch coverage) analiz et ve boşlukları doldur.
- [ ] **Visual Regressions**: Arayüzdeki beklenmedik değişiklikleri "Snapshot Testing" ile yakala.
- [ ] **Automated Pipeline**: Tüm testlerin CI/CD aşamasında çalıştığından emin ol.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Testler "Flaky" (bazen geçen bazen kalan) özellikten arındırıldı mı? |
| 2 | Mock veriler gerçek dünya senaryolarını yansıtıyor mu? |
| 3 | E2E testleri production ortamını simüle ediyor mu? |

---

*Testing v1.1 - Enhanced*
