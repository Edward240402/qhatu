# OPS-05 · Rendimiento, caos y capacidad

### OPS-05.1 · Campaña de rendimiento
- **Ola:** 10 · **Profundidad:** A
- **Depende de:** OPS-02.2, DB-02.5, INF-07.1

**Requerimientos**
- Pruebas de carga, estrés, picos (campaña) y resistencia sobre los recorridos críticos: reserva de stock, compra completa, cotización con promociones, ingesta de GPS, búsqueda.
- Ejecución semanal programada; detección de regresiones entre versiones.

**Terminado cuando**
- El informe muestra los objetivos de FND-03.2 cumplidos, o las brechas con su causa y plan.

**Aprender y documentar**
- Teoría de colas básica: por qué la latencia explota cerca de la saturación.

### OPS-05.2 · Ingeniería del caos
- **Ola:** 10 · **Profundidad:** A
- **Depende de:** OPS-05.1

**Requerimientos**
- Chaos Mesh (o LitmusChaos) en el clúster y Toxiproxy en integración: caída de *pods*, de un *broker* de Kafka, del primario de PostgreSQL, de un nodo de Elasticsearch; latencia y partición de red; base de datos lenta; agotamiento de recursos.
- Cada experimento con hipótesis, resultado y corrección aplicada; ejecución programada de los experimentos estables.

**Terminado cuando**
- Cada experimento tiene su informe y las correcciones están fusionadas.

**Aprender y documentar**
- Cómo diseñar un experimento de caos y limitar su radio de impacto.

### OPS-05.3 · Capacidad y coste
- **Ola:** 10 · **Profundidad:** B
- **Depende de:** OPS-05.2

**Requerimientos**
- Modelo de capacidad: recursos por unidad de carga por servicio y punto de saturación.
- Coste por transacción estimado en AWS y Azure.

**Terminado cuando**
- Existe una tabla de dimensionamiento para tres niveles de carga con su coste.

**Aprender y documentar**
- Planificación de capacidad a partir de mediciones.
