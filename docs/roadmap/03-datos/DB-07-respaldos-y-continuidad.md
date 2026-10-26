# DB-07 · Volcados, respaldos y continuidad

### DB-07.1 · Volcados lógicos y restauración
- **Ola:** 6 · **Profundidad:** A
- **Depende de:** DB-02.3, DB-06.1

**Requerimientos**
- `pg_dump` en formatos *custom* y *directory*, en paralelo, completo y selectivo (esquema, tabla, solo datos); `pg_restore` selectivo y en paralelo; manejo de roles y propietarios.
- Equivalentes para MongoDB (`mongodump`), Elasticsearch (*snapshots*) y ClickHouse.
- Volcados cifrados al almacenamiento de objetos con retención.
- **Prueba de restauración automatizada y programada**: un respaldo no probado no cuenta.

**Terminado cuando**
- Un flujo programado restaura el último volcado en un entorno limpio y verifica conteos.

**Aprender y documentar**
- Consistencia de un volcado lógico (instantánea MVCC); por qué un volcado no sirve para recuperación a un punto en el tiempo.

### DB-07.2 · Recuperación a un punto en el tiempo y simulacro
- **Ola:** 6 · **Profundidad:** A
- **Depende de:** DB-07.1

**Requerimientos**
- Respaldo físico con archivado continuo de WAL (pgBackRest o equivalente) al almacenamiento de objetos.
- **Simulacro**: borrado accidental de datos en `order-service` y recuperación al instante anterior, midiendo RPO y RTO contra los objetivos de FND-03.2.
- En Kubernetes, respaldos programados con el operador de CloudNativePG.

**Terminado cuando**
- El simulacro documentado recupera los datos dentro del RTO.

**Aprender y documentar**
- Respaldo físico frente a lógico; cómo funciona PITR con WAL; RPO y RTO en la práctica.

### DB-07.3 · Volcados anonimizados para entornos inferiores
- **Ola:** 6 · **Profundidad:** B
- **Depende de:** DB-07.1, SEC-04.1

**Requerimientos**
- Proceso que produce un volcado utilizable con datos personales enmascarados o seudonimizados de forma consistente entre servicios (el mismo cliente sigue siendo el mismo).
- Verificación automática de que no queda ningún dato personal en claro.

**Terminado cuando**
- El volcado anonimizado pasa la verificación y restaura un entorno funcional.

**Aprender y documentar**
- Anonimización frente a seudonimización y sus límites (reidentificación).
