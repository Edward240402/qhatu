# BE-03 · API Gateway reactivo

**Objetivo:** un único punto de entrada HTTPS, reactivo, que protege a los servicios y actúa como BFF de la web.

### BE-03.1 · Enrutamiento y borde HTTPS
- **Ola:** 1 · **Profundidad:** B
- **Depende de:** BE-01.2

**Requerimientos**
- Spring Cloud Gateway sobre WebFlux; rutas como código; TLS con certificado de la PKI; HTTP/2; cabeceras de seguridad; CORS estricto; límites de tamaño de petición.
- Propagación de contexto de traza y de `Idempotency-Key`.
- Agregación de la documentación OpenAPI de los servicios.

**Terminado cuando**
- Todo el tráfico externo entra por HTTPS y las cabeceras de seguridad están verificadas por prueba.

**Aprender y documentar**
- Modelo de *event loop* de Netty frente a hilo por petición; por qué un gateway es el caso natural para E/S no bloqueante.

### BE-03.2 · Patrón BFF y sesiones
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** BE-03.1, BE-02.2, DB-03.1

**Requerimientos**
- ADR: tokens en el navegador frente a BFF con cookie de sesión `HttpOnly` (recomendado: BFF).
- El gateway es cliente OIDC confidencial; la sesión vive en Redis (Spring Session) y el token se relaya a los servicios.
- Protección CSRF, cookies `Secure`, `SameSite`, rotación de sesión al autenticarse, cierre de sesión coordinado con Keycloak.

**Terminado cuando**
- Ningún token llega al navegador; una prueba demuestra el rechazo de una petición CSRF.

**Aprender y documentar**
- XSS y CSRF: cómo se mitiga cada uno con y sin BFF.

### BE-03.3 · Límites de tasa y resiliencia en el borde
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** BE-03.2

**Requerimientos**
- *Rate limiting* distribuido en Redis con **cubo de fichas** implementado en Lua (operación atómica, O(1)), por usuario, por cliente y por ruta; cabeceras estándar de límite.
- *Timeouts* por ruta, *circuit breaker* y reintentos solo en métodos idempotentes; respuesta degradada controlada.

**Terminado cuando**
- Superar el límite devuelve `429` con cabeceras correctas, también con varias réplicas del gateway; un servicio caído produce una respuesta degradada.

**Aprender y documentar**
- Cubo de fichas frente a ventana fija, deslizante y registro deslizante: precisión, memoria y complejidad. Se crea el documento de resiliencia, que BE-10.2 amplía.
