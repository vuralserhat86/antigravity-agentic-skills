---
name: postgres_pro
router_kit: FullStackKit
description: PostgreSQL döküman modelleme, sorgu optimizasyonu (EXPLAIN) ve admin operasyonları.
metadata:
  skillport:
    category: database
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, postgres pro, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - sql-expert
---

# 🐘 PostgreSQL Pro

> İleri seviye PostgreSQL veritabanı yönetimi ve sorgu iyileştirme.

---

*PostgreSQL Pro v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [PostgreSQL 17 Release Notes](https://www.postgresql.org/docs/17/release.html) & [Use The Index, Luke!](https://use-the-index-luke.com/)

### Aşama 1: Schema Design & Indexing
- [ ] **Normalization**: 3NF ile başla, performans gerekirse (Read-heavy) denormalize et.
- [ ] **Indexing Strategy**: Sorgu paternlerine göre B-Tree (Default), GIN (JSONB/Array), GiST (Geo/Range) veya BRIN (Time-series) seç.
- [ ] **Vector Search**: AI/ML projeleri için `pgvector` eklentisini kur ve HNSW indekslerini yapılandır.

### Aşama 2: Query Tuning
- [ ] **Explain Analyze**: `EXPLAIN (ANALYZE, BUFFERS)` ile sorgunun gerçek maliyetini ve I/O tüketimini gör.
- [ ] **Seq Scans**: Büyük tablolarda Sequential Scan varsa eksik indeks veya kötü istatistik (`ANALYZE table`) vardır.
- [ ] **CTE Materialization**: Postgres 12+ genellikle akıllıdır ama karmaşık CTE'lerde `NOT MATERIALIZED` gerekip gerekmediğini kontrol et.

### Aşama 3: Maintenance & Config
- [ ] **Autovacuum**: Tablo boyutuna göre scale olması için `autovacuum_vacuum_scale_factor` ayarlarını tune et.
- [ ] **Connection Pooling**: PgBouncer kullanarak bağlantı maliyetini düşür (Özellikle Serverless/Lambda için).
- [ ] **Backup**: WAL archiving (pgBackRest) ile Point-in-Time Recovery (PITR) stratejisi kur.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | JSONB sütunlarında çok sık güncelleme yapılıyor mu? (TOAST bloat riski). |
| 2 | `work_mem` ayarı bağlantı sayısına göre güvenli mi? (OOM hatası riski). |
| 3 | Slow Query Log açık mı? (`log_min_duration_statement`). |
