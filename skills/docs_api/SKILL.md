---
name: docs_api
router_kit: ManagementKit
description: OpenAPI/Swagger API documentation ve endpoint belgeleme şablonları.
metadata:
  skillport:
    category: operations
    tags: [accessibility, api integration, backend, browser apis, client-side, components, css3, debugging, deployment, docs api, frameworks, frontend, fullstack, html5, javascript, libraries, node.js, npm, performance optimization, responsive design, seo, state management, testing, typescript, ui/ux, web development]      - docs-code
---

# 🌐 Docs API

> API documentation ve OpenAPI best practices.

---

## 📋 OpenAPI Template

```yaml
openapi: 3.0.3
info:
  title: User API
  version: 1.0.0

paths:
  /users:
    get:
      summary: List users
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'

components:
  schemas:
    User:
      type: object
      properties:
        id: { type: string }
        email: { type: string, format: email }
```

---

## 📝 Endpoint Doc Template

```markdown
## Create User

`POST /api/v1/users`

### Request
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | Valid email |
| password | string | Yes | Min 8 chars |

### Response (201)
{ "success": true, "data": { "id": "...", "email": "..." } }

### Error (400)
{ "success": false, "error": { "code": "VALIDATION_ERROR" } }
```

---

*Docs API v1.0*
