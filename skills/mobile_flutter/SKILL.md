---
name: mobile_flutter
router_kit: FullStackKit
description: Flutter/Dart best practices, Riverpod state management ve performance optimization.
metadata:
  skillport:
    category: development
    tags: [architecture, automation, best practices, clean code, coding, collaboration, compliance, debugging, design patterns, development, documentation, efficiency, git, mobile flutter, optimization, productivity, programming, project management, quality assurance, refactoring, software engineering, standards, testing, utilities, version control, workflow]      - mobile-react-native
---

# 🐦 Mobile Flutter

> Flutter/Dart best practices ve performance optimization.

---

## 📁 1. Proje Yapısı (Feature-First)

```
lib/
├── core/
│   ├── theme/
│   └── widgets/
├── features/
│   ├── auth/
│   │   ├── data/
│   │   ├── domain/
│   │   └── presentation/
│   └── home/
├── services/
└── main.dart
```

---

## 🧩 2. Widget Best Practices

```dart
// ✅ const constructor kullan
class MyButton extends StatelessWidget {
  const MyButton({super.key, required this.onPressed});
  final VoidCallback onPressed;

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(onPressed: onPressed, child: Text('Click'));
  }
}

// ✅ const widget'ları işaretle
const SizedBox(height: 16),
```

---

## 📦 3. State (Riverpod)

```dart
final authProvider = StateNotifierProvider<AuthNotifier, AuthState>((ref) {
  return AuthNotifier(ref.watch(authRepositoryProvider));
});

class AuthNotifier extends StateNotifier<AuthState> {
  AuthNotifier(this._repo) : super(const AuthState());
  
  Future<void> login(String email, String password) async {
    state = state.copyWith(isLoading: true);
    final user = await _repo.login(email, password);
    state = state.copyWith(user: user, isLoading: false);
  }
}
```

---

## ⚡ 4. Performance

```dart
// ✅ ListView.builder (lazy loading)
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) => ItemCard(item: items[index]),
)

// ✅ RepaintBoundary
RepaintBoundary(child: ExpensiveWidget())

// ✅ Isolate for CPU-heavy
final result = await compute(parseUsers, jsonString);
```

---

## 🔐 5. Secure Storage

```dart
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

final storage = FlutterSecureStorage();
await storage.write(key: 'token', value: token);
final token = await storage.read(key: 'token');
```

---

## 📱 6. Responsive

```dart
// MediaQuery
final isTablet = MediaQuery.of(context).size.width > 600;

// LayoutBuilder
LayoutBuilder(
  builder: (context, constraints) {
    return constraints.maxWidth > 600 ? WideLayout() : NarrowLayout();
  },
)
```

---

*Mobile Flutter v1.0*
