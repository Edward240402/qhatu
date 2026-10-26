# OBS-04 · SLOs y alertas

### OBS-04.1 · SLI y SLO como código
- **Ola:** 5 · **Profundidad:** A
- **Depende de:** OBS-02.2, BE-13.3, BE-11.3

**Requerimientos**
- SLI y SLO por recorrido crítico (compra, seguimiento, búsqueda, cotización), derivados de FND-03.2; presupuesto de error visible.
- Alertas por **tasa de consumo del presupuesto** en varias ventanas; SLO como código (Sloth, Pyrra o reglas de Grafana).
- Pruebas de las reglas de alerta en CI.

**Terminado cuando**
- Un fallo inyectado consume presupuesto y dispara la alerta correcta (y solo esa).

**Aprender y documentar**
- SLI, SLO y SLA; presupuestos de error como herramienta de decisión; por qué alertar sobre síntomas y no sobre causas.

### OBS-04.2 · Guías de respuesta e incidentes
- **Ola:** 5 · **Profundidad:** B
- **Depende de:** OBS-04.1

**Requerimientos**
- Cada alerta enlaza a su guía en `docs/operacion/runbooks/`; enrutamiento por severidad; silencios e inhibición.
- Alertas de plataforma: retraso de Kafka, *slots* de replicación, disco, certificados por vencer, reinicios de *pods*.
- Simulacro de incidente con *postmortem* sin culpables documentado.

**Terminado cuando**
- Siguiendo la guía de una alerta disparada en el simulacro se llega a la causa.

**Aprender y documentar**
- Gestión de incidentes y fatiga de alertas.
