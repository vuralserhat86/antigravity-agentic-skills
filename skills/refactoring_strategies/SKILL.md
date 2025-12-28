---
name: refactoring_strategies
router_kit: FullStackKit
description: Safe refactoring süreci - test-first, incremental changes ve güvenlik ağı.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, refactoring strategies, software engineering, standards, testing, utilities, version control, workflow]      - refactoring-patterns
---

# 🛡️ Refactoring Strategies

> Safe refactoring süreci ve incremental değişiklikler.

---

## ⏰ Ne Zaman Refactor?

| Sinyal | Aksiyon |
|--------|---------|
| Code Smell | Refactor et |
| Before feature | Zemin hazırla |
| After bug fix | Kodu iyileştir |

### ❌ Ne Zaman YAPMA
- Deadline çok yakın
- Test coverage düşük
- Sistemi anlamadan

---

## 🔒 Güvenlik Ağı

```typescript
// Önce mevcut davranışı test et
describe('calculateTotal', () => {
  test('single item', () => {
    expect(calculateTotal([{ price: 100, qty: 1 }])).toBe(100);
  });
  
  test('multiple items', () => {
    expect(calculateTotal([
      { price: 100, qty: 2 },
      { price: 50, qty: 1 }
    ])).toBe(250);
  });
  
  test('empty array', () => {
    expect(calculateTotal([])).toBe(0);
  });
});
```

---

## 📊 Incremental Strategy

1. **Test yaz** → Mevcut davranışı belgele
2. **Küçük değişiklik** → Tek bir şeyi değiştir
3. **Test çalıştır** → Hala geçiyor mu?
4. **Commit** → Küçük, atomik commit
5. **Tekrarla**

---

## ✅ Checklist

- [ ] Testler geçiyor
- [ ] Davranış değişmedi
- [ ] Küçük commit'ler
- [ ] Feature ile karıştırma

---

*Refactoring Strategies v1.0*
