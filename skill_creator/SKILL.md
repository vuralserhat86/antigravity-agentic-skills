---
name: skill_creator
router_kit: DevOpsKit
description: Yeni AI skill'leri oluşturma, master list analizi ve dökümantasyon standartları.
metadata:
  skillport:
    category: core
    tags: [architecture, automation, best practices, cleanup, coaching, collaboration, documentation, efficiency, integrations, maintainability, metadata, open-source, optimization, performance, quality assurance, scalability, skill creator_1, skill development, software engineering, standards, testing, version control, web development, workflow]      - meta-skill
---

# 🛠️ Skill Creator

> Yeni uzmanlık alanları (Skills) oluşturma ve sistem standartlarına entegrasyon rehberi.

---

## 🏗️ Skill Yapısı

Her `SKILL.md` dosyası şu bölümleri içermelidir:

1. **Frontmatter**: `name`, `router_kit`, `description`, `metadata`.
2. **Title & Header**: Skill'in adı ve kısa özeti.
3. **Core Knowledge**: Tablolar, kod blokları ve teorik bilgi.
4. **Workflow**: En az 3 aşamalı (Plan, Execute, Verify) aksiyon planı.
5. **Checklist**: Doğrulama noktaları.

---

## 🔧 Workflow

> **Kaynak:** [Antigravity SkillPort Standard v2.0] & [Super Protokol v2 Rules]

### Aşama 1: Research & Scoping
- [ ] **Requirement**: Yeni skill'in hangi boşluğu (Gap) dolduracağını belirle.
- [ ] **Reference Discovery**: İlgili alanın resmi dökümantasyonlarını ve "Best Practice" repo'larını bul.
- [ ] **Naming**: Skill adını `snake_case` formatında veMaster List ile uyumlu seç.

### Aşama 2: Content Generation
- [ ] **Metadata**: YAML frontmatter bölümünü eksiksiz doldur. `tags` listesini anahtar kelimelerle zenginleştir.
- [ ] **Engineering Standards**: Skill içeriğinin teknik olarak doğru, güncel ve "Antigravity Engineering Culture" ile uyumlu olmasını sağla.
- [ ] **Turkish Support**: Açıklamalar ve Workflow adımlarını Türkçe (Demir Kural) hazırla.

### Aşama 3: Quality Check & Deployment
- [ ] **Validation**: `skill_evaluator` aracını kullanarak skill'in standartlara uygunluğunu denetle.
- [ ] **Folder Structure**: Skill dosyasını `.skillport/skills/[skill_name]/SKILL.md` yoluna kaydet.
- [ ] **Master List Update**: Yeni skill'i `skills_manifest.json` veya merkezi listeye ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Skill içeriğinde "Workflow" bölümü var mı? |
| 2 | Kod blokları İngilizce, açıklamalar Türkçe mi? (Kural 0). |
| 3 | Skill adı benzersiz mi? |

---

*Skill Creator v1.1 - Enhanced*
