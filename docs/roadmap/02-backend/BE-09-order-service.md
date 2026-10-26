# BE-09 · `order-service` — hexagonal, CQRS y outbox

**Objetivo:** el corazón transaccional. Modelo de escritura consistente, modelo de lectura optimizado, eventos confiables y reglas reales de pedidos multi-comercio.

### BE-09.1 · Dominio del pedido
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-01.2, FND-03.4

**Requerimientos**
- **Hexagonal**. Agregado `Order` con máquina de estados explícita; invariantes en el dominio.
- **Carrito multi-comercio** (decisión N2): pedido padre (un pago) → sub-pedidos por comercio → envíos por tienda, con el estado del padre derivado de los hijos.
- **Ciclo del sub-pedido** (decisión N7): aceptación del comercio con plazo (vencido o rechazado → cancelación con compensación), preparación y "listo"; al marcar un envío como listo se publica `OrderReadyForDispatch`.
- Escenarios Gherkin de FND-03.4.

**Terminado cuando**
- Las transiciones inválidas son imposibles por construcción y lo verifican pruebas de propiedades.

**Aprender y documentar**
- Diseño de agregados (tamaño, invariantes, consistencia dentro y fuera del agregado).

### BE-09.2 · Persistencia, carrito y concurrencia
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-09.1, BE-07.3, DB-05.3, DB-03.1

**Requerimientos**
- Tabla de pedidos **particionada desde el nacimiento** según DB-05.3.
- Carrito del lado del servidor en Redis con TTL y fusión del carrito anónimo con el del usuario al iniciar sesión.
- Creación de pedido a partir de una cotización congelada; `Idempotency-Key` obligatoria; concurrencia optimista expuesta con `ETag`/`If-Match`.

**Terminado cuando**
- Dos peticiones simultáneas con la misma clave de idempotencia crean un solo pedido.

**Aprender y documentar**
- Implementación correcta de idempotencia (almacenamiento de la respuesta, ventana de retención, carreras).

### BE-09.3 · Outbox y consumidores idempotentes
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-09.2, DB-04.3

**Requerimientos**
- Outbox en la misma transacción que el agregado, publicado por Debezium; `traceparent` dentro del registro outbox.
- Consumidores idempotentes (registro de mensajes procesados o *upsert* por versión), manejo de orden, reintentos con *backoff*, DLT con herramienta de reprocesamiento.

**Terminado cuando**
- Matar el servicio entre el *commit* y la publicación no pierde ni duplica efectos.

**Aprender y documentar**
- Semánticas de entrega en Kafka y qué significa realmente "exactamente una vez"; grupos de consumidores y rebalanceo.

### BE-09.4 · Modelo de lectura (CQRS)
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-09.3, DB-03.2

**Requerimientos**
- Proyección en MongoDB construida por eventos y optimizada para las pantallas de cliente, comercio y soporte.
- Reconstrucción completa desde los eventos (procedimiento probado); métrica de retraso de la proyección.

**Terminado cuando**
- La proyección reconstruida desde cero coincide con la original y el retraso se muestra en un dashboard.

**Aprender y documentar**
- CQRS frente a *event sourcing* (y por qué aquí no se usa ES completo); consistencia eventual vista desde la interfaz.

### BE-09.5 · Cancelaciones y devoluciones parciales
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-11.2

**Requerimientos**
- Ventanas de cancelación según el estado de cada sub-pedido; cancelación parcial de líneas.
- **Devolución parcial con descuentos ya repartidos**: el reembolso de una línea debe devolver su parte exacta del descuento (usa el reparto de BE-07.1) y recalcular promociones condicionadas (si al devolver deja de cumplirse un "NxM", se ajusta según la regla de negocio).
- Nuevas columnas sobre la tabla particionada con volumen (ejercicio de DB-01.2).

**Terminado cuando**
- Los escenarios de devolución con promociones condicionadas reembolsan exactamente lo que especifica FND-03.4.

**Aprender y documentar**
- Por qué las devoluciones son el caso más difícil de un motor de precios.
