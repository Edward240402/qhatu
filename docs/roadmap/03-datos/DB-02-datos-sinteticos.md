# DB-02 · Datos sintéticos y simulador de tráfico

**Objetivo:** datos realistas, deterministas y en el volumen que cada ola necesita. El generador produce **conjuntos de datos** independientes de los servicios (archivos Parquet o CSV en el almacenamiento de objetos); cada servicio tiene un **cargador** propio que los importa de forma eficiente. Así el generador no se acopla al esquema de nadie.

### DB-02.1 · Núcleo del generador y datos maestros
- **Ola:** 1 · **Profundidad:** B
- **Depende de:** BE-04.3, FND-04.1

**Requerimientos**
- Generador en `data/` con semilla fija, perfiles `S`, `M`, `L` y un único comando (`task data:generate PROFILE=M`).
- Distribuciones realistas: zonas de Lima con polígonos y densidad, clientes con direcciones geolocalizadas, comercios con varias tiendas, repartidores con zona base. Datos personales falsos pero con formatos peruanos válidos (DNI, RUC, teléfono, *ubigeo*).
- Cargador de `customer-service` con `COPY` por lotes, respetando el cifrado de campos (pasa por `common-crypto`).
- Instantáneas: volcado tras la carga y restauración rápida (`task data:restore`).

**Terminado cuando**
- `M` se genera y carga en minutos y dos ejecuciones con la misma semilla producen los mismos datos.

**Aprender y documentar**
- Generación de datos con distribuciones (Zipf para popularidad, Poisson para llegadas); por qué `COPY` es órdenes de magnitud más rápido que `INSERT`.

### DB-02.2 · Catálogo, tiendas y existencias
- **Ola:** 2 · **Profundidad:** B
- **Depende de:** DB-02.1, BE-05.1, BE-06.1

**Requerimientos**
- Productos por categoría con atributos heterogéneos coherentes, nombres y descripciones en español con variantes regionales (insumo para sinónimos de búsqueda), popularidad con cola larga.
- Existencias por tienda con escasez deliberada en productos populares (necesario para probar concurrencia).
- Cargadores para `catalog-service` e `inventory-service`.

**Terminado cuando**
- El perfil `M` produce un catálogo navegable y existencias que provocan contención en las pruebas de BE-06.3.

**Aprender y documentar**
- Cómo diseñar datos de prueba que ejerciten los casos difíciles, no solo los felices.

### DB-02.3 · Historial transaccional
- **Ola:** 4 · **Profundidad:** B
- **Depende de:** DB-02.2, BE-09.2, BE-10.1

**Requerimientos**
- Pedidos y pagos históricos con estacionalidad: día de la semana, quincena y fin de mes, feriados de Perú, campañas; cancelaciones y pagos fallidos en proporciones realistas.
- Cargadores para `order-service` (respetando particiones) y `payment-service`.

**Terminado cuando**
- El perfil `L` llena varios años de particiones y las consultas por rango de fecha se pueden medir sobre volumen real.

**Aprender y documentar**
- Series temporales con estacionalidad compuesta (es también la base de ML-03).

### DB-02.4 · Simulador de tráfico en vivo
- **Ola:** 5 · **Profundidad:** B
- **Depende de:** DB-02.3, BE-13.1, BE-11.2

**Requerimientos**
- Simulador de **clientes** que crea pedidos por la API pública a una tasa configurable (con OAuth2 real).
- Simulador de **comercios** que aceptan, rechazan y preparan sub-pedidos con tiempos y tasas de rechazo realistas.
- Simulador de **repartidores** que envía posiciones GPS siguiendo calles (rutas de un motor local como OSRM con datos abiertos de Lima, o interpolación justificada con ADR), acepta pedidos y completa entregas.
- Escenarios con nombre: día normal, hora punta, campaña, lluvia (velocidades bajas).

**Terminado cuando**
- Un comando pone el sistema "vivo" para demos y pruebas, y la tasa es controlable en tiempo real.

**Aprender y documentar**
- Modelos de carga abiertos y cerrados (enlaza con OPS-05).

### DB-02.5 · Volumen analítico y reproducción de eventos
- **Ola:** 6 · **Profundidad:** B
- **Depende de:** DB-02.4, DB-06.1

**Requerimientos**
- Generación de decenas de millones de eventos históricos directamente en Kafka y ClickHouse.
- **Reproducción** de un flujo de eventos grabado a velocidad real o acelerada, útil para pruebas de proyecciones y analítica.

**Terminado cuando**
- Los dashboards de FE-06 se pueden evaluar sobre el perfil `L`.

**Aprender y documentar**
- Reproducción de eventos como herramienta de pruebas; cuidados con el orden y con los efectos secundarios.

### DB-02.6 · Reseñas y conjunto etiquetado
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** DB-02.5, BE-05.3

**Requerimientos**
- Reseñas en español peruano (con jerga, errores ortográficos y emojis), generadas por plantillas y opcionalmente con un LLM, con la procedencia registrada.
- **Conjunto etiquetado a mano** de algunos cientos de reseñas para evaluar ML-02, separado de lo generado.

**Terminado cuando**
- El conjunto etiquetado está versionado con DVC y documentado.

**Aprender y documentar**
- Riesgos de evaluar un modelo con datos sintéticos; etiquetado y acuerdo entre anotadores.
