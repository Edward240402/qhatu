# DB-06 · Almacén analítico

### DB-06.1 · ClickHouse e ingesta desde Kafka
- **Ola:** 6 · **Profundidad:** B
- **Depende de:** DB-04.3, BE-11.3

**Requerimientos**
- ClickHouse con tablas `MergeTree` cuya clave de ordenación y partición salen de las consultas de los dashboards; ingesta desde Kafka con garantías explícitas (deduplicación por clave de evento).
- TTL de datos, compresión por columna medida.

**Terminado cuando**
- Un pedido creado aparece en ClickHouse en segundos y el conteo concilia con el origen.

**Aprender y documentar**
- Almacenamiento columnar, índices dispersos, *parts* y *merges*; por qué ClickHouse no es una base OLTP.

### DB-06.2 · Modelo dimensional, calidad y linaje
- **Ola:** 6 · **Profundidad:** B
- **Depende de:** DB-06.1

**Requerimientos**
- Hechos (pedidos, líneas, pagos, entregas, liquidaciones) y dimensiones (producto, comercio, zona, tiempo, cliente seudonimizado).
- Vistas materializadas para agregados de los dashboards.
- Validaciones de calidad automatizadas y conciliación de conteos y sumas con el origen.
- Linaje documentado: de qué evento sale cada tabla.
- **(Opcional)** dbt para las transformaciones.

**Terminado cuando**
- Las consultas de los dashboards responden dentro del objetivo sobre el perfil `L`.

**Aprender y documentar**
- Modelado dimensional (estrella, dimensiones lentamente cambiantes); OLTP frente a OLAP.
