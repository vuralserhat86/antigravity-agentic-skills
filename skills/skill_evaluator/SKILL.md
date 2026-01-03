---
name: skill_evaluator
router_kit: ManagementKit
description: Skill'lerin Anthropic standartlarına göre değerlendirilmesi, puanlanması ve raporlanması.
metadata:
  skillport:
    category: skills
    tags: [architecture, audit, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, metrics, optimization, productivity, programming, project management, quality assurance, quality check, refactoring, review, skill evaluator, software engineering, standards, testing, utilities, version control, workflow]      - quality-assurance
---

# 🛡️ Skill Evaluator

> Skill'lerin kalitesini, tutarlılığını ve standartlara uyumunu denetleme.

---

*Skill Evaluator v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Google Engineering Practices - Code Review](https://google.github.io/eng-practices/review/) & [Anthropic System Prompts](https://docs.anthropic.com/claude/docs/system-prompts)

### Aşama 1: Structural Analysis
- [ ] **Compliance**: Dosya yapısı (`scripts/`, `references/`) standarta uyuyor mu?
- [ ] **Metadata**: YAML frontmatter (`name`, `description`) eksiksiz ve valid mi?
- [ ] **Modularity**: Skill çok mu büyük? Bölünmesi gerekiyor mu? (Single Responsibility Principle).

### Aşama 2: Content & Semantic Review
- [ ] **Clarity**: Talimatlar emir kipiyle (Imperative) ve net yazılmış mı? Belirsizlik var mı?
- [ ] **Context Efficiency**: "Gereksiz nezaket" veya "aşırı açıklama" var mı? Token israfı önlenmeli.
- [ ] **Safety**: Skill tehlikeli bir işlem (dosya silme, yetkisiz erişim) öneriyor mu?

### Aşama 3: Functionality Verification
- [ ] **Script Audit**: `scripts/` içindeki Python/Bash kodları güvenli ve çalışır durumda mı?
- [ ] **Reference Check**: `references/` dosyaları gerçekten gerekli mi? Yoksa `SKILL.md` içine mi gömülmeli?
- [ ] **Usability**: Bir kullanıcı (veya ajan) bu skill'i okuyup hemen kullanabilir mi?

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Skill adı ve açıklaması birbiriyle tutarlı mı? |
| 2 | Anti-pattern (örn: Hardcoded path) tespit edildi mi? |
| 3 | Puanlama rubriğine göre objektif bir skor (1-5) verildi mi? |
