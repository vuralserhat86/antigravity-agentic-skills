---
name: backend_database
router_kit: FullStackKit
description: SQL/NoSQL veri tasarımı, repository pattern, indexing ve caching.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, backend database, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - backend-database
---

# 🗄️ Backend Database

> Veri tasarımı ve veritabanı erişim desenleri.

---

*Backend Database v1.2 - Verified*

## 🔄 Workflow

> **Kaynak:** [Database Reliability Engineering (Campbell)](https://www.oreilly.com/library/view/database-reliability-engineering/9781491925935/)

### Aşama 1: Schema Design
- [ ] **Data Model**: İlişkisel (Normalization) veya döküman tabanlı modellemeyi seç.
- [ ] **Constraints**: PK, FK ve Unique constraint'leri belirle.
- [ ] **Migration**: `prisma migrate` veya `drizzle-kit` gibi araçlarla versiyonlamayı kur.

### Aşama 2: Query Optimization
- [ ] **Explain**: Yavaş sorgular için `EXPLAIN ANALYZE` kullan.
- [ ] **Indexes**: Gerekli indexleri (B-Tree, GIN, Hash) ekle.
- [ ] **N+1 Check**: Relation yüklerken `include` veya `join` kullanımını doğrula.

### Aşama 3: Reliability & Caching
- [ ] **Pooling**: `pgpool` veya native driver pooling ayarlarını yap.
- [ ] **Cache**: Redis ile sık okunan verileri önbellekle.
- [ ] **Backup**: Otomatik yedekleme ve PITR (Point-in-Time Recovery) yapılandırmasını kontrol et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Veritabanı şeması "Code-First" mi takip ediliyor? |
| 2 | Sorgular index kullanıyor mu? (Full table scan yok) |
| 3 | Veritabanı şifreleri `.env` içinde mi? (Asla hardcoded olmamalı) |
