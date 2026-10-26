# OPS-01 · Integración continua

### OPS-01.1 · Esqueleto de CI y seguridad del pipeline
- **Ola:** 0 · **Profundidad:** B
- **Depende de:** FND-01.1

**Requerimientos**
- Flujos de GitHub Actions como **flujos reutilizables**, con detección de cambios por ruta para ejecutar solo lo afectado.
- Validación de Conventional Commits y del título del PR; **validador del roadmap** (`scripts/roadmap/roadmap.py validar`).
- Seguridad del propio pipeline: permisos mínimos del `GITHUB_TOKEN`, acciones de terceros fijadas por SHA, sin secretos en PR de *forks*, entornos con aprobación, sin interpolar entradas no confiables en scripts.

**Terminado cuando**
- Un PR con un commit inválido o un roadmap incoherente falla.

**Aprender y documentar**
- Modelo de ejecución de GitHub Actions; ataques a pipelines (inyección en flujos, acciones comprometidas) y sus defensas.

### OPS-01.2 · Pipeline de Java
- **Ola:** 1 · **Profundidad:** B
- **Depende de:** OPS-01.1, FND-02.3

**Requerimientos**
- Compilación, análisis, pruebas unitarias e integración por **módulo afectado y sus dependientes**; caché de dependencias; paralelismo.
- Resultados de pruebas y cobertura publicados en el PR.
- Objetivo de duración medido.

**Terminado cuando**
- Un PR que solo toca `web/` no ejecuta el pipeline de Java, y uno que toca una librería ejecuta los servicios que la usan.

**Aprender y documentar**
- Cómo se calcula el grafo de módulos afectados en Maven.
