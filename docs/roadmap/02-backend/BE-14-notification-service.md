# BE-14 · `notification-service` — mensajería reactiva y WhatsApp

**Objetivo:** notificar por varios canales sin acoplarse a quien origina el evento (coreografía).

### BE-14.1 · Consumo, plantillas y preferencias
- **Ola:** 5 · **Profundidad:** B
- **Depende de:** BE-11.3, BE-01.2

**Requerimientos**
- Quarkus con SmallRye Reactive Messaging consumiendo eventos de pedido, pago y despacho.
- Plantillas versionadas e internacionalizadas; preferencias y consentimiento del usuario; **horario de silencio** con reprogramación solo para mensajes no urgentes, nunca para los transaccionales (decisión N11).
- Entrega al menos una vez con deduplicación; registro en MongoDB con TTL.

**Terminado cuando**
- Un mismo evento recibido dos veces produce una sola notificación.

**Aprender y documentar**
- Modelo de canales de Reactive Messaging, *acknowledgement* y estrategias de fallo.

### BE-14.2 · WhatsApp Cloud API
- **Ola:** 5 · **Profundidad:** B
- **Depende de:** BE-14.1

**Requerimientos**
- Adaptador de WhatsApp Cloud API: plantillas aprobadas, *opt-in*, ventana de servicio de 24 h, webhooks de estado de entrega (firmados), límites de tasa del proveedor.
- Simulador local del proveedor para pruebas.

**Terminado cuando**
- Un cambio de estado del pedido produce un mensaje real en el entorno de pruebas de Meta y su estado de entrega queda registrado.

**Aprender y documentar**
- Cómo funciona la API de WhatsApp Business (plantillas, ventana de 24 h, categorías y su coste).

### BE-14.3 · Correo, *push* y conmutación de canal
- **Ola:** 5 · **Profundidad:** B
- **Depende de:** BE-14.2

**Requerimientos**
- Correo (Mailpit en local; servicio gestionado en la nube en INF-04/05) y *push* con FCM.
- Reintentos con *backoff*, DLT, límite de tasa por proveedor y **conmutación de canal** ante fallo según prioridad del mensaje.

**Terminado cuando**
- La caída de un proveedor no bloquea los demás canales y los mensajes críticos llegan por el alternativo.

**Aprender y documentar**
- Patrón de cola de mensajes muertos y reprocesamiento.
