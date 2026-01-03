---
name: firestore_patterns
router_kit: FullStackKit
description: Firestore NoSQL database design, indexing ve query optimization patterns.
metadata:
  skillport:
    category: database
    tags: [architecture, automation, backend, best practices, cloud computing, database design, development, firebase, firestore, firestore patterns, indexing, optimization, performance, real-time, scalability, software engineering, testing, utilities, workflow]      - database-design
---

# 🔥 Firestore Patterns

> Firestore (NoSQL) veritabanı tasarım ve optimizasyon patterns.

---

## 🏗️ Data Modeling

### 1. Root Collections vs Subcollections
- **Root**: Global veriler (users, products).
- **Subcollections**: Ebeveyne sıkı bağlı veriler (users/{id}/orders).

### 2. Denormalization (Read Optimization)
NoSQL'de join olmadığı için veriyi kopyalamak (denormalization) yaygındır.

```typescript
// Order dökümanında kullanıcı adını tutmak
{
  userId: "user123",
  userName: "Ahmet Yılmaz", // Denormalized
  total: 500,
  status: "pending"
}
```

---

## 🔍 querying & Indexing

| Index Tipi | Kullanım |
|------------|----------|
| **Single Field** | Basit sorgular (where id == x) |
| **Composite Index** | Çoklu filtreler (where status == x AND price > y) |
| **TTL Index** | Otomatik silinecek dökümanlar |

---

## 🛡️ Security Rules

```javascript
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

---

## 🎯 Best Practices

- **Avoid frequent writes** to same document (max 1 write/sec).
- **Use batched writes** for multi-document updates.
- **Use transactions** for atomic operations.
- **Handle offline data** with Firestore persistence.

---

*Firestore Patterns v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Firebase Documentation - Firestore Data Modeling](https://firebase.google.com/docs/firestore/manage-data/data-modeling)

### Aşama 1: Schema Design
- [ ] **Clustering**: İlişkili verileri subcollection'lara mı yoksa ayrı root collection'lara mı koyacağına karar ver.
- [ ] **Denormalization**: Read performansını artırmak için hangi verileri kopyalaman gerektiğini belirle.
- [ ] **IDs**: Auto-generated ID'ler kullan (Sıralı ID'ler hotspot yaratır).

### Aşama 2: Query Setup
- [ ] **Indexes**: Sorgularında kullandığın compound filtreler için `index.json` oluştur.
- [ ] **Pagination**: `startAfter()` kullanarak cursor-based pagination uygula.
- [ ] **Realtime**: `onSnapshot()` ile anlık güncellemeleri dinle.

### Aşama 3: Performance & Cost
- [ ] **Reads**: Gerekmedikçe `getDocs()` kullanma, limitleri dar tut.
- [ ] **Writes**: Çoklu döküman güncellemeleri için `writeBatch()` kullan.
- [ ] **Security**: `firestore.rules` dosyasında yetkisiz erişimleri kapat.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `firestore.rules` dosyası "allow read, write: if true" şeklinde mi? (Öyleyse HATA) |
| 2 | Bir döküman 1MB limitini aşıyor mu? |
| 3 | Composite indexler Firestore konsolunda tanımlandı mı? |
