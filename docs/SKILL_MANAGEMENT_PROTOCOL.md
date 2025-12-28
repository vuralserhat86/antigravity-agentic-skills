# Skill Management Protocol: The Manifest-First Strategy

> [!IMPORTANT]
> **Hedef:** Skill yönetimini tek bir noktadan (`skills_manifest.json`) yönetmek ve "Çift İş" yükünü ortadan kaldırmak.
> **Gerçek:** Sistem teknik olarak `.md` dosyalarından beslense de, biz yönetim katmanında Manifest'i "Master", `.md` dosyalarını "Slave" olarak kabul edeceğiz.

---

## 🏗️ Yeni Skill Ekleme Prosedürü

1.  **Manifest'e Kayıt Aç (Aşama 1)**
    *   `skills_manifest.json` dosyasını aç.
    *   İlgili Kit'in (örn. `FullStackKit` veya `DevOpsKit`) altına yeni skill ID'sini ve trigger kelimelerini ekle.
    *   *Örnek:*
        ```json
        "core_skills": [ ..., "super_new_skill" ]
        ```

2.  **SKILL.md Dosyasını Oluştur (Aşama 2)**
    *   Şablon kullanarak dosyanı `C:\Users\mSv\.skillport\skills\super_new_skill\SKILL.md` yolunda oluştur.
    *   **CRITICAL:** Dosya başındaki YAML metadata kısmına, Manifest'te belirlediğin keywords/tags leri MUTLAKA işle.
    *   *Örnek:*
        ```markdown
        ---
        name: super_new_skill
        router_kit: DevOpsKit
        description: ...
        metadata:
          skillport:
            tags:
              - keyword1
              - keyword2
              - synonym3
        ---
        ```

3.  **Sync & Restart (Aşama 3)**
    *   Eğer bir **"Auto-Sync Script"** varsa çalıştır. (Yoksa elle kontrol et).
    *   VS Code / Terminal restart yap (Skillport Cache Temizliği).

---

## 🛠️ Mevcut Skill Güncelleme Prosedürü

**Kural:** Asla ve asla doğrudan `SKILL.md` içine girip rastgele keyword ekleme.
1.  Önce `skills_manifest.json` dosyasına bak: Bu kelime hangi Kit'e ait olmalı?
2.  Manifest'e ekle (Dokümantasyon için).
3.  Sonra `SKILL.md` metadata kısmına ekle (Teknik arama için).
4.  Restart.

---

## 🧹 Skill Çıkartma/Silme Prosedürü

1.  Manifest'ten `core_skills` listesinden ID'yi sil.
2.  Skills klasöründen diski sil (`rm -rf ...`).
3.  Restart.

---

## 🤖 Otomasyon Hedefi (To-Do)

Bu süreci hızlandırmak için bir script (`sync_skills.py`) yazılması planlanmaktadır. Bu script şunları yapacaktır:
1.  `skills_manifest.json` dosyasını okur.
2.  Her skill için `SKILL.md` dosyasını bulur.
3.  Manifest'teki `auto_triggers` listesini, `SKILL.md` metadata kısmına enjekte eder.
4.  Böylece sadece Manifest'i güncellemek yeterli olur.

---

## 🤖 Agent ve Kullanıcı İşbirliği (The Pact)

> [!TIP]
> **Kullanıcı Beyanı:** "Eklenecek bir skills olursa sana ekletiyorum, sen gereken düzenlemeyi yaparsın."

**Agent Sorumluluğu:**
Kullanıcı yeni bir skill eklenmesini veya bir kelimenin kapsama alanına girmesini istediğinde, Agent şunları **manuel ama disiplinli** bir şekilde yapar:
1.  `skills_manifest.json` dosyasını günceller (Sözlük kaydı).
2.  İlgili `SKILL.md` dosyasını bulur ve metadata kısmını günceller (Teknik uygulama).
3.  Kullanıcıya "Restart Gerekli" uyarısını verir.

Bu süreçte kullanıcı teknik detaylarla (JSON/YAML formatı) uğraşmaz, sadece niyeti belirtir.
