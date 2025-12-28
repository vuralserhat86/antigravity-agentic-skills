---
name: deploy_monitoring
router_kit: DevOpsKit
description: Health checks, metrics, alerting ve rollback stratejileri.
metadata:
  skillport:
    category: operations
    tags: [automation, aws, bash scripting, ci/cd, cloud computing, containerization, deploy monitoring, deployment strategies, devops, docker, gitops, infrastructure, infrastructure as code, kubernetes, linux, logging, microservices, monitoring, orchestration, pipelines, reliability, scalability, security, server management, terraform]      - deploy-cicd
---

# 📊 Deploy Monitoring

> Monitoring, alerting ve rollback stratejileri.

---

## ❤️ Health Checks

```typescript
app.get('/health', (req, res) => {
  res.json({ status: 'healthy', version: process.env.APP_VERSION });
});

app.get('/ready', async (req, res) => {
  await db.$queryRaw`SELECT 1`;
  res.json({ status: 'ready' });
});
```

---

## 📈 Metrics (Prometheus)

```typescript
const httpDuration = new Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests',
  labelNames: ['method', 'route', 'status'],
});
```

---

## 🚨 Alert Rules

```yaml
- alert: HighErrorRate
  expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.05
  for: 5m
  labels:
    severity: critical
```

---

## ⏪ Rollback

```bash
# Kubernetes
kubectl rollout undo deployment/app

# Vercel
vercel rollback
```

---

*Deploy Monitoring v1.0*
