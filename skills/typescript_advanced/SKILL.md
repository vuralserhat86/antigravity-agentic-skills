---
name: typescript_advanced
router_kit: FullStackKit
description: TypeScript 5+ advanced patterns, type utilities ve best practices rehberi.
metadata:
  skillport:
    category: development
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, typescript advanced, utilities, version control, workflow]      - patterns
---

# 📘 TypeScript Advanced

> TypeScript 5+ advanced patterns rehberi.

---

## 📋 Utility Types

```typescript
// Partial - tüm prop'lar optional
type PartialUser = Partial<User>;

// Required - tüm prop'lar required
type RequiredUser = Required<User>;

// Pick - seçili prop'lar
type UserName = Pick<User, 'id' | 'name'>;

// Omit - prop'ları çıkar
type UserWithoutPassword = Omit<User, 'password'>;

// Record - key-value map
type UserMap = Record<string, User>;

// ReturnType - fonksiyon return tipi
type Result = ReturnType<typeof fetchUser>;
```

---

## 🔧 Advanced Patterns

### Discriminated Unions
```typescript
type Result<T> = 
  | { success: true; data: T }
  | { success: false; error: string };

function handle(result: Result<User>) {
  if (result.success) {
    console.log(result.data); // User
  } else {
    console.log(result.error); // string
  }
}
```

### Template Literal Types
```typescript
type EventName = `on${Capitalize<string>}`;
// "onClick", "onHover", etc.

type Route = `/${string}`;
```

### Conditional Types
```typescript
type NonNullable<T> = T extends null | undefined ? never : T;

type Flatten<T> = T extends Array<infer U> ? U : T;
```

---

## 🎯 Zod Integration

```typescript
import { z } from 'zod';

const UserSchema = z.object({
  id: z.string().uuid(),
  email: z.string().email(),
  age: z.number().min(0).max(120),
});

type User = z.infer<typeof UserSchema>;
```

---

## ⚡ Best Practices

1. **Strict mode** always on
2. **Avoid `any`** - use `unknown` instead
3. **Prefer interfaces** for objects
4. **Use const assertions** for literals
5. **Type narrowing** over type assertions

---

*TypeScript Advanced v1.0*
