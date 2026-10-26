# BE-02 · Identidad: OAuth2, OIDC y JWT

**Objetivo:** identidad centralizada en Keycloak, configurada como código, y librerías de autorización reutilizables.

### BE-02.1 · Keycloak como código
- **Ola:** 1 · **Profundidad:** B
- **Depende de:** SEC-03.2, DB-01.1

**Requerimientos**
- Keycloak en Compose con PostgreSQL propio y TLS.
- *Realm* versionado (proveedor de Terraform para Keycloak o `keycloak-config-cli`, ADR); un script recrea todo desde cero. Ningún cambio manual sin reflejo en el repositorio.
- Clientes: web (vía BFF, confidencial), móvil (público con PKCE), servicios (Client Credentials), integradores (Client Credentials con *scopes* propios).
- Roles `customer`, `merchant`, `courier`, `support`, `admin`; *scopes* por API; atributo de comercio en el token.
- Tema de inicio de sesión en español.

**Terminado cuando**
- `task keycloak:reset` recrea el *realm* idéntico y una colección de Postman obtiene tokens de cada cliente.

**Aprender y documentar**
- OAuth2 frente a OIDC; roles de cliente frente a roles de *realm*; qué es un *scope*.

### BE-02.2 · Flujos, tokens y políticas
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** BE-02.1

**Requerimientos**
- Authorization Code + PKCE, Client Credentials y (si se justifica) *token exchange* para propagar identidad entre servicios, con ADR (token del usuario frente a token de servicio con contexto).
- Duración corta de *access tokens*, rotación de *refresh tokens*, cierre de sesión (incluido *back-channel logout*), rotación de claves de firma.
- MFA (TOTP) obligatorio para `support` y `admin`. **(Opcional)** passkeys/WebAuthn.

**Terminado cuando**
- Pruebas automatizadas cubren: token expirado, firmado con otra clave, `aud` incorrecta, *refresh token* reutilizado tras rotación.

**Aprender y documentar**
- Cada flujo y cuándo usarlo; por qué PKCE; anatomía y validación de un JWT (firma, `iss`, `aud`, `exp`, JWKS); el problema de la revocación de JWT.

### BE-02.3 · Librerías de autorización
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** BE-02.2, BE-01.1

**Requerimientos**
- `libs/common-security` para Spring y Quarkus: conversión del JWT de Keycloak a autoridades, validación de `aud`, utilidades de **autorización por propiedad del recurso** (un comercio solo accede a sus recursos), auditoría de decisiones denegadas.
- Pruebas reutilizables para escenarios de autorización (base de la batería de SEC-06.3).

**Terminado cuando**
- Un servicio de ejemplo rechaza el acceso de un comercio a recursos de otro, verificado por prueba.

**Aprender y documentar**
- RBAC frente a ABAC; dónde se decide la autorización y por qué nunca solo en el cliente o el gateway.
