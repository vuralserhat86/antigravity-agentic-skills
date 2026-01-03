---
name: docker_optimization
router_kit: DevOpsKit
description: Docker image size reduction, multi-stage builds ve caching stratejileri.
metadata:
  skillport:
    category: operations
    tags: [architecture, automation, best practices, cleanup, containerization, deployment, devops, docker, docker optimization, infrastructure, lifecycle, microservices, optimization, orchestration, performance, scalability, software engineering, virtualization, workflow]      - kubernetes
---

# 🐳 Docker Optimization

> Docker imaj optimizasyonu ve best practices.

---

## 🏗️ Multi-Stage Build

```dockerfile
# Stage 1: Build
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Runtime
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY package*.json ./
EXPOSE 3000
CMD ["npm", "start"]
```

---

## 📏 Image Size Reduction

| Teknik | Fayda |
|--------|-------|
| **Alpine Linux** | ~100MB tasarruf |
| **.dockerignore** | Build context küçülür |
| **Layer concatenation** | Daha az katman |
| **Multi-stage** | Build araçları atılır |

---

## 🔒 Security Best Practices

- **Non-root user**: `USER node`
- **Minimal base images**: `distroless` or `alpine`
- **Scan images**: `docker scan`
- **Avoid secrets**: Don't use `ENV` for secrets.

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

---
*Docker Optimization v1.2 - Verified*
