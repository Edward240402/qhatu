# INF-01 · Contenedores

### INF-01.1 · Imágenes endurecidas
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** BE-04.1

**Requerimientos**
- `docs/estandares/contenedores.md` y Dockerfile multietapa para Spring Boot (capas del JAR con `jarmode`). Quarkus (JVM y nativo), Python y Angular siguen el estándar cuando aparezcan (adopción en sus sub-fases).
- Imagen base mínima (distroless o equivalente) fijada por *digest*; usuario no root; sistema de archivos de solo lectura; sin *shell* en la imagen final.
- ADR: Dockerfile frente a Buildpacks frente a Jib; JRE completo frente a `jlink`.
- Memoria de la JVM consciente del contenedor; señales y apagado ordenado.
- BuildKit: caché de dependencias, multi-arquitectura (amd64 y arm64), secretos de compilación que no quedan en capas.
- hadolint y escaneo de la imagen en CI.

**Terminado cuando**
- La imagen corre como no root, sin vulnerabilidades críticas, y la tabla de tamaño y arranque está publicada.

**Aprender y documentar**
- Qué es un contenedor (*namespaces*, *cgroups*, capas); por qué importa el PID 1; cómo la JVM detecta los límites del contenedor.

### INF-01.2 · Sistema completo en Compose
- **Ola:** 1 · **Profundidad:** B
- **Depende de:** INF-01.1, BE-03.1

**Requerimientos**
- Servicios de aplicación en el Compose con perfiles por ola, sobre la infraestructura de FND-04.
- Manuales `docs/operacion/02-docker.md` (un servicio suelto) y `03-docker-compose.md` actualizados.

**Terminado cuando**
- Desde un clon limpio, un comando levanta el esqueleto andante completo por HTTPS.

**Aprender y documentar**
- Compose como herramienta de desarrollo frente a orquestador de producción.
