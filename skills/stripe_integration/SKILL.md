---
name: stripe_integration
router_kit: FullStackKit
description: Stripe Checkout, abonelikler, webhooks ve ödeme güvenliği (PCI Compliance).
metadata:
  skillport:
    category: business
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, payment integration, performance optimization, responsive design, seo, state management, stripe integration, testing, typescript, ui/ux, web development]      - payments
---

# 💳 Stripe Integration

> Güvenli ödeme sistemleri ve abonelik yönetimi entegrasyonu.

---

*Stripe Integration v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Stripe Integration Builder](https://stripe.com/docs/checkout/quickstart) & [Stripe Webhook Best Practices](https://stripe.com/docs/webhooks/best-practices)

### Aşama 1: Product & Checkout Setup
- [ ] **Product Definition**: Dashboard veya API üzerinden Product ve Price objelerini tanımla.
- [ ] **Checkout Integration**: `Stripe Checkout` (Hosted) veya `Payment Element` (Custom) arasından ihtiyaca uygun olanı kur.
- [ ] **SCA Compliance**: European (3D Secure) ödemeler için gerekli SCA (Strong Customer Authentication) adımlarını ekle.

### Aşama 2: Webhook & Background Processing
- [ ] **Webhook Listener**: Ödeme başarısı (`payment_intent.succeeded`) veya abonelik durumu değişiklikleri için güvenli bir webhook endpoint'i kur.
- [ ] **Signature Verification**: Gelen isteklerin Stripe'tan geldiğini `endpoint secret` ile doğrula.
- [ ] **Idempotency**: Aynı webhook isteğinin birden fazla işlenmesini önlemek için `Stripe-Idempotency-Key` veya veritabanı kontrolü kullan.

### Aşama 3: Exception Handling & Fulfillment
- [ ] **Payment Failures**: Ödeme başarısızlıklarını kullanıcıya bildir ve süreci (örn: Sepeti koru) yönet.
- [ ] **Order Fulfillment**: Ödeme onaylandığında siparişi tamamla, veritabanını güncelle ve e-posta gönder.
- [ ] **Customer Portal**: Kullanıcıların aboneliklerini yönetebileceği "Customer Portal" linkini entegre et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Ödeme miktarları "Cents" (USD ise 100 = $1.00) bazında mı gönderiliyor? |
| 2 | Webhook endpoint'i production'da HTTPS üzerinden mi çalışıyor? |
| 3 | Test mode'da "4242..." kartı ile tüm akış (Success/Fail/3DS) denendi mi? |
