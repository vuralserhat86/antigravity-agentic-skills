---
name: specification_validation
router_kit: DevOpsKit
description: Spec doğrulama, implementation karşılaştırma ve completeness kontrolü rehberi.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, specification validation, standards, testing, utilities, version control, workflow]      - quality
---

# ✅ Specification Validation

> Spec doğrulama ve completeness kontrolü rehberi.

---

## 📋 İçindekiler

1. [Validation Framework](#1-validation-framework)
2. [Completeness Check](#2-completeness-check)
3. [Consistency Check](#3-consistency-check)
4. [Implementation Comparison](#4-implementation-comparison)

---

## 1. Validation Framework

### Validation Dimensions

| Dimension | Açıklama | Kontrol |
|-----------|----------|---------|
| **Completeness** | Tüm gereksinimler tanımlandı mı? | Eksik alan yok |
| **Consistency** | Çelişen tanımlar var mı? | Tutarlılık |
| **Correctness** | Gereksinimler doğru mu? | Domain doğruluğu |
| **Clarity** | Belirsizlik var mı? | Net tanımlar |
| **Testability** | Test edilebilir mi? | Measurable criteria |

### Validation Checklist
```checklist
- [ ] Tüm use case'ler tanımlandı mı?
- [ ] Error case'ler belirtildi mi?
- [ ] Edge case'ler düşünüldü mü?
- [ ] Acceptance criteria net mi?
- [ ] Dependencies tanımlandı mı?
- [ ] Non-functional requirements var mı?
```

---

## 2. Completeness Check

### Required Sections
```markdown
## Spec Completeness Template

### 1. Overview
- [ ] Problem statement
- [ ] Goals ve objectives
- [ ] Success metrics

### 2. Functional Requirements
- [ ] User stories / use cases
- [ ] Input/output specifications
- [ ] Business rules

### 3. Non-Functional Requirements
- [ ] Performance requirements
- [ ] Security requirements
- [ ] Scalability requirements

### 4. Technical Details
- [ ] Architecture decisions
- [ ] API contracts
- [ ] Data models

### 5. Edge Cases & Errors
- [ ] Error handling
- [ ] Fallback behavior
- [ ] Validation rules
```

### Gap Analysis
```
Missing: [Alan adı]
Impact: High / Medium / Low
Recommendation: [Önerilen aksiyon]
```

---

## 3. Consistency Check

### Cross-Reference Matrix
| Requirement | UI Spec | API Spec | DB Schema | Test Spec |
|-------------|---------|----------|-----------|-----------|
| User Login  | ✅      | ✅       | ✅        | ⚠️        |
| Password Reset | ✅   | ❌       | ⚠️        | ❌        |

### Conflict Detection
```markdown
## Conflict Report

**Conflict ID:** C-001
**Location:** API Spec vs UI Spec
**Description:** 
- API: `email` field max 100 chars
- UI: `email` input allows 255 chars

**Resolution:** Align to 100 chars (API standard)
```

---

## 4. Implementation Comparison

### Spec vs Code Comparison
```bash
# Spec'te tanımlı endpoint'ler
grep -r "POST\|GET\|PUT\|DELETE" spec.md

# Kod'da mevcut endpoint'ler
grep -r "@Post\|@Get\|@Put\|@Delete" src/

# Karşılaştır
diff spec_endpoints.txt code_endpoints.txt
```

### Implementation Status
| Feature | Spec | Implemented | Tested | Notes |
|---------|------|-------------|--------|-------|
| Login | ✅ | ✅ | ✅ | |
| Signup | ✅ | ✅ | ⚠️ | E2E test eksik |
| Password Reset | ✅ | ❌ | ❌ | Backlog'da |

---

*Specification Validation v1.1 - Enhanced*

## 🔄 Workflow

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
