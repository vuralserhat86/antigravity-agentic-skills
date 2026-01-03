---
name: performance_profiling
router_kit: FullStackKit
description: Kod seviyesinde CPU, bellek ve I/O profilleme araçları ve teknikleri.
metadata:
  skillport:
    category: debugging
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, performance profiling, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - profiling
---

# 🔍 Performance Profiling

> Kodun yürütme maliyetini derinlemesine analiz etme ve iyileştirme.

---

*Performance Profiling v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Node.js Performance Profiling Guide](https://nodejs.org/en/docs/guides/simple-profiling/) & [Chrome DevTools Profiling](https://developer.chrome.com/docs/devtools/performance/)

### Aşama 1: tool Selection & Setup
- [ ] **Backend**: `v8-profiler` (Node), `cProfile` (Python) veya `pprof` (Go) seç.
- [ ] **Frontend**: Chrome DevTools `Performance` tab veya `Lighthouse` kullan.

### Aşama 2: Recording (Capturing)
- [ ] **Scenario**: Darboğazın yaşandığı aksiyonu (Örn: sayfa yükleme, rapor üretme) izole et.
- [ ] **Profiling**: CPU profilini (Sampling) al veya Memory heap snapshot'ını kaydet.

### Aşama 3: Analysis (Interpretation)
- [ ] **Flamegraph**: "Hot path"leri (en çok zaman alan fonksiyonlar) görselleştir.
- [ ] **Heap Analizi**: Bellek sızıntılarını (Memory leaks) tespit etmek için `Destached DOM nodes` veya `Global variables` tara.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Profilleme verisi "Production build" üzerinde mi alındı (Sourcemaps)? |
| 2 | "Anonymized data" ile mi çalışıldı (Gizlilik)? |
| 3 | En büyük "Self Time" sahibi fonksiyon optimize edilebilir mi? |
