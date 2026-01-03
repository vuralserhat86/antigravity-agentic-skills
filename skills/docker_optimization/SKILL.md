---
name: docker_optimization
router_kit: DevOpsKit
description: Docker imaj boyutu optimizasyonu, multi-stage builds ve güvenli container yapılandırması.
metadata:
  skillport:
    category: devops
    tags: [automation, aws, bash scripting, ci/cd, cloud computing, containerization, deployment strategies, devops, docker, docker optimization, gitops, infrastructure, infrastructure as code, kubernetes, linux, logging, microservices, monitoring, orchestration, pipelines, reliability, scalability, security, server management, terraform]      - images
---

# 🐳 Docker Optimization

> Yüksek performanslı ve güvenli Docker yapılandırmaları.

---

*Docker Optimization v1.2 - Verified*

## 🔄 Workflow

> **Kaynak:** [Docker Build Best Practices](https://docs.docker.com/build/building/best-practices/) & [Trivy Docs](https://aquasecurity.github.io/trivy/)

### Aşama 1: Base & Structure
- [ ] **Base Image**: Üretim için `-alpine` veya `-slim` imajını seç (Pin version: `python:3.11.9-slim`).
- [ ] **Layers**: Değişmeyen katmanları (Dependency Install) yukarı taşı, kod kopyalamayı (`COPY . .`) en alta al.
- [ ] **Multi-Stage**: Build araçlarını (`gcc`, `npm`) builder stage'de bırak, runtime stage'e taşıma.

### Aşama 2: Security & Linting
- [ ] **Linter**: Dockerfile'ı `hadolint` ile tara (`hadolint Dockerfile`).
- [ ] **User**: `USER appuser` ile root olmayan kullanıcıya geç.
- [ ] **Secrets**: `ENV` ile secret geçme, secret mount kullan.

### Aşama 3: Performance Check
- [ ] **Context**: `.dockerignore` dosyası `.git`, `node_modules` ve testleri hariç tutuyor mu?
- [ ] **Cache**: `RUN --mount=type=cache` kullanarak paket yöneticisi önbelleğini hızlandır.
- [ ] **Scan**: İmajı `trivy image <name>` ile tarat ve kritik açıkları gider.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | İmaj boyutu builder stage'den %50+ daha küçük mü? |
| 2 | `dive <image>` ile bakıldığında gizli dosya/key kalmış mı? |
| 3 | Container root olmadan çalışabiliyor mu? |
