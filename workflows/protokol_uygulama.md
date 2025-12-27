---
description: protokol_uygulama (Legacy - v6.0'da otomatik çalışır)
---

> ⚠️ **NOT:** v6.0'dan itibaren bu workflow'u manuel çağırmaya gerek yoktur. 
> GEMINI.md kuralları her prompt'ta **otomatik olarak** çalışır.

---

## 0. Sistem Başlatma (BOOT SEQUENCE)

Her yeni oturumda AI **otomatik olarak** şunları yapar:

1. **🧠 Memory Kontrolü:**
   * `mcp_memory_search_nodes("AntigravityState")`
   * Varsa → Kayıtlı Kit ve Skill bilgisini kullan
   * Yoksa → İlk boot prosedürü

2. **⚖️ Anayasa (Global Rules):**
   * **Yol:** `%USER_PROFILE%\.gemini\GEMINI.md`
   * **Amaç:** Etik kurallar, kodlama standartları ve temel prensipleri yükle.

3. **🗺️ Yetenek Haritası (Skills Manifest):**
   * **Yol:** `%USER_PROFILE%\.skillport\skills_manifest.json`
   * **Amaç:** Hangi görev için hangi araç setini (Kit) kullanacağını öğren.

**Onay Mesajı:** 
```
✅ Core: Yüklendi
🗺️ Manifest: Okundu (v9.1)
📦 Kit: [Kit-Adı] Aktif (X Skill)
```

---

## 1. Akıllı Yönlendirme (Router Logic)

Her PROMPT için otomatik keyword analizi yapılır:

| Anahtar Kelimeler | Seçilecek Kit |
|-------------------|---------------|
| react, css, database, api | FullStackKit |
| docker, aws, kubernetes | DevOpsKit |
| prompt, ai, llm, rag | AIKit |
| security, auth, vuln | SecurityKit |
| plan, agile, scrum | ManagementKit |

---

## 2. Skill Yükleme (Absolute Path Injection)

Manifest'ten seçilen skill'leri şu şablona göre yükle:

> **PATH:** `%USER_PROFILE%\.skillport\skills\{skill_name}\SKILL.md`

Örnek: Eğer `DevOpsKit` seçildiyse, sadece o kitin içindeki araçları (örn: `aws_architect`, `terraform_engineer`) bu yoldan çekip bağlama ekle.

---

## 3. Deneyim Kaydı (Learning Loop)

Görevi bitirmeden önce kendine sor: "Bu görev sırasında, gelecekte hatırlamam gereken kritik bir şey öğrendim mi?"

Eğer evet ise, MCP Memory'ye kaydet:
```
mcp_memory_add_observations({
  observations: [{
    entityName: "AntigravityState",
    contents: ["learned: {öğrenilen bilgi}"]
  }]
})
```

---

**Protokol v6.0 - Auto-Trigger + MCP Memory Router**
