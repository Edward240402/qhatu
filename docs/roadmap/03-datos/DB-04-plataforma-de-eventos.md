# DB-04 · Plataforma de eventos: Kafka, registro de esquemas y CDC

**Objetivo:** que cuando los servicios empiecen a publicar eventos (ola 2), la plataforma ya tenga sus reglas, su gobierno de esquemas y su mecanismo de publicación confiable.

### DB-04.1 · Kafka como plataforma
- **Ola:** 2 · **Profundidad:** A
- **Depende de:** FND-04.2, SEC-03.2, FND-03.3

**Requerimientos**
- Ampliación de `docs/estandares/eventos.md`: nombres de temas, número de particiones y factor de réplica, retención frente a compactación por tema, `min.insync.replicas`, configuración estándar de productores (`acks=all`, idempotencia) y consumidores (confirmación manual, aislamiento `read_committed` donde aplique), política de reintentos y temas de mensajes muertos.
- Temas declarados como código (no autocreación).
- ACL por servicio con identidad mTLS.

**Terminado cuando**
- Un servicio no puede publicar en un tema ajeno; perder un *broker* del perfil de tres no pierde mensajes confirmados.

**Aprender y documentar**
- Registro distribuido, particiones, réplicas, ISR y elección de líder; semánticas de entrega; por qué el orden solo existe por partición. Experimento: matar al líder durante una producción con `acks=1` y con `acks=all`.

### DB-04.2 · Registro de esquemas y evolución
- **Ola:** 2 · **Profundidad:** A
- **Depende de:** DB-04.1

**Requerimientos**
- Avro o Protobuf (ADR) para eventos; reglas de compatibilidad por tema (hacia atrás por defecto).
- Generación de código desde esquemas; verificación de compatibilidad en el PR (se automatiza en OPS-03.3).
- Enlace entre AsyncAPI y los esquemas del registro.

**Terminado cuando**
- Un cambio incompatible de esquema es rechazado antes de llegar a `main`.

**Aprender y documentar**
- Compatibilidad hacia atrás, hacia adelante y completa, con ejemplos de cambios permitidos y prohibidos; formato binario y su relación con el registro.

### DB-04.3 · Kafka Connect y Debezium
- **Ola:** 2 · **Profundidad:** A
- **Depende de:** DB-04.2, DB-01.2

**Requerimientos**
- Kafka Connect en modo distribuido; Debezium para PostgreSQL con el **enrutador de eventos outbox** (tabla outbox → tema por agregado) y conector de MongoDB.
- Vigilancia de los *slots* de replicación (un *slot* abandonado llena el disco del servidor de base de datos) con alerta.
- Primer adoptante real: `customer-service` publica `MerchantChanged` y `StoreChanged` mediante outbox (consumidos después por inventario, búsqueda y precios). Sirve de referencia para BE-05 y BE-06.

**Terminado cuando**
- Un registro insertado en una tabla outbox de ejemplo aparece en su tema con la clave y las cabeceras correctas, incluso tras reiniciar Connect.

**Aprender y documentar**
- WAL y replicación lógica de PostgreSQL; cómo Debezium lee el WAL y guarda su posición; el problema de la doble escritura que resuelve el outbox.
