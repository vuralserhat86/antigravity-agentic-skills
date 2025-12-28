---
name: regex_builder
router_kit: FullStackKit
description: Regular expression oluşturma, test etme, debug ve açıklama rehberi.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, regex builder, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - text-processing
---

# 🔤 Regex Builder

> Regular expression oluşturma ve test rehberi.

---

## 📋 Temel Syntax

### Karakter Sınıfları
| Pattern | Eşleşir | Örnek |
|---------|---------|-------|
| `.` | Herhangi karakter | `a.c` → "abc", "a1c" |
| `\d` | Rakam [0-9] | `\d+` → "123" |
| `\w` | Word char [a-zA-Z0-9_] | `\w+` → "hello_123" |
| `\s` | Whitespace | `a\sb` → "a b" |
| `\D` | Rakam değil | `\D+` → "abc" |
| `\W` | Word char değil | `\W+` → "!@#" |

### Quantifiers
| Pattern | Anlam | Örnek |
|---------|-------|-------|
| `*` | 0 veya daha fazla | `ab*c` → "ac", "abc", "abbc" |
| `+` | 1 veya daha fazla | `ab+c` → "abc", "abbc" |
| `?` | 0 veya 1 | `ab?c` → "ac", "abc" |
| `{n}` | Tam n kere | `a{3}` → "aaa" |
| `{n,m}` | n ile m arası | `a{2,4}` → "aa", "aaa", "aaaa" |
| `{n,}` | En az n | `a{2,}` → "aa", "aaa", ... |

### Anchors
| Pattern | Anlam |
|---------|-------|
| `^` | Satır başı |
| `$` | Satır sonu |
| `\b` | Word boundary |
| `\B` | Non-word boundary |

---

## 🔧 Yaygın Patterns

### Email
```regex
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

### URL
```regex
https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)
```

### Telefon (TR)
```regex
^(\+90|0)?[0-9]{10}$
```

### IP Address
```regex
^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$
```

### Date (YYYY-MM-DD)
```regex
^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$
```

### Password (Strong)
```regex
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$
```

---

## 🧪 Test Komutları

### JavaScript
```javascript
const regex = /pattern/flags;
regex.test('string');      // true/false
'string'.match(regex);     // matches array
'string'.replace(regex, 'replacement');
```

### Python
```python
import re

re.search(r'pattern', 'string')
re.findall(r'pattern', 'string')
re.sub(r'pattern', 'replacement', 'string')
```

### CLI (ripgrep)
```bash
rg 'pattern' file.txt
rg -o 'pattern' file.txt  # Only matching
rg -c 'pattern' file.txt  # Count
```

---

## 🔍 Debugging Tips

1. **Escape special chars**: `. * + ? ^ $ { } [ ] ( ) | \`
2. **Lazy vs Greedy**: `.*?` (lazy) vs `.*` (greedy)
3. **Non-capturing group**: `(?:pattern)` 
4. **Lookahead**: `(?=pattern)` ve `(?!pattern)`
5. **Lookbehind**: `(?<=pattern)` ve `(?<!pattern)`

---

*Regex Builder v1.0*
