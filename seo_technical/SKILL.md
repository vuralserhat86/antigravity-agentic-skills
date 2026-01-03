---
name: seo_technical
router_kit: FullStackKit
description: Teknik SEO optimizasyonu, Core Web Vitals, semantik HTML ve arama motoru görünürlüğü.
metadata:
  skillport:
    category: growth
    tags: [accessibility, architecture, automation, best practices, cleanup, coaching, coding, collaboration, compliance, core web vitals, development, documentation, efficiency, hhead-tags, integrations, maintainability, metadata, open-source, optimization, performance, quality assurance, scalability, search engine optimization, semantic html, seo, seo technical_1, software engineering, standards, technical seo, testing, version control, web development, workflow]      - growth-engineering
---

# 🔍 Technical SEO

> Arama motoru örümceklerinin dökümanı daha iyi anlaması ve sıralama optimizasyonu.

---

## 🧱 On-Page Architecture

### 1. Semantic HTML
- `<h1>` (Sadece bir adet)
- `<h2>`, `<h3>` (Hiyerarşik yapı)
- `<nav>`, `<article>`, `<footer>` gibi yapısal tagler.

### 2. Meta Tags (SEO Essentials)
```html
<title>Proje Adı | Anahtar Kelime</title>
<meta name="description" content="Kullanıcıyı tıklamaya çeken, max 160 karakterlik özet.">
<link rel="canonical" href="https://example.com/page">
```

### 3. Open Graph (Social SEO)
```html
<meta property="og:title" content="...">
<meta property="og:image" content="/og-image.jpg">
```

---

## ⚡ Core Web Vitals

| Metrik | Anlamı | Hedef Skoru |
|--------|--------|-------------|
| **LCP** | Largest Contentful Paint (Görsel Yükleme) | < 2.5s |
| **FID** | First Input Delay (İnteraksiyon Gecikmesi) | < 100ms |
| **CLS** | Cumulative Layout Shift (Kayma Oranı) | < 0.1 |

---

## 🔧 Workflow

> **Kaynak:** [Google Search Central - SEO Content Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) & [Ahrefs Technical SEO Checklist](https://ahrefs.com/blog/technical-seo-checklist/)

### Aşama 1: Structure & Accessibility
- [ ] **Crawlability**: `robots.txt` ve `sitemap.xml` dosyalarının doğruluğunu kontrol et.
- [ ] **Hierarchy**: Başlık yapısının (H1 -> H6) mantıksal sırayla kullanıldığından emin ol.
- [ ] **Alt-Tags**: Tüm görsellere arama motorunun içeriği anlamasını sağlayacak `alt` açıklamalarını ekle.

### Aşama 2: Performance & Indexing
- [ ] **Lighthouse Audit**: Sayfayı "Lighthouse" ile tarayarak SEO ve Performance skorlarını 90+ seviyesine çıkar.
- [ ] **Schema.org**: Yapılandırılmış veri (`JSON-LD`) kullanarak Rich Snippets (Ürün, SSS, Event) desteği ekle.
- [ ] **Responsive**: Sayfanın mobil uyumluluğunu (Mobile-friendly test) doğrula.

### Aşama 3: Verification & Monitoring
- [ ] **Broken Links**: 404 sayfalarını tespit et ve 301 yönlendirmesi veya link düzeltmesi yap.
- [ ] **Lazy Loading**: Ekran dışındaki (Off-screen) içerikleri ve resimleri `loading="lazy"` ile yükle.
- [ ] **Verification**: Google Search Console üzerinden mülkiyet doğrulamasını yap ve crawl hatalarını izle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Birden fazla H1 kullanımı var mı? (Hatalı). |
| 2 | Sayfanın canonical tag'i kendine mi bakıyor? |
| 3 | Core Web Vitals metrikleri "Green" (Yeşil) seviyede mi? |

---

*Technical SEO v1.1 - Enhanced*
