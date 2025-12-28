---
name: mobile_react_native
router_kit: FullStackKit
description: React Native best practices, hooks, navigation ve performance optimization.
metadata:
  skillport:
    category: development
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, frameworks, frontend, fullstack, html5, javascript, libraries, mobile react native, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - mobile-flutter
---

# 📱 Mobile React Native

> React Native best practices ve performance optimization.

---

## 📁 1. Proje Yapısı

```
src/
├── components/
│   ├── common/        # Reusable
│   └── screens/       # Screen components
├── hooks/             # Custom hooks
├── services/          # API, storage
├── store/             # State (Zustand)
├── navigation/
└── App.tsx
```

---

## ⚡ 2. Performance

```typescript
// FlatList optimizasyonu
<FlatList
  data={items}
  keyExtractor={(item) => item.id}
  removeClippedSubviews={true}
  maxToRenderPerBatch={10}
  windowSize={5}
  getItemLayout={(data, index) => ({
    length: ITEM_HEIGHT,
    offset: ITEM_HEIGHT * index,
    index,
  })}
/>

// Memoization
const Component = React.memo(({ data }) => { });
const callback = useCallback(() => {}, [deps]);
const value = useMemo(() => compute(), [deps]);
```

---

## 🔐 3. Secure Storage

```typescript
// ❌ AsyncStorage güvenli değil
// ✅ SecureStore kullan
import * as SecureStore from 'expo-secure-store';

await SecureStore.setItemAsync('token', userToken);
const token = await SecureStore.getItemAsync('token');
```

---

## 🧭 4. Navigation

```typescript
type RootStackParamList = {
  Home: undefined;
  Profile: { userId: string };
};

const Stack = createNativeStackNavigator<RootStackParamList>();
```

---

## 📦 5. State (Zustand)

```typescript
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

const useAuthStore = create(
  persist(
    (set) => ({
      user: null,
      login: (user) => set({ user }),
      logout: () => set({ user: null }),
    }),
    { name: 'auth-storage' }
  )
);
```

---

## 📱 6. Platform-Specific

```typescript
import { Platform } from 'react-native';

const padding = Platform.select({ ios: 20, android: 0 });

// Dosya bazlı: Button.ios.tsx, Button.android.tsx
```

---

*Mobile React Native v1.0*
