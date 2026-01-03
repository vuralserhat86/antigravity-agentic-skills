---
name: seo_technical
router_kit: FullStackKit
description: Core Web Vitals, Structured Data, Robots.txt ve crawling optimizasyonu.
metadata:
  skillport:
    category: business
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo technical, seo, state management, testing, typescript, ui/ux, web development]      - search-engine-optimization
---

# 🔍 SEO Technical

> Arama motorlarının siteyi kolayca tarayıp anlamasını sağlayan teknik altyapı.

---

*SEO Technical v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Google Search Central - Technical SEO Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) & [Ahrefs Technical SEO Audit](https://ahrefs.com/blog/technical-seo/)

### Aşama 1: Crawlability & Indexing
- [ ] **Robots.txt**: Arama motorlarının hangi sayfaları tarayabileceğini doğru yapılandır.
- [ ] **Sitemap**: Tüm önemli URL'leri içeren `sitemap.xml` dosyasını oluştur ve Search Console'a ilet.
- [ ] **Canonicals**: Dublike içerikleri önlemek için `rel="canonical"` taglerini kontrol et.

### Aşama 2: Page Experience (Core Web Vitals)
- [ ] **LCP/FID/CLS**: Sayfa yükleme hızı, etkileşim ve görsel stabiliteyi (Lighthouse ile) optimize et.
- [ ] **Mobile-Friendly**: Sitenin mobil cihazlarda hatasız çalıştığını doğrula.
- [ ] **HTTPS**: Sitenin güvenli (SSL) sertifikasına sahip olduğundan emin ol.

### Aşama 3: Structured Data & Semantic
- [ ] **Schema.org**: JSON-LD kullanarak zengin sonuçlar (Rich Results) için yapılandırılmış veri ekle.
- [ ] **Heading Order**: H1-H6 hiyerarşisinin doğru ve anlamlı olduğunu kontrol et.
- [ ] **Alt Tags**: Tüm görseller için açıklayıcı ALT metinleri ekle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | `noindex` tagi yanlışlıkla önemli sayfalarda kalmış mı? |
| 2 | Sayfa hızı (Lighthouse) skoru 90+ mı? |
| 3 | 404 hataları ve kırık linkler (Broken links) temizlendi mi? |
