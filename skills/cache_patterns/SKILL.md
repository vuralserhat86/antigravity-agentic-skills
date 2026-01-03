---
name: cache_patterns
router_kit: FullStackKit
description: Instruction set for enabling and operating the Spring Cache abstraction in Spring Boot when implementing application-level caching for performance-sensitive workloads.
allowed-tools: Read, Write, Bash
category: backend
tags: [architecture, automation, best practices, cache patterns, cache-managers, cacheable, caching, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, performance, productivity, programming, project management, quality assurance, refactoring, software engineering, spring-boot, standards, testing, utilities, version control, workflow]
version: 1.1.0
metadata:
  skillport:
    category: auto-healed
    tags:
      - cache_patterns
---

# Spring Boot Cache Abstraction

---

*Cache Patterns v2.0 - With Workflow*

## 🔄 Workflow

> **Kaynak:** [Spring Boot Caching Guide](https://spring.io/guides/gs/caching/) & [Caffeine Cache Best Practices](https://github.com/ben-manes/caffeine/wiki/Best-Practices)

### Aşama 1: Strategy & Provider Selection
- [ ] **Identifying Hot Paths**: En çok beklenen ve nadir değişen veri okuma (I/O) noktalarını belirle.
- [ ] **Provider Selection**: Bellek içi (Caffeine) veya dağıtık (Redis) cache seçimine karar ver.
- [ ] **Key Design**: SpEL kullanarak benzersiz ve tahmin edilebilir cache key strategy'si oluştur.

### Aşama 2: Annotation Implementation
- [ ] **@Cacheable**: Veriyi cache'e yaz we sonraki çağrılarda oradan oku.
- [ ] **@CachePut**: Veri güncellendiğinde cache'i de yenile.
- [ ] **@CacheEvict**: Silme işlemlerinde veya belirli periyotlarda cache'i temizle (`allEntries=true` opsiyonunu değerlendir).

### Aşama 3: LifeCycle & Monitoring
- [ ] **TTL/Eviction**: Veri tazeliği (TTL) ve temizleme (Eviction) politikalarını (LRU/LFU) konfigüre et.
- [ ] **Actuator Audit**: `cache` endpoint'i üzerinden hit/miss oranlarını izle.
- [ ] **Integration Testing**: `@SpringBootTest` ile cache izolasyonunu ve tutarlılığını test et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Transactional işlemler sırasında cache tutarlılığı (Data drift) bozuluyor mu? |
| 2 | "Cache-aside" veya "ReadOnly" stratejisi doğru uygulandı mı? |
| 3 | Çoklu instance yapısında "Cache Stampede" riski önlendi mi? |
