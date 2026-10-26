# FND-05 · Sistema de agentes de desarrollo

**Objetivo:** el flujo de trabajo con Claude Code validado, versionado y seguro. Es en sí mismo evidencia de portafolio.

### FND-05.1 · Skill, subagentes, permisos, hooks y MCP
- **Ola:** 0 · **Profundidad:** B
- **Depende de:** FND-01.1

**Requerimientos**
- Validar y ajustar lo entregado: `CLAUDE.md`, skill `/fase`, subagentes `analista-dependencias`, `revisor-calidad` y `docente`.
- `.claude/settings.json` del proyecto: permisos mínimos (build, pruebas, compose, lectura de git), lectura denegada de `.env`, claves y carpetas de secretos; acciones destructivas o con coste siempre con aprobación.
- Hooks: bloqueo de edición de rutas protegidas (migraciones Flyway ya aplicadas, archivos de bloqueo, secretos). El hook de formato se añade en FND-02.3.
- Verificar nombres de eventos y formato de permisos contra la documentación vigente de Claude Code.
- Servidores MCP justificados: documentación actualizada de librerías, GitHub, base de datos local en solo lectura, navegador para pruebas.
- `docs/agentes.md`: cómo se usa IA en el proyecto, qué decide la persona, qué el agente, y cómo se revisa lo generado.

**Terminado cuando**
- `/fase FND-02.1` ejecuta el análisis y se detiene esperando aprobación.
- Un intento del agente de leer `.env` o editar una ruta protegida es bloqueado.

**Aprender y documentar**
- Skills, subagentes, hooks y MCP: qué resuelve cada uno; gestión de contexto; por qué el estado vive en archivos.
