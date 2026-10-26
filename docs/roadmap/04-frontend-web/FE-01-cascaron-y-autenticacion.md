# FE-01 · Cascarón, autenticación y roles

### FE-01.1 · *Workspace* y sistema de diseño
- **Ola:** 1 · **Profundidad:** B
- **Depende de:** FND-02.1

**Requerimientos**
- *Workspace* con librerías por dominio y por tipo (`feature`, `ui`, `data-access`, `util`) y límites forzados por lint. ADR: Angular CLI frente a Nx.
- `docs/estandares/frontend.md`; presupuestos de tamaño en el build.
- Sistema de diseño (librería de componentes con ADR), *tokens* de diseño compartibles con el móvil, tema claro y oscuro.
- Pipeline de CI del front (lint, pruebas, build) reutilizando los flujos de OPS-01.1.

**Terminado cuando**
- Una importación que viola los límites entre librerías falla el lint en CI.

**Aprender y documentar**
- Cómo funcionan los *signals* y la detección de cambios sin zonas; inyección de dependencias jerárquica.

### FE-01.2 · Autenticación por BFF, roles y seguridad del navegador
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** FE-01.1, BE-03.2

**Requerimientos**
- Inicio de sesión OIDC a través del BFF del gateway (cookie `HttpOnly`); nunca tokens en el navegador.
- *Guards* funcionales por rol, directiva de permisos, menú según rol (la autorización real es del backend).
- Interceptores: errores RFC 9457 → mensajes, reintentos idempotentes, propagación de `traceparent`.
- HTTPS en desarrollo con la PKI; Content Security Policy estricta con *nonces*, Trusted Types, cabeceras de seguridad.

**Terminado cuando**
- Cada rol ve su área y recibe un `403` controlado al forzar una ruta ajena; el reporte de CSP no registra violaciones.

**Aprender y documentar**
- CSP y Trusted Types: qué ataques bloquean; por qué el BFF es más seguro que guardar tokens en el navegador.
