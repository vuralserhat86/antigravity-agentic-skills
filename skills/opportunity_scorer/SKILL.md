---
name: opportunity_scorer
router_kit: FullStackKit
description: Fırsat puanlama, scoring rubric ve go/no-go karar verme rehberi.
metadata:
  skillport:
    category: business
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, opportunity scorer, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - prioritization
---

# 📊 Opportunity Scorer

> Fırsat puanlama ve karar verme rehberi.

---

## 📋 Scoring Framework

### Kriterler (0-10)
| Kriter | Ağırlık | Açıklama |
|--------|---------|----------|
| Market Size | 20% | TAM/SAM büyüklüğü |
| Fit | 25% | Yetenek/strateji uyumu |
| Competition | 15% | Rekabet yoğunluğu |
| Effort | 20% | Uygulama zorluğu |
| Timeline | 10% | Zaman çerçevesi |
| Risk | 10% | Risk seviyesi |

---

## 🔧 Scoring Template

```markdown
## Opportunity: [Name]

| Kriter | Score (0-10) | Weight | Weighted |
|--------|--------------|--------|----------|
| Market Size | 8 | 20% | 1.6 |
| Fit | 9 | 25% | 2.25 |
| Competition | 6 | 15% | 0.9 |
| Effort | 7 | 20% | 1.4 |
| Timeline | 8 | 10% | 0.8 |
| Risk | 7 | 10% | 0.7 |
| **TOTAL** | | | **7.65** |
```

---

## 🎯 Decision Thresholds

| Score | Recommendation | Action |
|-------|----------------|--------|
| 8.0+ | STRONG GO | Prioritize |
| 6.5-7.9 | GO | Proceed |
| 5.0-6.4 | CONDITIONAL | More research |
| <5.0 | NO GO | Pass |

---

## 📊 Comparison Matrix

| Opportunity | Score | Rank | Decision |
|-------------|-------|------|----------|
| Opp A | 8.2 | 1 | STRONG GO |
| Opp B | 7.1 | 2 | GO |
| Opp C | 5.8 | 3 | CONDITIONAL |
| Opp D | 4.2 | 4 | NO GO |

---

*Opportunity Scorer v1.0*
