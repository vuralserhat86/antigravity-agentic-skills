---
name: arch_decisions
router_kit: DevOpsKit
description: ADR template, database selection, capacity planning ve scalability.
metadata:
  skillport:
    category: thinking
    tags: [arch decisions, architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - arch-patterns
---

# 📋 Architecture Decisions

> ADR, database selection ve capacity planning.

---

## 📝 ADR Template

```markdown
# ADR-001: Database Selection

## Status: Accepted

## Context
[Problem açıklaması]

## Decision
PostgreSQL kullanacağız.

## Consequences
### Positive
- ACID compliance
### Negative
- Horizontal scaling zor

## Alternatives
- MongoDB: Rejected - JOINs için uygun değil
```

---

## 🗄️ Database Selection

| SQL | NoSQL |
|-----|-------|
| Complex JOINs | Flexible schema |
| ACID | High throughput |
| Transactions | Horizontal scale |

---

## 📊 Capacity Planning

```markdown
DAU: 1M users
Requests: 20/user/day = 20M/day
RPS: 20M / 86400 = ~230 RPS
Peak: 230 × 3 = ~700 RPS
```

---

*Architecture Decisions v1.0*
