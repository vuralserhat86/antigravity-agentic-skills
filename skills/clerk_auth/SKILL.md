---
name: clerk_auth
router_kit: SecurityKit
description: Clerk modern authentication, WebAuthn, passkeys ve social auth entegrasyonu rehberi.
metadata:
  skillport:
    category: authentication
    tags: [accessibility, api integration, backend, browser apis, clerk auth, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - webauthn
---

# 🔐 Clerk Auth

> Clerk modern authentication rehberi.

---

## 📋 Kurulum

```bash
npm install @clerk/nextjs
```

### middleware.ts
```typescript
import { clerkMiddleware } from '@clerk/nextjs/server';

export default clerkMiddleware();

export const config = {
  matcher: ['/((?!.*\\..*|_next).*)', '/', '/(api|trpc)(.*)'],
};
```

---

## 🔧 Provider Setup

```typescript
// app/layout.tsx
import { ClerkProvider } from '@clerk/nextjs';

export default function Layout({ children }) {
  return (
    <ClerkProvider>
      <html>
        <body>{children}</body>
      </html>
    </ClerkProvider>
  );
}
```

---

## 👤 Components

```typescript
import { 
  SignInButton, 
  SignUpButton, 
  UserButton,
  SignedIn,
  SignedOut 
} from '@clerk/nextjs';

function Header() {
  return (
    <header>
      <SignedOut>
        <SignInButton />
        <SignUpButton />
      </SignedOut>
      <SignedIn>
        <UserButton />
      </SignedIn>
    </header>
  );
}
```

---

## 🔒 Server-side Auth

```typescript
import { auth, currentUser } from '@clerk/nextjs/server';

export async function GET() {
  const { userId } = await auth();
  
  if (!userId) {
    return new Response('Unauthorized', { status: 401 });
  }
  
  const user = await currentUser();
  return Response.json({ user });
}
```

---

*Clerk Auth v1.0*
