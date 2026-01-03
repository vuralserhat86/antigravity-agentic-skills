---
name: github_project_automation
router_kit: ManagementKit
description: GitHub Projects, actions ve label automation rehberi.
metadata:
  skillport:
    category: operations
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, development, devops, efficiency, git, GitHub CLI, github project automation, infrastructure, optimization, productivity, programming, project management, quality assurance, software engineering, standards, testing, utilities, version control, workflow]      - git-workflow
---

# 🤖 GitHub Project Automation

> GitHub projelerini ve iş akışlarını otomatikleştirme.

---

## 📊 Project Board setup

- **Todo**: Yeni açılan issue'lar otomatik buraya düşer.
- **In Progress**: Bir branch açıldığında veya PR oluşturulduğunda.
- **Review**: PR açıldığında review için bekleyenler.
- **Done**: PR merge edildiğinde veya issue kapatıldığında.

---

## 🏷️ Labeling System

| Label | Renk | Anlam |
|-------|------|-------|
| `bug` | Kırmızı | Hatalı davranış |
| `feat` | Yeşil | Yeni özellik |
| `docs` | Mavi | Dokümantasyon |
| `high` | Turuncu | Yüksek öncelik |
| `help` | Mor | Yardıma muhtaç |

---

## ⚙️ GitHub Actions (CI/CD)

```yaml
name: Test and Lint
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install
        run: npm install
      - name: Lint
        run: npm run lint
      - name: Test
        run: npm test
```

---

*GitHub Project Automation v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [GitHub Actions Documentation](https://docs.github.com/en/actions) & [GitHub Projects Guide](https://docs.github.com/en/issues/planning-and-tracking-with-projects)

### Aşama 1: Structure & labels
- [ ] **Labels**: Standart etiket setini (`bug`, `feat`, `chore`, `priority`) oluştur.
- [ ] **Milestones**: Roadmap hedeflerini Milestone olarak tanımla.
- [ ] **Board View**: Tabloları (Kanban) ve Timeline (Roadmap) görünümlerini ayarla.

### Aşama 2: Workflow Automation
- [ ] **Issue Templates**: Hata bildirimleri ve özellik talepleri için şablonlar oluştur.
- [ ] **Auto-Move**: Issue state'i değiştiğinde (örn: In Progress) kartın yerini otomatik değiştir.
- [ ] **PR Sync**: Linked issue'ları PR merge edildiğinde otomatik kapat.

### Aşama 3: CI/CD Pipeline
- [ ] **Lint & Test**: Her push sonrası kod kalitesini denetleyen Action kur.
- [ ] **Deploy**: `main` branch'ine yapılan push'larda otomatik deployment tetikle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Label renkleri anlamsal olarak mantıklı (Kırmızı: Hata vb.) mı? |
| 2 | Bir PR açıldığında ilgili testler otomatik başlıyor mu? |
| 3 | Project Board'da sahipsiz (Unassigned) kart var mı? |
