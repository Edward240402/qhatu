# MOB-04 · Mapas, seguimiento, notificaciones y modo repartidor

### MOB-04.1 · Seguimiento, *push* y WhatsApp
- **Ola:** 9 · **Profundidad:** B
- **Depende de:** MOB-03.2, BE-13.3, BE-14.3

**Requerimientos**
- Google Maps: autocompletado de direcciones y seguimiento en vivo con reconexión.
- Notificaciones *push* (FCM) con enlaces profundos al pedido; enlace a WhatsApp con contexto.

**Terminado cuando**
- Una notificación abre la app en el pedido correcto, incluso con la app cerrada.

**Aprender y documentar**
- Cómo funcionan FCM y APNs.

### MOB-04.2 · Modo repartidor
- **Ola:** 9 · **Profundidad:** B
- **Depende de:** MOB-04.1, BE-12.2

**Requerimientos**
- Aceptar o rechazar pedidos, navegación, **ubicación en segundo plano** con permisos bien pedidos, envío por lotes adaptado a batería y red, almacenamiento temporal sin señal.
- Prueba de entrega con foto y código.

**Terminado cuando**
- Una entrega completa se realiza con dos dispositivos y el seguimiento sobrevive a que la app pase a segundo plano.

**Aprender y documentar**
- Restricciones de ejecución en segundo plano de Android e iOS; consumo de batería del GPS.
