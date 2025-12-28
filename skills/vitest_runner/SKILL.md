---
name: vitest_runner
router_kit: FullStackKit
description: Modern JavaScript/TypeScript testing with Vitest including mocking and coverage.
metadata:
  skillport:
    category: auto-healed
    tags: [architecture, assertions, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, jest compatible, mocking, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, unit testing, utilities, version control, vite, vitest runner, workflow]
---

# Vitest

## Description

Modern JavaScript/TypeScript testing with Vitest including mocking and coverage.

## When to Use

- Testing JavaScript/TypeScript
- React component testing
- Unit and integration tests

---

## Core Patterns

### Basic Tests

```typescript
import { describe, it, expect } from 'vitest';

describe('math', () => {
  it('should add numbers', () => {
    expect(1 + 1).toBe(2);
  });

  it('should throw on invalid input', () => {
    expect(() => divide(1, 0)).toThrow('Division by zero');
  });
});
```

### Mocking

```typescript
import { vi, describe, it, expect } from 'vitest';

// Mock module
vi.mock('./api', () => ({
  fetchUser: vi.fn().mockResolvedValue({ id: 1 })
}));

// Mock function
const callback = vi.fn();
callback('arg');
expect(callback).toHaveBeenCalledWith('arg');
```

### Async Tests

```typescript
it('should fetch data', async () => {
  const data = await fetchData();
  expect(data).toEqual({ id: 1 });
});

it('should reject on error', async () => {
  await expect(fetchData()).rejects.toThrow('Error');
});
```

### React Testing

```typescript
import { render, screen } from '@testing-library/react';
import { userEvent } from '@testing-library/user-event';

it('should handle click', async () => {
  const onClick = vi.fn();
  render(<Button onClick={onClick}>Click</Button>);

  await userEvent.click(screen.getByRole('button'));
  expect(onClick).toHaveBeenCalled();
});
```

## Best Practices

1. Use describe blocks for grouping
2. Prefer async/await for async tests
3. Use userEvent over fireEvent
4. Mock at module boundaries
5. Clean up after tests

## Common Pitfalls

- **Not awaiting async**: Always await promises
- **Stale mocks**: Clear mocks between tests
- **Testing implementation**: Test behavior
