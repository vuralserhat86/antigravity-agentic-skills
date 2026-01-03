---
name: pdf
router_kit: FullStackKit
description: PDF oluşturma, okuma, form doldurma ve imzalama işlemleri (PDFKit, Puppeteer).
metadata:
  skillport:
    category: automation
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, pdf, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - documents
---

# 📄 PDF Automation

> Programatik olarak PDF dökümanları oluşturma ve işleme.

---

*PDF Automation v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Puppeteer PDF Generation Guide](https://pptr.dev/api/playwright.page.pdf) & [pdf-lib Docs](https://pdf-lib.js.org/)

### Aşama 1: Tool Selection
- [ ] **HTML-to-PDF**: Puppeteer veya Playwright (En esnek CSS desteği).
- [ ] **Native PDF**: PDFKit veya pdf-lib (Yüksek performans, düşük kaynak).

### Aşama 2: Layout Design
- [ ] **CSS**: Yazıcı (Print) CSS kurallarını `@media print` ile tanımla.
- [ ] **Fonts**: PDF içine gömülecek fontları (subsetting) hazırla.
- [ ] **Header/Footer**: Sayfa numaraları ve tekrarlayan başlıkları ayarla.

### Aşama 3: Processing & Security
- [ ] **Merge/Split**: Birden fazla dosyayı birleştir veya sayfaları ayır.
- [ ] **Forms**: PDF form alanlarını (AcroForms) doldur.
- [ ] **Encryption**: Şifreleme (Password protection) ve izinleri (Print only vb.) ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Türkçe karakterler düzgün görünüyor mu (Encoding)? |
| 2 | Resimler yüksek çözünürlüklü (DPI) mi? |
| 3 | Sayfa sonu (Page break) mantığı tabloları bozuyor mu? |
