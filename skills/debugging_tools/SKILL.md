---
name: debugging_tools
router_kit: FullStackKit
description: Debugging araçları - console, debugger, network, profiling.
metadata:
  skillport:
    category: quality
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, debugging tools, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - debugging-methodology
---

# 🛠️ Debugging Tools

> Debugging araçları ve teknikleri.

---

## 💻 Console Methods

```typescript
console.log('Value:', value);
console.table(arrayData);
console.group('Section');
console.trace('Stack trace');
console.time('op'); /* ... */ console.timeEnd('op');
```

---

## 🔴 Debugger

```typescript
function process(data) {
  debugger; // Breakpoint
  return transform(data);
}
```

```bash
# Node Inspector
node --inspect src/index.js
# chrome://inspect
```

---

## 🌐 Network

```typescript
// Axios interceptor
axios.interceptors.request.use(config => {
  console.log('Request:', config);
  return config;
});
```

---

## 📊 Logging

```typescript
import pino from 'pino';

const logger = pino({ level: 'info' });
logger.info({ userId }, 'User logged in');
logger.error({ err }, 'Login failed');
```

---

*Debugging Tools v1.0*
