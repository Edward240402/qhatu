# OBS-02 · Métricas y dashboards

### OBS-02.1 · JVM, RED/USE y dashboards generados
- **Ola:** 2 · **Profundidad:** A
- **Depende de:** OBS-01.2, BE-04.4

**Requerimientos**
- **JVM**: memoria (*heap* por generación, fuera de *heap*, metaspace, *buffers* directos), GC (pausas, frecuencia), **hilos** (de plataforma por estado; virtual threads montados, en cola, *pinned*), clases, CPU.
- Método RED por *endpoint* y USE por recurso; histogramas nativos para latencias.
- **Dashboards como código** (Grafana Foundation SDK, Jsonnet o Terraform): visión global y uno por servicio generado desde una plantilla común. Todo servicio nuevo obtiene el suyo automáticamente.

**Terminado cuando**
- Durante una prueba de carga se observan en vivo hilos, memoria y GC de cada servicio.

**Aprender y documentar**
- Contadores, medidores e histogramas, y por qué no se promedian percentiles; PromQL esencial; cómo leer el comportamiento del GC.

### OBS-02.2 · Dependencias y métricas de negocio
- **Ola:** 2 · **Profundidad:** A
- **Depende de:** OBS-02.1, BE-06.5, DB-04.1

**Requerimientos**
- *Pools* de conexiones, PostgreSQL, MongoDB, Redis, Kafka (**retraso de consumidores**, rebalanceos), tolerancia a fallos (estado de circuitos, reintentos, rechazos), caché (tasa de aciertos).
- Métricas de negocio con su dashboard: productos publicados, reservas, sobreventa evitada; se amplía en cada ola (pedidos por estado, sagas compensadas, conversión, tiempo de asignación).
- Control de cardinalidad de etiquetas con reglas y alerta.

**Terminado cuando**
- Existe un dashboard de negocio y uno por dependencia, y una etiqueta de alta cardinalidad es detectada.

**Aprender y documentar**
- Explosión de cardinalidad: por qué ocurre y cuánto cuesta.
