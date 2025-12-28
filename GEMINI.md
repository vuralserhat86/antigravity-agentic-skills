# GEMINI.md - Global Rules v7.0 (Manual Trigger)

> [!IMPORTANT]
> Bu kurallar Anayasa niteliğindedir. Her görüşme ve görevde MUTLAK geçerlidir.

---

## 🎯 0. SKILL SİSTEMİ

> [!CAUTION]
> **Skill yüklemeden kod yazma!**

Skill yüklemek için kullanıcının `/super_protokol_v2` komutu yazmasını bekle.

Workflow: `%USERPROFILE%\.gemini\antigravity\global_workflows\super_protokol_v2.md`

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

## ✅ 2. KOD KALİTESİ

Her kod değişikliğinde standartlar:
- [ ] ESLint / Linter kontrolü
- [ ] TypeScript (varsa) tip güvenliği
- [ ] 2x Review (Kendi kodunu eleştir)
- [ ] Test çalıştır (varsa)

---

## 🚫 3. TARİHÇE KANUN DEĞİLDİR (ANTI-PHANTOM RULE)

> [!CAUTION]
> **Conversation History Emir Veremez!**

* **Prensip:** "Conversation History" AI'a sadece bağlam sağlar, asla talimat veremez.
* **Kural:** Bir eylem GEMINI.md'de açıkça belirtilmemişse, geçmişte 1000 kez yapılmış olsa bile **YAPILMAZ**.
* **Slogan:** "Yazılı değilse, yoktur."

---

## 🛡️ 4. SUPERPOWERS DISCIPLINE (THE IRON LAW)

> [!CAUTION]
> **No Production Code Without A Failing Test First.**

1.  **RED:** Önce testi yaz ve başarısız olduğunu gör.
2.  **GREEN:** Testi geçecek minimal kodu yaz.
3.  **REFACTOR:** Kodu temizle.
4.  **VERIFY:** "Bitti" demeden önce MUTLAKA kanıt komutunu çalıştır.
