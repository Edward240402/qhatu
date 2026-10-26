# OBS-05 · Perfilado y diagnóstico

### OBS-05.1 · Perfilado continuo y JFR
- **Ola:** 2 · **Profundidad:** A
- **Depende de:** OBS-02.1

**Requerimientos**
- Pyroscope (CPU, asignaciones, bloqueos) enlazado desde las trazas.
- JFR con grabación continua de bajo coste y volcado bajo demanda; eventos de virtual threads; transmisión de eventos de JFR como métricas.

**Terminado cuando**
- Desde una traza lenta se llega al perfil de CPU de ese intervalo.

**Aprender y documentar**
- Cómo funciona un perfilador por muestreo y sus sesgos (*safepoint bias*); qué registra JFR y a qué coste.

### OBS-05.2 · Casos prácticos de diagnóstico
- **Ola:** 10 · **Profundidad:** A
- **Depende de:** OPS-05.1, OBS-05.1

**Requerimientos**
- Procedimientos ensayados: volcado de hilos, volcado de *heap* y análisis de fuga, memoria nativa, diagnóstico de `OOMKilled`.
- Casos reproducibles en ramas de demostración: fuga de memoria, interbloqueo, *pinning* de virtual threads, consulta N+1, agotamiento del *pool*, *event loop* bloqueado.

**Terminado cuando**
- Cada caso tiene su guía "síntoma → herramienta → evidencia → causa → corrección".

**Aprender y documentar**
- Regiones de memoria de la JVM; cómo leer un volcado de hilos y un *flame graph*.
