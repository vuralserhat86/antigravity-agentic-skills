---
name: debugging_methodology
router_kit: FullStackKit
description: Sistematik hata ayıklama süreci, root cause analizi ve hata raporlama.
metadata:
  skillport:
    category: quality
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging methodology, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - root-cause
---

# 🔍 Debugging Methodology

> Sistematik hata ayıklama ve problem çözme.

---

*Debugging Methodology v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [The Scientific Method of Debugging](https://en.wikipedia.org/wiki/Debugging#Scientific_method)

### Aşama 1: Observation & Reproduction
- [ ] **Reproduce**: Hatayı "her zaman" tetikleyecek en basit adımları belirle.
- [ ] **Collect Data**: Loglar, ekran görüntüleri ve kullanıcı verilerini topla.

### Aşama 2: Hypothesis Generation
- [ ] **Brainstorm**: Hataya neden olabilecek 2-3 potansiyel sebebi listele.
- [ ] **Prioritize**: En olası sebebi en üste al.

### Aşama 3: Testing & Fix
- [ ] **Experiment**: Hipotezini test etmek için küçük kod değişiklikleri yap.
- [ ] **Verify**: Düzeltmenin hatayı gerçekten giderdiğini ve yan etki yaratmadığını doğrula.

### Aşama 4: Prevention
- [ ] **Test Case**: Hatayı önleyecek bir unit/integration test ekle.
- [ ] **Doc**: Root cause'u ve çözümü not et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1     | Hata güvenilir şekilde tekrar edilebiliyor mu? |
| 2     | Hipotez veriye mi yoksa tahmine mi dayanıyor? |
| 3     | Çözüm başka bir yeri bozdu mu (Regression)? |
