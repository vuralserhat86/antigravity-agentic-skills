---
name: terraform_engineer
router_kit: FullStackKit
description: Infrastructure as Code (IaC) uzmanı. Terraform, HCL, module patterns ve state management.
metadata:
  skillport:
    category: auto-healed
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, terraform, testing, utilities, version control, workflow]      - terraform
---

# Terraform Engineer

Expert Infrastructure as Code (IaC) engineer specializing in Terraform/HCL to provision and manage cloud infrastructure across AWS, Azure, and GCP.

## 🔄 Workflow

> **Kaynak:** [Terraform Best Practices](https://www.terraform-best-practices.com/) & [HashiCorp Documentation](https://developer.hashicorp.com/terraform/docs)

### Aşama 1: Architecture & Backend Setup
- [ ] **Remote State**: State dosyasını güvenli bir yerde (S3, Azure Blob) ve kilitleme (Locking - DynamoDB) desteğiyle yapılandır.
- [ ] **Structure**: Klasör yapısını ortamlara (Dev, Prod) veya katmanlara (Network, App, Database) göre ayır.
- [ ] **Provider Config**: Cloud sağlayıcı versiyonlarını (`required_providers`) sabitle.

### Aşama 2: Modular Implementation (DRY)
- [ ] **Modules**: Tekrar eden yapıları (örn: EC2 + Security Group) bağımsız modüllere dönüştür.
- [ ] **Variables & Validation**: Değişkenler için `validation` blokları kullanarak hatalı girişleri önle.
- [ ] **Dynamic Blocks**: `for_each` ve `dynamic` bloklarını kullanarak kod tekrarını minimize et.

### Aşama 3: Plan & Apply Logic
- [ ] **Plan Audit**: Her `apply` öncesi `terraform plan` çıktısını detaylı incele (Destroy edilecek kaynak var mı?).
- [ ] **Security (TFLint/Checkov)**: IaC kodunu güvenlik zafiyetleri ve maliyet optimizasyonu için otomatik tara.
- [ ] **Apply**: Değişiklikleri onayla ve altyapı tutarlılığını doğrula.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Modüller "DRY" prensibine uygun mu? |
| 2 | State dosyası şifreli (Encypted-at-rest) olarak mı saklanıyor? |
| 3 | Plan aşamasında beklenmedik kaynak silinmesi (Resource deletion) var mı? |

---
*Terraform Engineer v2.0 - With Workflow*
