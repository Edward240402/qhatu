# DB-01 · PostgreSQL base y Flyway

### DB-01.1 · Convenciones de PostgreSQL y mínimo privilegio
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** FND-04.1, SEC-03.2

**Requerimientos**
- Una base de datos por servicio. Roles separados: propietario del esquema (solo migraciones), usuario de aplicación (DML sobre sus tablas), solo lectura (soporte y analítica).
- `docs/estandares/sql.md`: nombres, claves primarias (UUIDv7 frente a secuencias, ADR), tipos para dinero (`numeric` con escala fija) y tiempo (`timestamptz`), restricciones siempre en la base, borrado lógico solo con justificación.
- *Pooling* en la aplicación con HikariCP dimensionado; PgBouncer evaluado con ADR (modos de *pooling* y su incompatibilidad con ciertas funciones).
- TLS con `verify-full` hacia la base.

**Terminado cuando**
- La aplicación de ejemplo arranca con un usuario que no puede alterar el esquema, y la conexión sin TLS es rechazada.

**Aprender y documentar**
- Arquitectura de procesos de PostgreSQL (un proceso por conexión) y por qué el *pooling* es obligatorio; roles y privilegios por defecto.

### DB-01.2 · Estrategia de migraciones con Flyway
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** DB-01.1

**Requerimientos**
- `docs/estandares/migraciones.md`:
  - versionadas `V<n>__desc.sql` (nunca se editan una vez aplicadas; el hook de FND-05.1 lo impide), repetibles `R__` para vistas, funciones y procedimientos, migraciones en Java para transformaciones de datos por lotes;
  - *callbacks*, *placeholders* por entorno, `validate` al arrancar, `baseline` para bases existentes, `outOfOrder` desactivado;
  - **sin tiempo de inactividad**: patrón expandir/contraer repartido en **versiones desplegadas distintas**, índices `CONCURRENTLY`, `lock_timeout` y `statement_timeout` en cada migración, compatibilidad con la versión anterior del servicio;
  - estrategia de vuelta atrás: corrección hacia adelante (las migraciones *undo* de Flyway son de pago y además son una mala idea para datos), con justificación.
- Migraciones ejecutadas como paso separado del arranque (en Kubernetes, un Job previo; en local, un objetivo de `task`).
- Lint de migraciones en CI (Squawk) y **prueba de migración**: la base se lleva a la versión anterior, se siembran datos y se aplica la nueva.
- **Ejercicios de evolución planificados** (para que se vea el versionado real, no solo una `V1`):

| Servicio | Evolución | Sub-fase |
|---|---|---|
| `customer-service` | `V1` perfiles → `V2` direcciones y consentimientos | BE-04.1, BE-04.2 |
| `customer-service` | Renombrar una columna en tres despliegues (añadir, escribir en ambas y rellenar, eliminar la antigua) | BE-04.2 |
| `customer-service` | Cifrado de columnas existentes: añadir columnas cifradas, migración Java de relleno por lotes, eliminar columnas en claro en un despliegue posterior | BE-04.3 |
| Varios | Trigger genérico de auditoría añadido a tablas existentes | DB-05.2 |
| `inventory-service` | Convertir una tabla grande existente en particionada sin parar el servicio | DB-05.3 |
| `order-service` | Añadir columnas con valor por defecto sobre una tabla particionada con volumen | BE-09.5 |
| `settlement-service` | Cambiar la firma de una función usada por procedimientos (versionado de funciones con `R__`) | BE-16.3 |
| `catalog-service` (MongoDB) | Cambio de forma de documentos con migración perezosa y campo de versión de esquema | BE-05.3 |

**Terminado cuando**
- Una migración insegura (por ejemplo, `ALTER TABLE` que reescribe la tabla) es rechazada por CI, y la prueba de migración desde la versión anterior corre en el pipeline.

**Aprender y documentar**
- Cómo Flyway registra el estado (`flyway_schema_history`, sumas de comprobación); niveles de bloqueo del DDL en PostgreSQL y por qué un `ALTER` mal hecho detiene producción. Experimento: bloquear una tabla con un `ALTER` y ver la cola de bloqueos en `pg_locks`.
