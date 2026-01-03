---
name: incident_response
router_kit: DevOpsKit
description: IT incident response, on-call rotation ve post-mortem analizi.
metadata:
  skillport:
    category: operations
    tags: [alerting, automation, availability, backups, best practices, business continuity, communication, compliance, cybersecurity, disaster recovery, documentation, incident management, incident response, infrastructure, monitoring, observability, post-mortem, recovery, reliability, resilience, risk management, security, software engineering, troubleshooting, workflow]      - deploy-monitoring
---

# 🚨 Incident Response

> Sistem kesintileri ve hataları yönetme süreci.

---

## 🏗️ 4-Phase Lifecycle

1. **Detection**: İzleme araçları (Prometheus, Grafana, Sentry) üzerinden hatanın fark edilmesi.
2. **Containment**: Hatanın yayılmasını durdurma (Örn: sorunlu servisi izole etme, trafiği yönlendirme).
3. **Recovery**: Sistemin normal çalışma durumuna döndürülmesi (Örn: rollback, restart).
4. **Post-Mortem**: Hatanın nedeninin analizi ve tekrar etmemesi için aksiyon planı.

---

## 📞 Roles & Responsibilities

| Rol | Sorumluluk |
|-----|------------|
| **Incident Commander** | Süreci yönetir, karar vericidir. |
| **Technical Lead** | Teknik çözüme odaklanır. |
| **Communication Lead** | Paydaşlara (müşteri, yönetim) bilgi verir. |

---

## 📝 Post-Mortem Template

```markdown
# Incident Report: [Tarih/Başlık]

## Summary
- **Impact**: [Kaç kullanıcı etkilendi?]
- **Duration**: [Ne kadar sürdü?]
- **Root Cause**: [Neden oldu?]

## Timeline
- 10:00 - Hata fark edildi
- 10:15 - Rollback yapıldı
- 10:30 - Sistem normale döndü

## Lessons Learned
- [Ne öğrendik?]
- [Neyi daha iyi yapabilirdik?]

## Action Items
- [ ] [Aksiyon 1]
- [ ] [Aksiyon 2]
```

---

*Incident Response v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Google SRE Book - Incident Response](https://sre.google/sre-book/incident-response/) & [PagerDuty Incident Response](https://response.pagerduty.com/)

### Aşama 1: Triage (Assessment)
- [ ] **Severity**: Olayın ciddiyetini belirle (P0: Down, P1: Degraded, P2: Minor).
- [ ] **Alert**: İlgili on-call ekibini Slack/Pager veya telefon ile haberdar et.
- [ ] **War Room**: Müdahale ekibi için geçici bir iletişim kanalı (Zoom/Meet/Slack) aç.

### Aşama 2: Mitigation (Repair)
- [ ] **Stop the Bleeding**: Kalıcı çözüm yerine önce geçici iyileştirme (Rollback, Cache Flush) uygula.
- [ ] **Collect Evidence**: Logları, metrikleri ve state'i analiz için kaydet (Silme!).
- [ ] **Update**: Paydaşlara düzenli aralıklarla (örn: 30dk'da bir) durum bilgisi geç.

### Aşama 3: Prevention (Learning)
- [ ] **Post-Mortem**: Olay kapandıktan sonra 48 saat içinde "Blameless" post-mortem toplantısı yap.
- [ ] **Five Whys**: Kök nedene ulaşmak için 5 kere "Neden?" diye sor.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Müşteri hatayı bizden önce mi fark etti? (Monitörler eksik mi?) |
| 2 | Post-mortem'de birini suçladık mı? (Yapılmamalı!) |
| 3 | Action item'lar için JIRA/Ticket açıldı mı? |
