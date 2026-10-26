# BE-12 · `dispatch-service` — orientado a eventos y algoritmos de asignación

**Objetivo:** asignar repartidores y agrupar entregas reaccionando solo a eventos, con algoritmos de asignación y rutas cuya calidad y coste estén medidos.

### BE-12.1 · Esqueleto orientado a eventos
- **Ola:** 5 · **Profundidad:** A
- **Depende de:** BE-11.3, DB-03.1

**Requerimientos**
- Sin API síncrona en el camino crítico: consume `OrderReadyForDispatch` (uno por envío, decisión N2), publica `CourierAssigned`, `DeliveryStarted`, `DeliveryCompleted`.
- Adopción en `catalog-service`: adaptador real de `PurchaseVerifier` a partir de `DeliveryCompleted` y activación de la creación de reseñas (decisión N10).
- Estado de repartidores (disponible, en ruta, en pausa) y posición en Redis GEO.

**Terminado cuando**
- Un pedido listo produce eventos de asignación y entrega en el orden correcto.

**Aprender y documentar**
- Notificación por evento frente a transferencia de estado por evento.

### BE-12.2 · Algoritmo de asignación por lotes
- **Ola:** 5 · **Profundidad:** A
- **Depende de:** BE-12.1, DB-02.4

**Requerimientos**
- Asignación **por lotes** cada pocos segundos y por zona, en lugar de "el más cercano" uno a uno (que es localmente bueno y globalmente malo).
- Matriz de costos repartidor × pedido (tiempo estimado con distancia y factor de vía) con **poda de candidatos**: solo los *k* más cercanos por pedido mediante Redis GEO, O(n·k) en lugar de O(n²).
- Dos estrategias comparadas: **algoritmo húngaro** (óptimo, O(n³), viable con lotes acotados por zona) y **voraz** sobre aristas ordenadas (O(E log E)). Calidad (tiempo total de espera) frente a latencia de cálculo, medidas con el simulador.
- Bloqueo distribuido con *fencing token* para que un repartidor nunca reciba dos asignaciones simultáneas; reasignación por rechazo o tiempo de espera.

**Terminado cuando**
- El informe muestra calidad y latencia de ambas estrategias en varios tamaños de lote, y nunca hay doble asignación bajo concurrencia.

**Aprender y documentar**
- Problema de asignación y algoritmo húngaro; por qué los bloqueos en Redis necesitan *fencing tokens*.

### BE-12.3 · Agrupación de pedidos y rutas
- **Ola:** 5 · **Profundidad:** A
- **Depende de:** BE-12.2

**Requerimientos**
- Agrupar varios pedidos en un mismo repartidor cuando comparten zona y ventana de tiempo.
- Ruta con restricciones de precedencia (recoger antes de entregar) y ventanas de entrega: inserción más barata + mejora 2-opt respetando restricciones, con un máximo de paradas que acota el costo a O(s²) por iteración.
- Comparación con la ruta óptima por fuerza bruta en instancias pequeñas, para medir el error de la heurística.

**Terminado cuando**
- La heurística queda dentro del margen de error definido frente al óptimo en las instancias pequeñas.

**Aprender y documentar**
- Problema de rutas de vehículos con recogida y entrega; heurísticas constructivas y de mejora local.

### BE-12.4 · Agregaciones en tiempo real con Kafka Streams
- **Ola:** 5 · **Profundidad:** A
- **Depende de:** BE-12.3

**Requerimientos**
- Topología de Kafka Streams: pedidos pendientes y repartidores disponibles por zona en ventanas deslizantes; tiempos de espera; **relación oferta/demanda por zona** publicada para el recargo de BE-07.4.
- *State stores*, consultas interactivas, manejo de eventos tardíos (*grace period*).
- Concurrencia estructurada de Java 25 (en vista previa: activada de forma explícita y aislada, con ADR) para consultar fuentes en paralelo con cancelación.

**Terminado cuando**
- Las agregaciones alimentan un dashboard en vivo y sobreviven al reinicio de la instancia sin perder estado.

**Aprender y documentar**
- Topologías, *changelog topics*, ventanas y tiempo de evento frente a tiempo de proceso en Kafka Streams.
