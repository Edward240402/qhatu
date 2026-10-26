# 09 · Observabilidad (`OBS`)

Pila de referencia: **OpenTelemetry** para instrumentar y transportar, y la pila de **Grafana** como destino: Prometheus o Mimir (métricas), Loki (logs), Tempo (trazas), Pyroscope (perfiles), Grafana (visualización y alertas), con Grafana Alloy u OpenTelemetry Collector como recolector. Todo como código.

Objetivo de fondo: responder **"¿qué le pasó a este pedido?"** y **"¿por qué está lento esto?"** en menos de dos minutos, saltando entre métricas, trazas, logs y perfiles sin perder el contexto.

| Fase | Título | Olas |
|---|---|---|
| [OBS-01](OBS-01-base-de-telemetria.md) | Base de telemetría | 1 |
| [OBS-02](OBS-02-metricas-y-dashboards.md) | Métricas y dashboards | 2 |
| [OBS-03](OBS-03-trazabilidad.md) | Trazabilidad distribuida | 4, 5 |
| [OBS-04](OBS-04-slos-y-alertas.md) | SLOs y alertas | 5 |
| [OBS-05](OBS-05-perfilado-y-diagnostico.md) | Perfilado y diagnóstico | 2, 10 |
| [OBS-06](OBS-06-kubernetes-y-nube.md) | Observabilidad en Kubernetes y nube | 8 |

## Requisitos comunes

- Toda sub-fase de cualquier frente que añada código añade su telemetría según `docs/estandares/observabilidad.md` (OBS-01.2).
- Cada sub-fase `OBS` que introduce una capacidad nueva la adopta en **todo lo ya construido** (regla de adopción retroactiva).
