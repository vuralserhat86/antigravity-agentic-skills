---
name: skill_creator
router_kit: ManagementKit
description: Yeni skill'lerin Anthropic standartlarına uygun olarak tasarlanması ve oluşturulması.
metadata:
  skillport:
    category: skills
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, skill creator, software engineering, standards, testing, utilities, version control, workflow]      - skill-authoring
---

# 🛠️ Skill Creator

> Yüksek kaliteli ve standartlara uygun yeni ajan yetenekleri (Skills) oluşturma.

---

*Skill Creator v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Anthropic - Agent Skill Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/agent-skills)

### Aşama 1: Design & Scoping
- [ ] **Need Analysis**: Gerçek bir ihtiyacı veya problemi tanımla (Neden bu skill var?).
- [ ] **Naming**: Dosya ve skill adını küçük harf, rakam ve tire (`-`) kullanarak belirle (Maks 64 karakter).
- [ ] **Scope**: Skill'in sorumluluğunu ("Single Responsibility") netleştir.

### Aşama 2: Content Authoring (SKILL.md)
- [ ] **YAML Frontmatter**: `name`, `description` ve `metadata` alanlarını eksiksiz doldur.
- [ ] **Role Definition**: Skill'in hangi uzmana ait olduğunu (Role) belirt.
- [ ] **Workflow**: En az 3-4 adımlı, kontrol noktaları içeren bir "🔄 Workflow" bölümü oluştur.

### Aşama 3: References & Scripts
- [ ] **References**: Karmaşık detayları ana dosyadan çıkarıp `references/*.md` dosyalarına taşı.
- [ ] **Scripts**: Tekrarlayan veya karmaşık mantıklar için `scripts/*.py` veya `*.sh` dosyaları oluştur.
- [ ] **Validation**: Skill'i `skill_evaluator` ile test ederek kalite skorunu (1-5) ölç.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Açıklama (Description) aktivasyon tetikleyicilerini (Triggers) içeriyor mu? |
| 2 | `SKILL.md` dosyası 500 satırın altında mı? (Progressive Disclosure). |
| 3 | Tüm yollar (Paths) ileri eğik çizgi (`/`) kullanılarak mı yazıldı? |
