---
name: sparc_methodology
router_kit: DevOpsKit
description: SPARC (Specification, Pseudocode, Architecture, Review, Commit) metodolojisi ile güvenli geliştirme.
metadata:
  skillport:
    category: engineering
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, organizational skills, productivity, programming, project management, quality assurance, refactoring, software engineering, sparc methodology_1, standards, testing, utilities, version control, workflow]      - software-engineering
---

# ⚡ SPARC Methodology

> Hızlı, güvenli ve yüksek kaliteli yazılım geliştirme döngüsü.

---

## 🏗️ SPARC Adımları

### 1. Specification (S)
Ne yapılacağını netleştir. Girdi, çıktı ve kısıtları belirle.

### 2. Pseudocode (P)
Kod yazmadan önce mantığı (Logic) doğal dilde veya basit şemayla planla.

### 3. Architecture (A)
Kullanılacak dosya yapısı, patternlar ve bağımlılıkları kararlaştır.

### 4. Review (R)
Planın üzerinden geç, "Bu daha iyi yapılabilir mi?" diye sor, gerekirse düzelt.

### 5. Commit (C) - Implementation
Kodu yaz, test et ve anlamlı bir commit mesajıyla tamamla.

---

## 🔧 Workflow

> **Kaynak:** [SPARC Engineering Framework] & [Clean Code Principles]

### Aşama 1: Framing (S & P)
- [ ] **Spec**: Gereksinimi tek cümleye indirge. Başarı kriterlerini listele.
- [ ] **Planning**: Algoritmayı yorum satırlarıyla (Pseudocode) taslakla. Karmaşıklığı önceden gör.
- [ ] **Data Flow**: Verinin nereden gelip nereye gideceğini (Flow) görselleştir veya yaz.

### Aşama 2: Blueprinting (A & R)
- [ ] **Structural Design**: Dosyanın nereye ekleneceğini ve hangi component/module ile konuşacağını belirle.
- [ ] **Sanity Check**: Hazırladığın planı mevcut sistem standartlarıyla (Linter, Design System) karşılaştır.
- [ ] **Edge Case Audit**: "Null gelirse ne olur?", "Bağlantı koparsa ne olur?" gibi uç durumları plana ekle.

### Aşama 3: Realization (C)
- [ ] **TDD (Optional)**: Önce testi yaz (eğer sistem destekliyorsa), sonra kodu geliştir.
- [ ] **Implementation**: Plandaki yorum satırlarını tek tek gerçek koda dönüştür.
- [ ] **Validation**: Kodu bitirdikten sonra build ve test süreçlerini çalıştırıp sonuca "Approve" ver.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Planlama aşaması (S, P, A) atlandı mı? (Atlanmamalı!). |
| 2 | Kod yazılırken plandan sapıldı mı? (Sapıldıysa R adımına dön). |
| 3 | Commit mesajı "feat:", "fix:" gibi standartlara uyuyor mu? |

---

*SPARC Methodology v1.1 - Enhanced*
