# OBS-01 · Base de telemetría

### OBS-01.1 · Pila de observabilidad como código
- **Ola:** 1 · **Profundidad:** B
- **Depende de:** FND-04.1

**Requerimientos**
- Pila en el perfil `observability` del Compose, con retenciones cortas para local.
- Recolector como único punto de salida: recepción OTLP, procesamiento por lotes, límite de memoria, enriquecimiento con atributos de recurso.
- Fuentes de datos de Grafana enlazadas entre sí (métrica → traza con ejemplares, traza → logs y viceversa); aprovisionamiento de fuentes, carpetas y dashboards como código.

**Terminado cuando**
- La pila levanta sana desde cero y su configuración está íntegramente en el repositorio.

**Aprender y documentar**
- Las tres señales y qué pregunta responde cada una; arquitectura *pull* de Prometheus frente a *push* de OTLP.

### OBS-01.2 · Estándar de instrumentación
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** OBS-01.1, BE-01.1

**Requerimientos**
- ADR: agente Java de OpenTelemetry frente a instrumentación nativa (Micrometer + OTLP en Spring Boot; extensión OpenTelemetry en Quarkus).
- `docs/estandares/observabilidad.md`: convenciones semánticas, atributos de recurso obligatorios (`service.name`, versión, entorno), nombres de métricas, niveles de log y qué se registra.
- `libs/common-observability`: logs JSON con `trace_id` y `span_id`; **redacción de datos personales** en el recolector y en la aplicación, con una prueba que falla si un dato personal llega a un log.
- Muestreo inicial definido.

**Terminado cuando**
- Una petición de ejemplo se sigue desde la métrica hasta la traza y sus logs en tres clics.

**Aprender y documentar**
- Modelo de datos de OpenTelemetry (recurso, *span*, contexto, enlaces); cómo viaja el contexto (W3C Trace Context).
