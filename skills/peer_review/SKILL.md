---
name: peer_review
router_kit: FullStackKit
description: Akademik/teknik doküman review, methodology değerlendirme. ⚠️ Doküman/araştırma için kullan. Kod review için → code-review.
metadata:
  skillport:
    category: research
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, peer review, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - quality
---

# 📝 Peer Review

> Akademik ve teknik peer review metodolojisi rehberi.

---

## 📋 Review Framework

### Değerlendirme Alanları
| Alan | Sorular |
|------|---------|
| **Clarity** | Açık ve anlaşılır mı? |
| **Methodology** | Yöntem uygun mu? |
| **Validity** | Sonuçlar geçerli mi? |
| **Originality** | Özgün katkı var mı? |
| **Completeness** | Eksik var mı? |

---

## 🔍 Code Review Checklist

```checklist
## Functionality
- [ ] Kod beklendiği gibi çalışıyor mu?
- [ ] Edge case'ler handle ediliyor mu?
- [ ] Error handling yeterli mi?

## Code Quality
- [ ] DRY prensibi uygulanmış mı?
- [ ] Naming convention tutarlı mı?
- [ ] Comments yeterli mi?

## Security
- [ ] Input validation var mı?
- [ ] SQL injection riski var mı?
- [ ] Sensitive data korumalı mı?

## Performance
- [ ] Gereksiz işlem var mı?
- [ ] Memory leak riski var mı?
```

---

## 📄 Document Review Template

```markdown
## Review Summary
**Document:** [Doküman adı]
**Reviewer:** [İsim]
**Date:** [Tarih]

## Overall Assessment
[Genel değerlendirme - 1-2 paragraf]

## Strengths
1. ...
2. ...

## Areas for Improvement
1. ...
2. ...

## Specific Comments
| Section | Comment | Severity |
|---------|---------|----------|
| ... | ... | Major/Minor |

## Recommendation
[ ] Accept
[ ] Minor Revisions
[ ] Major Revisions
[ ] Reject
```

---

## 💬 Constructive Feedback

### İyi Feedback
```
✅ "Bu fonksiyon X durumunda hata verebilir. 
    Try-catch eklemeyi düşünebilir misin?"

✅ "Güzel implementasyon! Bir öneri: 
    Bu method extract edilse daha okunabilir olur."
```

### Kaçınılması Gereken
```
❌ "Bu yanlış"
❌ "Neden böyle yaptın?"
❌ "Ben olsam böyle yapmazdım"
```

---

*Peer Review v1.0 - Constructive Criticism*
