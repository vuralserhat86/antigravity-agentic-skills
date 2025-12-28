
<div align="center">

# 🌌 Antigravity Agentic Skills
### The Cognitive Engine & Long-Term Memory for Autonomous Agents

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/Skills-138-blue)](./skills)
[![Health Pass](https://img.shields.io/badge/Audit-100%25%20Passing-brightgreen)](./scripts)
[![Protocol](https://img.shields.io/badge/Protocol-Super%20v2-purple)](./workflows/super_protokol_v2.md)

[🇬🇧 English Documentation](#-english-documentation) | [🇹🇷 Türkçe Dokümantasyon](#-türkçe-dokümantasyon)

</div>

---

# 🇬🇧 English Documentation

## 🚀 Overview

**Antigravity Agentic Skills** is not just a code repository; it is a **dynamic cognitive architecture** designed to give AI agents (like Claude/Gemini) long-term memory, specialized expertise, and rigorous engineering discipline.

Typical AI sessions are ephemeral (amnesic). This system bridges that gap by providing a persistent, audited, and self-healing library of **138+ Expert Skills** that the agent can "download" into its context on demand.

## 🧠 System Architecture

This repository represents the **"Brain"** of the agent defined by the `Super Protokol v2`.

```mermaid
graph TD
    User[User Prompt] -->|Query| Protocol[Super Protokol v2]
    Protocol -->|Search Keywords| MCP[MCP Server (Skillport)]
    MCP -->|Scans| Manifest[skills_manifest.json]
    Manifest -->|Indexes| Library[Skill Library (.skillport/skills)]
    Library -->|Loads Context| Agent[AI Agent Context]
    Agent -->|Executes| Code[Perfect Code Generation]
    
    subgraph "Self-Healing Loop"
    Audit[audit_skills.py] -->|Checks| Library
    Heal[heal_skills.py] -->|Injects Metadata| Library
    end
```

## 📂 Repository Structure

The file system is the agent's brain structure.

```ascii
root/
├── .gemini/                    # The Agent's Configuration
│   └── GEMINI.md               # The Constitution (Iron Laws & Rules)
│
├── workflows/                  # Operational Logic
│   └── super_protokol_v2.md    # The "Engine" (How to think & execute)
│
├── docs/                       # Governance & Maintenance
│   └── SKILL_MANAGEMENT.md     # Engineering standards for adding skills
│
├── scripts/                    # Automation & Self-Healing
│   ├── audit_skills.py         # The Doctor: Scans for broken metadata
│   └── heal_skills.py          # The Healer: Fixes missing tags automatically
│
├── skills_manifest.json        # The Central Nervous System (Router)
│
└── skills/                     # The Knowledge Base (138+ Skills)
    ├── react_expert/           # Specialized React 19 knowledge
    ├── aws_architect/          # Cloud infrastructure patterns
    ├── python_pro/             # Type-safe, async Python mastery
    └── ... (135 more)
```

## 🌟 Key Components

### 1. The Skills (`skills/`)
Each folder matches a specific domain. The `SKILL.md` inside is not just text; it contains:
*   **Role Definition:** Who the agent becomes (e.g., "Senior DevOps Engineer").
*   **Trigger Metadata:** Hidden tags ensuring the skill is found by the search engine.
*   **Instructions:** "Iron Rules" specific to that technology (e.g., "Always use `chmod +x`").

### 2. The Engine (`workflows/super_protokol_v2.md`)
This is the operating system. It forces the agent to follow a strict loop:
1.  **Phase 0 (Skill Acquisition):** Search & Load necessary skills.
2.  **Phase 1 (Alignment):** Clarify ambiguity with the user.
3.  **Phase 2 (Planning):** Break down tasks into micro-steps.
4.  **Phase 3 (Engineering):** Test-Driven Development (Red -> Green -> Refactor).
5.  **Phase 4 (Handoff):** Verify and report.

### 3. The Self-Healing Scripts (`scripts/`)
We adhere to the **"100% Initiative"**.
*   `audit_skills.py`: Verifies every single skill has proper metadata and rich descriptions.
*   `heal_skills.py`: Synchronizes the centralized manifest with the distributed skill files.

## 🛠️ Installation & Usage

1.  **Clone this repository** to your machine.
2.  **Configure MCP:** Point your MCP server (Skillport) to this `skills` directory.
   ```json
   "library_root": "%USERPROFILE%/.skillport/skills"
   ```
3.  **Activate Protocol:**
   Start a conversation with:
   > `/super_protokol_v2`

---

# 🇹🇷 Türkçe Dokümantasyon

## 🚀 Genel Bakış

**Antigravity Agentic Skills**, sıradan bir kod deposu değildir. Bu, AI ajanlarına (Claude/Gemini gibi) uzun süreli hafıza, profesyonel uzmanlık ve sıkı mühendislik disiplini kazandırmak için tasarlanmış **dinamik bir bilişsel mimaridir**.

Standart AI oturumları unutkandır (her sohbet sıfırdan başlar). Bu sistem, ajanın ihtiyaç duyduğunda bağlamına yükleyebileceği, sürekli denetlenen ve kendi kendini onaran **138+ Uzman Yetenek** kütüphanesi ile bu sorunu çözer.

## 🧠 Sistem Mimarisi

Bu repo, `Super Protokol v2` tarafından yönetilen **"Dijital Beyni"** temsil eder.

*   **Kullanıcı İsteği:** Ajan önce isteği analiz eder.
*   **Arama (Discovery):** Ajanın "kör" kalmaması için anlamsal arama yapar (örn: "AWS" derseniz "aws_architect" yeteneğini bulur).
*   **Yükleme (Loading):** Sadece ilgili bilgi belleğe yüklenir (Context optimization).
*   **İcra (Execution):** Yüklenen uzmanlıkla "TDD" (Test-Driven Development) kurallarına göre kod yazılır.

## 📂 Klasör Yapısı ve Anlamları

```ascii
root/
├── .gemini/                    # Ajan Konfigürasyonu
│   └── GEMINI.md               # Anayasa (Değiştirilemez Kurallar)
│
├── workflows/                  # İşleyiş Mantığı
│   └── super_protokol_v2.md    # "Motor" (Ajanın nasıl düşüneceğini belirler)
│
├── scripts/                    # Otomasyon Araçları
│   ├── audit_skills.py         # Doktor: Eksik veya hatalı skilleri tarar.
│   └── heal_skills.py          # Şifacı: Eksik etiketleri otomatik tamir eder.
│
├── skills_manifest.json        # Merkezi Sinir Sistemi (Yönlendirici)
│
└── skills/                     # Bilgi Bankası (138+ Yetenek)
    ├── react_expert/           # React 19 ve Modern UI uzmanlığı
    ├── secops_core/            # Güvenlik ve Pentest prosedürleri
    └── ... (135 diğer yetenek)
```

## 🌟 Temel Bileşenler

### 1. Yetenekler (`skills/`)
Her klasör bir uzmanlık alanıdır. İçindeki `SKILL.md` dosyası şunları barındırır:
*   **Rol Tanımı:** Ajan o an kime dönüşmeli? (Örn: "Kıdemli Sistem Mimarı").
*   **Gizli Metadata:** Arama motorunun bu yeteneği %100 isabetle bulmasını sağlayan etiketler.
*   **Talimatlar:** O teknolojiye özel katı kurallar.

### 2. Motor (`workflows/super_protokol_v2.md`)
Bu sistemin işletim sistemidir. Ajanı şu döngüye zorlar:
1.  **Faz 0 (Edinim):** İşe başlamadan önce gereken yetenekleri "indir".
2.  **Faz 1 (Hizalanma):** Kullanıcı ile hedefler konusunda anlaş.
3.  **Faz 2 (Planlama):** İşi atomik parçalara böl (`task.md`).
4.  **Faz 3 (Mühendislik):** Önce test yaz, sonra kod yaz (Red -> Green).
5.  **Faz 4 (Teslim):** Kanıtla ve raporla.

### 3. Kendi Kendini İyileştirme (`scripts/`)
**"%100 İnisiyatifi"** gereği sistem asla hata kabul etmez.
*   `audit_skills.py`: Tek bir tıklamayla tüm sistemi tarar ve "Weak" (zayıf) tanımı olan yetenekleri raporlar.
*   `heal_skills.py`: Manifest dosyasındaki tanımları yüzlerce dosyaya saniyeler içinde işler.

## 🛠️ Kurulum ve Kullanım

1.  **Repoyu Klonlayın:** Bu klasörü bilgisayarınıza indirin.
2.  **MCP Ayarı:** Skillport sunucunuzu bu `skills` klasörüne yönlendirin.
3.  **Protokolü Başlatın:**
   AI ile konuşurken sihirli sözcüğü söyleyin:
   > `/super_protokol_v2`

---
<div align="center">
  <i>Designed for the future of Agentic Coding. Built with Discipline.</i>
</div>
