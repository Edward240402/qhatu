# DB-03 · NoSQL: Redis y MongoDB

### DB-03.1 · Redis
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** FND-04.1, SEC-03.2

**Requerimientos**
- `docs/estandares/redis.md`: catálogo de usos del proyecto con la estructura adecuada para cada uno — sesiones del BFF (hashes), límite de tasa (scripts Lua), caché (cadenas y hashes con TTL), índice geoespacial (GEO), contadores atómicos, conjuntos ordenados para ventanas deslizantes, estructuras probabilísticas (HyperLogLog, filtro de Bloom), *streams* o pub/sub para difusión.
- Convención de nombres de claves, TTL obligatorio salvo excepción documentada, política de expulsión, persistencia (RDB/AOF) y dimensionamiento de memoria.
- Usuarios con ACL por servicio y TLS.
- ADR Redis frente a Valkey (licencia y compatibilidad).

**Terminado cuando**
- Un servicio de ejemplo no puede leer claves de otro prefijo por ACL; existe una prueba que detecta claves sin TTL.

**Aprender y documentar**
- Cómo logra Redis la atomicidad (bucle de eventos de un hilo, Lua, `MULTI`); persistencia y sus riesgos; complejidad de cada comando usado.

### DB-03.2 · MongoDB
- **Ola:** 2 · **Profundidad:** B
- **Depende de:** FND-04.1, SEC-03.2

**Requerimientos**
- `docs/estandares/mongodb.md`: modelado por patrones de acceso (incrustar frente a referenciar), patrones (atributo, cubeta, versión de esquema), validación con JSON Schema, índices compuestos (regla ESR), colecciones *time-series*, TTL, *change streams*, transacciones y cuándo evitarlas.
- Migraciones versionadas con herramienta (Mongock o equivalente) y estrategia de migración perezosa.
- *Write concern* y *read concern* elegidos por caso de uso.

**Terminado cuando**
- Existe el documento de modelado con las consultas principales y su `explain()`.

**Aprender y documentar**
- Conjunto de réplicas y elección de primario; garantías de *write concern*; teorema CAP y PACELC aplicados a MongoDB, Redis y PostgreSQL; cuándo **no** usar NoSQL.
