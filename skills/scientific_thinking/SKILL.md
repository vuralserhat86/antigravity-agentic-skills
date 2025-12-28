---
name: scientific_thinking
router_kit: DevOpsKit
description: Bilimsel metod, hipotez, kanıt değerlendirme, bias analizi. ⚠️ Araştırma/analiz için kullan. Mimari karar için → ultrathink-core.
metadata:
  skillport:
    category: research
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, scientific thinking, software engineering, standards, testing, utilities, version control, workflow]      - analysis
---

# 🔬 Scientific Thinking

> Bilimsel düşünce ve kritik analiz metodolojisi.

---

## ⚡ Bilimsel Metod (Hızlı)

```
Gözlem → Soru → Hipotez → Test → Analiz → Sonuç
```

| Yazılım Karşılığı |
|-------------------|
| Bug report → "Neden?" → "Muhtemelen X" → POC/Test → Log analizi → Root cause |

---

## 📝 Hipotez Template

```markdown
**Hipotez:** [Net, test edilebilir ifade]
**Dayanak:** [Gözlemler]
**Test:** [Nasıl doğrulanacak]
**Beklenen:** [Doğruysa ne olmalı]
```

### İyi Hipotez = TFSM
- **T**estable (Test edilebilir)
- **F**alsifiable (Yanlışlanabilir)
- **S**pecific (Belirli)
- **M**easurable (Ölçülebilir)

---

## ⚖️ Kanıt Hiyerarşisi

```
Güçlü ←────────────────────→ Zayıf

Kontrollü    Gözlemsel    Anekdot    Otorite
  Deney       Çalışma      Örnek     Görüşü
   │            │            │          │
A/B Test    Log/Metrics  "Bende oldu"  "X söyledi"
```

---

## 🧠 Bias & Fallacy Checklist

| Bias | Açıklama | Önlem |
|------|----------|-------|
| Confirmation | Destekleyen kanıt arama | Yanlışlayıcı kanıt ara |
| Anchoring | İlk bilgiye bağlanma | Birden fazla kaynak |
| Sunk Cost | Yatırıma bağlılık | Zero-based thinking |

| Fallacy | Örnek |
|---------|-------|
| Ad Hominem | "O junior, ne bilir" |
| False Dichotomy | "Ya A ya B" |
| Appeal to Authority | "Google yapıyor" |

---

## 📊 Karar Matrisi

```markdown
| Kriter | Ağırlık | A | B | C |
|--------|---------|---|---|---|
| Maliyet | 30% | 3 | 5 | 4 |
| Süre | 25% | 4 | 3 | 5 |
| Risk | 25% | 5 | 4 | 3 |
| **Toplam** | | X | Y | Z |
```

---

*Scientific Thinking v2.0 - Compact*
