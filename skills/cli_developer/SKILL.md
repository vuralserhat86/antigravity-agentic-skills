---
name: cli_developer
router_kit: FullStackKit
description: Node.js/Python CLI araçları, commander.js, yargs, interactive prompts (inquirer/enquirer). ⚠️ CLI logic yazarken kullan. Git otomasyonu için → git-workflow.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, cli developer, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - interactive-prompts
---

# 💻 CLI Developer

> Modern ve kullanıcı dostu CLI araçları geliştirme.

---

*CLI Developer v1.2 - Verified*

## 🔄 Workflow

> **Kaynak:** [Command Line Interface Guidelines](https://clig.dev/)

### Aşama 1: Project Setup (Architecture)
- [ ] **Binary**: `package.json` içine `"bin": { "my-cli": "./dist/index.js" }` ekle.
- [ ] **Paradigm**: "Subcommand" (git push gibi) veya "Interactive" (y/n soruları) yapısını seç.
- [ ] **Colors**: `chalk` veya `picocolors` ile terminal çıktılarını renklendir.

### Aşama 2: Parameter Handling
- [ ] **Arguments**: `commander` veya `yargs` ile argümanları ve flagleri (`--force`, `-v`) yönet.
- [ ] **Environment**: Gerekirse `.env` desteği veya config dosyası (`~/.my-cli-rc`) ekle.
- [ ] **Progress**: Uzun işlemler için `ora` (spinner) veya `cli-progress` kullan.

### Aşama 3: UX & Exit Codes
- [ ] **Prompts**: `inquirer` veya `enquirer` ile interaktif seçimler yaptır.
- [ ] **Errors**: Hata durumunda anlamlı mesajlar ve doğru Exit Code'lar dön (0: Başarı, 1: Hata).
- [ ] **Help**: `--help` komutu ile tüm komutları listele.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Komut yapısı "tahmin edilebilir" mi? (Intuitive) |
| 2 | `myscript > file.txt` yapınca loglar dosyaya karışıyor mu? (Karışmamalı) |
| 3 | Startup time < 50ms mi? |
