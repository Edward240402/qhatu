# FND-04 · Infraestructura local con Docker Compose

**Objetivo:** levantar la infraestructura de apoyo con un comando, con consumo de memoria controlado. La seguridad de transporte (TLS) llega en SEC-03.2, dentro de la misma ola 0.

### FND-04.1 · Almacenes de datos
- **Ola:** 0 · **Profundidad:** B
- **Depende de:** FND-02.1

**Requerimientos**
- `deploy/compose/` con **perfiles** (`core`, `messaging`, `search`, `observability`, `analytics`, `full`) para trabajar con 16 GB levantando solo lo necesario.
- PostgreSQL, Redis, MongoDB (conjunto de réplicas de un nodo, necesario para transacciones y *change streams*) y almacenamiento de objetos compatible con S3. Verificar en el análisis el estado de la edición comunitaria de MinIO; alternativas: SeaweedFS, Garage, LocalStack.
- `healthcheck` y `depends_on: condition: service_healthy` en todo; volúmenes con nombre; límites de recursos.
- `.env` ignorado y `.env.example` versionado.
- `Taskfile` (o `Makefile`) con `up`, `down`, `reset`, `logs`, `status`, ejecutado siempre desde WSL.
- Primera versión de `docs/operacion/03-docker-compose.md`.

**Terminado cuando**
- Desde un clon limpio, `task up PROFILE=core` deja todo sano y `task reset` lo devuelve a cero.

**Aprender y documentar**
- Redes, volúmenes y DNS interno de Docker; por qué los *healthchecks* importan para el orden de arranque.

### FND-04.2 · Mensajería y búsqueda
- **Ola:** 0 · **Profundidad:** B
- **Depende de:** FND-04.1

**Requerimientos**
- Kafka en modo KRaft (tres *brokers* en el perfil `full` para poder experimentar con réplicas; uno en `messaging`), registro de esquemas e interfaz web para Kafka.
- Elasticsearch y Kibana con seguridad activada (la seguridad de Elasticsearch no se desactiva ni en local).
- Mailpit como servidor de correo local.

**Terminado cuando**
- Se produce y consume un mensaje de prueba; Elasticsearch responde con autenticación.

**Aprender y documentar**
- Por qué Kafka ya no usa ZooKeeper (KRaft); qué hace el registro de esquemas.
