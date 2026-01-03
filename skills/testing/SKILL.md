---
name: testing
router_kit: FullStackKit
description: Kapsamlı test stratejileri ve 2025 test araçları. Unit, integration, e2e ve visual testing.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - quality-assurance
---

# Testing Skill - Kalite Güvence ve Test Stratejileri

> Yazılım kalitesini sağlamak için sistematik test yaklaşımları.
> 2025 modern test araçları ve piramit test stratejisi.

---

# 📋 İçindekiler

1. [Test Piramidi](#1-test-piramidi)
2. [Unit Testing (Jest)](#2-unit-testing-jest)
3. [Integration Testing](#3-integration-testing)
4. [E2E Testing (Playwright)](#4-e2e-testing-playwright)
5. [Visual Regression Testing](#5-visual-regression-testing)
6. [TDD (Test Driven Development)](#6-tdd-test-driven-development)
7. [Test Yazım Kuralları](#7-test-yazım-kuralları)
8. [Kontrol Listesi](#8-kontrol-listesi)
9. [Yapma Listesi](#9-yapma-listesi)
10. [Mutlaka Yap Listesi](#10-mutlaka-yap-listesi)

---

# 1. Test Piramidi

```
      / \
     /E2E\  ← En az (Yavaş, Pahalı, Kırılgan)
    /-----\
   / INTEGR\ ← Orta (Hız ve Güven dengesi)
  /---------\
 /   UNIT    \ ← En çok (Hızlı, Ucuz, İzole)
/-------------\
```

| Tip | Kapsam | Hız | Maliyet |
|-----|--------|-----|---------|
| **Unit** | Fonksiyon/Component | ⚡⚡⚡ | 💸 |
| **Integration** | DB/API/Module arası | ⚡⚡ | 💸💸 |
| **E2E** | Tam kullanıcı akışı | ⚡ | 💸💸💸 |

---

# 2. Unit Testing (Jest)

## 2.1 Temel Test Yapısı

```typescript
import { sum } from './math';

describe('sum function', () => {
  test('adds 1 + 2 to equal 3', () => {
    expect(sum(1, 2)).toBe(3);
  });

  test('handles zero correctly', () => {
    expect(sum(0, 0)).toBe(0);
  });
});
```

## 2.2 Mocking

```typescript
// Service mock'lama
jest.mock('./apiService');
import { fetchData } from './apiService';

test('should use mocked data', async () => {
  (fetchData as jest.Mock).mockResolvedValue({ id: 1, name: 'Test' });
  const data = await getServiceData();
  expect(data.name).toBe('Test');
});
```

---

# 3. Integration Testing

## 3.1 API Integration

```typescript
import request from 'supertest';
import app from './app';

describe('POST /api/users', () => {
  test('should create a new user and return it', async () => {
    const response = await request(app)
      .post('/api/users')
      .send({ email: 'test@example.com', name: 'Test' });

    expect(response.status).toBe(201);
    expect(response.body.email).toBe('test@example.com');
  });
});
```

---

# 4. E2E Testing (Playwright)

## 4.1 Login Akışı

```typescript
import { test, expect } from '@playwright/test';

test('user can login successfully', async ({ page }) => {
  await page.goto('/login');
  await page.fill('input[name="email"]', 'user@example.com');
  await page.fill('input[name="password"]', 'password123');
  await page.click('button[type="submit"]');

  await expect(page).toHaveURL('/dashboard');
  await expect(page.locator('h1')).toContainText('Hoş Geldiniz');
});
```

---

# 5. Visual Regression Testing

```typescript
// Playwright visual test
test('dashboard visual comparison', async ({ page }) => {
  await page.goto('/dashboard');
  await expect(page).toHaveScreenshot('dashboard.png');
});
```

---

# 6. TDD (Test Driven Development)

1. **RED:** Testi yaz ve başarısız olduğunu gör.
2. **GREEN:** Testin geçmesi için gereken minimum kodu yaz.
3. **REFACTOR:** Kodu ve testi temizle, standartlara uygun hale getir.

---

# 7. Test Yazım Kuralları

- **AAA Pattern:** Arrange, Act, Assert.
- **Isolasyon:** Testler birbirinden bağımsız olmalı.
- **Hız:** Unit testler çok hızlı çalışmalı.
- **Readable:** Test ismi neyi test ettiğini açıkça söylemeli.
- **Deterministic:** Aynı girdiyle her zaman aynı sonuç.

---

## 🔄 Workflow

> **Kaynak:** [Spotify's Testing Pyramid](https://engineering.atspotify.com/2018/01/testing-of-microservices/) & [Playwright Best Practices](https://playwright.dev/docs/best-practices)

### Aşama 1: Strategy & Test Plan
- [ ] **Define Coverage Scope**: Kritik kullanıcı akışlarını ve test gerektiren logic'leri belirle.
- [ ] **Choose Level**: Test piramidine göre (Unit -> Integration -> E2E) doğru test seviyesini seç.
- [ ] **Infrastructure Setup**: Vitest/Jest veya Playwright ortamını yapılandır, gerekli mock'ları hazırla.

### Aşama 2: Implementation & Interaction
- [ ] **Unit Tests**: Fonksiyonları ve UI bileşenlerini izole (Stub/Mock kullanarak) test et.
- [ ] **Integration Flows**: Servislerin ve veritabanı/API katmanının uyumunu doğrula.
- [ ] **E2E Scenarios**: Playwright ile gerçek tarayıcı üzerinde "Login -> Checkout" gibi tam akışları simüle et.

### Aşama 3: Verification & CI/CD
- [ ] **Coverage Audit**: Test kapsamını (Line/Branch coverage) analiz et ve boşlukları doldur.
- [ ] **Visual Regressions**: Arayüzdeki beklenmedik değişiklikleri "Snapshot Testing" ile yakala.
- [ ] **Automated Pipeline**: Tüm testlerin CI/CD aşamasında (Check-in'den önce) çalıştığından emin ol.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Testler "Flaky" (bazen geçen bazen kalan) özellikten arındırıldı mı? |
| 2 | Mock veriler gerçek dünya senaryolarını (Edge cases) yansıtıyor mu? |
| 3 | E2E testleri production ortamını birebir simüle ediyor mu? |

---
*Testing v2.5 - With Workflow*
