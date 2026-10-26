# OPS-02 · Estrategia y automatización de pruebas

### OPS-02.1 · Estrategia, matriz y base de pruebas
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** BE-01.1

**Requerimientos**
- `docs/estandares/pruebas.md`: pirámide del proyecto, la matriz del [README](README.md#matriz-de-pruebas-qué-se-ejecuta-y-cuándo), qué **no** se prueba y por qué, umbrales de cobertura (líneas y ramas sobre código nuevo) y de mutación.
- `common-test`: Testcontainers con contenedores reutilizables y TLS real; dobles de prueba recomendados; datos de prueba con constructores.
- Biblioteca de reglas ArchUnit por estilo de arquitectura (de `arquitectura.md`), lista para importar.
- Etapas del pipeline alineadas con la matriz.

**Terminado cuando**
- La matriz está implementada en los flujos de CI existentes y un servicio de ejemplo usa las reglas ArchUnit.

**Aprender y documentar**
- Tipos de dobles de prueba y cuándo usar cada uno; por qué la cobertura no mide calidad.

### OPS-02.2 · Base de pruebas de carga
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** OBS-01.1, INF-01.2

**Requerimientos**
- k6 o Gatling (ADR) como código en `tests/load/`; **modelo de carga abierto** (tasa de llegada) por defecto; autenticación OAuth2 real.
- Resultados enviados a Prometheus y dashboard de la prueba junto a los dashboards del sistema.
- Prueba de humo de carga en el pipeline tras fusionar; umbrales derivados de FND-03.2.

**Terminado cuando**
- Las sub-fases que necesitan pruebas de carga (BE-04.4, BE-06.3) pueden escribirlas reutilizando la base.

**Aprender y documentar**
- Percentiles frente a promedios; omisión coordinada; modelos abiertos y cerrados.

### OPS-02.3 · Pruebas de contrato dirigidas por el consumidor
- **Ola:** 3 · **Profundidad:** A
- **Depende de:** BE-08.2

**Requerimientos**
- Pact con *broker* autoalojado para HTTP y para **mensajes** (primer caso: `search-service` como consumidor de los eventos de catálogo e inventario).
- Verificación del proveedor en su pipeline y `can-i-deploy` antes de desplegar.
- Adopción en los pares consumidor-proveedor ya existentes.

**Terminado cuando**
- Un cambio en un evento que rompe a un consumidor es bloqueado antes de fusionar.

**Aprender y documentar**
- Contratos dirigidos por el consumidor frente a compatibilidad de esquemas: qué detecta cada uno.

### OPS-02.4 · Mutación y propiedades
- **Ola:** 2 · **Profundidad:** A
- **Depende de:** BE-06.3

**Requerimientos**
- PIT sobre el código de dominio (empezando por `inventory-service`), incremental en PR y completo nocturno, con umbral.
- jqwik para invariantes (stock, asignación de tiendas) y como estándar para los algoritmos de fases posteriores.

**Terminado cuando**
- Un mutante sobreviviente relevante hace fallar el umbral y su corrección mejora una prueba real.

**Aprender y documentar**
- Qué es un mutante y qué revela uno sobreviviente; pruebas basadas en propiedades y reducción de contraejemplos.

### OPS-02.5 · Pruebas de extremo a extremo del sistema
- **Ola:** 4 · **Profundidad:** B
- **Depende de:** BE-11.3

**Requerimientos**
- Batería E2E de API sobre el sistema completo en Compose para los recorridos críticos (compra feliz y caminos de fallo de la saga), estable y con datos aislados por prueba.
- Política anti-inestabilidad: sin esperas fijas, esperas por condición, reintentos solo en infraestructura.

**Terminado cuando**
- La batería corre en cada fusión a `main` con tasa de inestabilidad medida y bajo umbral.

**Aprender y documentar**
- Por qué las E2E son pocas y cómo hacerlas deterministas.
