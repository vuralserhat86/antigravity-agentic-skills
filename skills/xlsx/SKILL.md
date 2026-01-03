---
name: xlsx
router_kit: FullStackKit
description: Excel dosyalarını okuma, yazma, formülleme ve stil verme (SheetJS, ExcelJS).
metadata:
  skillport:
    category: automation
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, xlsx, version control, workflow]      - excel
---

# 📊 Excel Automation

> Programatik olarak Excel (XLSX/CSV) dökümanları oluşturma ve veri işleme.

---

*Excel Automation v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [SheetJS (xlsx) Documentation](https://docs.sheetjs.com/) & [ExcelJS Github](https://github.com/exceljs/exceljs)

### Aşama 1: Library Selection & Setup
- [ ] **SheetJS**: Basit okuma/yazma ve yüksek performans için tercih et.
- [ ] **ExcelJS**: Karmaşık stil verme, imaj ekleme ve formülleme işlemleri için tercih et.

### Aşama 2: Data Transformation
- [ ] **JSON to Sheet**: Veriyi Excel formatına (Worksheet) dönüştürmeden önce temizle ve normalize et.
- [ ] **Headers & Widths**: Sütun başlıklarını isimlendir ve içerik genişliğine göre (Auto-width) ayarla.
- [ ] **Formatting**: Para birimi, tarih ve sayı formatlarını hücre seviyesinde tanımla.

### Aşama 3: advanced Operations
- [ ] **Styles**: Hücre renkleri, kenarlıklar ve font stillerini (ExcelJS ile) belirle.
- [ ] **Merges**: Başlıklar veya rapor düzeni için hücreleri birleştir.
- [ ] **Formulas**: Dinamik hesaplamalar için hücrelere Excel formülleri ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Türkçe karakterler ve encoding (UTF-8) doğru mu? |
| 2 | Dosya boyutu büyükse "Streaming" (ExcelJS streaming writer) kullanıldı mı? |
| 3 | Tarih formatları farklı Excel sürümlerinde tutarlı mı? |
