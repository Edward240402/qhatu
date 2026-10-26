# OBS-03 · Trazabilidad distribuida

### OBS-03.1 · Propagación por límites asíncronos y muestreo
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** BE-11.1

**Requerimientos**
- Propagación de contexto por **todos** los caminos: HTTP, gRPC, Kafka (cabeceras; enlaces entre *spans* en procesamiento por lotes), outbox y CDC, cambios de hilo, virtual threads, cadenas reactivas y Kafka Streams.
- *Baggage* controlado para contexto de negocio.
- Muestreo en cabecera para volumen y **en cola** en el recolector para conservar siempre errores y trazas lentas.
- Adopción retroactiva en todos los productores y consumidores existentes.

**Terminado cuando**
- Una compra se ve como una sola traza desde el gateway hasta la solicitud de despacho, incluyendo los saltos por Kafka.

**Aprender y documentar**
- Cómo se rompe una traza en límites asíncronos y cómo repararla; relación padre-hijo frente a enlaces; costes del muestreo en cola.

### OBS-03.2 · Trazabilidad de negocio y auditoría
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** OBS-03.1, BE-11.2

**Requerimientos**
- *Spans* de negocio con atributos útiles (identificador de pedido, paso de la saga) y eventos.
- Búsqueda por identificador de pedido que devuelve toda su historia entre servicios.
- Registro de auditoría como señal separada, inmutable y con retención propia.
- Trazas de SQL sin valores de parámetros sensibles.

**Terminado cuando**
- Soporte reconstruye la historia completa de un pedido con compensación a partir de su identificador.

**Aprender y documentar**
- Trazas frente a auditoría: por qué no son lo mismo.

### OBS-03.3 · Monitorización de usuarios reales
- **Ola:** 5 · **Profundidad:** B
- **Depende de:** FE-04.2

**Requerimientos**
- RUM en la web (Grafana Faro u OpenTelemetry para navegador): errores, Core Web Vitals y trazas que **empiezan en el navegador** y continúan en el backend. La app móvil se suma en MOB-06.2.

**Terminado cuando**
- Un clic en "pagar" se ve en la misma traza que la saga resultante.

**Aprender y documentar**
- Propagación de contexto desde el navegador y sus implicaciones de privacidad y CORS.
