# BE-06 · `inventory-service` — hexagonal, gRPC y concurrencia extrema

**Objetivo:** reservar stock correctamente bajo miles de peticiones concurrentes sobre los mismos productos, y decidir desde qué tiendas se atiende un pedido.

### BE-06.1 · Dominio hexagonal de existencias
- **Ola:** 2 · **Profundidad:** A
- **Depende de:** BE-01.2, DB-01.2

**Requerimientos**
- **Hexagonal** en Quarkus: puertos de entrada y salida, dominio sin anotaciones de framework.
- Existencias por tienda (un comercio tiene varias tiendas), reservas con expiración, tabla de movimientos (crecerá mucho: se particionará en DB-05.3).
- Imperativo sobre virtual threads (`@RunOnVirtualThread`).

**Terminado cuando**
- Las invariantes (nunca existencias negativas, reservas que no superan lo disponible) están cubiertas por pruebas de dominio.

**Aprender y documentar**
- Puertos y adaptadores: qué va dónde y cómo se prueba cada lado.

### BE-06.2 · API gRPC
- **Ola:** 2 · **Profundidad:** B
- **Depende de:** BE-06.1

**Requerimientos**
- Contrato proto (reservar, confirmar, liberar) con *deadlines*, códigos de estado correctos, reintentos configurados en el cliente y metadatos de traza; REST para administración.
- Idempotencia de comandos por clave.

**Terminado cuando**
- Un cliente con *deadline* vencido recibe `DEADLINE_EXCEEDED` y la reserva no queda a medias.

**Aprender y documentar**
- HTTP/2 y Protobuf: por qué gRPC es más rápido y qué se pierde frente a REST.

### BE-06.3 · Estrategias de concurrencia comparadas
- **Ola:** 2 · **Profundidad:** A
- **Depende de:** BE-06.2, OPS-02.2, DB-02.2

**Requerimientos**
- Cuatro estrategias implementadas detrás del mismo puerto: bloqueo optimista con reintento, bloqueo pesimista (`SELECT … FOR UPDATE`), actualización atómica condicional en SQL, contador atómico en Redis (Lua) con reconciliación a PostgreSQL.
- Pruebas de concurrencia deterministas y prueba de carga con el objetivo de FND-03.2; la ganadora queda por defecto, con ADR.

**Terminado cuando**
- Cero sobreventa bajo la carga objetivo y latencia p99 dentro de umbral; informe comparativo publicado.

**Aprender y documentar**
- MVCC, niveles de aislamiento y anomalías en PostgreSQL; bloqueo optimista frente a pesimista. Experimentos: reproducir una actualización perdida y un interbloqueo.

### BE-06.4 · Asignación de tiendas a un pedido
- **Ola:** 2 · **Profundidad:** A
- **Depende de:** BE-06.3

**Requerimientos**
- Dado un carrito de *m* productos y las *n* tiendas del comercio **abiertas** y dentro del radio de entrega (datos de tiendas replicados desde `StoreChanged`), elegir desde dónde se atiende. Cada tienda elegida genera un envío (decisión N2) y no altera la tarifa ya cotizada (decisión N5):
  1. preferir **una sola tienda** que tenga todo: representación de disponibilidad por tienda como conjunto de bits, verificación O(n·m/64);
  2. si ninguna cubre todo, dividir en el **mínimo número de tiendas**: es el problema de cobertura de conjuntos (NP-difícil). Se usa el algoritmo voraz con garantía de aproximación logarítmica y un límite máximo de tiendas por pedido;
  3. desempate por distancia al cliente.
- Escenarios Gherkin de FND-03.4, benchmark JMH y pruebas de propiedades (la solución siempre cubre el carrito y nunca supera el límite de tiendas).

**Terminado cuando**
- El algoritmo cumple los escenarios y su latencia está dentro del presupuesto de la reserva.

**Aprender y documentar**
- Cobertura de conjuntos, por qué es NP-difícil y qué garantiza la aproximación voraz; cuándo una heurística es la decisión correcta de ingeniería.

### BE-06.5 · Eventos, expiración y tolerancia a fallos
- **Ola:** 2 · **Profundidad:** A
- **Depende de:** BE-06.4, DB-04.3

**Requerimientos**
- Outbox para `StockReserved`, `StockReleased`, `StockDepleted`.
- Expiración de reservas con trabajadores concurrentes usando `FOR UPDATE SKIP LOCKED`.
- SmallRye Fault Tolerance (equivalente de Resilience4j en Quarkus), comparado después con BE-10.2.

**Terminado cuando**
- Varias réplicas expiran reservas en paralelo sin procesar dos veces la misma.

**Aprender y documentar**
- Colas sobre PostgreSQL con `SKIP LOCKED`: por qué funciona y sus límites.
