# BE-07 · `pricing-service` — precios, promociones y tarifas

**Objetivo:** el motor de reglas de negocio más complejo del sistema. Calcula cuánto paga el cliente: precios, IGV, promociones combinables, tarifa de envío y recargo dinámico, con explicación de cada cálculo.

**Arquitectura:** núcleo funcional e inmutable (el cálculo es una función pura de sus entradas) con una capa imperativa que carga datos y publica eventos. Facilita las pruebas de propiedades, el benchmark y la explicación del resultado.

### BE-07.1 · Dinero, impuestos y listas de precios
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-01.2, FND-03.4

**Requerimientos**
- Tipo `Money` propio (`BigDecimal` con escala fija y redondeo `HALF_EVEN` documentado); nunca `double`.
- IGV (18 %): el precio al consumidor siempre lo incluye; el comercio puede cargar precios con o sin IGV y se normalizan (decisión N3). Redondeo por línea frente a por total con su justificación.
- **Reparto de descuentos entre líneas sin perder céntimos**: método del mayor residuo, O(n log n), con la propiedad de que la suma repartida es exactamente el total (prueba de propiedades).
- Réplica local de los precios de lista desde `ProductChanged` (el dueño es el catálogo, decisión N1), con historial por vigencia: permite cotizar sin llamadas síncronas y auditar el precio de cualquier fecha en O(log n).

**Terminado cuando**
- Las propiedades de reparto y redondeo se cumplen para entradas aleatorias.

**Aprender y documentar**
- Aritmética decimal frente a binaria; modos de redondeo y su sesgo.

### BE-07.2 · Motor de promociones
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-07.1, DB-03.1

**Requerimientos**
- Tipos: porcentaje, monto fijo, NxM, paquete, escalonado por cantidad o monto, envío gratis, cupón.
- Cada promoción declara su **financiador** (plataforma o comercio) y solo aplica a productos del comercio que la financia, salvo las de plataforma (decisión N4). El desglose de la cotización conserva el financiador por línea para la liquidación y las devoluciones.
- Condiciones como **especificaciones componibles** (patrón *Specification*): producto, categoría, comercio, zona, franja horaria, primer pedido, segmento.
- Reglas de combinación: prioridad, grupos de exclusión, acumulables o no, topes por usuario (contadores atómicos en Redis) y **presupuesto por campaña** consumido de forma atómica.
- **Selección de la mejor combinación**: el problema general es exponencial en el número de promociones aplicables. Se acota: índice de promociones por producto y categoría para que la evaluación de elegibilidad sea O(líneas × promociones candidatas) y no O(líneas × todas); búsqueda con poda (*branch and bound*) sobre grupos de exclusión con un máximo de promociones simultáneas definido por negocio. Complejidad y cota documentadas.
- **Explicación** del resultado: qué promoción se aplicó, cuál no y por qué.
- Escenarios Gherkin de FND-03.4 ejecutados con Cucumber.

**Terminado cuando**
- Todos los escenarios pasan, el benchmark JMH cumple el presupuesto de latencia con el máximo de promociones, y el presupuesto de una campaña nunca se excede bajo concurrencia.

**Aprender y documentar**
- Motores de reglas propios frente a Drools u otros (ADR); *branch and bound*; por qué acotar el problema es una decisión de producto.

### BE-07.3 · Cotización congelada y eventos
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-07.2, DB-04.3

**Requerimientos**
- API de **cotización**: devuelve un identificador de cotización con su desglose, firmado y con caducidad; `order-service` compra con esa cotización y no recalcula, evitando la carrera entre cambio de precio y compra.
- Caché de listas de precios y promociones activas con invalidación por evento.
- Eventos `PriceChanged` y `PromotionActivated` para búsqueda y analítica.

**Terminado cuando**
- Una cotización alterada o caducada es rechazada; la latencia p99 de cotización está dentro del objetivo.

**Aprender y documentar**
- Firmas para integridad de datos entre servicios; consistencia entre lo que el cliente vio y lo que paga.

### BE-07.4 · Tarifa de envío y recargo dinámico
- **Ola:** 5 · **Profundidad:** A
- **Depende de:** BE-07.3, BE-12.4

**Requerimientos**
- Zonas como **rejilla hexagonal H3**: una tarifa por sub-pedido según la zona del cliente y la del comercio, nunca según la tienda (decisión N5), con búsqueda de zona en O(1).
- Interacción con promociones: "envío gratis" cubre la tarifa base; el recargo se cobra salvo indicación de la promoción (decisión N5).
- **Recargo dinámico** a partir de la relación oferta/demanda por zona que calcula Kafka Streams en BE-12.4, con suavizado para evitar oscilaciones, límites máximos y transparencia para el cliente.
- Recargo incluido en la cotización congelada.

**Terminado cuando**
- Con el simulador generando demanda en una zona, el recargo sube de forma suave y se mantiene dentro de sus límites.

**Aprender y documentar**
- Índices geoespaciales jerárquicos (H3 frente a geohash); amortiguamiento de señales para precios.
