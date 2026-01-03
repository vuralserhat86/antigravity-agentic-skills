---
name: git_workflow
router_kit: ManagementKit
description: Professional Git workflow, branching strategies ve conventional commits.
metadata:
  skillport:
    category: operations
    tags: [architecture, automation, best practices, branching, clean code, coding, collaboration, compliance, debugging, deployment, development, devops, efficiency, git, git workflow, GitHub CLI, optimization, productivity, programming, quality assurance, software engineering, standards, testing, version control, workflow]      - code-review
---

# 🌿 Git Workflow

> Professional Git workflow ve collaboration standartları.

---

## 🏗️ Branching Strategy

| Branch | Amaç |
|--------|------|
| `main` | Production (Her zaman stabil) |
| `develop` | Integration (Yeni özelliklerin toplandığı yer) |
| `feature/*` | Yeni özellik geliştirme |
| `fix/*` | Bug fix |
| `hotfix/*` | Acil production yamaları |

---

## 📜 Conventional Commits

Format: `<type>(<scope>): <description>`

- `feat`: Yeni bir özellik
- `fix`: Bug düzeltmesi
- `docs`: Dokümantasyon değişikliği
- `style`: Kod formatı değişikliği (boşluk, virgül vb)
- `refactor`: Ne özellik ekleyen ne de bug düzelten kod değişikliği
- `test`: Test ekleme veya mevcut testleri düzeltme
- `chore`: Build süreci veya yardımcı araç değişiklikleri

---

## 🔄 PR Workflow

1. **Pull**: En güncel `develop` branch'ini çek.
2. **Branch**: Yeni bir feature branch oluştur.
3. **Commit**: Küçük, atomik ve conventional commit'ler yap.
4. **Push**: Branch'i remote'a push et.
5. **PR**: Bir Pull Request aç ve ekip arkadaşlarını review için ata.
6. **Merge**: Onay sonrası `squash and merge` ile birleştir.

---

*Git Workflow v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Conventional Commits](https://www.conventionalcommits.org/) & [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)

### Aşama 1: Branching & Commits
- [ ] **Naming**: Branch ismini `type/issue-id-short-description` (örn: `feat/12-user-login`) formatında aç.
- [ ] **Atomic**: Her commit tek bir mantıksal değişikliği temsil etsin.
- [ ] **Conventional**: Commit mesajlarını standartlara göre yaz.

### Aşama 2: Peer Review (PR)
- [ ] **Description**: PR açıklamasında "ne yapıldı?", "nasıl test edilir?" ve "ilgili issue" bilgilerini ver.
- [ ] **Self-Review**: PR'ı başkasına atmadan önce kendin kodunu diff üzerinden gözden geçir.
- [ ] **Feedback**: Gelen yorumları hızlıca cevapla ve gerekli düzeltmeleri yap.

### Aşama 3: Cleanup
- [ ] **Merge**: Merge sonrası lokal ve remote branch'leri sil.
- [ ] **Rebase**: `main` geride kaldıysa `git rebase main` ile çelişkileri (conflict) çöz.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Commit mesajı 50 karakterden kısa ve emir kipiyle (Imperative) başlıyor mu? |
| 2 | PR'da "Work In Progress" (WIP) etiketi var mı? |
| 3 | Merge edilmeden önce tüm CI/CD testleri geçti mi? |
