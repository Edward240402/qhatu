# FND-01 · Repositorio, convenciones y gestión del trabajo

**Objetivo:** un monorepo con reglas de contribución como las de una empresa, y el trabajo organizado y visible.

### FND-01.1 · Estructura del monorepo y convenciones
- **Ola:** 0 · **Profundidad:** B
- **Depende de:** —

**Requerimientos**
- Estructura raíz (un solo repositorio Git, una sola carpeta abierta como proyecto del IDE):
  ```
  services/     un directorio por microservicio
  libs/         librerías técnicas compartidas (nunca dominio)
  functions/    serverless
  web/          Angular
  mobile/       Flutter
  ml/           notebooks, entrenamiento, inferencia
  contracts/    openapi/, asyncapi/, proto/, avro/, graphql/
  deploy/       compose/, helm/, environments/, terraform/
  db/           scripts operativos
  data/         generador de datos sintéticos (código; los datos generados no se versionan)
  tests/        postman/, load/, chaos/, e2e/
  scripts/      utilidades (roadmap/, hooks/, doctor.sh)
  docs/         roadmap/, fases/, adr/, estandares/, aprendizaje/, operacion/
  .claude/      skills, agentes, configuración del agente
  ```
- `.gitattributes` con `* text=auto eol=lf` (imprescindible: el IDE corre en Windows y el código en WSL) y `core.autocrlf=input` documentado; `.editorconfig`; `.gitignore` por ecosistema.
- Conventional Commits validado por un hook `commit-msg` (commitlint) instalado con un comando documentado.
- `LICENSE`, `SECURITY.md`, `CONTRIBUTING.md`, plantillas de PR y de issue.
- Plantilla de ADR (formato MADR) en `docs/adr/` y ADR-0001: monorepo frente a polirepo. Debe recoger el coste real: en empresas cada microservicio suele tener su propio repositorio; aquí se elige monorepo por cambios atómicos entre contratos y consumidores, un único pipeline y visibilidad del portafolio. La independencia de despliegue se demuestra con versión, imagen y pipeline por componente.
- **Configuración del IDE para un solo proyecto**: el POM raíz agrega solo los módulos Java; `web/`, `mobile/` y `ml/` mantienen su build nativo; carpetas generadas excluidas del índice (`node_modules`, `target`, `dist`, `.dart_tool`, `.venv`, `.terraform`); configuraciones de ejecución compartidas en `.run/`; resto de `.idea/` ignorado; IntelliJ conectado al repositorio dentro de WSL (soporte nativo de WSL o JetBrains Gateway); guía para abrir un subconjunto cuando falte memoria.

**Terminado cuando**
- Un commit con mensaje inválido es rechazado localmente.
- El repositorio abre en IntelliJ desde WSL con todas las carpetas visibles y sin indexar carpetas generadas.

**Aprender y documentar**
- Monorepo frente a polirepo: qué ganas y qué pagas.
- Cómo funcionan los hooks de Git y por qué LF importa entre Windows y Linux.

### FND-01.2 · Gobierno del repositorio, versionado y seguimiento del trabajo
- **Ola:** 0 · **Profundidad:** B
- **Depende de:** OPS-01.1

**Requerimientos**
- Protección de `main`: PR obligatorio, checks requeridos (los de OPS-01.1), historial lineal, sin *push* directo.
- `CODEOWNERS`; ADR-0002: trunk-based con ramas cortas por sub-fase.
- Estándar `docs/estandares/versionado-y-git.md`: nombres de ramas, alcance obligatorio en los commits (`feat(order-service): …`), versión semántica **por componente**, etiquetas `componente/vX.Y.Z`, política para librerías internas y contratos (ver [90-gobierno-transversal.md](../90-gobierno-transversal.md#5-git-y-versionado)).
- Configuración base de release-please en modo monorepo (se activa por componente a medida que aparecen).
- **GitHub Projects**: tablero con hitos por ola, issue por sub-fase, etiquetas por frente y tipo; plantilla de issue de sub-fase enlazada a su carpeta en `docs/fases/`.

**Terminado cuando**
- Un PR sin checks en verde no puede fusionarse.
- El tablero muestra la ola 0 con sus sub-fases como issues.

**Aprender y documentar**
- Trunk-based frente a GitFlow; versionado semántico en un monorepo y cómo release-please deduce versiones de los commits.
