---
name: fase
description: Ejecuta el siguiente paso (análisis de dependencias, planificación o implementación) de una sub-fase del roadmap de Qhatu, deteniéndose entre pasos para aprobación del usuario.
argument-hint: "[ID-de-sub-fase] [ok|estado]"
disable-model-invocation: true
---

# /fase — ciclo de una sub-fase del roadmap

Argumentos recibidos: `$ARGUMENTS`

Ejecutas **un solo paso por invocación** y terminas el turno. Nunca encadenes dos pasos.

## 0. Interpretar los argumentos

- **Sin argumentos:** ejecuta `python3 scripts/roadmap/roadmap.py validar`, lee la sección 5 de `ROADMAP.md` y `docs/fases/ESTADO.md`, e indica la siguiente sub-fase pendiente cuyas dependencias estén cerradas, con su título, ola y dependencias. No hagas nada más.
- **`<ID>`** (formato `XX-NN.M`, por ejemplo `BE-09.3`): determina el paso con la tabla de abajo y ejecútalo.
- **`<ID> ok`:** el usuario aprueba el documento pendiente de esa sub-fase. Márcalo como aprobado y ejecuta el paso siguiente.
- **`<ID> estado`:** resume el paso actual, las tareas hechas y pendientes, y los bloqueos. No modifiques nada.

Si recibes el ID de una fase sin sub-fase (`BE-09`), indica sus sub-fases y su estado, y pide cuál ejecutar.

Localiza la definición: `docs/roadmap/*/<FASE>-*.md` (por ejemplo `docs/roadmap/02-backend/BE-09-*.md`), sección `### <ID> · …`. Lee también el `README.md` de esa carpeta (requisitos comunes del frente). Si el ID no existe, dilo y detente.

## Determinar el paso

Carpeta: `docs/fases/<ID>/`. Cada documento empieza con una línea `Estado: BORRADOR` o `Estado: APROBADO`.

| Situación | Acción |
|---|---|
| No existe `01-analisis.md` | Paso 1 |
| `01-analisis.md` en BORRADOR, sin `ok` | Recuerda que espera revisión y resume las preguntas abiertas. Detente |
| `01-analisis.md` en BORRADOR, con `ok` | Si hay bloqueantes sin resolver, enuméralos y no avances. Si no, márcalo APROBADO y ejecuta el paso 2 |
| `01` APROBADO, no existe `02-plan.md` | Paso 2 |
| `02-plan.md` en BORRADOR, sin `ok` | Recuerda que espera aprobación. Detente |
| `02-plan.md` en BORRADOR, con `ok` | Márcalo APROBADO y ejecuta el paso 3 |
| `02` APROBADO, no existe `03-cierre.md` | Paso 3 (retoma desde la primera tarea sin marcar) |
| Existe `03-cierre.md` | Sub-fase cerrada. Indícalo y sugiere la siguiente |

Si el usuario pide cambios a un documento en BORRADOR, aplícalos y vuelve a detenerte.

---

## Paso 1 — Análisis de dependencias (no se toca código)

Delega la investigación en el subagente `analista-dependencias` y redacta `docs/fases/<ID>/01-analisis.md` con `Estado: BORRADOR`:

1. **Sub-fase, objetivo, ola y nivel de profundidad** — copia fiel del roadmap.
2. **Dependencias** — cada sub-fase de "Depende de", su estado en `ESTADO.md` y comprobación real en el repositorio de que su entregable existe y funciona.
3. **Estado actual del repositorio** — lo que la sub-fase usará o modificará; contratos, estándares y ADR relacionados.
4. **Herramientas y versiones** — instaladas y su versión; para cada dependencia nueva, última versión estable **verificada hoy en su fuente oficial**, compatibilidad con `docs/versiones.md` y avisos de obsolescencia.
5. **Requisitos externos** — cuentas, claves, sandbox, cuotas o gasto que solo el usuario puede gestionar.
6. **Tamaño** — si la sub-fase excede el tamaño objetivo (`90-gobierno-transversal.md`, sección 1), propón su división en `<ID>a`, `<ID>b` con el contenido de cada una.
7. **Riesgos y decisiones abiertas** — incluidas las que el roadmap deja para el análisis.
8. **Preguntas para el usuario.**
9. **Veredicto** — `LISTA PARA PLANIFICAR` o `BLOQUEADA` con sus bloqueantes.

Crea el issue de la sub-fase en GitHub con `gh` si el repositorio remoto y el tablero existen (título `<ID> · <título>`, hito de la ola, etiqueta del frente) y enlázalo en el análisis. Actualiza `ESTADO.md` (→ `EN ANÁLISIS`). Termina con un resumen de cinco líneas como máximo y las preguntas abiertas. **Detente.**

Si el usuario aprueba una división, aplícala en el archivo de la fase, en la sección 5 de `ROADMAP.md`, regenera `ESTADO.md` con `roadmap.py estado` y valida antes de continuar.

## Paso 2 — Planificación (no se toca código)

Lee el análisis aprobado, la sub-fase, el `README.md` del frente, `ROADMAP.md` (reglas transversales), `90-gobierno-transversal.md`, `91-estandar-documentacion.md`, los estándares aplicables de `docs/estandares/` y la lista `dod-<frente>.md`. Escribe `docs/fases/<ID>/02-plan.md` con `Estado: BORRADOR`:

1. **Qué tendrás al final** — lo que el usuario podrá ver, ejecutar y demostrar, en lenguaje llano.
2. **Alcance** — incluido y, explícitamente, excluido. Si algo no cabe con calidad, propón moverlo; nunca un atajo.
3. **Decisiones de diseño** — opciones reales, recomendación, razón y ADR. Explicado de modo que sirva para aprender.
4. **Diseño** — contratos que se crean o cambian (primero), modelo de datos y migraciones con su número de versión, estructura según la arquitectura asignada, diagramas Mermaid.
5. **Lógica de negocio y algoritmos** (si aplica) — escenarios, definición del problema, complejidad del problema exacto, algoritmo elegido con su complejidad en tiempo y espacio, garantía o error esperado, benchmark previsto.
6. **Estándares aplicables** — tabla "estándar → cómo se cumple en esta sub-fase", incluida la **adopción retroactiva** si la sub-fase introduce o endurece uno.
7. **Tareas** — lista numerada con casillas `- [ ]`, cada una un commit, con archivos principales y **cómo se verifica**. Contrato y pruebas antes o junto a la implementación.
8. **Pruebas** — niveles según la matriz de `08-calidad-y-cicd/README.md`, incluidos casos de fallo.
9. **Observabilidad** y **seguridad** — lo que se añade y las amenazas relevantes.
10. **Documentación** — documentos de aprendizaje a crear o ampliar (con la profundidad del nivel A, B o C) y sus experimentos; manuales de operación; estándares; ADR.
11. **Criterios de aceptación** — los de "Terminado cuando" más la definición de terminado común, cada uno con el comando o evidencia que lo demostrará.
12. **Riesgos y plan B.**

Actualiza `ESTADO.md` (→ `PLANIFICADA`). Resume en diez líneas como máximo, señalando las decisiones que más merecen revisión. **Detente.**

## Paso 3 — Implementación y cierre

Trabaja en la rama `fase/<id-en-minúsculas>`. Actualiza `ESTADO.md` (→ `EN IMPLEMENTACIÓN`).

Por cada tarea, en orden:

1. Implementa solo esa tarea siguiendo `CLAUDE.md` y los estándares.
2. Verifícala como indica el plan, ejecutando los comandos de verdad.
3. Marca la casilla en `02-plan.md` y haz un commit (Conventional Commits con alcance del componente).
4. Explica en dos o tres frases qué se hizo, por qué así y qué conviene aprender de ello.

Durante la implementación:

- Si el plan está mal o incompleto, **detente y propón el cambio**; no improvises desviaciones ni arreglos temporales.
- Si una verificación falla tres veces por la misma causa, detente y expón el bloqueo con la salida. No debilites pruebas ni reglas de análisis.
- Si la sub-fase es larga, puedes terminar el turno entre tareas con el plan actualizado; la siguiente invocación retoma.

Al marcar todas las tareas:

1. Ejecuta la verificación completa del frente y cada criterio de aceptación; guarda la evidencia.
2. Usa el subagente `docente` para crear o ampliar `docs/aprendizaje/` y ejecutar sus experimentos.
3. Actualiza `docs/operacion/` y prueba los pasos modificados.
4. Usa el subagente `revisor-calidad` sobre el diff de la rama y corrige lo que encuentre.
5. Escribe `docs/fases/<ID>/03-cierre.md`: entregado, evidencia por criterio, desviaciones y por qué, pendientes (como issues), versiones fijadas, "Lo que aprendí" y preguntas de autoevaluación para el usuario.
6. Actualiza `ESTADO.md` (→ `CERRADA`, con fecha) y `docs/versiones.md`.

Si algún criterio no se cumple, **no cierres la sub-fase**: repórtalo tal cual y deja `EN IMPLEMENTACIÓN`.

Termina indicando la rama lista para PR (que debe cerrar el issue), un experimento que el usuario debería ejecutar por sí mismo y la siguiente sub-fase según el orden canónico.
