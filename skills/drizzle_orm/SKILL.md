---
name: drizzle_orm
router_kit: FullStackKit
description: Drizzle ORM setup, schema definitions, migrations (D1/SQLite) ve TypeScript integration.
metadata:
  skillport:
    category: backend
    tags: [architecture, automation, backend, best practices, cloudflare, cloudflare d1, database, database design, design patterns, development, drizzle orm, edge computing, migration, optimization, orm, postgresql, scalability, schema, software engineering, sqlite, testing, typescript, workflow]      - cloudflare-d1
---

# 💧 Drizzle ORM (D1/SQLite)

> Drizzle ORM setup, schema definitions ve migration yönetimi.

---

## 🛠️ Schema Definition (SQLite/D1)

```typescript
import { sqliteTable, text, integer } from 'drizzle-orm/sqlite-core';

export const users = sqliteTable('users', {
  id: integer('id').primaryKey({ autoIncrement: true }),
  name: text('name').notNull(),
  email: text('email').notNull().unique(),
  createdAt: integer('created_at', { mode: 'timestamp' }).$defaultFn(() => new Date()),
});
```

---

## 🚀 Migration Workflow

### 1. Generate Migration
```bash
npx drizzle-kit generate
```

### 2. Apply Migration (Local)
```bash
npx wrangler d1 migrations apply DB_NAME --local
```

### 3. Apply Migration (Production)
```bash
npx wrangler d1 migrations apply DB_NAME --remote
```

---

## 🔍 Type-Safe Queries

```typescript
import { drizzle } from 'drizzle-orm/d1';
import { users } from './db/schema';
import { eq } from 'drizzle-orm';

const db = drizzle(env.DB);

// Get user by email
const user = await db.select()
  .from(users)
  .where(eq(users.email, 'test@example.com'))
  .get();
```

---

*Drizzle ORM v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Drizzle Kit Migrations](https://orm.drizzle.team/docs/kit-overview)

### Aşama 1: Schema Definition
- [ ] **Types**: `text`, `integer` gibi doğru veri tiplerini seç (SQLite/D1 uyumlu).
- [ ] **Constraints**: `notNull()`, `unique()`, `primaryKey()` kısıtlarını tanımla.
- [ ] **Relations**: Tablolar arası ilişkileri `relations()` fonksiyonu ile belirt.

### Aşama 2: Migration Lifecycle
- [ ] **Generate**: `drizzle-kit generate` ile SQL oluştur.
- [ ] **Review**: Oluşan `.sql` dosyasını manuel kontrol et (Veri kaybı riski?).
- [ ] **Apply**: `wrangler d1 migrations apply --local` ile önce lokalde test et.

### Aşama 3: Query Implementation
- [ ] **Queries**: `.select().from()` ile type-safe sorgular yaz.
- [ ] **Performance**: N+1 sorununu `include` veya `with` kullanarak önle.
- [ ] **Batch**: Toplu işlemleri `db.batch([])` içine al.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `migrations` klasörü versiyon kontrolünde (Git) mi? |
| 2 | Üretim ortamına (`--remote`) geçmeden önce `--local` test edildi mi? |
| 3 | Hassas veriler `.env` üzerinden mi okunuyor? |
