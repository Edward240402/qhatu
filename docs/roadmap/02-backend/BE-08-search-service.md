# BE-08 · `search-service` — Elasticsearch

**Objetivo:** búsqueda de productos de calidad profesional. Es un **modelo de lectura** que agrega datos de varios servicios (catálogo, existencias, precios, tiendas), el caso real que justifica un servicio de búsqueda separado.

**Runtime:** Spring Boot + cliente oficial de Elasticsearch. Elasticsearch se usa para búsqueda; **no** para logs (la observabilidad usa Loki, con la comparación documentada).

### BE-08.1 · Modelado de índices y análisis de texto
- **Ola:** 3 · **Profundidad:** B
- **Depende de:** BE-01.2, FND-04.2

**Requerimientos**
- *Mappings* explícitos (sin mapeo dinámico), plantillas de índice y **alias** desde el inicio.
- Analizadores para español: *stemming*, plegado de acentos, **sinónimos con términos peruanos** (palta/aguacate, chompa/suéter, etc.), *edge n-grams* para autocompletado, analizador de búsqueda distinto del de indexación donde aporte.
- API `_analyze` usada en pruebas para fijar el comportamiento de los analizadores.

**Terminado cuando**
- Las pruebas de analizadores cubren acentos, plurales, sinónimos y errores de tipeo comunes.

**Aprender y documentar**
- Índice invertido, segmentos, *refresh*, *flush* y *merge*; por qué la búsqueda es "casi en tiempo real".

### BE-08.2 · Proyección desde eventos
- **Ola:** 3 · **Profundidad:** A
- **Depende de:** BE-08.1, BE-05.5, BE-06.5

**Requerimientos**
- Consumo de `ProductChanged` (incluido el precio de lista), de eventos de existencias y de `StoreChanged`; documento de búsqueda que los combina.
- *Upserts* idempotentes con **versionado externo** (un evento antiguo nunca pisa uno nuevo), indexación en lotes (*bulk*) con control de presión hacia Elasticsearch, DLT.
- Reconstrucción completa del índice desde los eventos o desde los servicios de origen.

**Terminado cuando**
- Reordenar eventos a propósito no deja documentos desactualizados.

**Aprender y documentar**
- Concurrencia optimista en Elasticsearch; consistencia eventual de un modelo de lectura.

### BE-08.3 · Consultas y relevancia
- **Ola:** 3 · **Profundidad:** A
- **Depende de:** BE-08.2, DB-02.2

**Requerimientos**
- Búsqueda con BM25 y `function_score` (popularidad, calificación bayesiana, disponibilidad), filtro y ordenamiento por **distancia geográfica** a la tienda, facetas con agregaciones, paginación con `search_after`, resaltado, autocompletado, corrección de errores (*fuzzy*).
- **Evaluación de relevancia** con listas de juicios y la API `_rank_eval` (métricas como nDCG), ejecutada en CI para detectar regresiones de relevancia.
- Analítica de búsquedas: consultas sin resultados y consultas más frecuentes.

**Terminado cuando**
- La métrica de relevancia supera el umbral fijado y una regresión hace fallar el pipeline.

**Aprender y documentar**
- BM25 frente a TF-IDF; cómo se combina la puntuación con `function_score`; métricas de relevancia.

### BE-08.4 · Operación de Elasticsearch
- **Ola:** 3 · **Profundidad:** B
- **Depende de:** BE-08.3

**Requerimientos**
- **Reindexado sin tiempo de inactividad** con cambio atómico de alias (cambios de *mapping* incompatibles).
- *Snapshots* al almacenamiento de objetos y restauración probada.
- Dimensionamiento de *shards* y réplicas justificado; ILM para el índice de analítica de búsquedas.
- Clúster de tres nodos en el perfil `full` para alta disponibilidad.

**Terminado cuando**
- Un reindexado con cambio de *mapping* se completa mientras corre una prueba de carga de búsqueda, sin errores.

**Aprender y documentar**
- *Shards* primarios y réplicas, asignación y recuperación; elección de nodo maestro.

### BE-08.5 · Precios y promociones en la búsqueda
- **Ola:** 4 · **Profundidad:** B
- **Depende de:** BE-08.4, BE-07.3

**Requerimientos**
- Consumo de `PriceChanged` y `PromotionActivated`: precio efectivo, distintivo de promoción y filtro por "en oferta".
- Adopción en la proyección y reindexado según BE-08.4.

**Terminado cuando**
- Activar una promoción se refleja en los resultados de búsqueda en segundos.

**Aprender y documentar**
- Coste de desnormalizar datos volátiles en un índice de búsqueda.
