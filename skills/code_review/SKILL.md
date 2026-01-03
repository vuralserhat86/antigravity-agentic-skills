---
name: code_review
router_kit: FullStackKit
description: PR review, code smell detection, best practice kontrolü. ⚠️ Kod incelerken kullan. Deliverable kontrolü için → quality-validator, doküman review için → peer-review.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, code review, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - code-smell
---

# 🔍 Code Review

> Etkili kod inceleme ve kalite kontrol rehberi.

---

*Code Review v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Google Engineering Practices](https://google.github.io/eng-practices/review/reviewer/)

### Aşama 1: Triage (Ön Kontrol)
- [ ] **CI Checks**: Testler geçmiş mi? Lint hatası var mı?
- [ ] **Scope**: PR çok mu büyük? (>400 satır ise bölmesini iste).
- [ ] **Description**: "Ne" ve "Neden" açıkça anlatılmış mı?

### Aşama 2: Deep Dive
- [ ] **Logic**: Kodun algoritması doğru ve verimli mi?
- [ ] **Architecture**: Mevcut mimari desenlere uyuyor mu?
- [ ] **Test**: Yeni özellikler için test yazılmış mı?

### Aşama 3: Feedback
- [ ] **Comments**: Yapıcı, nazik ve net yorumlar yaz (`suggestion:`, `question:`).
- [ ] **Decision**: Approve, Request Changes veya Comment.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | PR açıklaması boş ise reddedildi mi? |
| 2 | Breaking change varsa versiyonlamaya dikkat edildi mi? |
| 3 | Yorumlar kişiye değil koda mı yönelik? |
