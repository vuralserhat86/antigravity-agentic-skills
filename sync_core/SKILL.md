---
name: sync_core
router_kit: DevOpsKit
description: Veri senkronizasyonu, state syncing, conflict resolution ve realtime engine yönetimi.
metadata:
  skillport:
    category: engineering
    tags: [architecture, automation, best practices, cleanup, coaching, collaboration, conflict resolution, data synchronization, development, documentation, efficiency, integrations, maintainability, metadata, open-source, optimization, performance, quality assurance, realtime, scalability, software engineering, standards, state sync, sync core_1, testing, version control, web development, workflow]      - connectivity
---

# 🔄 Sync Core

> Çoklu istemciler (Clients) ve sunucular arası veri senkronizasyonu ve tutarlılık rehberi.

---

## 🏗️ Sync Strategies

### 1. Optimistic Updates
İşlemi önce client'da yap, sonra server'a gönder. Hata alırsan geri al (Rollback).
- **Avantaj**: Hızlı UX.
- **Dezavantaj**: Conflict riski.

### 2. Delta Sync (Incremental)
Tüm veriyi değil, sadece değişen (Diff) kısımları gönder.
- **Mekanizma**: `updated_at` timestamp veya `sequence_id` kullanımı.

### 3. Conflict Resolution
Çelişen verilerde kimin kazanacağına karar verme:
- **LWW (Last Write Wins)**: Zaman mührü en yeni olan kazanır.
- **Manual**: Kullanıcıya sor.
- **Merge**: Verileri birleştir (Örn: JSON patch).

---

## 🛠️ Implementation Patterns

### CRDTs (Conflict-free Replicated Data Types)
Matematiksel olarak çelişki oluşturmayan veri yapıları (Örn: Yjs, Automerge).

### WebSockets & SSE
Sunucudan client'a anlık veri push etme.

---

## 🔧 Workflow

> **Kaynak:** [Designing Data-Intensive Applications (Martin Kleppmann)](https://dataintensive.net/) & [Yjs Documentation](https://docs.yjs.dev/)

### Aşama 1: Architecture & Model Selection
- [ ] **Consistency Model**: "Eventual Consistency" mi yoksa "Strong Consistency" mi gerektiğini belirle.
- [ ] **Audit Trail**: Her değişikliği merkezi bir log (Oplog) veya versiyon numarasıyla takip et.
- [ ] **Storage Strategy**: Lokal state (IndexedDB/SQLite) ile sunucu state'i arasındaki bağıntıyı kur.

### Aşama 2: Delta Engine & Conflict Logic
- [ ] **Diff Creation**: Sadece değişen kolonları/objeleri paketle (Payload reduction).
- [ ] **Timestamp/Vector Clocks**: Değişikliklerin sırasını korumak için zaman mühürleri veya vektör saatleri kullan.
- [ ] **Resolution Rules**: Çatışma anında otomatik uygulanacak "İş Kuralları"nı (örn: En yüksek tutar kazanır) kodla.

### Aşama 3: Verification & Network Resilience
- [ ] **Offline Support**: İnternet koptuğunda verileri kuyruğa (Queue) al ve tekrar bağlandığında "Replay" yap.
- [ ] **Reconciliation**: Periyodik olarak (örn: sayfa yenilendiğinde) tam veri kontrolü (Full sync) yaparak tutarlılığı teyit et.
- [ ] **Stress Testing**: Aynı anda 100 kullanıcının aynı alanı değiştirmesi senaryosunu test et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | "Race conditions" (Yarış durumları) için mutex veya locking kullanıldı mı? |
| 2 | Veri boyutu büyüdükçe sync süresi doğrusal mı artıyor? (Logaritmik olmalı). |
| 3 | Sync hataları kullanıcıya (veya sisteme) raporlanıyor mu? |

---

*Sync Core v1.1 - Enhanced*
