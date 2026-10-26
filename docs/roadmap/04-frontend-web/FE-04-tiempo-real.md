# FE-04 · Tiempo real: Google Maps y WhatsApp

### FE-04.1 · Direcciones y cobertura con Google Maps
- **Ola:** 5 · **Profundidad:** B
- **Depende de:** FE-03.3, BE-04.2

**Requerimientos**
- Autocompletado de direcciones (Places) con tokens de sesión, geocodificación, validación de zona de cobertura.
- Clave restringida por dominio y por API; carga diferida del SDK; cuotas y coste controlados.
- Capa de abstracción del proveedor de mapas.

**Terminado cuando**
- Una dirección fuera de cobertura se rechaza antes del *checkout* y el consumo de la API está medido.

**Aprender y documentar**
- Modelo de precios de Google Maps Platform y cómo no gastar de más.

### FE-04.2 · Seguimiento en vivo
- **Ola:** 5 · **Profundidad:** B
- **Depende de:** FE-04.1, BE-13.3

**Requerimientos**
- Mapa con la ruta y el marcador del repartidor con interpolación suave; tiempo estimado.
- WebSocket o SSE con reconexión con *backoff*, reanudación y control del ritmo de actualización en el cliente.

**Terminado cuando**
- Con el simulador en marcha, el recorrido se ve en vivo y la conexión se recupera sola tras un corte de red.

**Aprender y documentar**
- WebSocket frente a SSE frente a *polling*; RxJS frente a *signals* para flujos en tiempo real.

### FE-04.3 · WhatsApp y centro de notificaciones
- **Ola:** 5 · **Profundidad:** B
- **Depende de:** FE-04.2, BE-14.2

**Requerimientos**
- Consentimiento explícito para avisos por WhatsApp; enlace de conversación con soporte con el contexto del pedido; historial de notificaciones enviadas.
- Centro de notificaciones en la aplicación.

**Terminado cuando**
- El usuario puede dar y retirar el consentimiento y el cambio se respeta en el siguiente evento.

**Aprender y documentar**
- Consentimiento y privacidad en canales de mensajería.
