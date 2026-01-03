---
name: secops_core
router_kit: DevOpsKit
description: Security operations (SecOps) temel prensipleri, zafiyet tarama, IAM ve cloud security.
metadata:
  skillport:
    category: operations
    tags: [architecture, automation, best practices, cleanup, coaching, compliance, development, documentation, efficiency, iam, integrations, maintainability, metadata, network security, open-source, optimization, performance, quality assurance, scalability, secops, secops core_1, security, security operations, software engineering, standards, testing, version control, vulnerability scanning, web development, workflow]      - security
---

# 🛡️ SecOps Core

> Güvenlik operasyonları, zafiyet yönetimi ve güvenli altyapı rehberi.

---

## 🧱 Temel Prensipler

### 1. Zero Trust (Sıfır Güven)
"Asla güvenme, her zaman doğrula." - Cihazın veya kullanıcının ağ içinde olması ona otomatik güven sağlamaz.

### 2. Least Privilege (En Az Yetki)
Kullanıcılara veya servislere sadece işlerini yapmaları için gereken minimum yetkiyi ver.

### 3. Defense in Depth
Tek bir güvenlik katmanına güvenme; network, host, uygulama ve veri seviyesinde çok katmanlı koruma sağla.

---

## 🛠️ SecOps Araç Seti

| Kategori | Araçlar |
|----------|---------|
| **Vulnerability Scanning** | Trivy, Nessus, Snyk |
| **IAM (Access)** | AWS IAM, Okta, Clerk |
| **Logging & Monitoring** | ELK Stack, Splunk, Datadog Security |
| **Secrets Management** | HashiCorp Vault, AWS Secrets Manager |

---

## 🔧 Workflow

> **Kaynak:** [CIS Benchmarks](https://www.cisecurity.org/benchmark) & [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)

### Aşama 1: Hardening & Vulnerability Scan
- [ ] **Asset Discovery**: Tüm altyapı bileşenlerini (Server, Containers, S3 Buckets) envantere al.
- [ ] **Static Scanning**: Kod depolarında (SAST) ve Docker imajlarında (Trivy) zafiyet taraması yap.
- [ ] **Secrets Audit**: Kod içinde asla açıkta şifre veya API key (Hardcoded secrets) bulunmadığından emin ol (`gitleaks`).

### Aşama 2: Identity & Access Management (IAM)
- [ ] **MFA**: Tüm kritik erişimler için Çok Faktörlü Doğrulama (MFA) zorunlu tut.
- [ ] **Role Review**: RBAC (Role-Based Access Control) kurallarını periyodik olarak denetle ve kullanılmayan yetkileri al.
- [ ] **Least Privilege**: Servis hesaplarının (`Service Accounts`) sadece ilgili depolara erişimi olduğunu doğrula.

### Aşama 3: Incident Response & Logging
- [ ] **Centralized Logging**: Tüm güvenlik loglarını merkezi bir SIEM sistemine aktar.
- [ ] **Alerting**: "Anormal login" veya "Döküman silme" gibi kritik olaylar için anlık alarmlar kur.
- [ ] **Patch Management**: Kritik zafiyet yamalarını (Patches) CI/CD pipeline'ı üzerinden otomatize bir şekilde uygula.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `public` erişime açık olan S3/Storage bucket'ları var mı? (Gerekmedikçe kapalı olmalı). |
| 2 | SSH şifreleri yerine Key-based authentication kullanılıyor mu? |
| 3 | Firewall (Security Groups) kuralları "Default Deny" (Varsayılan reddet) prensibiyle mi kuruldu? |

---

*SecOps Core v1.1 - Enhanced*
