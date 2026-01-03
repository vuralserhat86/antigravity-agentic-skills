---
name: tdd_workflow
router_kit: DevOpsKit
description: Test Driven Development (TDD) döngüsü - Red, Green, Refactor ve test-first yaklaşımı.
metadata:
  skillport:
    category: engineering
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, functional testing, git, maintainability, optimization, productivity, programming, quality assurance, refactoring, regression testing, software engineering, standards, tdd, tdd workflow_1, testing, unit testing, utilities, version control, workflow]      - software-quality
---

# 🧪 TDD Workflow

> Önce testi yaz, sonra kodu geliştir. Yazılım kalitesini "İnşa sırasında" garanti altına al.

---

## 🔄 TDD Döngüsü (Red-Green-Refactor)

### 1. 🔴 RED (Başarısız Test)
Henüz var olmayan bir özellik için testi yaz. Testin **başarısız** (Failed) olduğunu gör.
- **Amaç**: Testin gerçekten bir şeyi kontrol ettiğinden emin olmak.

### 2. 🟢 GREEN (Geçen Test)
Testi geçirmek için **minimum** seviyede kodu yaz. Kodun mükemmel olması gerekmez.
- **Amaç**: Testten "Yeşil" (Passed) ışığı almak.

### 3. 🔵 REFACTOR (İyileştirme)
Hem koda hem de teste odaklan. Okunabilirliği artır, duplicate kodları temizle.
- **Amaç**: Kaliteyi artırırken testlerin hala yeşil kalmasını sağlamak.

---

## 🏆 Faydaları
- **Design Guidance**: Test yazarken API/Fonksiyon tasarımını kullanıcı gözüyle görürsün.
- **Regression Safety**: Her değişiklikte tüm sistemin çalıştığını saniyeler içinde anlarsın.
- **Documentation**: Testler, kodun nasıl çalışması gerektiğinin canlı dökümanıdır.

---

## 🔧 Workflow

> **Kaynak:** [Test Driven Development: By Example (Kent Beck)](https://www.oreilly.com/library/view/test-driven-development/0321146530/) & [Clean Code (Robert C. Martin)](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

### Aşama 1: Test Definition (RED)
- [ ] **Isolate Logic**: Test edilecek en küçük mantık birimini (Unit) seç.
- [ ] **Write Assertion**: Beklenen sonucu (`expect(result).toBe(expected)`) içeren testi yaz.
- [ ] **Run & Fail**: Testi çalıştır ve `ReferenceError` veya `AssertionError` aldığını teyit et.

### Aşama 2: Implementation (GREEN)
- [ ] **Minimal Code**: Sadece testi geçirecek kadar kod yaz (Örn: Statik bir değer dönmek bile bazen yeterlidir).
- [ ] **Verification**: Tüm test paketini çalıştır ve "Yeşil"e ulaştığından emin ol.
- [ ] **Commit**: Bu aşamada "Test passed" durumunu commit'le.

### Aşama 3: Optimization (REFACTOR)
- [ ] **Code Cleanup**: `Magic numbers`, `Duplicate logic` ve `Naming` sorunlarını düzelt.
- [ ] **Test Cleanup**: Test verilerini (Mocks, Stubs) daha okunabilir hale getir.
- [ ] **Final Pass**: Refactor sonrası testlerin hala yeşil olduğunu (Davranışın değişmediğini) kanıtla.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Test yazmadan önce kod yazıldı mı? (KURAL İHLALİ!). |
| 2 | Refactor aşamasında yeni bir fonksiyonellik eklendi mi? (Yapılmamalı). |
| 3 | Testler "Hızlı" mı? (Saniyeler içinde bitti mi?). |

---

*TDD Workflow v1.1 - Enhanced*
