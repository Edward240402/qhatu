# ML-04 · Servicio de inferencia e integración

### ML-04.1 · Servicio `ml-inference`
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** ML-02.2, INF-02.4

**Requerimientos**
- FastAPI + ONNX Runtime; contrato OpenAPI; validación de entradas; agrupación de peticiones en lotes; carga del modelo desde el registro por versión; *readiness* solo con el modelo cargado.
- OpenTelemetry enlazado con las trazas Java; métricas de latencia y de distribución de predicciones.
- Imagen mínima sin GPU según `contenedores.md`; *chart* de Helm; pruebas de contrato con los consumidores Java.

**Terminado cuando**
- El servicio responde dentro del presupuesto de latencia y aparece en los dashboards estándar.

**Aprender y documentar**
- Patrones de servido (en línea, por lotes, por flujo).

### ML-04.2 · Integración asíncrona de reseñas
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** ML-04.1, BE-05.5

**Requerimientos**
- Consume `ReviewCreated` y publica `ReviewAnalyzed`; `catalog-service` actualiza el resumen. El modelo nunca está en el camino crítico de una petición.
- Reseñas marcadas por moderación entran a la cola de soporte.

**Terminado cuando**
- Publicar una reseña actualiza su sentimiento en segundos, con una traza Java → Kafka → Python → Kafka → Java.

**Aprender y documentar**
- Por qué desacoplar la inferencia del camino crítico.

### ML-04.3 · Integración por lotes del pronóstico
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** ML-04.2, ML-03.3, BE-17.1

**Requerimientos**
- Trabajo programado que genera pronósticos y los escribe en ClickHouse con la versión del modelo.
- `reporting-service` los expone; `inventory-service` los usa para sugerencias de reposición y `dispatch-service` para pre-posicionar repartidores, siempre como sugerencia con respaldo si no hay pronóstico.

**Terminado cuando**
- El pronóstico aparece en el dashboard de comercio y las sugerencias funcionan aunque el servicio de inferencia esté caído.

**Aprender y documentar**
- Diseño de sistemas que consumen predicciones con degradación controlada.
