---
name: deps_npm
router_kit: FullStackKit
description: npm/yarn dependency management, package.json best practices ve version control.
metadata:
  skillport:
    category: development
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, deps npm, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - deps-security
---

# 📦 Deps NPM

> npm dependency management ve best practices.

---

## 📋 package.json Best Practices

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "engines": { "node": ">=20.0.0" },
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "lint": "eslint .",
    "test": "vitest"
  }
}
```

---

## 🔒 Version Control

| Prefix | Anlamı | Örnek |
|--------|--------|-------|
| `^1.2.3` | Minor updates OK | 1.x.x |
| `~1.2.3` | Patch only | 1.2.x |
| `1.2.3` | Exact version | 1.2.3 |

```bash
# Lock file ZORUNLU
npm ci  # package-lock.json kullan
```

---

## 📊 Dependency Types

```json
{
  "dependencies": {},      // Production
  "devDependencies": {},   // Development only
  "peerDependencies": {}   // Consumer provides
}
```

---

*Deps NPM v1.0*
