---
name: refactoring_patterns
router_kit: FullStackKit
description: Common refactoring patterns - Extract, Rename, Move ve code smell çözümleri.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, refactoring patterns, software engineering, standards, testing, utilities, version control, workflow]      - refactoring-strategies
---

# 🔄 Refactoring Patterns

> Common refactoring patterns ve code smell çözümleri.

---

## 🎯 Altın Kural

> **Davranışı DEĞİŞTİRME, sadece yapıyı iyileştir**

```
Before: Input X → [Code A] → Output Y
After:  Input X → [Code B] → Output Y (AYNI!)
```

---

## 🔍 Code Smells

| Smell | Çözüm |
|-------|-------|
| Long Method | Extract Method |
| Large Class | Extract Class |
| Duplicate Code | Extract + Reuse |
| Long Parameter List | Parameter Object |
| Feature Envy | Move Method |
| Data Clumps | Extract Class |

---

## 📦 Extract Method

```typescript
// ❌ Before
function processOrder(order) {
  // 20 lines of validation
  // 30 lines of calculation
  // 15 lines of formatting
}

// ✅ After
function processOrder(order) {
  validateOrder(order);
  const total = calculateTotal(order);
  return formatOutput(total);
}
```

---

## 🔄 Replace Conditional with Polymorphism

```typescript
// ❌ Before
function getPrice(type) {
  if (type === 'premium') return 100;
  if (type === 'basic') return 50;
  return 30;
}

// ✅ After
const pricing = { premium: 100, basic: 50, free: 30 };
const getPrice = (type) => pricing[type] ?? 30;
```

---

*Refactoring Patterns v1.0*
