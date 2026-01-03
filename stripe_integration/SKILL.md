---
name: stripe_integration
router_kit: FullStackKit
description: Stripe API ödeme entegrasyonu, subscription yönetimi, elements ve webhook handling.
metadata:
  skillport:
    category: development
    tags: [architecture, automation, best practices, cleanup, coaching, compliance, development, documentation, efficiency, financial services, integrations, maintainability, metadata, open-source, optimization, payment gateway, performance, quality assurance, scalability, software engineering, standards, stripe, stripe integration_1, testing, versions control, web development, workflow]      - fintech
---

# 💳 Stripe Integration

> Stripe API ile güvenli ödeme, abonelik ve finansal işlemler rehberi.

---

## 🚀 Entegrasyon Modelleri

### 1. Stripe Checkout (Pre-built)
Stripe tarafından barındırılan hazır ödeme sayfası. Hızlı ve güvenli.

### 2. Stripe Elements (Custom UI)
Kendi siten içine gömülen, tamamen özelleştirilebilir ama PCI uyumlu UI bileşenleri.

### 3. Payment Intents API
Kendi sunucun üzerinden tam kontrol sağlayan, kompleks ödeme akışları için.

---

## 🔒 Security & Webhooks

### Webhook Signature Verification
```javascript
const event = stripe.webhooks.constructEvent(
  req.body,
  sig,
  process.env.STRIPE_WEBHOOK_SECRET
);
```

### Idempotence
Aynı işlemin (Network hatası vb.) iki kez gerçekleşmesini önlemek için `idempotency_key` kullan.

---

## 🔧 Workflow

> **Kaynak:** [Stripe Documentation](https://stripe.com/docs) & [Stripe API Reference](https://stripe.com/docs/api)

### Aşama 1: Provider Setup & Key Management
- [ ] **Account Setup**: Stripe Dashboard üzerinden `Test Keys` ve `Live Keys` ayarlarını yap.
- [ ] **Security**: API anahtarlarını client-side'a (`PK`) ve server-side'a (`SK`) doğru paylaştır. Asla SK'yı tarayıcıya gönderme.
- [ ] **Products**: Ürünleri (Products) ve fiyatları (Prices) Dashboard üzerinden veya API ile tanımla.

### Aşama 2: Payment Flow & Elements
- [ ] **Checkout Session**: Sunucu tarafında bir `checkout session` oluştur ve kullanıcıyı yönlendir.
- [ ] **Elements Integration**: Custom UI kullanılıyorsa `CardElement` veya `PaymentElement` bileşenlerini sayfaya göm.
- [ ] **Error Handling**: Yetersiz bakiye, reddedilen kart gibi durumlar için net kullanıcı geri bildirimleri ekle.

### Aşama 3: Post-Payment & Webhooks
- [ ] **Webhook Endpoint**: `payment_intent.succeeded` ve `checkout.session.completed` olaylarını dinleyen bir endpoint yaz.
- [ ] **Audit Trail**: Her başarılı ödeme sonrası veritabanında sipariş durumunu "Paid" olarak güncelle ve fatura oluştur.
- [ ] **Testing**: `Stripe CLI` (stripe listen) kullanarak lokalde webhook testlerini gerçekleştir.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Webhook endpoint'i imza doğrulaması (Signature check) yapıyor mu? |
| 2 | Kredi kartı verileri sunucu loglarına yazılıyor mu? (Asla yazılmamalı!). |
| 3 | 3D Secure (SCA) gerektiren kartlar için akış test edildi mi? |

---

*Stripe Integration v1.1 - Enhanced*
