---
name: market_analyst
router_kit: FullStackKit
description: Pazar analizi, TAM/SAM/SOM hesaplama, rekabet analizi ve müşteri segmentasyonu rehberi.
metadata:
  skillport:
    category: research
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, market analyst, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - competition
---

# 📊 Market Analyst

> Pazar analizi ve opportunity sizing rehberi.

---

## 📈 TAM/SAM/SOM

### Tanımlar
| Metric | Açıklama |
|--------|----------|
| **TAM** | Total Addressable Market - Toplam pazar |
| **SAM** | Serviceable Addressable Market - Ulaşılabilir pazar |
| **SOM** | Serviceable Obtainable Market - Gerçekçi hedef |

### Hesaplama
```
TAM = Toplam müşteri sayısı × Ortalama gelir

SAM = TAM × (Hedeflenebilir segment %)

SOM = SAM × (Pazar payı hedefi %)
```

### Örnek
```
TAM: 10M şirket × $1000/yıl = $10B
SAM: $10B × 20% (SMB segment) = $2B
SOM: $2B × 2% (1. yıl hedef) = $40M
```

---

## 🔍 Rekabet Analizi

### Competitor Matrix
| Feature | Us | Competitor A | Competitor B |
|---------|----|--------------|--------------| 
| Price | $$ | $$$ | $ |
| Features | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| UX | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Support | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |

### SWOT Analysis
```
         Helpful          Harmful
       ┌─────────────┬─────────────┐
Internal│ STRENGTHS   │ WEAKNESSES  │
       │ • Fast dev  │ • Small team│
       │ • UX focus  │ • No brand  │
       ├─────────────┼─────────────┤
External│ OPPORTUNITIES│ THREATS     │
       │ • Growing   │ • Big players│
       │   market    │ • Regulation │
       └─────────────┴─────────────┘
```

---

## 👥 Müşteri Segmentasyonu

### Segment Kriterleri
| Kriter | Açıklama |
|--------|----------|
| Demographic | Yaş, cinsiyet, gelir |
| Geographic | Konum, bölge |
| Psychographic | Değerler, yaşam tarzı |
| Behavioral | Kullanım, sadakat |

### B2B Segmentasyon
| Segment | Company Size | Budget | Sales Cycle |
|---------|-------------|--------|-------------|
| Enterprise | 1000+ | $$$$ | 6-12 ay |
| Mid-Market | 100-999 | $$$ | 3-6 ay |
| SMB | 10-99 | $$ | 1-3 ay |
| Startup | <10 | $ | <1 ay |

---

## 📋 Market Research Template

```markdown
## Market Overview
- Industry: [Sektör]
- Market Size: [TAM]
- Growth Rate: [CAGR %]

## Target Segments
1. Primary: [Segment A]
2. Secondary: [Segment B]

## Competitive Landscape
- Market leader: [Company]
- Key differentiators: [...]

## Trends
1. [Trend 1]
2. [Trend 2]

## Opportunities
1. [Opportunity 1]
2. [Opportunity 2]
```

---

*Market Analyst v1.0*
