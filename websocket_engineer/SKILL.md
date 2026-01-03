---
name: websocket_engineer
router_kit: FullStackKit
description: Real-time iletişim, WebSockets (Socket.io), event-driven mimari ve state synchronization.
metadata:
  skillport:
    category: development
    tags: [architecture, automation, backend, best practices, cleanup, coaching, collaboration, communication, development, documentation, efficiency, event-driven, full-duplex, integrations, maintainability, metadata, open-source, optimization, performance, quality assurance, real-time, scalability, socket.io, software engineering, standards, testing, version control, web development, websocket engineer_1, workflow]      - realtime-systems
---

# 🔌 WebSocket Engineer

> Çift yönlü (Full-duplex), düşük gecikmeli (Low-latency) realtime iletişim rehberi.

---

## 🏗️ Architecture Models

### 1. Persistent Connections
HTTP gibi "İstek-Cevap" yerine, bağlantının sürekli açık kalması.

### 2. Event-Driven Communication
Verinin sadece değiştiğinde (Push) gönderilmesi.
- **Pattern**: Pub/Sub (Publisher/Subscriber).

### 3. Socket.io (Common Tooling)
- **Features**: Otomatik reconnection, Rooms, Namespaces, Fallback to HTTP Polling.

---

## 🛡️ Scalability & Reliability

- **Sticky Sessions**: Load balancer arkasında aynı client'ın aynı node'a gitmesi.
- **Redis Adapter**: Birden fazla node arasında mesajları senkronize etme.
- **Heartbeat (Ping/Pong)**: Bağlantının canlılığını kontrol etme.

---

## 🔧 Workflow

> **Kaynak:** [Socket.io Documentation](https://socket.io/docs/v4/) & [The WebSocket API (MDN)](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

### Aşama 1: Connection & Protocol Design
- [ ] **Handshake**: WebSocket bağlantısından önce auth (JWT via Query/Headers) sürecini planla.
- [ ] **Event Schema**: Gönderilecek ve alınacak mesajların JSON şemalarını (Events) tanımla.
- [ ] **Transport Choice**: Ham WebSocket mi yoksa Socket.io/Pusher gibi kütüphaneler mi kullanılacak karar ver.

### Aşama 2: Interaction Logic
- [ ] **Room Management**: Kullanıcıları ilgi alanlarına (örn: `room_order_123`) göre grupla.
- [ ] **Ack Mechanism**: Kritik mesajların karşıya ulaştığına dair "Acknowledgment" (Onay) yapısını kur.
- [ ] **Throttling**: Sunucu yüklendiğinde mesaj frekansını kontrol altına al.

### Aşama 3: Scaling & Error Handling
- [ ] **Pub/Sub Backend**: Çoklu sunucu dağıtımında mesajları dağıtmak için `Redis` veya `NATS` entegrasyonu yap.
- [ ] **Reconnect Logic**: Bağlantı koptuğunda client tarafında "Exponential Backoff" ile tekrar bağlanma stratejisini uygula.
- [ ] **Monitoring**: Açık bağlantı sayısı (Concurrent connections) ve mesaj boyutlarını izle.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Yetkisiz kullanıcılar "Room"lara sızabiliyor mu? |
| 2 | Mesaj sırası (Order) bozulursa sistem nasıl davranıyor? |
| 3 | Load Balancer "WebSocket Upgrade" isteğini destekliyor mu? |

---

*WebSocket Engineer v1.1 - Enhanced*
