# SEC-05 · Análisis estático y cadena de suministro

### SEC-05.1 · SAST, SonarQube, dependencias y secretos
- **Ola:** 1 · **Profundidad:** B
- **Depende de:** OPS-01.2

**Requerimientos**
- **SonarQube** (SonarCloud si el repositorio es público, o instancia en Compose): *quality gate* sobre código nuevo — cero errores y vulnerabilidades nuevas, cobertura mínima, duplicación máxima — bloqueante en el PR. Perfiles para Java, TypeScript, Dart y Python (se activan a medida que aparecen).
- SAST adicional (CodeQL o Semgrep).
- Análisis de dependencias (OWASP Dependency-Check o Trivy), con política de plazos por severidad y excepciones con fecha de caducidad.
- gitleaks en *pre-commit* y en CI, con el historial completo escaneado.
- Revisión de licencias de dependencias.

**Terminado cuando**
- Un PR con una vulnerabilidad conocida, un secreto o una caída del *quality gate* no se puede fusionar.

**Aprender y documentar**
- SAST, SCA y DAST: qué encuentra cada uno; cómo leer un CVE y su puntuación, y decidir.

### SEC-05.2 · SBOM, firma de imágenes y procedencia
- **Ola:** 3 · **Profundidad:** B
- **Depende de:** OPS-04.1, INF-01.1

**Requerimientos**
- SBOM CycloneDX por artefacto e imagen, publicado junto a ella.
- Escaneo de imágenes, IaC y manifiestos de Kubernetes.
- **Firma de imágenes** con cosign (firma sin claves con OIDC de GitHub) y atestaciones de procedencia SLSA.
- Renovate con agrupación y fusión automática de parches que pasan las pruebas.

**Terminado cuando**
- Toda imagen publicada tiene SBOM, firma y procedencia verificables con un comando documentado.

**Aprender y documentar**
- Ataques a la cadena de suministro y qué mitiga cada control; cómo funciona la firma sin claves (Sigstore, Fulcio, Rekor).
