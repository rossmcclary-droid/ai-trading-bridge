---
name: API artifact routing
description: API artifacts preserve their configured service path when requests reach the application.
---

API services must register routes with awareness of the artifact's configured path prefix, while retaining unprefixed routes for direct ASGI use when practical.

**Why:** The shared proxy forwards the `/api` path to the service instead of stripping it, so a route defined only at `/health` returns 404 through the preview.

**How to apply:** For API artifacts with `paths = ["/api"]`, verify the proxied endpoint at `/api/<route>` and configure the startup health path the same way.