# BE-19 · Endurecimiento y rendimiento

**Objetivo:** demostrar con números las afirmaciones de rendimiento del portafolio.

### BE-19.1 · Perfilado y ajuste
- **Ola:** 10 · **Profundidad:** A
- **Depende de:** OPS-05.1

**Requerimientos**
- Perfilado con JFR y perfilado continuo sobre la campaña de carga de OPS-05.1; eliminación de los puntos calientes encontrados.
- Ajuste de GC y memoria en contenedor (`MaxRAMPercentage`, elección de recolector), *compact object headers* y **AOT cache** de Java 25, medidos antes y después.
- Ajuste de *pools*, productores y consumidores de Kafka y *pipelining* de Redis, con evidencia.

**Terminado cuando**
- Cada ajuste tiene su medición antes y después y su justificación.

**Aprender y documentar**
- Cómo leer un *flame graph*; recolectores de Java 25 y cuándo elegir cada uno.

### BE-19.2 · Comparativa de modelos de ejecución
- **Ola:** 10 · **Profundidad:** A
- **Depende de:** BE-19.1

**Requerimientos**
- Mismo caso de uso equivalente en Spring MVC con virtual threads, WebFlux, Quarkus JVM y Quarkus nativo: rendimiento, latencia, memoria, arranque, complejidad del código.

**Terminado cuando**
- Informe reproducible con metodología, entorno, resultados y conclusiones.

**Aprender y documentar**
- Trampas de las pruebas de rendimiento (omisión coordinada, calentamiento del JIT, ruido del entorno).

### BE-19.3 · Revisión de decisiones
- **Ola:** 10 · **Profundidad:** B
- **Depende de:** BE-19.2

**Requerimientos**
- Revisión de todos los ADR: cuáles se confirmaron, cuáles se corregirían y por qué, con la evidencia del proyecto.

**Terminado cuando**
- Cada ADR tiene su estado actualizado y una nota de retrospectiva.

**Aprender y documentar**
- Qué aprendiste del proyecto que cambiaría tus decisiones la próxima vez.
