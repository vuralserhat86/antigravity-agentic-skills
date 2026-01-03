---
name: better_auth
router_kit: SecurityKit
description: Clerk modern authentication, WebAuthn, passkeys ve social auth entegrasyonu rehberi.
metadata:
  skillport:
    category: cybersecurity
    tags: [accessibility, api integration, backend, better auth, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - access-control
---

# Better Auth Skill

Better Auth is comprehensive, framework-agnostic authentication/authorization framework for TypeScript with built-in email/password, social OAuth, and powerful plugin ecosystem for advanced features.

---

*Better Auth v2.1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Better Auth Docs](https://www.better-auth.com/docs)

### Aşama 1: Setup & Config
- [ ] **Install**: Paketi kur ve `.env` (Source of Truth) ayarla.
- [ ] **Client/Server**: `auth.ts` (Server) ve `auth-client.ts` (Client) dosyalarını oluştur.
- [ ] **Database**: Şemayı oluştur ve migrate et.

### Aşama 2: Method Implementation
- [ ] **Strategy**: Email/Pass, OAuth veya Magic Link seçimi.
- [ ] **UI Integration**: Frontend formlarını `authClient` metodlarına bağla.
- [ ] **Protection**: Middleware veya Hook ile sayfaları koru.

### Aşama 3: Verification
- [ ] **Flow Test**: Sign-up -> Sign-in -> Session Check -> Sign-out.
- [ ] **Error Handling**: Yanlış şifre/email durumlarını test et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `BETTER_AUTH_SECRET` ve `BETTER_AUTH_URL` tanımlı |
| 2 | Veritabanında `user` ve `session` tabloları oluştu |
| 3 | Middleware korumalı sayfalara limitsiz erişimi engelliyor |
