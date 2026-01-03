---
name: spring_boot
router_kit: FullStackKit
description: Java Spring Boot ile kurumsal backend geliştirme, Microservices ve Security.
metadata:
  skillport:
    category: development
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, spring boot, standards, testing, utilities, version control, workflow]      - java-enterprise
---

# 🍃 Spring Boot

> Kurumsal düzeyde, sağlam ve ölçeklenebilir Java backend uygulamaları.

---

*Spring Boot v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Spring Boot Reference Guide](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/) & [Baeldung Spring Boot Tutorials](https://www.baeldung.com/spring-boot)

### Aşama 1: Foundation & dependency
- [ ] **Starter**: `Spring Initializr` ile projeyi kur ve gerekli starter'ları (Web, Data JPA, Security) ekle.
- [ ] **Config**: `application.yml` veya `.properties` dosyalarında ortam değişkenlerini yapılandır.

### Aşama 2: Data & Business Logic
- [ ] **Models**: JPA Entity'lerini ve aralarındaki ilişkileri tanımla.
- [ ] **Service Layer**: İş mantığını (Business logic) servis sınıflarında topla.
- [ ] **REST API**: `@RestController` ve `@RequestMapping` ile endpoint'leri oluştur.

### Aşama 3: Security & Monitoring
- [ ] **Security**: `Spring Security` ile JWT veya OAuth2 tabanlı yetkilendirme kur.
- [ ] **Actuator**: Uygulama sağlığını ve metriklerini takip etmek için Actuator'ı aktif et.
- [ ] **Testing**: `JUnit 5` ve `Mockito` ile kapsamlı unit ve integration testlerini yaz.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Dependency Injection (DI) doğru şekilde (Constructor injection tercih edilmeli) yapıldı mı? |
| 2 | Exception'lar `GlobalExceptionHandler` ile merkezi olarak yönetiliyor mu? |
| 3 | Veritabanı bağlantı havuzu (HikariCP) optimize edildi mi? |
