# BE-11 · Saga de compra

**Objetivo:** transacción distribuida de compra con consistencia garantizada sin 2PC, respetando las decisiones N6 a N8.

### BE-11.1 · Orquestador y camino feliz
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-09.4, BE-10.2, BE-06.5

**Requerimientos**
- **Saga orquestada** en `order-service`: validar cotización → reservar stock de todos los sub-pedidos (gRPC, todo o nada) → autorizar el pago (incluye 3-D Secure, con espera asíncrona del resultado) → esperar la aceptación de cada comercio → capturar → confirmar stock. El despacho no es un paso de la saga: lo inicia el comercio al marcar el envío como listo (decisión N7).
- **Tiempos derivados** (decisión N8): caducidad de la reserva mayor que el *timeout* del paso de pago; plazo de aceptación del comercio menor que la validez de la autorización.
- Estado de la saga persistido; comandos y respuestas por Kafka; *timeout* por paso.
- Identificación de pasos compensables, pivote y reintentables.
- ADR: orquestador propio frente a un motor de flujos (Temporal u otro).

**Terminado cuando**
- Una compra completa recorre todos los pasos y se ve como una traza.

**Aprender y documentar**
- Por qué no 2PC; garantías de una saga frente a ACID; orquestación frente a coreografía.

### BE-11.2 · Compensaciones y recuperación
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-11.1

**Requerimientos**
- Compensaciones: liberar stock, anular la autorización, reembolsar. Antes del cobro el fallo es todo o nada; tras la captura, el rechazo o la cancelación de un sub-pedido produce reembolso parcial de ese sub-pedido (decisión N6), con el descuento revertido a su financiador (N4).
- Recuperación tras la caída del orquestador en cualquier punto.
- Mitigación de la falta de aislamiento: bloqueo semántico con estados `PENDING`, relectura de valores.

**Terminado cuando**
- Cada escenario de fallo (sin stock en un comercio, pago rechazado, 3-D Secure abandonado, pago con *timeout*, comercio que no acepta a tiempo, caída del orquestador a mitad) termina en un estado consistente, verificado automáticamente.

**Aprender y documentar**
- Anomalías por falta de aislamiento en sagas y sus contramedidas.

### BE-11.3 · Operación de sagas y coreografía
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-11.2

**Requerimientos**
- Vista de administración del estado de cada saga y acción manual auditada para sagas atascadas.
- Pruebas de extremo a extremo de cada camino de fallo sobre el sistema en Compose.
- Diseño de la **coreografía** de despacho → notificación (se implementa en BE-12 y BE-14) y comparación escrita entre ambos estilos.
- **(Opcional)** la misma saga con el motor de flujos en una rama de comparación.

**Terminado cuando**
- Una saga atascada a propósito se detecta, se alerta y se resuelve desde la vista de administración.

**Aprender y documentar**
- Operar sagas en producción: observabilidad, intervención manual y cuándo un humano debe decidir.
