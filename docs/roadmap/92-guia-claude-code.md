# 92 · Guía de uso de Claude Code en este proyecto

Esta guía es para ti, no para el agente. Explica cómo trabajar el roadmap sin repetir instrucciones en cada sub-fase.

## 1. La idea central

Tres pasos separados por sub-fase — **análisis de dependencias → planificación sin código → implementación** — sin pedirlos cada vez. Lo resuelven piezas ya incluidas en el repositorio:

| Pieza | Archivo | Qué hace |
|---|---|---|
| Memoria del proyecto | [CLAUDE.md](../../CLAUDE.md) | Reglas que el agente lee al iniciar cada sesión |
| Skill `/fase` | [.claude/skills/fase/SKILL.md](../../.claude/skills/fase/SKILL.md) | Máquina de estados que ejecuta **solo el siguiente paso** de una sub-fase y se detiene |
| Subagentes | [.claude/agents/](../../.claude/agents/) | `analista-dependencias`, `revisor-calidad`, `docente`, cada uno con contexto propio |
| Validador | [scripts/roadmap/roadmap.py](../../scripts/roadmap/roadmap.py) | Comprueba la coherencia del orden y genera `ESTADO.md` |

El estado vive en archivos (`docs/fases/<ID>/`, `ESTADO.md`), no en la conversación: puedes cerrar la sesión, cambiar de modelo o retomar otro día sin perder nada.

## 2. El ciclo de una sub-fase

```
/fase BE-09.3        →  Paso 1: análisis    →  01-analisis.md, issue en GitHub; se detiene
   (lees; respondes preguntas abiertas)
/fase BE-09.3 ok     →  Paso 2: plan        →  02-plan.md; se detiene
   (lees; pides cambios hasta que te convenza)
/fase BE-09.3 ok     →  Paso 3: implementación, documentación y cierre → 03-cierre.md, rama lista para PR
```

| Comando | Efecto |
|---|---|
| `/fase` | Propone la siguiente sub-fase según el orden canónico y el estado |
| `/fase BE-09.3 estado` | Resume en qué paso está y qué falta |
| `/fase BE-09.3` con implementación a medias | Retoma desde la primera tarea sin marcar |

**`ok` es tu aprobación explícita.** Sin él, el agente no avanza. Un pedido de cambios no es una aprobación.

### Qué revisar en cada puerta

- **Tras el análisis:** cuentas o credenciales que solo tú puedes crear, versiones vigentes, si la sub-fase debería dividirse, preguntas abiertas.
- **Tras el plan** (la revisión más importante): ¿entiendes cada decisión y su alternativa descartada? ¿"Qué tendrás al final" es lo que esperas? ¿La tabla de estándares aplicables está completa? ¿La complejidad de los algoritmos está justificada? ¿Están los documentos de aprendizaje con sus experimentos? Si no entiendes algo, **pregunta antes de aprobar**.
- **Tras la implementación:** lee `03-cierre.md`, ejecuta tú un experimento del documento de aprendizaje y responde las preguntas de autoevaluación.

## 3. Hábitos que marcan la diferencia

- **Una sesión por sub-fase** (o `/clear` al cambiar). El estado está en archivos; el contexto limpio mejora la calidad.
- **Modo plan para lo que no es una sub-fase** (exploraciones, dudas): el agente investiga sin modificar archivos.
- **El modelo más capaz para análisis y plan.** No ahorres en el plan; uno más rápido sirve para tareas mecánicas ya planificadas.
- **Pide verificación, no afirmaciones**: "ejecuta y pega la salida".
- **Commits pequeños por tarea y PR por sub-fase**, aunque trabajes solo: el PR ejecuta el pipeline, cierra el issue y deja historial.
- **Corrige el sistema, no la conversación.** Si el agente repite un error, añade la regla a `CLAUDE.md`, a la skill o a un estándar con su mecanismo de cumplimiento.
- **`CLAUDE.md` corto**: reglas y punteros; el detalle vive en los roadmaps.

## 4. Aprender mientras se implementa

- **Estilos de salida** "Explanatory" o "Learning" en las sub-fases de nivel A: el primero explica el porqué de cada decisión; el segundo además te deja piezas pequeñas para que las escribas tú.
- **Predice antes de ejecutar** cada experimento; la diferencia entre lo previsto y lo observado es lo que aprendes.
- **Pide el modelo mental**: "explícame paso a paso qué ocurre desde que el virtual thread hace la llamada JDBC hasta que recibe la respuesta, señalando nuestro código".
- **Hazte examinar**: "hazme 5 preguntas de entrevista senior sobre la asignación de repartidores, una por una, y corrige mis respuestas con referencia al código".
- **Escribe tú una pieza central por sub-fase** de nivel A (la máquina de estados de la saga, el motor de promociones, una política de Resilience4j) y pide revisión. Leer código generado no equivale a saber escribirlo.
- **Rompe cosas a propósito**: los experimentos de fallo son la parte más valiosa.

## 5. Subagentes, hooks, MCP y bucles

### Subagentes

| Agente | Cuándo | Permisos |
|---|---|---|
| `analista-dependencias` | Paso 1 de `/fase` | Solo lectura y búsqueda web |
| `revisor-calidad` | Antes de cerrar el paso 3 | Solo lectura |
| `docente` | Paso 3, documentación de aprendizaje; o cuando quieras profundizar en un tema | Escritura solo en `docs/aprendizaje/` |

Además, `/code-review` y `/security-review` sobre la rama antes de fusionar.

### Hooks (se configuran en FND-05.1 y FND-02.3)

Los ejecuta la herramienta, no el modelo: son garantías, no recordatorios. Ejemplo de partida para `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": ["Bash(./mvnw *)", "Bash(task *)", "Bash(docker compose *)", "Bash(kubectl get *)", "Bash(git status)", "Bash(git diff *)", "Bash(python3 scripts/roadmap/roadmap.py *)"],
    "deny": ["Read(./.env)", "Read(./**/*.pem)", "Read(./**/*.key)", "Read(./**/secrets/**)"]
  },
  "hooks": {
    "PreToolUse": [
      { "matcher": "Edit|Write", "hooks": [{ "type": "command", "command": "scripts/hooks/block-protected-paths.sh" }] }
    ],
    "PostToolUse": [
      { "matcher": "Edit|Write", "hooks": [{ "type": "command", "command": "scripts/hooks/format-changed-file.sh" }] }
    ]
  }
}
```

- `block-protected-paths.sh` impide editar migraciones Flyway ya aplicadas, archivos de bloqueo y rutas de secretos.
- `format-changed-file.sh` formatea el archivo editado (Spotless, Prettier, `dart format`, `ruff`).

Los nombres de eventos y el formato de permisos evolucionan: FND-05.1 los valida contra la documentación vigente. Nada destructivo o con coste (`terraform apply`, `kubectl delete`, `git push --force`) debe estar permitido sin tu aprobación en el momento.

### MCP

Solo lo que aporta, porque cada servidor ocupa contexto: documentación actualizada de librerías (crítico con Spring Boot 4, Quarkus y Angular recientes), GitHub (issues, PR, estado del pipeline), base de datos local en solo lectura, navegador para verificar el front y Grafana.

### Bucles

- **Bucle de verificación dentro de una tarea**: "itera hasta que `./mvnw -pl services/order-service -Pintegration verify` pase; si tras tres intentos falla por la misma causa, detente y explícame el bloqueo". La condición de parada es obligatoria: sin ella, un bucle acaba debilitando una prueba, que es el atajo prohibido.
- **`/loop`** para vigilar procesos largos: pruebas de resistencia, despliegues, simulacros.
- **Modo no interactivo** (`claude -p`) para tareas repetibles: verificación semanal de versiones nuevas, comprobar que los manuales siguen siendo ejecutables.
- **Sesiones en paralelo con *worktrees*** para sub-fases consecutivas sin dependencia entre sí (por ejemplo, el móvil mientras avanza el backend). Nunca dos sesiones sobre los mismos archivos.

## 6. Qué no delegar

- **Aprobar planes y decisiones de arquitectura.** El ADR lo firmas tú y debes poder defenderlo.
- **Cuentas, credenciales y gasto en la nube.** Tú creas las cuentas y apruebas cualquier `apply` con coste; confirmas el `destroy`.
- **La comprensión.** Si no puedes explicar lo que se fusionó, la sub-fase no está terminada para el segundo objetivo del proyecto.

## 7. Evidencia del uso de agentes

La carpeta `.claude/` versionada, `docs/agentes.md`, el historial de `docs/fases/` y los PR pequeños y revisados demuestran un proceso de ingeniería con agentes. Eso es lo que se valora, no que "la IA lo hizo".

## 8. Trabajar desde WSL

- **Ejecuta Claude Code dentro de WSL**, en la raíz del repositorio, no desde Windows sobre `\\wsl$`. Así usa el mismo bash, JDK, Docker y `kubectl` que tú, y los hooks `.sh` funcionan sin adaptación. Si usas la app de escritorio, abre la sesión sobre la carpeta de WSL y comprueba con `uname -a` que la terminal es la de Linux.
- **El repositorio vive en `~/…`**, nunca en `/mnt/d`.
- **La configuración personal de Claude Code es por entorno**: `~/.claude/` de WSL es distinta de la de Windows (inicio de sesión, MCP personales). Lo versionado en `.claude/` del proyecto viaja con el repositorio.
- **El agente no ve tu Windows**: para verificar interfaz usa un navegador controlado desde WSL (Playwright sin cabeza) o pásale capturas; los pasos **[Windows]** los ejecutas tú.
- **Memoria**: con el Compose completo más un build, WSL puede quedarse sin memoria y matar procesos sin aviso claro. Usa perfiles de Compose y revisa `.wslconfig`.

## 9. Primeros pasos

1. Copia la carpeta a WSL conservando la estructura, incluida `.claude/` (carpeta oculta):
   ```bash
   mkdir -p ~/proyectos && cp -r /mnt/d/Proyectos/portafolio/qhatu ~/proyectos/qhatu
   ```
2. Inicializa el repositorio y comprueba el roadmap:
   ```bash
   cd ~/proyectos/qhatu && git init -b main && python3 scripts/roadmap/roadmap.py validar
   ```
3. Crea el repositorio en GitHub y el tablero de GitHub Projects (FND-01.2 lo formaliza).
4. Abre Claude Code en esa carpeta, dentro de WSL, ejecuta `/fase` y confirma que propone `FND-01.1`.
5. Ejecuta `/fase FND-01.1` y sigue el ciclo.
