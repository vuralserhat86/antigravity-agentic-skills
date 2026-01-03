---
name: error_handling
router_kit: FullStackKit
description: Robust error handling patterns, circuit breakers ve global error boundaries.
metadata:
  skillport:
    category: development
    tags: [architecture, best practices, cleanup, debugging, development, error handling, error monitoring, error recovery, exception handling, logging, maintainability, performance, quality assurance, resilience, software engineering, stability, testing, troubleshooting, validation, workflow]      - debugging-methodology
---

# 🛠️ Error Handling

> Hata yönetimi, resilience patterns ve global boundaries.

---

## 🏗️ Patterns

### 1. Result Pattern (Type-Safe Errors)

```typescript
type Result<T, E = Error> = 
  | { success: true; data: T }
  | { success: false; error: E };

async function getUser(id: string): Promise<Result<User>> {
  try {
    const user = await db.users.findUnique({ where: { id } });
    if (!user) return { success: false, error: new Error('User not found') };
    return { success: true, data: user };
  } catch (e) {
    return { success: false, error: e as Error };
  }
}
```

### 2. Global Error Boundary (React)

```tsx
class ErrorBoundary extends React.Component {
  state = { hasError: false };

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return this.props.children;
  }
}
```

---

## 🛡️ Circuit Breaker Pattern

Prevent cascading failures in distributed systems.

```python
class CircuitBreaker:
    def __init__(self, failure_threshold=5, timeout=60):
        self.state = "CLOSED"
        self.failures = 0
        self.last_failure_time = None

    def call(self, func):
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.timeout:
                self.state = "HALF_OPEN"
            else:
                raise Exception("Circuit is OPEN")
        
        try:
            result = func()
            self.reset()
            return result
        except Exception as e:
            self.record_failure()
            raise e
```

---

## 🎯 Best Practices

- **Never swallow errors**: Log it or re-throw it.
- **Use custom errors**: `class ValidationError extends Error {}`
- **Provide context**: Log `request_id`, `user_id`, `params`.
- **User feedback**: Don't show raw stack traces to users.

---

*Error Handling v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Sentry Best Practices](https://docs.sentry.io/product/sentry-basics/guides/error-monitoring-best-practices/)

### Aşama 1: Prevention (Design Time)
- [ ] **Typed Errors**: Generic `Exception` yerine `UserNotFound` gibi özel hatalar tanımla.
- [ ] **Boundaries**: API ve UI katmanlarında global `ErrorBoundary` veya `try-catch` wrapper'lar kur.

### Aşama 2: Handling (Run Time)
- [ ] **Recover**: Hata oluştuğunda kullanıcıya "Unknown Error" yerine anlamlı bir durum göster (Graceful Degradation).
- [ ] **Context**: Hatayı yakalarken `user_id`, `input_params` gibi bağlamları da logla.
- [ ] **Clean**: Açık kalan DB bağlantılarını veya dosyaları `finally` bloğunda kapat.

### Aşama 3: Monitoring (Post Design)
- [ ] **Track**: Hataları Sentry/Datadog gibi bir servise gönder (Silent failure olmasın).
- [ ] **Alert**: Kritik hatalar (500, Payment Failed) için Slack/Email alarmı kur.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Hata fırlatıldığında uygulama çöküyor mu yoksa hata sayfası mı gösteriyor? |
| 2 | Loglarda "Error: object Object" gibi anlamsız satırlar var mı? |
| 3 | Hassas veriler (Password, Token) loglanıyor mu? (Maskelenmeli) |
