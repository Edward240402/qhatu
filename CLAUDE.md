# Qhatu — instrucciones para el agente

Marketplace multi-comercio con logística de última milla (Perú). Proyecto de portafolio senior backend y, a la vez, de **aprendizaje profundo**: el dueño del repositorio quiere entender por qué se usa cada tecnología y cómo funciona por dentro.

## Dónde está cada cosa

- Orden canónico de sub-fases y reglas globales: `ROADMAP.md`
- Requerimientos: `docs/roadmap/<NN-frente>/<FASE>-*.md` (requisitos comunes del frente en su `README.md`)
- Gobierno transversal (estándares, profundidad, Git, algoritmos): `docs/roadmap/90-gobierno-transversal.md`
- Progreso: `docs/fases/ESTADO.md` y `docs/fases/<ID>/`
- Estándares que se hacen cumplir: `docs/estandares/` · Decisiones: `docs/adr/` · Versiones verificadas: `docs/versiones.md`
- Aprendizaje: `docs/aprendizaje/` · Manual de operación: `docs/operacion/`

## Flujo de trabajo

- La unidad de trabajo es la **sub-fase** (`BE-09.3`) y se ejecuta con `/fase <ID>`: análisis → plan → implementación, un paso por turno, con aprobación del usuario entre pasos. No escribas código de producto fuera del paso de implementación de una sub-fase con plan aprobado.
- Si el usuario pide algo que pertenece a una sub-fase sin plan aprobado, dilo y propone `/fase`.
- El estado vive en archivos. Al retomar, lee `ESTADO.md` y la carpeta de la sub-fase.
- Cualquier cambio en el roadmap pasa por `python3 scripts/roadmap/roadmap.py validar`.

## Reglas de ingeniería

- **Prohibidos los atajos**: sin soluciones temporales, sin pruebas deshabilitadas o debilitadas, sin `TODO` sin issue, sin secretos en el repositorio, sin desactivar reglas de análisis sin justificación escrita, sin TLS sin verificar. Si algo no cabe bien, propone recortar alcance; nunca calidad.
- **Contrato primero**: OpenAPI, AsyncAPI, Protobuf o GraphQL antes que la implementación.
- **Estándares**: cumple los de `docs/estandares/` aplicables y la lista `dod-<frente>.md`. Si una sub-fase introduce o endurece un estándar, adóptalo en todo lo ya construido.
- **Versiones**: verifica la última estable en la fuente oficial antes de añadir o subir una dependencia y regístrala en `docs/versiones.md`. Nunca uses números de versión de memoria.
- **ADR** para toda decisión con alternativas reales.
- Cada servicio respeta su arquitectura asignada (`docs/roadmap/00-vision-y-negocio.md`), verificada con ArchUnit o Spring Modulith. Ningún servicio accede a la base de otro; nada de librerías compartidas con lógica de dominio.
- **Lógica de negocio y algoritmos**: escenarios ejecutables, complejidad en tiempo y espacio documentada, JMH en el camino crítico, pruebas de propiedades para invariantes.
- **Flyway**: nunca se edita una migración aplicada; todo cambio de esquema es una versión nueva, con expandir/contraer cuando rompe compatibilidad.
- Todo lo nuevo nace con pruebas, logs estructurados, métricas y trazas.
- Código, commits (Conventional Commits con alcance del componente) y nombres de API y eventos en inglés. Documentación en español.
- Si una prueba falla o algo no pudo verificarse, repórtalo tal cual con la salida. No declares terminado lo que no ejecutaste.

## Objetivo de aprendizaje

- Explica brevemente el porqué de cada decisión no obvia y la alternativa descartada.
- Toda tecnología, patrón o algoritmo introducido crea o amplía su documento en `docs/aprendizaje/` según `docs/roadmap/91-estandar-documentacion.md`, con la profundidad del nivel de la sub-fase (A, B o C).
- Todo cambio en cómo se levanta, configura o despliega algo actualiza `docs/operacion/` en la misma sub-fase.
- No simplifiques una explicación hasta volverla incorrecta. Si no estás seguro de un detalle interno, verifícalo en la fuente primaria o dilo.

## Entorno

- Desarrollo en **WSL2 (Linux) sobre Windows 11**. El repositorio vive en `~/…`, nunca bajo `/mnt/c` o `/mnt/d`. Comandos y scripts en bash.
- Herramientas instaladas dentro de WSL con las versiones fijadas en el repositorio. Docker según el ADR de FND-02.1.
- En Windows solo quedan navegador, IDE (conectado a WSL), emulador de Android y almacén de certificados; los pasos de ese lado se marcan **[Windows]**.
- Fin de línea LF; los scripts conservan el bit de ejecución.
- Los comandos de build, prueba y arranque se registran aquí al cerrar FND-02.3 y FND-04.1.
