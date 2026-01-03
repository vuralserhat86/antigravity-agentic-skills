---
name: peer_review
router_kit: ManagementKit
description: Etkili ekip içi code review ve dokümantasyon inceleme süreçleri.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, peer review, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - collaboration
---

# 👥 Peer Review

> Yapıcı geribildirim ve yüksek kod kalitesi için inceleme süreci.

---

*Peer Review v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Google Engineeer's Guide to Code Reviews](https://google.github.io/eng-practices/review/) & [The Art of Peer Review](https://stackoverflow.blog/2019/09/30/how-to-make-good-code-reviews-better/)

### Aşama 1: Preparation (Author Side)
- [ ] **Self-Review**: Kodu başkasına göndermeden önce kendin incele (typo, debug logs).
- [ ] **Context**: PR açıklamasında "Neden" bu değişikliği yaptığını ve test sonuçlarını belirt.
- [ ] **Size**: Büyük değişiklikleri küçük, incelenebilir PR'lara böl (<400 satır).

### Aşama 2: Reviewing (Reviewer Side)
- [ ] **Objectivity**: Kişisel tercihler (style) yerine standartlara (Style guide) sadık kal.
- [ ] **Constructiveness**: Sorunları soru sorarak veya öneri vererek belirt ("Bunu X yerine Y ile yazabilir miyiz?").
- [ ] **Priority**: Kritik hataları (Security, Logic) stil hatalarından (Typo) ayır.

### Aşama 3: Resolution & Approval
- [ ] **Address**: Tüm yorumlara cevap ver veya kodu güncelle.
- [ ] **Approval**: Şüphe kalmadığında "Approve" et veya "Request Changes" ile gerekçeni açıkla.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | İnceleme 24 saatten fazla bekledi mi (Cycle time)? |
| 2 | Yorumlar "Hangi kurala" dayandırılarak yapıldı? |
| 3 | Kodun bakımı (Maintainability) bu PR ile arttı mı? |
