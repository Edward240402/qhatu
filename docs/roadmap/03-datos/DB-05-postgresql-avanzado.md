# DB-05 · PostgreSQL avanzado

**Objetivo:** herramientas y patrones de PostgreSQL avanzado, aplicados primero a servicios existentes (adopción retroactiva) para que los servicios nuevos de la ola 4 nazcan con ellos.

### DB-05.1 · Diagnóstico y rendimiento de consultas
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-06.5, DB-02.2

**Requerimientos**
- `pg_stat_statements` y `auto_explain` activados; dashboard de consultas más costosas.
- Índices avanzados aplicados donde los planes lo justifiquen en servicios existentes: parciales, por expresión, cubrientes (`INCLUDE`), GIN, BRIN.
- Pruebas que detectan regresiones de plan en las consultas críticas.

**Terminado cuando**
- Las consultas principales de `customer-service` e `inventory-service` tienen su plan documentado y una mejora medida.

**Aprender y documentar**
- Cómo planifica PostgreSQL (estadísticas, estimación de cardinalidad, tipos de *join* y de *scan*); MVCC, `VACUUM` y *bloat*. Experimento: estadísticas desactualizadas que provocan un mal plan.

### DB-05.2 · Funciones, procedimientos y triggers con pruebas
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** DB-05.1

**Requerimientos**
- Convenciones para lógica en base de datos: funciones SQL y PL/pgSQL con volatilidad correcta (`IMMUTABLE`, `STABLE`, `VOLATILE`), procedimientos con control transaccional, manejo de errores, `SECURITY DEFINER` solo con `search_path` fijado.
- ADR: qué lógica va en la base de datos y cuál en la aplicación.
- **Trigger genérico de auditoría** (historial con valor anterior y nuevo, usuario y traza), aplicado mediante nuevas migraciones a las tablas auditables existentes.
- Trigger de validación de transiciones de estado como defensa en profundidad.
- **pgTAP** (o Testcontainers) para probar funciones, procedimientos y triggers en CI.

**Terminado cuando**
- La auditoría registra cambios en los servicios existentes y las pruebas pgTAP corren en el pipeline.

**Aprender y documentar**
- Coste de los triggers por fila y por sentencia, tablas de transición; seguridad de `SECURITY DEFINER`. Experimento: medir el coste de un trigger de auditoría bajo carga.

### DB-05.3 · Particionado y seguridad a nivel de fila
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** DB-05.2

**Requerimientos**
- Particionado declarativo por rango con creación automática de particiones futuras y archivado de antiguas (pg_partman o propio, ADR); índices por partición; poda verificada con `EXPLAIN`.
- **Conversión en caliente** de la tabla de movimientos de `inventory-service` (ya existente y con volumen) a particionada, sin parar el servicio.
- Seguridad a nivel de fila (RLS) para aislar datos por comercio, como patrón para los servicios que lo necesiten.
- Vistas materializadas con refresco concurrente; `pgcrypto` comparado con el cifrado en aplicación de SEC-04.1.

**Terminado cuando**
- `EXPLAIN (ANALYZE)` muestra poda de particiones; la conversión de la tabla se hizo con el servicio recibiendo carga; un usuario de un comercio no lee filas de otro ni con una consulta sin filtro.

**Aprender y documentar**
- Particionado frente a *sharding*; límites del particionado (claves únicas, claves foráneas); cómo se evalúa una política RLS.
