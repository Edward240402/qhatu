# BE-15 · `partner-service` — API para integradores, GraphQL y webhooks salientes

**Objetivo:** que los comercios grandes integren sus sistemas (ERP, punto de venta) como en las grandes plataformas de comercio electrónico: API flexible, eventos hacia sus sistemas y carga masiva de archivos.

**Arquitectura:** **monolito modular** con Spring Modulith (módulos `graphql-api`, `webhooks`, `bulk-import`). Muestra la alternativa a "un microservicio por cosa" y cuándo es la decisión correcta.

### BE-15.1 · Monolito modular y autenticación de integradores
- **Ola:** 6 · **Profundidad:** A
- **Depende de:** BE-01.2, BE-02.3

**Requerimientos**
- Límites de módulos verificados por Spring Modulith; comunicación entre módulos por eventos con el registro de publicación de eventos; documentación de módulos generada.
- Integradores autenticados con Client Credentials (cliente por comercio) y *scopes* finos; cuotas por integrador.

**Terminado cuando**
- Una dependencia indebida entre módulos hace fallar las pruebas.

**Aprender y documentar**
- Monolito modular frente a microservicios: costes, señales para dividir.

### BE-15.2 · API GraphQL
- **Ola:** 6 · **Profundidad:** A
- **Depende de:** BE-15.1, OPS-03.3

**Requerimientos**
- Spring for GraphQL con esquema primero: productos, existencias, pedidos y liquidaciones del comercio, agregando datos de varios servicios.
- **DataLoader** para eliminar el problema N+1 (demostrado con métricas antes y después); paginación por conexiones (*cursor*); autorización por campo.
- Límites de profundidad y **complejidad de consulta**; consultas persistidas.
- El portal de comercio en Angular (FE-05.1) consume esta API.

**Terminado cuando**
- Una consulta anidada que antes hacía cientos de llamadas hace un número constante; una consulta abusiva es rechazada por complejidad.

**Aprender y documentar**
- GraphQL frente a REST frente a gRPC: cuándo cada uno; cómo funciona la resolución por campos y por qué aparece el N+1.

### BE-15.3 · Webhooks salientes
- **Ola:** 6 · **Profundidad:** A
- **Depende de:** BE-15.2, BE-11.3

**Requerimientos**
- Suscripciones por tipo de evento con verificación del *endpoint* (desafío).
- Siguiendo la especificación *Standard Webhooks*: firma HMAC con rotación de secreto (dos secretos válidos durante la transición), identificador y marca de tiempo por entrega.
- Reintentos con *backoff* exponencial y *jitter* durante horas, *circuit breaker* por *endpoint*, desactivación automática de *endpoints* que fallan siempre, registro de entregas y **reenvío manual**.
- Orden por clave cuando el integrador lo necesita.

**Terminado cuando**
- Con un *endpoint* caído durante una hora, todas las entregas llegan al recuperarse y en orden por clave.

**Aprender y documentar**
- Diseño de webhooks como productor: garantías, seguridad y experiencia del integrador.

### BE-15.4 · Importación masiva de archivos
- **Ola:** 6 · **Profundidad:** A
- **Depende de:** BE-15.3, BE-05.5, BE-06.5

**Requerimientos**
- Carga de catálogo y existencias por CSV o JSON Lines, aplicada a través de las APIs o comandos de `catalog-service` e `inventory-service` (nunca escribiendo en sus bases): subida con URL prefirmada, validación en *streaming* (memoria constante, O(n) en filas), aplicación por lotes idempotente por fila, informe de errores descargable.
- Trabajo asíncrono con progreso y cancelación; webhook al terminar.

**Terminado cuando**
- Un archivo de un millón de filas se procesa con memoria constante (demostrado en métricas) y una segunda carga del mismo archivo no duplica nada.

**Aprender y documentar**
- Integración por archivos en empresas: por qué sigue existiendo y cómo hacerla robusta.
