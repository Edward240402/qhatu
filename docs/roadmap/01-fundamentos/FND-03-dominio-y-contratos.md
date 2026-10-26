# FND-03 · Dominio, requisitos y contratos

**Objetivo:** que los límites de los microservicios y las reglas de negocio salgan del dominio, y que los contratos existan antes que el código.

### FND-03.1 · Event storming y mapa de contextos
- **Ola:** 0 · **Profundidad:** A
- **Depende de:** FND-01.1

**Requerimientos**
- Event storming documentado de los flujos: compra multi-comercio, despacho y entrega, cancelación y devolución, liquidación y facturación, integración de comercios.
- Mapa de contextos (contextos delimitados y sus relaciones: cliente-proveedor, conformista, capa anticorrupción) y glosario de lenguaje ubicuo en español con su término en inglés.
- Catálogo de eventos de dominio con propietario, clave de partición y garantías de orden esperadas.

**Terminado cuando**
- Cada servicio de [00-vision-y-negocio.md](../00-vision-y-negocio.md) se justifica por un contexto del mapa.

**Aprender y documentar**
- DDD estratégico; cómo se decide un límite de servicio; eventos de dominio frente a eventos de integración.

### FND-03.2 · Arquitectura objetivo y requisitos no funcionales
- **Ola:** 0 · **Profundidad:** A
- **Depende de:** FND-03.1

**Requerimientos**
- Diagramas C4 como código (contexto, contenedores; componentes para `order-service`).
- **Requisitos no funcionales cuantificados**: reservas de stock por segundo en campaña, latencia p99 por recorrido, posiciones GPS por segundo, usuarios concurrentes, volumen de datos por año, **objetivos de disponibilidad por componente**, RPO y RTO. Son la base de las pruebas de carga, los SLO y el diseño de alta disponibilidad.
- ADR por servicio que justifica su runtime, arquitectura y estilo de comunicación.
- Estándar `docs/estandares/arquitectura.md`: reglas de dependencia de cada estilo (capas, hexagonal, clean, orientada a eventos, monolito modular) que luego se codifican en ArchUnit.
- ADR de la tecnología móvil con un conteo de vacantes en portales peruanos.

**Terminado cuando**
- Existen los diagramas, los NFR con números y un ADR por servicio.

**Aprender y documentar**
- Modelo C4; cómo convertir un requisito vago ("que aguante mucho") en uno verificable.

### FND-03.3 · Guías de estilo y contratos esqueleto
- **Ola:** 0 · **Profundidad:** A
- **Depende de:** FND-03.2

**Requerimientos**
- `docs/estandares/api.md`: nombres, paginación, filtros, errores RFC 9457, versionado, idempotencia (`Idempotency-Key`), concurrencia (`ETag`/`If-Match`), códigos de estado; reglas de Spectral que lo verifican.
- `docs/estandares/eventos.md`: sobre del evento (CloudEvents), nombres, versionado de esquemas, claves, garantías.
- Contratos esqueleto en `contracts/`: OpenAPI 3.1 por servicio síncrono, AsyncAPI 3 del bus, `.proto` de inventario, esquema GraphQL de la API de integradores.

**Terminado cuando**
- Los contratos esqueleto pasan sus linters.

**Aprender y documentar**
- Diseño contrato-primero; anatomía de OpenAPI 3.1 y AsyncAPI 3.

### FND-03.4 · Reglas de negocio especificadas por ejemplos
- **Ola:** 0 · **Profundidad:** A
- **Depende de:** FND-03.1

**Requerimientos**
- Especificación en Gherkin (español) de las reglas complejas del catálogo de [00-vision-y-negocio.md](../00-vision-y-negocio.md#4-lógica-de-negocio-compleja): promociones y su combinación, tarifa de envío y recargo dinámico, asignación de repartidores, asignación de tiendas, cancelación y devolución parcial, comisiones y liquidación, facturación.
- Escenarios para cada decisión de coherencia N1 a N11 de la sección 4.1, en especial donde dos reglas interactúan (promoción de envío gratis con recargo, devolución de una línea con descuento financiado por la plataforma, rechazo de un comercio tras la captura del pago).
- Para cada regla: casos normales, límites y contraejemplos, con números concretos.
- Estándar `docs/estandares/reglas-de-negocio-y-algoritmos.md` (ver [90-gobierno-transversal.md](../90-gobierno-transversal.md#8-reglas-para-algoritmos-y-lógica-de-negocio)).

**Terminado cuando**
- Cada regla tiene escenarios que un experto de negocio podría validar sin leer código.

**Aprender y documentar**
- Especificación por ejemplos y BDD: para qué sirven y cuándo son ceremonia.
