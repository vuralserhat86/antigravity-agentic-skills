---
name: webapp_testing
router_kit: FullStackKit
description: Modern web uygulamaları için kapsamlı test stratejileri, Cypress/Playwright ve RTL.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, cleanup, coding, collaboration, compliance, cypres, debugging, development, documentation, e2e testing, efficiency, frontend, git, maintainability, optimization, performance, playwright, productivity, programming, quality assurance, react testing library, software engineering, standards, testing, unit testing, utilities, version control, webapp testing_1, workflow]      - quality-assurance
---

# 🧪 WebApp Testing

> Web uygulamaları için modern test metodolojileri ve stabilite rehberi.

---

## 🏁 Test Türleri

| Tür | Odak | Araç |
|-----|------|------|
| **Unit** | Mantık (Logic) | Vitest, Jest |
| **Component** | UI & State | React Testing Library |
| **Integration** | Sayfalar arası akış | Playwright, Cypress |
| **Visual** | CSS & Layout | Chromatic, Percy |
| **Accessibility (a11y)** | Erişilebilirlik | Axe-core |

---

## 🛠️ Best Practices (RTL)

```javascript
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('submits form with user data', async () => {
  render(<MyForm />);
  
  // Neden: Kullanıcı gözüyle bulmak (Role/Label)
  await userEvent.type(screen.getByLabelText(/name/i), 'John');
  await userEvent.click(screen.getByRole('button', { name: /submit/i }));
  
  expect(await screen.findByText(/success/i)).toBeInTheDocument();
});
```

---

## 🔧 Workflow

> **Kaynak:** [Testing Library Guiding Principles](https://testing-library.com/docs/guiding-principles/) & [Modern Web Testing (Playwright)](https://playwright.dev/docs/intro)

### Aşama 1: Strategy & Environment
- [ ] **Audit Goals**: Hangi kullanıcı akışlarının (Critical paths) test edileceğini belirle.
- [ ] **Tooling**: Proje tipine göre (Next.js, Vite vb.) test ortamını (Vitest/Playwright) kur.
- [ ] **Mocking Strategy**: Harici API'lar için `MSW` (Mock Service Worker) kurulumunu yap.

### Aşama 2: Testing Layers
- [ ] **Component Tests**: Bileşenlerin props ve state değişimlerine verdiği tepkileri "Behavioral" olarak test et.
- [ ] **E2E Tests**: Playwright ile birden fazla tarayıcıda (Chromium, Firefox) tam akışları (Transaction flow vb.) koştur.
- [ ] **Accessibility**: Otomatik a11y testleriyle (Axe) temel erişilebilirlik hatalarını temizle.

### Aşama 3: Automation & CI
- [ ] **Parallelization**: Testleri paralel çalıştırarak CI süresini minimize et.
- [ ] **Flakiness Check**: Rastgele kalan (Flaky) testleri tespit et ve deterministik hale getir.
- [ ] **Reporting**: Hata anında kanıt (Screenshot, Video, Trace) üretilmesini sağla.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Testler implementasyon detaylarını mı (setState vb.) yoksa kullanıcı davranışını mı test ediyor? |
| 2 | API request'leri mock'landı mı? |
| 3 | Test coverage önemli alanlarda %80'in üzerinde mi? |

---

*WebApp Testing v1.1 - Enhanced*
