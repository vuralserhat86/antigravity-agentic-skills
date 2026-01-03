---
name: deps_npm
router_kit: FullStackKit
description: NPM/Yarn bağımlılık yönetimi, package.json best practices ve security audit.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, deps npm, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - package-json
---

# 📦 Dependencies (NPM/Yarn)

> Güvenli ve verimli bağımlılık yönetimi.

---

*Dependencies (NPM) v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [NPM Security Best Practices](https://docs.npmjs.com/specifying-dependencies-and-devdependencies-in-a-package-json-file)

### Aşama 1: Selection & Installation
- [ ] **Select**: Paket popülerliğini ve bakım durumunu (npmtrends.com) kontrol et.
- [ ] **Install**: DevDependencies vs. Dependencies ayrımını doğru yap.
- [ ] **Lockfile**: `package-lock.json` veya `yarn.lock` dosyasını mutlaka commit et.

### Aşama 2: Maintenance & Audit
- [ ] **Update**: `npm outdated` ile güncel olmayan paketleri bul.
- [ ] **Security**: `npm audit` komutu ile güvenlik açıklarını tara.
- [ ] **Pruning**: Kullanılmayan (`depcheck`) paketleri kaldır.

### Aşama 3: Versioning Strategy
- [ ] **Semantic**: `^` veya `~` kullanımına karar ver (Strict vs. Range).

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Gereksiz (Overhead) paketler var mı? |
| 2 | Güvenlik açığı olan paketler ignore edildi mi? |
| 3 | Lockfile ve package.json senkronize mi? |
