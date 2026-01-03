---
name: supabase_patterns
router_kit: FullStackKit
description: Supabase (PostgreSQL) mimarisi, Row Level Security (RLS), Edge Functions ve realtime updates.
metadata:
  skillport:
    category: backend
    tags: [architecture, authentication, automation, backend, best practices, cleanup, cloud, database, database design, deployment, development, edge functions, efficiency, maintainability, metadata, optimization, performance, quality assurance, realtime, rls, scalability, software engineering, standards, supabase, supabase patterns_1, testing, uiversity, version control, workflow]      - baas
---

# ⚡ Supabase Patterns

> Supabase ile Backend-as-a-Service (BaaS) mimarisi ve güvenli Postgres kullanımı.

---

## 🏗️ Architecture Layers

### 1. Database (PostgreSQL)
- **RLS (Row Level Security)**: Veriye kimin erişeceğini SQL seviyesinde kısıtla.
```sql
CREATE POLICY "Users can see only their own data"
ON items FOR SELECT
USING (auth.uid() = user_id);
```

### 2. Auth (GoTrue)
- Email/Password, Magic Link ve Social Login (Google, GitHub) entegrasyonu.

### 3. Edge Functions (Deno)
- Sunucu tarafı logic yazmak için (Örn: Webhook işleme, Email gönderme).

---

## 🚀 Realtime & Storage

- **Realtime**: Veritabanı değişikliklerini (Insert/Update/Delete) client'a anlık push etme.
- **Storage**: Büyük dosyaları (Images, PDFs) bucketlarda saklama ve CDN üzerinden sunma.

---

## 🔧 Workflow

> **Kaynak:** [Supabase Documentation](https://supabase.com/docs) & [Supabase Best Practices](https://supabase.com/docs/guides/database/best-practices)

### Aşama 1: Schema Design & RLS
- [ ] **Modeling**: Tabloları oluştur, veri tiplerini seç ve `UUID` kullanımına dikkat et.
- [ ] **Enable RLS**: Tüm tablolarda `Row Level Security`'yi aktif et (Default Deny).
- [ ] **Policies**: `auth.uid()` fonksiyonunu kullanarak CRUD operasyonları için güvenlik politikalarını yaz.

### Aşama 2: SDK & Auth Integration
- [ ] **Client Setup**: `@supabase/supabase-js` ile client bağlantısını kur (Keyleri `.env`'den al).
- [ ] **User Auth**: Kayıt (Sign up) ve Giriş (Sign in) akışlarını kur, `Session` yönetimini kontrol et.
- [ ] **Triggers**: Yeni kullanıcı kaydolduğunda profil tablosu oluşturmak için `Postgres Triggers` kullan.

### Aşama 3: Edge Functions & Storage
- [ ] **Secret Management**: API keyleri Supabase Dashboard üzerinden "Secrets" olarak güvenle sakla.
- [ ] **Function Deploy**: `supabase functions deploy` ile logic'leri edge'e taşı.
- [ ] **Bucket Security**: Storage bucket'ları için okuma/yazma politikalarını (RLS) tanımla.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `service_role` key'i asla client-side (frontend) kodda kullanıldı mı? |
| 2 | RLS politikaları "Public" olarak mı ayarlandı? (Risk!). |
| 3 | Veritabanı index'leri (özellikle RLS'de kullanılan kolonlar için) oluşturuldu mu? |

---

*Supabase Patterns v1.1 - Enhanced*
