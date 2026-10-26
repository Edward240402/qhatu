# BE-13 · `tracking-service` — WebFlux y backpressure

**Objetivo:** reactividad de punta a punta donde realmente aporta: un flujo masivo de posiciones GPS hacia muchos clientes conectados.

### BE-13.1 · Ingesta reactiva de posiciones
- **Ola:** 5 · **Profundidad:** A
- **Depende de:** BE-12.1

**Requerimientos**
- Spring WebFlux: ingesta por HTTP y WebSocket desde la app de repartidor (posiciones en lotes) hacia Kafka.
- **Cliente Kafka reactivo:** en el análisis, verificar el estado de soporte de Reactor Kafka. Si está descontinuado, elegir con ADR entre el *binder* reactivo de Spring Cloud Stream, un puente propio acotado sobre el cliente oficial, u otra opción vigente.
- Ninguna llamada bloqueante, verificado con BlockHound en las pruebas.

**Terminado cuando**
- El simulador de DB-02.4 (que depende de esta sub-fase) puede enviar posiciones a la tasa objetivo.

**Aprender y documentar**
- Especificación Reactive Streams (`request(n)`); *cold* frente a *hot publishers*; `publishOn` frente a `subscribeOn`.

### BE-13.2 · Almacenamiento de posiciones
- **Ola:** 5 · **Profundidad:** B
- **Depende de:** BE-13.1, DB-03.2

**Requerimientos**
- Última posición en Redis; histórico en una colección *time-series* de MongoDB con controlador reactivo, TTL y agregaciones por recorrido.

**Terminado cuando**
- El recorrido completo de una entrega se reconstruye desde el histórico.

**Aprender y documentar**
- Cómo almacena MongoDB las colecciones *time-series* (cubetas) y por qué es eficiente.

### BE-13.3 · Difusión a clientes y backpressure
- **Ola:** 5 · **Profundidad:** A
- **Depende de:** BE-13.2, DB-02.4

**Requerimientos**
- Difusión por WebSocket y SSE con autorización por pedido (el cliente solo ve a su repartidor). **(Opcional)** RSocket.
- **Backpressure explícito y demostrado**: `buffer` acotado, `drop`, `latest`, muestreo; control de demanda; límites de concurrencia en `flatMap`; pausa del consumo de Kafka cuando el destino es lento.
- Pruebas con `StepVerifier` y tiempo virtual.

**Terminado cuando**
- Con un consumidor lento conectado, la memoria se mantiene estable y la estrategia de descarte es visible en métricas; una prueba de carga sostiene la tasa objetivo.

**Aprender y documentar**
- Qué es backpressure y qué ocurre sin él; reactivo frente a virtual threads con datos de este proyecto. Experimento: provocar un desbordamiento y resolverlo con cada estrategia.

### BE-13.4 · Suavizado, geocercas y tiempo estimado
- **Ola:** 5 · **Profundidad:** A
- **Depende de:** BE-13.3

**Requerimientos**
- **Suavizado del ruido del GPS** con un filtro de Kalman simple (O(1) por punto) y descarte de saltos imposibles por velocidad.
- **Geocercas**: detección de llegada a tienda y a destino con prefiltro por celda H3 y punto-en-polígono (O(v) solo en las celdas candidatas).
- Tiempo estimado de llegada incremental (se mejora con el modelo de ML en la ola 7, opcional).

**Terminado cuando**
- Con GPS ruidoso del simulador, la llegada se detecta sin falsos positivos en los escenarios de prueba.

**Aprender y documentar**
- Filtro de Kalman en una dimensión explicado sin rodeos; algoritmo de punto-en-polígono por trazado de rayos.
