---
name: specification_validation
router_kit: ManagementKit
description: Gereksinim dokümanı (Spec) denetimi, tutarlılık analizi ve teknik fizibilite kontrolü.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, cleanup, coaching, collaboration, compliance, coordinate, development, documentation, efficiency, integrations, maintainability, management, metadata, open-source, optimization, performance, quality assurance, quality control, requirement analysis, software engineering, specification validation_1, standards, testing, traceabilty, version control, web development, workflow]      - requirements
---

# 📋 Specification Validation

> Bir işe başlamadan önce gereksinimlerin (Spec) tam, net ve uygulanabilir olduğunun denetimi.

---

## 🎯 Denetim Matrisi

| Kriter | Anlamı | Kontrol Sorusu |
|--------|--------|----------------|
| **Netlik** | Muğlaklık yok mu? | "Hızlı" yerine "200ms" denmiş mi? |
| **Tamlık** | Eksik parça var mı? | Hata durumları (Error States) yazılmış mı? |
| **Tutarlılık** | Çelişki var mı? | Sayfa 1 ile Sayfa 5 aynı şeyi mi söylüyor? |
| **Fizibilite** | Mümkün mü? | Mevcut teknoloji ile bu sürelerde biter mi? |

---

## 🛠️ Validation Tools

```bash
# Markdown Link Check (Spec içindeki linkler kırık mı?)
npx markdown-link-check spec.md

# Karşılaştır
diff spec_endpoints.txt code_endpoints.txt
```

---

## 🔧 Workflow

> **Kaynak:** [IREB Requirements Engineering](https://www.ireb.org/en/cpre/foundation/) & [IEEE 29148 Standard](https://standards.ieee.org/ieee/29148/6936/)

### Aşama 1: Structural Integrity (Completeness)
- [ ] **Template Compliance**: Spec dokümanı belirlenen şablona (örn: Volere, IEEE 830) uyuyor mu?
- [ ] **Missing Sections**: Zorunlu başlıklar (Security, Performance, Error Handling) atlanmış mı?
- [ ] **TBD Check**: Doküman içinde "TBD" (To Be Defined) veya "???" kalmış mı? Ara ve temizle.

### Aşama 2: Content Quality (Clarity & Consistency)
- [ ] **Ambiguity Audit**: "Hızlı", "Güzel", "Mümkün olduğunca" gibi muğlak ifadeleri "200ms altında", "Material Design", "%99 uptime" gibi ölçülebilir değerlerle değiştir.
- [ ] **Term Consistency**: Aynı kavram için farklı terimler kullanılmış mı? (örn: User vs Customer). Glossary oluştur.
- [ ] **Conflict Check**: İş kuralları arasında çelişki var mı? (örn: "Herkes görebilir" vs "Sadece admin görebilir").

### Aşama 3: Verify & Validatate
- [ ] **Traceability**: Her gereksinimin bir kaynağı (Business Goal) ve bir testi (Test Case) var mı?
- [ ] **Stakeholder Approval**: İlgili tüm paydaşlar (Dev, QA, Product) dokümanı okuyup onayladı mı?
- [ ] **Feasibility**: Teknik ekip "Bu yapılabilir" onayı verdi mi?

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Her gereksinim atomik (tek bir şeyi ifade ediyor) mi? |
| 2 | Doküman versiyon kontrolü altında mı? (Change Log var mı?). |
| 3 | Gereksinimlerin öncelikleri (MoSCoW) belirlenmiş mi? |

---

*Specification Validation v1.1 - Enhanced*
