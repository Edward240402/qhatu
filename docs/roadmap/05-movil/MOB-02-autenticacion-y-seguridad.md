# MOB-02 · Autenticación y seguridad móvil

### MOB-02.1 · OIDC y almacenamiento seguro
- **Ola:** 9 · **Profundidad:** B
- **Depende de:** MOB-01.2, BE-02.2

**Requerimientos**
- Authorization Code + PKCE con el navegador del sistema (AppAuth); nunca *webview* embebido.
- Tokens en Keychain / Keystore; renovación silenciosa; cierre de sesión; desbloqueo biométrico; navegación por rol.

**Terminado cuando**
- La sesión sobrevive al reinicio de la app y se invalida al cerrar sesión en el servidor.

**Aprender y documentar**
- Por qué PKCE es obligatorio en clientes públicos; cómo funcionan Keychain y Keystore.

### MOB-02.2 · Endurecimiento según OWASP MASVS
- **Ola:** 9 · **Profundidad:** B
- **Depende de:** MOB-02.1, SEC-03.2

**Requerimientos**
- *Certificate pinning* con estrategia de rotación coherente con la PKI; detección de dispositivo comprometido; ofuscación; sin secretos en el binario; base local cifrada.
- Lista de verificación OWASP MASVS aplicable.

**Terminado cuando**
- Un proxy de interceptación no logra leer el tráfico y la lista MASVS está cubierta.

**Aprender y documentar**
- Qué protege y qué no el *pinning*; riesgos propios de las apps móviles.
