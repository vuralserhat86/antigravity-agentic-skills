---
name: websocket_engineer
router_kit: FullStackKit
description: Real-time iletişim, Socket.io ve düşük gecikmeli veri akışı yönetimi.
metadata:
  skillport:
    category: development
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, websocket engineer, workflow]      - real-time
---

# 🔌 WebSocket Engineer

> Anlık veri iletişimi ve çift yönlü (Bidirectional) bağlantı yönetimi.

---

*WebSocket Engineer v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Socket.io Documentation](https://socket.io/docs/v4/) & [Mozilla WebSockets API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

### Aşama 1: Handshake & Configuration
- [ ] **Transport Selection**: WebSocket (veya Polling fallback) yapılandırmasını kur.
- [ ] **Auth Hook**: Bağlantı öncesi JWT veya Session üzerinden yetkilendirme (Handshake middleware) yap.
- [ ] **Heartbeat**: Bağlantının kopup kopmadığını anlamak için Ping/Pong mekanizmasını hazırla.

### Aşama 2: Event Orchestration
- [ ] **Rooms & Namespaces**: Mesajları ilgili gruplara (Rooms) veya işlevlere (Namespaces) ayırarak izole et.
- [ ] **State Sync**: Gelen mesajlarla yerel state'i (Frontend) tutarlı bir şekilde güncelle.
- [ ] **Acknowledgment**: Kritik mesajların ulaştığından emin olmak için "callback" yapılarını kullan.

### Aşama 3: Scaling & Reliability
- [ ] **Reconnection Strategy**: Bağlantı koptuğunda "Backoff" stratejisiyle otomatik tekrar bağlanma kur.
- [ ] **Adapter Layer**: Birden fazla sunucu (Server clusters) varsa `Redis Adapter` ile mesaj trafiğini dağıt.
- [ ] **Binary Support**: Performans gerekiyorsa JSON yerine `Buffer` veya `Protocol Buffers` tercih et.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | "Zombi bağlantılar" (Idle connections) doğru şekilde temizleniyor mu? |
| 2 | Mesaj trafiği (Throughput) sistem kaynaklarını (CPU/RAM) tüketiyor mu? |
| 3 | Güvenlik: Cross-Origin Resource Sharing (CORS) ayarları doğru mu? |
