---
name: roadmap_planner
router_kit: ManagementKit
description: Implementation roadmap, timeline oluşturma, risk yönetimi ve kaynak planlaması rehberi.
metadata:
  skillport:
    category: planning
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, roadmap planner, software engineering, standards, testing, utilities, version control, workflow]      - risk
---

# 🗺️ Roadmap Planner

> Implementation roadmap ve proje planlama rehberi.

---

## 📋 Roadmap Template

```markdown
# [Proje Adı] Roadmap

## Vision
[Uzun vadeli hedef]

## Milestones

### Phase 1: Foundation (Q1)
- [ ] Milestone 1.1
- [ ] Milestone 1.2

### Phase 2: Core Features (Q2)
- [ ] Milestone 2.1
- [ ] Milestone 2.2

### Phase 3: Polish & Launch (Q3)
- [ ] Milestone 3.1
- [ ] Milestone 3.2
```

---

## ⏱️ Timeline Oluşturma

### Gantt Chart Formatı
```
Task              | W1 | W2 | W3 | W4 | W5 | W6 |
------------------|----|----|----|----|----|----|
Research          | ██ | ██ |    |    |    |    |
Design            |    | ██ | ██ |    |    |    |
Development       |    |    | ██ | ██ | ██ |    |
Testing           |    |    |    |    | ██ | ██ |
Launch            |    |    |    |    |    | ██ |
```

### Estimation Guideline
| Complexity | Duration | Buffer |
|------------|----------|--------|
| Simple | 1-2 gün | +20% |
| Medium | 3-5 gün | +30% |
| Complex | 1-2 hafta | +40% |
| Unknown | 2+ hafta | +50% |

---

## ⚠️ Risk Yönetimi

### Risk Matrix
```
           IMPACT
         Low  Med  High
    Low   🟢   🟢   🟡
L
I  Med   🟢   🟡   🔴
K
E  High  🟡   🔴   🔴
L
I
H
O
O
D
```

### Risk Register Template
| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|----|------|------------|--------|------------|-------|
| R1 | API rate limits | Med | High | Caching, retry | Dev |
| R2 | Scope creep | High | Med | Strict PR | PM |

---

## 👥 Kaynak Planlaması

### Team Allocation
| Role | Phase 1 | Phase 2 | Phase 3 |
|------|---------|---------|---------|
| Frontend | 1 | 2 | 1 |
| Backend | 2 | 2 | 1 |
| QA | 0 | 1 | 2 |
| DevOps | 0.5 | 0.5 | 1 |

### Capacity Planning
```
Haftalık saat = Kişi sayısı × 40 × Verimlilik(0.7)
Örnek: 3 dev × 40 × 0.7 = 84 saat/hafta
```

---

## 📊 Progress Tracking

### Status Indicators
- 🟢 On track
- 🟡 At risk
- 🔴 Blocked
- ✅ Completed

### Weekly Status Template
```markdown
## Week [N] Status

### Completed
- [x] Task A
- [x] Task B

### In Progress
- [ ] Task C (60%)
- [ ] Task D (30%)

### Blocked
- Task E - Waiting for API access

### Next Week
- Task F
- Task G
```

---

*Roadmap Planner v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Product Roadmap Guide (Atlassian)](https://www.atlassian.com/agile/product-management/product-roadmaps) & [Outcome-Based Roadmaps](https://www.prodpad.com/blog/outcome-based-roadmaps/)

### Aşama 1: Strategic Alignment (Outcome Oriented)
- [ ] **Goal Definition**: "Özellik" (Feature) yerine "Çıktı" (Outcome) odaklı hedefler belirle (Örn: "Login sayfası yap" ❌ → "Kayıt olma süresini %20 düşür" ✅).
- [ ] **Now-Next-Later**: Tarih bazlı (Ocak, Şubat) yerine zaman dilimi bazlı (Şimdi, Sonra, İlerde) planlama yap.
- [ ] **Stakeholder Mapping**: Kimin ne beklediğini belirle ve öncelikleri şeffaf bir şekilde paylaş.

### Aşama 2: Execution Planning (Output Oriented)
- [ ] **Vertical Slicing**: Büyük özellikleri (Epics) bağımsız deploy edilebilir küçük parçalara böl (MVP mantığı).
- [ ] **Dependency Graph**: Hangi işin hangisine bağlı olduğunu görselleştir (Critical Path Analysis).
- [ ] **Buffer Management**: Her faz için %20-30 oranında "bilinmeyen" (unknown) zamanı ekle.

### Aşama 3: Review & Adapt
- [ ] **Bi-Weekly Review**: Yol haritasını 2 haftada bir gözden geçir ve statik kalmadığından emin ol.
- [ ] **Risk Re-assessment**: Her milestone bitiminde riskleri tekrar puanla (Likelihood x Impact).
- [ ] **Communication**: Değişiklikleri proaktif olarak duyur (Neden gecikildi? Plan ne?).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Hedefler SMART (Specific, Measurable, Achievable, Relevant, Time-bound) mı? |
| 2 | Kritik yol (Critical Path) üzerinde darboğaz var mı? |
| 3 | Ekip kapasitesi gerçekçi hesaplandı mı? (Tatiller, toplantılar düştü mü?). |
