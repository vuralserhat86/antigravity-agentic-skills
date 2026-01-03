---
name: performance_profiling
router_kit: FullStackKit
description: CPU/Memory profiling, bottleneck analizi, benchmark teknikleri ve performans optimizasyonu rehberi.
metadata:
  skillport:
    category: optimization
    tags: [big data, cleaning, csv, data analysis, data engineering, data science, database, etl pipelines, export, import, json, machine learning basics, migration, nosql, numpy, pandas, performance profiling, python data stack, query optimization, reporting, schema design, sql, statistics, transformation, visualization]      - optimization
---

# ⚡ Performance Profiling

> CPU, Memory profiling ve bottleneck analizi rehberi.

---

## 📋 İçindekiler

1. [JavaScript/Node.js Profiling](#1-javascriptnodejs-profiling)
2. [React Profiling](#2-react-profiling)
3. [Memory Leak Detection](#3-memory-leak-detection)
4. [Benchmark Teknikleri](#4-benchmark-teknikleri)
5. [Database Profiling](#5-database-profiling)

---

## 1. JavaScript/Node.js Profiling

### Chrome DevTools
```javascript
// Console timing
console.time('operation');
// ... code
console.timeEnd('operation');

// Performance API
const start = performance.now();
// ... code
const end = performance.now();
console.log(`Execution time: ${end - start}ms`);
```

### Node.js Profiling
```bash
# CPU profiling
node --prof app.js
node --prof-process isolate-*.log > profile.txt

# Clinic.js (kapsamlı)
npx clinic doctor -- node app.js
npx clinic flame -- node app.js
npx clinic bubbleprof -- node app.js
```

### V8 Profiler
```javascript
const v8Profiler = require('v8-profiler-next');

v8Profiler.startProfiling('CPU');
// ... code
const profile = v8Profiler.stopProfiling('CPU');
profile.export((error, result) => {
  fs.writeFileSync('profile.cpuprofile', result);
  profile.delete();
});
```

---

## 2. React Profiling

### React DevTools Profiler
```jsx
import { Profiler } from 'react';

function onRenderCallback(
  id, phase, actualDuration, baseDuration, startTime, commitTime
) {
  console.log({ id, phase, actualDuration, baseDuration });
}

<Profiler id="MyComponent" onRender={onRenderCallback}>
  <MyComponent />
</Profiler>
```

### why-did-you-render
```javascript
// wdyr.js
import React from 'react';
import whyDidYouRender from '@welldone-software/why-did-you-render';

whyDidYouRender(React, {
  trackAllPureComponents: true,
});
```

### Render Optimization
```jsx
// useMemo - hesaplama cache
const expensiveValue = useMemo(() => computeExpensive(a, b), [a, b]);

// useCallback - fonksiyon referans
const handleClick = useCallback(() => doSomething(id), [id]);

// React.memo - component memoization
const MemoizedComponent = React.memo(MyComponent);
```

---

## 3. Memory Leak Detection

### Yaygın Leak Kaynakları
| Kaynak | Örnek | Çözüm |
|--------|-------|-------|
| Event listeners | `addEventListener` | `removeEventListener` cleanup |
| Timers | `setInterval` | `clearInterval` cleanup |
| Closures | Büyük objeler referans | Weak references |
| DOM references | Detached DOM | Null atama |
| Global variables | `window.data = large` | Scope sınırlama |

### Chrome DevTools Memory Tab
```
1. Memory tab → Heap snapshot
2. Perform actions
3. Take another snapshot
4. Compare snapshots (Comparison view)
5. Filter by "Detached" for DOM leaks
```

### Node.js Memory
```bash
# Memory usage monitoring
node --expose-gc app.js

# heapdump
npm install heapdump
```

```javascript
const heapdump = require('heapdump');
heapdump.writeSnapshot('./heap-' + Date.now() + '.heapsnapshot');
```

---

## 4. Benchmark Teknikleri

### JavaScript Benchmarking
```javascript
// Benchmark.js
const Benchmark = require('benchmark');
const suite = new Benchmark.Suite;

suite
  .add('Method A', () => methodA())
  .add('Method B', () => methodB())
  .on('cycle', (event) => console.log(String(event.target)))
  .on('complete', function() {
    console.log('Fastest: ' + this.filter('fastest').map('name'));
  })
  .run({ async: true });
```

### HTTP Benchmarking
```bash
# autocannon (Node.js)
npx autocannon -c 100 -d 30 http://localhost:3000

# wrk
wrk -t12 -c400 -d30s http://localhost:3000

# ab (Apache Bench)
ab -n 10000 -c 100 http://localhost:3000/
```

### Lighthouse CI
```bash
npx lhci autorun --collect.url=http://localhost:3000
```

---

## 5. Database Profiling

### PostgreSQL
```sql
-- Slow query log
ALTER SYSTEM SET log_min_duration_statement = 1000; -- 1s

-- EXPLAIN ANALYZE
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT * FROM users WHERE email = 'test@example.com';

-- pg_stat_statements
SELECT query, calls, mean_time, total_time
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;
```

### MongoDB
```javascript
// Profiling enable
db.setProfilingLevel(1, { slowms: 100 });

// Query profiler
db.system.profile.find().sort({ ts: -1 }).limit(10);

// Explain
db.users.find({ email: "test@example.com" }).explain("executionStats");
```

---

## 🎯 Quick Performance Checklist

```checklist
- [ ] Bundle size analizi (webpack-bundle-analyzer)
- [ ] Core Web Vitals (LCP, FID, CLS)
- [ ] Network waterfall analizi
- [ ] Memory leak kontrolü
- [ ] Database query optimization
- [ ] Caching stratejisi (Redis, CDN)
- [ ] Code splitting / Lazy loading
```

---

*Performance Profiling v1.1 - Enhanced*

## 🔄 Workflow

> **Kaynak:** [Chrome DevTools Performance Features](https://developer.chrome.com/docs/devtools/performance/) & [Node.js Diagnostics](https://nodejs.org/en/docs/guides/diagnostics/flame-graphs/)

### Aşama 1: Capture
- [ ] **Tool Selection**: CPU yoğun işler için `Node --prof` veya `py-spy`, Frontend için `Chrome DevTools`.
- [ ] **Environment**: Profiling işlemini mümkünse Prod-like bir ortamda, değilse Prod'da (Sampling profiler ile) yap.
- [ ] **Recording**: Yeterli veri toplamak için en az 30-60 saniye kayıt al.

### Aşama 2: Analysis (Flamegraph)
- [ ] **Width**: Grafikte *geniş* yer kaplayan bloklar (Zaman harcayan fonksiyonlar) hedeftir.
- [ ] **Depth**: *Derin* stack'ler genellikle recursion veya karmaşık framework çağrılarını gösterir.
- [ ] **Hot Path**: En sık çağrılan ve toplam süresi en yüksek olan fonksiyonu bul.

### Aşama 3: Optimization & Verification
- [ ] **De-optimization**: V8 (JS) optimizasyonunu bozan pattern'leri (Örn: delete keyword, hidden class changes) temizle.
- [ ] **Memory**: Garbage Collection (Minor/Major GC) sıklığını kontrol et. Çok sık GC = Memory thrashing.
- [ ] **Verify**: Düzeltme sonrası tekrar profil alıp farkı kanıtla.

### Kontrol Noktaları
| Aşama | Doğrulama |
|-------|-----------|
| 1 | Profiling yaparken Debug mod (logging) kapalı mı? |
| 2 | Anonim fonksiyonlar yerine isimlendirilmiş fonksiyonlar kullanılıyor mu? (Stack trace okunabilirliği için). |
| 3 | "Idle" zamanı ile "System" zamanı ayrıştırıldı mı? |
