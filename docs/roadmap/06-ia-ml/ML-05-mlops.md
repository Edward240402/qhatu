# ML-05 · MLOps: ciclo de vida

### ML-05.1 · Reentrenamiento automatizado
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** ML-04.3, OPS-01.2

**Requerimientos**
- Pipeline programado: extracción → validación de datos → entrenamiento → evaluación contra el modelo vigente → registro → promoción con aprobación manual.
- Pruebas del pipeline en CI (datos, entrenamiento de humo, regresión de métricas).
- Trazabilidad de una predicción hasta la versión del modelo, sus datos y su código.

**Terminado cuando**
- Un reentrenamiento produce una versión candidata comparada automáticamente con la vigente.

**Aprender y documentar**
- Diferencias entre CI/CD de software y de modelos.

### ML-05.2 · Monitoreo y despliegue seguro de modelos
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** ML-05.1, OBS-02.2

**Requerimientos**
- Deriva de datos y de predicciones; exactitud real cuando llega la verdad observada; alertas en Grafana.
- Modo sombra o canario para modelos nuevos, con vuelta atrás a la versión anterior.

**Terminado cuando**
- Una deriva inyectada a propósito dispara la alerta y la versión candidata se evalúa en modo sombra.

**Aprender y documentar**
- Tipos de deriva y por qué un modelo se degrada.
