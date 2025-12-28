---
name: debugging_methodology
router_kit: FullStackKit
description: Sistematik debugging döngüsü - reproduce, isolate, hypothesize, fix.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, debugging methodology, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - debugging-tools
---

# 🔍 Debugging Methodology

> Sistematik hata ayıklama döngüsü.

---

## 🔄 Debugging Döngüsü

```
REPRODUCE → UNDERSTAND → ISOLATE → HYPOTHESIZE → TEST → FIX → REFLECT
```

---

## 1️⃣ Reproduce
```markdown
### Tekrarlama Raporu
- Hata: [Açıklama]
- Adımlar: 1. ... 2. ... 3. → Hata
- Ortam: [OS, Node, Browser]
- Tekrarlanabilirlik: [%100 / %50 / Nadiren]
```

---

## 2️⃣ 5 Whys

```markdown
Problem: Login çalışmıyor
1. Neden? → API 401 dönüyor
2. Neden? → Token geçersiz
3. Neden? → Token expire
4. Neden? → Refresh çalışmıyor
5. Neden? → Endpoint değişmiş
```

---

## 3️⃣ Binary Search (git bisect)

```bash
git bisect start
git bisect bad HEAD
git bisect good v1.0.0
git bisect run npm test
```

---

## 4️⃣ Hipotez Listesi

| # | Hipotez | Olasılık | Test |
|---|---------|----------|------|
| 1 | Null pointer | %40 | console.log |
| 2 | Race condition | %30 | timeout ekle |

---

*Debugging Methodology v1.0*
