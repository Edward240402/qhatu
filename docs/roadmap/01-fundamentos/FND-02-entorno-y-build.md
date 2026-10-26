# FND-02 · Entorno WSL, cadena de herramientas y build

**Objetivo:** un entorno reproducible en WSL2 y un build de Maven con calidad forzada desde el primer módulo.

### FND-02.1 · Entorno WSL2 y herramientas versionadas
- **Ola:** 0 · **Profundidad:** B
- **Depende de:** FND-01.1

**Requerimientos**
- Primera sección de `docs/operacion/00-requisitos.md`: distro soportada, `systemd` habilitado en `/etc/wsl.conf`, `%UserProfile%\.wslconfig` con memoria, CPU y *swap* para el proyecto (por defecto WSL toma solo una parte de la RAM) y recuperación de memoria y disco.
- Repositorio en el sistema de archivos de Linux (`~/proyectos/qhatu`), con la explicación de por qué `/mnt/c` y `/mnt/d` son lentos y rompen permisos y vigilancia de archivos.
- Docker: ADR entre Docker Desktop con integración WSL y Docker Engine nativo en la distro (licencia, consumo, comodidad).
- **Versiones de herramientas fijadas en el repositorio** con un gestor único (`mise` recomendado, ADR frente a SDKMAN + nvm + pyenv): JDK 25, Maven, Node, Python, kubectl, Helm, Terraform, etc. Una persona que clona el repo obtiene exactamente las mismas versiones.
- `scripts/doctor.sh`: comprueba cada requisito, su versión, la memoria asignada a WSL y el acceso a Docker; indica cómo corregir cada fallo.
- Acceso desde Windows: reenvío de `localhost`, resolución de `*.qhatu.localhost`, y qué hacer cuando no funciona.
- `docs/versiones.md` con su formato (componente, versión, fuente consultada, fecha, notas de compatibilidad).

**Terminado cuando**
- En una distro limpia, siguiendo solo el manual, `scripts/doctor.sh` termina en verde.

**Aprender y documentar**
- Arquitectura de WSL2 (máquina virtual ligera, sistema de archivos 9P en `/mnt`, red NAT o *mirrored*) y sus consecuencias prácticas.

### FND-02.2 · Build multi-módulo de Maven
- **Ola:** 0 · **Profundidad:** A
- **Depende de:** FND-02.1

**Requerimientos**
- Maven Wrapper; Toolchains fijando Java 25; `maven-enforcer` (versiones de Java y Maven, convergencia de dependencias, dependencias prohibidas).
- POM raíz agregador + `libs/platform-bom` (importa los BOM de Spring Boot y de Quarkus, nunca mezclados en un mismo módulo) + POM padre por runtime (`spring-parent`, `quarkus-parent`).
- Módulo de ejemplo que se eliminará al crear el primer servicio real.
- Builds reproducibles (`project.build.outputTimestamp`); build selectivo (`-pl`, `-am`).

**Terminado cuando**
- `./mvnw verify` construye el módulo de ejemplo y dos ejecuciones producen artefactos idénticos.
- Introducir una dependencia con versión divergente hace fallar el enforcer.

**Aprender y documentar**
- Ciclo de vida, fases y *goals*; herencia frente a agregación; BOM y `import` scope; resolución de dependencias (mediación por cercanía) y convergencia. Experimento: provocar y resolver un conflicto de versiones transitivas.

### FND-02.3 · Perfiles de Maven y calidad en compilación
- **Ola:** 0 · **Profundidad:** A
- **Depende de:** FND-02.2

**Requerimientos**
- **Perfiles con propósito real**, documentados y sin duplicar lo que hacen los perfiles de Spring o Quarkus: `quality` (formato, análisis, cobertura, mutación), `integration` (Testcontainers vía Failsafe), `native`, `container`, `security` (dependencias, SBOM) y `ci` (composición de los anteriores). Activación explícita, no por magia.
- Spotless; Error Prone + NullAway con anotaciones JSpecify; Checkstyle; JaCoCo con umbral sobre código nuevo.
- Caché de build evaluada (Maven Build Cache Extension) con ADR.
- Estándar `docs/estandares/codigo-java.md`.
- Hook del agente que formatea el archivo editado (se configura aquí, ver FND-05.1).
- Comandos de build y prueba registrados en `CLAUDE.md`.

**Terminado cuando**
- `./mvnw -Pci verify` pasa en limpio; romper el formato o introducir un posible `NullPointerException` hace fallar el build.

**Aprender y documentar**
- Cuándo un perfil de Maven es la herramienta correcta y cuándo no; perfiles de Maven frente a perfiles de aplicación; cómo Error Prone se engancha al compilador.
