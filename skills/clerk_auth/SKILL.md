---
name: clerk_auth
router_kit: SecurityKit
description: Clerk modern authentication, WebAuthn, passkeys ve social auth entegrasyonu rehberi.
metadata:
  skillport:
    category: authentication
    tags: [accessibility, api integration, backend, browser apis, clerk auth, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - webauthn
---

# 🔐 Clerk Auth

> Clerk modern authentication rehberi.

---

*Clerk Auth v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Clerk Documentation](https://clerk.com/docs)

### Aşama 1: Integration
- [ ] **Install**: `@clerk/nextjs` paketi ve API Key'ler.
- [ ] **Middleware**: Public/Private rotaları `clerkMiddleware` ile ayır.
- [ ] **Provider**: Root layout'u `ClerkProvider` ile sarmala.

### Aşama 2: UX & Components
- [ ] **Header**: `SignedIn` / `SignedOut` şartlı render yapısı kur.
- [ ] **Profile**: `UserButton` veya `UserProfile` bileşenini ekle.
- [ ] **Custom Flow**: Gerekirse Custom Sign-in sayfası yap.

### Aşama 3: Server Logic
- [ ] **Protect**: API rotalarında `auth().userId` kontrolü yap.
- [ ] **Data**: `currentUser()` ile kullanıcı verisine eriş.
- [ ] **Sync**: Webhook kullanarak kullanıcıyı kendi veritabanınla eşle (Opsiyonel).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Middleware statik dosyaları (image, css) engellemiyor |
| 2 | Sign-out sonrası login sayfasına yönlendiriyor |
| 3 | API request'leri tokensiz atılınca 401 dönüyor |
