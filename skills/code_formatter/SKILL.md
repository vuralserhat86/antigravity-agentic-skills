---
name: code_formatter
router_kit: FullStackKit
description: Otomatik kod formatlama, Prettier/ESLint entegrasyonu ve kod stil tutarlılığı rehberi.
metadata:
  skillport:
    category: development
    tags: [big data, cleaning, code formatter, csv, data analysis, data engineering, data science, database, etl pipelines, export, import, json, machine learning basics, migration, nosql, numpy, pandas, python data stack, query optimization, reporting, schema design, sql, statistics, transformation, visualization]      - code-style
---

# 🎨 Code Formatter

> Otomatik kod formatlama ve stil tutarlılığı rehberi.

---

*Code Formatter v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Prettier Docs](https://prettier.io/docs/en/install.html)

### Aşama 1: Installation
- [ ] **Packages**: `prettier`, `eslint` ve ilgili pluginleri kur.
- [ ] **Config**: `.prettierrc` ve `.eslintrc` dosyalarını kök dizine ekle.
- [ ] **Ignore**: `.prettierignore` dosyasına `build/`, `dist/` ekle.

### Aşama 2: Automation
- [ ] **Scripts**: `package.json` içine `format` ve `lint` scriptlerini ekle.
- [ ] **VS Code**: `.vscode/settings.json` ile "Format on Save" aç.
- [ ] **Hooks**: Husky ve lint-staged ile commit öncesi kontrol ekle.

### Aşama 3: CI Integration
- [ ] **Pipeline**: CI sürecine `npm run lint` ve `prettier --check` adımlarını ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `npm run format` çalışınca dosyalar değişiyor mu? |
| 2 | Hatalı bir kod commit edilmeye çalışıldığında Husky engelliyor mu? |
| 3 | CI pipeline format hatası olduğunda fail ediyor mu? |
