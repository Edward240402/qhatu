# BE-10 · `payment-service` — Resilience4j, webhooks y riesgo

**Objetivo:** cobrar de forma segura contra pasarelas externas que fallan, y detectar fraude.

### BE-10.1 · Dominio de pagos y primera pasarela
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-01.2, SEC-04.1

**Requerimientos**
- **Hexagonal** con puerto `PaymentGateway`; adaptador de la primera pasarela con sandbox en Perú (candidatas: Culqi, Mercado Pago, Izipay, Niubiz; se confirma en el análisis).
- Máquina de estados (autorizado, capturado, anulado, fallido, reembolsado total o parcial, en revisión); **autorización por el total y captura posterior** (decisión N6), verificando en el análisis qué permiten las pasarelas elegidas (captura diferida, plazo de la autorización, anulación); idempotencia estricta en cada operación.
- Tokenización en el cliente: el backend nunca ve números de tarjeta (alcance PCI DSS mínimo, documentado).

**Terminado cuando**
- Un cobro y un reembolso funcionan contra el sandbox y repetir la petición no cobra dos veces.

**Aprender y documentar**
- Flujo de un pago con tarjeta (autorización, captura, liquidación); qué es el alcance PCI.

### BE-10.2 · Segunda pasarela y resiliencia completa
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-10.1

**Requerimientos**
- Segundo adaptador y enrutamiento por configuración y por salud.
- **Resilience4j razonado**: *circuit breaker* (ventana deslizante), *retry* con *backoff* exponencial y *jitter* solo donde es seguro, *time limiter*, *bulkhead* (semáforo frente a *pool* de hilos y su relación con virtual threads), *rate limiter*; orden de composición justificado; métricas en Grafana.
- Comparación con las anotaciones de resiliencia de Spring Framework 7 y con SmallRye Fault Tolerance (BE-06.5).
- Pruebas con WireMock y Toxiproxy (latencia, cortes, respuestas corruptas).

**Terminado cuando**
- Con la pasarela primaria degradada, el circuito abre, se conmuta a la secundaria y nadie es cobrado dos veces, demostrado por prueba automatizada y dashboard.

**Aprender y documentar**
- Cada patrón de resiliencia: qué fallo evita y qué fallo puede causar (tormentas de reintentos). Experimentos con Toxiproxy para abrir y cerrar el circuito.

### BE-10.3 · Webhooks entrantes y conciliación
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-10.2

**Requerimientos**
- Recepción de webhooks de las pasarelas: verificación de firma, protección contra repetición (marca de tiempo y nonce), respuesta inmediata y procesamiento asíncrono, idempotencia por identificador del evento.
- Túnel local (cloudflared o similar, ADR) para recibir webhooks del sandbox en desarrollo.
- **Conciliación** periódica contra la pasarela para estados inciertos (webhook perdido, *timeout* en la captura).

**Terminado cuando**
- Un webhook repetido o con firma inválida no tiene efecto, y un pago con webhook perdido se resuelve por conciliación.

**Aprender y documentar**
- Webhooks frente a *polling*; firma HMAC; por qué un webhook nunca es la única fuente de verdad.

### BE-10.4 · Módulo de riesgo y fraude
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-10.3, DB-03.1

**Requerimientos**
- **Controles de velocidad** con ventanas deslizantes en conjuntos ordenados de Redis (intentos por huella de tarjeta que entregue la pasarela —los tokens suelen ser de un solo uso—, por dispositivo, por dirección): O(log n) por evento.
- **Lista de bloqueo con filtro de Bloom** (comprobación O(k), sin falsos negativos, con tasa de falsos positivos dimensionada) con verificación exacta posterior.
- Puntuación de riesgo por reglas ponderadas; decisión aprobar, revisar o rechazar; cola de revisión manual para soporte.

**Terminado cuando**
- Una ráfaga de intentos con tarjetas distintas desde un mismo dispositivo es detenida, y la tasa de falsos positivos del filtro medida coincide con la diseñada.

**Aprender y documentar**
- Filtros de Bloom (fórmula de falsos positivos); ventanas deslizantes exactas frente a aproximadas.
