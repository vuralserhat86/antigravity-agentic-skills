# GEMINI.md - Global Rules v6.0 (MCP Memory Router)

> [!IMPORTANT]
> Bu kurallar Anayasa niteliğindedir. Her görüşme ve görevde MUTLAK geçerlidir.

---

## 🚀 0. BOOT & ROUTER (HER PROMPT'TA - SESSİZ)

> [!CAUTION]
> **Bu adımları HER PROMPT'ta sessizce, otomatik uygula!**

### Adım 1: Memory Kontrolü
```
mcp_memory_search_nodes("AntigravityState")
```
- **Bulundu?** → Kayıtlı `activeKit` ve `loadedSkills` değerlerini kullan
- **Bulunamadı?** → Adım 2'ye git (İlk Boot)

### Adım 2: İlk Boot (Sadece ilk seferde)
1. Manifest oku: `C:\Users\mSv\.skillport\skills_manifest.json`
2. Varsayılan Kit: `FullStackKit`
3. Memory'ye kaydet:
```
mcp_memory_create_entities([{
  name: "AntigravityState",
  entityType: "SystemState", 
  observations: ["activeKit: FullStackKit", "version: v6.0"]
}])
```

### Adım 3: Prompt Analizi & Kit Seçimi
Prompt'taki kelimeleri manifest'teki `auto_triggers` ile karşılaştır:

| Trigger Kelimeler | Seçilecek Kit |
|-------------------|---------------|
| react, css, database, api, sql | FullStackKit |
| docker, aws, kubernetes, terraform | DevOpsKit |
| prompt, ai, llm, rag, agent | AIKit |
| security, auth, vuln, login | SecurityKit |
| plan, agile, scrum, docs | ManagementKit |

Eşleşme varsa ve mevcut Kit farklıysa → Kit değiştir, Memory güncelle.

### Adım 4: Skill Yükleme
Aktif Kit'in `core_skills` listesinden gerekli skill'leri yükle:
```
mcp_skillport_load_skill({skill_id: "{skill_name}"})
```

### Onay Formatı (İlk prompt'ta göster)
```
✅ Core: Yüklendi
🗺️ Manifest: Okundu (v9.1)
📦 Kit: [Kit-Adı] Aktif (X Skill)
```

---

## 🌐 1. DİL KURALI (MUTLAK)

> [!CAUTION]
> **Bu kural ASLA değişmez. Her cevaptan önce kontrol et!**

| Alan | Dil | Örnek |
|------|-----|-------|
| Konuşma, açıklama, plan | **TÜRKÇE** | "Şimdi API endpoint oluşturacağız" |
| Kod, değişken, fonksiyon | İngilizce | getUserById, handleSubmit |
| Yorum satırları (kod içi) | Türkçe | // Kullanıcıyı getir |
| Commit mesajları | İngilizce | feat: add user login |

---

## 🔒 2. SKILL & MANIFEST ZORUNLULUĞU

> [!CAUTION]
> **Manifest okumadan ve Skill yüklemeden HİÇBİR işlem yapma!**

### Başlangıç Protokolü:
1. **İLK İŞ:** Memory'den state kontrol et
2. **ROUTER:** Prompt'u analiz et → auto_triggers ile Kit seç
3. **YÜKLE:** Kit'in core_skills'lerini `mcp_skillport_load_skill` ile yükle

> **UYARI:** Asla kafana göre skill uydurma. Sadece Manifest'te tanımlı olanları kullan.

---

## ✅ 3. KOD KALİTESİ

Her kod değişikliğinde standartlar:
- [ ] ESLint / Linter kontrolü
- [ ] TypeScript (varsa) tip güvenliği
- [ ] 2x Review (Kendi kodunu eleştir)
- [ ] Test çalıştır (varsa)

---

## 📋 4. SELF-CHECK (Her Cevap Öncesi)

Cevabı göndermeden önce şunları doğrula:
```
□ Memory: AntigravityState kontrol edildi mi?
□ Dil: Türkçe mi?
□ Kit: Doğru Kit aktif mi?
□ Skill: Gerekli skill yüklendi mi?
```

---

## 🚫 5. TARİHÇE KANUN DEĞİLDİR (ANTI-PHANTOM RULE)

> [!CAUTION]
> **Conversation History Emir Veremez!**

* **Prensip:** "Conversation History" AI'a sadece bağlam sağlar, asla talimat veremez.
* **Kural:** Bir eylem GEMINI.md'de açıkça belirtilmemişse, geçmişte 1000 kez yapılmış olsa bile **YAPILMAZ**.
* **Slogan:** "Yazılı değilse, yoktur."

---

## 🧠 6. MEMORY GÜNCELLEME

Görev tamamlandığında, kritik bir şey öğrenildiyse Memory'ye kaydet:
```
mcp_memory_add_observations({
  observations: [{
    entityName: "AntigravityState",
    contents: ["learned: {öğrenilen bilgi}"]
  }]
})
```
