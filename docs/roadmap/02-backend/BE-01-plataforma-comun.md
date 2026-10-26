# BE-01 · Plataforma común

**Objetivo:** librerías técnicas y plantillas para que cada microservicio nuevo nazca cumpliendo los estándares, en lugar de depender de la memoria de quien lo crea.

### BE-01.1 · Librerías técnicas compartidas
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** FND-02.3, FND-03.3

**Requerimientos**
- `libs/common-web` (Problem Details, manejo uniforme de errores, correlación), `libs/common-events` (sobre CloudEvents, cabeceras estándar, serialización), `libs/common-test` (base para Testcontainers y generadores de datos de prueba). `common-observability`, `common-security` y `common-crypto` llegan en OBS-01.2, BE-02.3 y SEC-04.1.
- Módulos equivalentes para Quarkus donde aplique (extensión propia o módulo CDI).
- ADR sobre qué se comparte y qué no: **nunca lógica ni modelos de dominio** (evita el "monolito distribuido").
- Versionado y publicación de las librerías según `versionado-y-git.md`.

**Terminado cuando**
- Las librerías tienen pruebas propias y un servicio de ejemplo las consume por versión publicada.

**Aprender y documentar**
- Autoconfiguración de Spring Boot por dentro (`@AutoConfiguration`, condiciones, orden) y cómo escribir un *starter*; arranque en tiempo de compilación de Quarkus y por qué cambia la forma de escribir extensiones.

### BE-01.2 · Plantillas de servicio
- **Ola:** 1 · **Profundidad:** B
- **Depende de:** BE-01.1, BE-02.3, OBS-01.2, OPS-02.1

**Requerimientos**
- Generador (arquetipo de Maven o similar) para servicios Spring Boot y Quarkus que incluye: estructura según la arquitectura elegida, reglas ArchUnit, seguridad, observabilidad, Flyway, Testcontainers, Dockerfile, configuración por perfiles, OpenAPI y entrada base del manual.
- Pruebas de la propia plantilla en CI (se genera un servicio y se construye).

**Terminado cuando**
- Un servicio generado compila, pasa sus pruebas, arranca, expone salud y emite trazas sin escribir código propio.

**Aprender y documentar**
- Por qué las plantillas son la capa de cumplimiento más eficaz después de la automatización.

### BE-01.3 · *Feature flags*
- **Ola:** 1 · **Profundidad:** B
- **Depende de:** BE-01.2

**Requerimientos**
- OpenFeature con un proveedor autoalojado (flagd u otro, ADR), integrado en la plantilla.
- Tipos de *flags* (liberación, operación, experimento, permiso) con fecha de caducidad y procedimiento de retiro.

**Terminado cuando**
- Una funcionalidad se activa y desactiva en ejecución sin desplegar, y un *flag* caducado hace fallar una verificación.

**Aprender y documentar**
- Separar despliegue de liberación; deuda técnica de los *flags*.
