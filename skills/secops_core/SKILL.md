---
name: secops_core
router_kit: DevOpsKit
description: Güvenlik odaklı operasyonlar, zaafiyet tarama ve güvenli kod yazım standartları.
metadata:
  skillport:
    category: security
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, secops core, software engineering, standards, testing, utilities, version control, workflow]      - cybersecurity
---

# 🛡️ SecOps Core

> Güvenliği yazılım yaşam döngüsünün (SDLC) her aşamasına entegre etme.

---

*SecOps Core v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [OWASP Top 10](https://owasp.org/www-project-top-ten/) & [SANS Institute - Secure DevOps](https://www.sans.org/white-papers/37292/)

### Aşama 1: Secure Design & Coding
- [ ] **Threat Modeling**: Olası saldırı vektörlerini (Data flow, Trust boundaries) tasarım aşamasında belirle.
- [ ] **Secrets Management**: Şifreleri ve API Key'leri kodda tutma (Vault, AWS Secrets Manager vb. kullan).
- [ ] **SAST**: Statik kod analizi (SonarQube, Snyk) ile zaafiyetleri henüz geliştirme aşamasında yakala.

### Aşama 2: CI/CD Security (DevSecOps)
- [ ] **SCA**: Bağımlılıklardaki (NPM/Python paketleri) bilinen açıkları tara (`npm audit`, `safety`).
- [ ] **DAST**: Uygulama ayağa kalktığında dinamik tarama (OWASP ZAP) yap.
- [ ] **Container Security**: Docker imajlarını (Trivy) zaafiyetlere karşı tara.

### Aşama 3: Monitoring & Response
- [ ] **Logging**: Tüm kritik ve başarısız işlemleri (Login, Admin actions) audit loglarına kaydet.
- [ ] **Alerting**: Şüpheli aktiviteler için anlık uyarı sistemlerini kur.
- [ ] **Incident Plan**: Olası bir sızıntı durumunda yapılacak "Müdahale Planı"nı hazır tut.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | PII (Kişisel veri) şifrelenmiş olarak mı saklanıyor? |
| 2 | En son OWASP Top 10 listesindeki açıklar kontrol edildi mi? |
| 3 | Public endpointler için "Rate Limiting" aktif mi? |
