---
name: form_builder
router_kit: FullStackKit
description: Dynamic form generation, validation ve state management patterns.
metadata:
  skillport:
    category: frontend
    tags: [accessibility, api integration, automation, backend, best practices, browser apis, client-side, components, development, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - tdd-workflow
---

# 📝 Form Builder

> Dinamik form oluşturma, validasyon ve state yönetimi.

---

## 🏗️ Core Architecture

### 1. Schema-Based Forms (Zod/Yup)
Form yapısını ve validasyon kurallarını bir şema ile tanımla.

```typescript
const loginSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8)
});
```

### 2. State Management (React Hook Form)
Performans için uncontrolled component'ler ve `register` pattern'ı kullan.

```tsx
const { register, handleSubmit } = useForm();
```

---

## 🔧 Component types

| Tip | Kullanım |
|-----|----------|
| **Input** | Text, Email, Password |
| **Select** | Dropdown listeler |
| **Checkbox/Radio** | Çoklu/Tekli seçim |
| **Datepicker** | Tarih seçimi |
| **File Upload** | Dosya yükleme |

---

## ✅ Validation Strategies

- **On Blur**: Kullanıcı alandan çıktığında.
- **On Change**: Kullanıcı yazarken (sadece hata düzeltirken önerilir).
- **On Submit**: Form gönderilirken (final check).

---

## 🎯 Best Practices

- **Accessibility**: Her input için `<label>` kullan.
- **Error Feedback**: Hataları net ve inputun hemen altında göster.
- **Loading State**: Form gönderilirken butonları disable et.
- **Multi-step**: Karmaşık formları aşamalara böl (Wizard).

---

*Form Builder v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Nielsen Norman Form Design](https://www.nngroup.com/articles/web-form-design/) & [React Hook Form](https://react-hook-form.com/)

### Aşama 1: Structure & validation
- [ ] **Schema**: Zod/Yup ile validasyon şemasını backend ile uyumlu tanımla.
- [ ] **Labels**: Her input için açık, erişilebilir (`htmlFor`) etiket koy.
- [ ] **Grouping**: İlişkili alanları `<fieldset>` veya görsel gruplarla ayır.

### Aşama 2: User Experience
- [ ] **Defaults**: Akıllı varsayılanlar (ülke, telefon kodu) ekle.
- [ ] **Feedback**: Hataları submit'ten önce (onBlur) veya yazarken göster.
- [ ] **Loading**: Submit sırasında butonu disable et ve spinner göster.

### Aşama 3: Accessibility
- [ ] **Keyboard**: Sadece Tab tuşu ile tüm formu doldurabiliyor musun?
- [ ] **Error Focus**: Hata olduğunda focus ilk hatalı alana gidiyor mu?

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Zorunlu alanlar (*) açıkça belli mi? |
| 2 | Enter tuşuna basınca form submit oluyor mu? |
| 3 | Ekran okuyucu hatayı sesli okuyor mu? |
