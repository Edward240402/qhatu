# FE-02 · Búsqueda, catálogo, carrito y caché

### FE-02.1 · Búsqueda y catálogo
- **Ola:** 3 · **Profundidad:** B
- **Depende de:** FE-01.2, BE-08.3

**Requerimientos**
- Búsqueda con autocompletado (con cancelación de peticiones obsoletas y *debounce*), facetas, filtros y orden, resultados con resaltado, ordenamiento por cercanía de tienda.
- Detalle de producto con variantes, imágenes optimizadas (`NgOptimizedImage`, tamaños adaptables) y reseñas.
- *Scroll* virtual para listados largos; estado de la búsqueda reflejado en la URL (sin datos sensibles).

**Terminado cuando**
- Las E2E cubren búsqueda con sinónimos, facetas y navegación al detalle.

**Aprender y documentar**
- Gestión de condiciones de carrera en búsquedas en vivo (cancelación con RxJS frente a recursos con *signals*).

### FE-02.2 · Caché en capas, PWA y SSR
- **Ola:** 3 · **Profundidad:** B
- **Depende de:** FE-02.1, BE-05.4

**Requerimientos**
- Capas de caché con propósito e invalidación definidos: HTTP (`ETag`, `Cache-Control`, `stale-while-revalidate`) coordinada con BE-05.4; en memoria por consulta; **Service Worker** (recursos estáticos y lecturas del catálogo sin conexión); estado transferido desde SSR.
- SSR con hidratación para páginas públicas (ADR); medición de Core Web Vitals contra presupuestos.

**Terminado cuando**
- El catálogo visitado se navega sin conexión y cada capa tiene documentado cómo se invalida.

**Aprender y documentar**
- Ciclo de vida de un Service Worker y sus estrategias de caché; semántica de las cabeceras de caché HTTP.

### FE-02.3 · Carrito
- **Ola:** 4 · **Profundidad:** B
- **Depende de:** FE-02.2, BE-09.2

**Requerimientos**
- Carrito multi-comercio sincronizado con el servidor (BE-09.2), con fusión al iniciar sesión.
- Estado con *signals* (almacén basado en *signals*; ADR frente a NgRx clásico); actualizaciones optimistas con reversión ante error.

**Terminado cuando**
- Un fallo del servidor revierte la actualización optimista con un mensaje claro y sin estados intermedios incoherentes.

**Aprender y documentar**
- Actualizaciones optimistas y reconciliación de estado.
