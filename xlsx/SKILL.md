---
name: xlsx
router_kit: ManagementKit
description: Excel (.xlsx) formülleri, veri analizi, otomasyon ve Pivot tablolar uzmanlığı.
metadata:
  skillport:
    category: operations
    tags: [automation, best practices, business, cleanup, collaboration, compliance, data analysis, development, documentation, efficiency, excel, formulas, maintainability, metadata, open-source, optimization, performance, pivot tables, productivity, quality assurance, scalability, software engineering, standards, testing, version control, web development, workflow, xlsx_1]      - spreadsheet-mastery
---

# 📊 Excel (XLSX) Mastery

> İleri seviye Excel formülleri, veri analizi ve otomasyon rehberi.

---

## 🧪 Advanced Formulas

- **XLOOKUP**: Esnek veri arama ve eşleme.
- **IFS / SWITCH**: Çoklu koşul yönetimi.
- **UNIQUE / FILTER / SORT**: Dinamik dizi (Dynamic Array) formülleri.
- **LET**: Formül içinde değişken tanımlayarak performansı artırma.

---

## 📈 Veri Analizi

### Pivot Tables
- Büyük veri setlerini saniyeler içinde özetleme.
- Slicer'lar ile interaktif dashboard hazırlama.

### Power Query
- Harici kaynaklardan (CSV, Web, SQL) veri çekme, temizleme (Text-to-columns, Unpivot) ve yükleme.

---

## 🔧 Workflow

> **Kaynak:** [Microsoft Excel Support](https://support.microsoft.com/en-us/excel) & [Exceljet Formula Guide](https://exceljet.net/)

### Aşama 1: Structure & Cleaning
- [ ] **Raw Data**: Veriyi "Table" (Ctrl+T) formatına çevir. Dinamik aralıklar kullan.
- [ ] **Cleaning**: Duplicate'leri temizle, tarih ve sayı formatlarını standartlaştır.
- [ ] **Data Validation**: Hatalı girişi önlemek için Drop-down listeler ve input kuralları koy.

### Aşama 2: Analysis & Formulas
- [ ] **Logic**: İstemi karşılayacak en verimli formül kombinasyonunu kur (XLOOKUP > VLOOKUP).
- [ ] **Audit**: `Trace Precedents/Dependents` ile formül hatalarını ve döngüsel başvuruları ayıkla.
- [ ] **Named Ranges**: Formülleri okunaklı kılmak için hücre aralıklarına isim ver.

### Aşama 3: Presentation & Security
- [ ] **Conditional Formatting**: Kritik eşik değerlerini (Target vs Actual) görselleştir.
- [ ] **Protection**: Formülleri kilitle ve sayfayı şifreleyerek sadece input alanlarını açık bırak.
- [ ] **Export**: Sonuçları profesyonel bir PDF veya Dashboard sayfası olarak hazırla.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Formül sonuçları Manuel olarak 2-3 satırda doğrulandı mı? |
| 2 | Dosya boyutu gereksiz şişti mi? (Clear formatting). |
| 3 | Gizli veriler (Hidden sheets) dökümanda kaldı mı? |

---

*XLSX Mastery v1.1 - Enhanced*
