# 90 · Gobierno transversal

Reglas que aplican a **todas** las sub-fases, sin importar el frente. Este documento responde a cómo se garantiza que lo decidido en una fase temprana se cumpla en todas las demás.

---

## 1. Unidad de trabajo: la sub-fase

- **Fase** (`BE-09`): agrupa un tema o un servicio completo. Es el nivel en el que se lee el roadmap.
- **Sub-fase** (`BE-09.3`): unidad que ejecuta `/fase` (análisis → plan → implementación). Es lo que se planifica, implementa, revisa y cierra.

Criterios de tamaño de una sub-fase:

| Criterio | Objetivo |
|---|---|
| Duración | De 1 a 3 sesiones de trabajo con el agente |
| Tareas en el plan | Hasta unas 12, cada una un commit |
| Resultado | **Uno** demostrable y verificable de forma independiente |
| Aprendizaje | Uno o dos temas tratados a fondo, no seis en la superficie |

Si en el análisis la sub-fase resulta más grande de lo previsto, el agente propone dividirla (`BE-09.3a`, `BE-09.3b`). Tú lo apruebas, y la división se refleja en el archivo de la fase, en `ROADMAP.md` y en `ESTADO.md`. El validador del roadmap admite ese sufijo.

Una fase puede tener sub-fases en **olas distintas** (por ejemplo, `DB-02` genera datos en cada ola, y `SEC-03` evoluciona la gestión de certificados de local a la nube). Las dependencias siempre se declaran **a nivel de sub-fase**.

---

## 2. Coherencia del orden

`ROADMAP.md` define el orden canónico de todas las sub-fases. El script `scripts/roadmap/roadmap.py` comprueba que:

1. toda sub-fase definida en `docs/roadmap/*/` aparece una sola vez en el orden;
2. la ola declarada en la sub-fase coincide con la ola en la que figura en el orden;
3. **toda dependencia aparece antes en el orden** (ninguna sub-fase temprana requiere una posterior);
4. no hay referencias a sub-fases inexistentes.

```bash
python3 scripts/roadmap/roadmap.py validar
```

Se ejecuta en CI desde `OPS-01.1` y en el paso de análisis de `/fase`. Cualquier cambio en el roadmap pasa por él.

---

## 3. Estándares: cómo se hacen cumplir

Las fases fundacionales no producen "recomendaciones": producen un **estándar** en `docs/estandares/` y el **mecanismo que lo hace cumplir**. Un estándar sin mecanismo de cumplimiento no se acepta.

### Capas de cumplimiento (de más fuerte a más débil)

1. **Automatización en CI y en el build**: si se incumple, el build falla (linters, ArchUnit, *quality gates*, validadores de contratos, lint de migraciones).
2. **Plantillas**: los servicios nuevos nacen desde la plantilla de `BE-01.2`, que ya trae incorporados los estándares técnicos.
3. **Hooks del agente**: bloquean acciones prohibidas (editar migraciones aplicadas, leer secretos).
4. **Plan de la sub-fase**: el paso 2 de `/fase` incluye obligatoriamente una tabla "Estándares aplicables → cómo se cumplen en esta sub-fase".
5. **Revisión**: el subagente `revisor-calidad` contrasta el diff con los estándares y con la lista de terminado del frente.

### Registro de estándares

| Estándar (`docs/estandares/`) | Lo crea | Se hace cumplir con |
|---|---|---|
| `versionado-y-git.md` | FND-01.2 | commitlint, protección de rama, release-please |
| `codigo-java.md` | FND-02.3 | Spotless, Error Prone + NullAway, Checkstyle en el build |
| `arquitectura.md` (reglas por estilo) | FND-03.2 | Reglas ArchUnit en cada servicio (OPS-02.1) |
| `api.md` | FND-03.3 | Spectral y oasdiff en el PR (OPS-03.1) |
| `eventos.md` | FND-03.3, ampliado en DB-04.1 | Validación AsyncAPI y compatibilidad en el registro de esquemas (OPS-03.3) |
| `reglas-de-negocio-y-algoritmos.md` | FND-03.4 | Escenarios ejecutables (Cucumber) y JMH en CI; revisión de complejidad |
| `seguridad.md`, `clasificacion-de-datos.md` | SEC-01.1 | Sonar/SAST (SEC-05.1), pruebas de autorización, ZAP (SEC-06) |
| `certificados.md` | SEC-03.1 | Alertas de expiración (OBS-04), cert-manager, prohibición de TLS sin verificar en el revisor |
| `secretos.md` | SEC-02.1 | gitleaks, permisos denegados al agente, External Secrets |
| `criptografia.md` | SEC-04.1 | Uso obligatorio de `common-crypto`; regla ArchUnit que prohíbe primitivas criptográficas fuera de ella |
| `sql.md` | DB-01.1 | Revisión; pruebas pgTAP desde DB-05.2 |
| `migraciones.md` | DB-01.2 | Squawk en CI, `flyway validate`, hook que bloquea editar migraciones aplicadas, prueba de migración desde la versión anterior |
| `redis.md`, `mongodb.md` | DB-03 | Convención de claves verificada en pruebas; TTL obligatorio |
| `observabilidad.md` | OBS-01.2 | Plantilla de servicio, prueba que falla si se registra un dato personal, dashboard generado automáticamente |
| `pruebas.md` (matriz nivel × momento) | OPS-02.1 | Umbrales de cobertura y mutación, pipeline por etapas |
| `contenedores.md` | INF-01.1 | hadolint y Trivy en CI; Kyverno en el clúster (SEC-06.2) |
| `kubernetes.md`, `alta-disponibilidad.md` | INF-02.2 | `helm lint`, kubeconform, políticas Kyverno (réplicas, PDB, recursos) |
| `frontend.md` | FE-01.1 | ESLint con reglas de límites, presupuestos de build, axe en E2E |
| `documentacion.md` | FND-06.1 | Verificador de enlaces y de referencias `ruta:línea` en CI |
| `dod-<frente>.md` (listas de terminado) | FND-06.1 | Paso de cierre de `/fase` y revisor |

### Regla de adopción retroactiva

Cuando una sub-fase **introduce o endurece** un estándar, incluye en su plan la adopción en **todo lo ya construido**. Nunca se deja "para los servicios nuevos". Ejemplos:

- `OBS-03.1` añade propagación de trazas por Kafka → actualiza todos los productores y consumidores existentes.
- `SEC-03.3` introduce certificados de corta vida → migra todos los servicios ya desplegados.
- `DB-05.2` introduce el trigger genérico de auditoría → nueva migración en los servicios que manejan datos auditables.

Si la adopción es grande, se crea una sub-fase propia de adopción, ubicada inmediatamente después.

---

## 4. Profundidad: profesional siempre, a fondo donde importa

**Toda implementación es de nivel profesional**: configuración segura, pruebas, observabilidad y operación real. Lo que varía es **cuánto se profundiza en el aprendizaje**, porque con esta cantidad de tecnologías no es posible (ni útil) estudiar todas a nivel de código fuente. Cada sub-fase declara su nivel:

| Nivel | Significa | Se aplica a |
|---|---|---|
| **A · Dominio** | Mecanismo interno, casos límite, experimentos de fallo, mediciones propias y comparación de alternativas. Lo puedes defender en una entrevista técnica senior | Concurrencia en Java, Spring, Kafka, PostgreSQL, sagas y consistencia, resiliencia, seguridad (OAuth2, criptografía, PKI), lógica de negocio y algoritmos, observabilidad |
| **B · Profesional** | Funcionamiento suficiente para diseñar, operar y diagnosticar en producción. Decisiones justificadas y al menos un experimento de fallo | Quarkus, WebFlux, Elasticsearch, Redis, MongoDB, Kubernetes, Terraform, nube, CI/CD, Angular, ML |
| **C · Competente** | Uso correcto según las buenas prácticas, conceptos clave y compromisos documentados | Malla de servicios, Jenkins, Flutter, serverless, herramientas opcionales |

Esta es mi recomendación explícita: el proyecto es *backend-first*, así que el nivel A se concentra ahí. Si quieres subir el nivel de un tema, cámbialo en la sub-fase antes de planificarla.

---

## 5. Git y versionado

Lo que podía parecer contradictorio son dos cosas distintas:

- **Repositorio Git: uno solo** (monorepo) para todo el proyecto. Es la opción recomendada aquí: cambios atómicos entre contrato y consumidores, un único lugar para el portafolio y menos coste de mantenimiento para una persona.
- **Sistema de build: uno por ecosistema.** Maven para Java, npm para Angular, Flutter para móvil, `uv` para Python. Viven en el mismo repositorio, pero cada uno con su herramienta nativa.
- **Versión de release: una por componente desplegable.** Cada microservicio, la web, la app móvil, el servicio de inferencia y cada *chart* tiene su propia versión semántica.

Cómo se gestiona (se implementa en FND-01.2 y OPS-04.1):

- **Trunk-based**: rama `main` protegida, ramas cortas por sub-fase (`fase/be-09.3`), PR obligatorio con checks.
- **Conventional Commits con alcance del componente**: `feat(order-service): …`, `fix(web): …`.
- **release-please en modo monorepo**: lee los commits por ruta, calcula la versión de cada componente afectado, mantiene su `CHANGELOG.md` y crea etiquetas `order-service/v1.4.0`, `web/v0.9.2`.
- **Imágenes** etiquetadas con esa versión y con el *digest*; los despliegues siempre por *digest*.
- **Librerías internas** (`libs/`) versionadas igual; los servicios dependen de versiones publicadas, no de `SNAPSHOT`, para que un cambio en una librería no rompa servicios en silencio.
- **Contratos** versionados por su propia política (versión mayor en la ruta de la API, compatibilidad en el registro de esquemas).

---

## 6. Gestión del trabajo: GitHub Projects, sin Jira ni Confluence

Recomendación: **GitHub Issues + GitHub Projects**.

| Opción | Coste | Valor para este proyecto |
|---|---|---|
| GitHub Projects | Gratis | Integrado con PR y commits (`Closes #123`), visible públicamente en el portafolio, automatizable con `gh` desde el agente |
| Jira (plan gratuito) | Gratis hasta un número limitado de usuarios | Es lo más usado en empresas peruanas, pero su uso básico se aprende en días y su valor real es en equipos. Duplicaría el seguimiento y no sería visible para quien vea el portafolio |
| Confluence / Notion | Gratis con límites | Contradicen la documentación como código: separan la documentación del código que describe y no se versionan con él |

Organización:

- **Hito (milestone)** = ola. **Issue** = sub-fase, creado en el paso 1 de `/fase` y cerrado por el PR. **Etiquetas** por frente (`frente:backend`) y por tipo (`tipo:deuda`, `tipo:bug`).
- Las deudas y pendientes que aparezcan en un cierre se registran como issues; nunca como `TODO` sueltos en el código.
- `docs/fases/ESTADO.md` sigue siendo la fuente de verdad del estado para el agente; el issue es el ancla de la discusión y del PR.

Si quieres practicar Jira por empleabilidad, la opción razonable es conectar un Jira gratuito al repositorio durante una sola ola, como ejercicio, sin convertirlo en la fuente principal.

---

## 7. Dónde vive la documentación

**En el repositorio**, como código, y **publicada** como sitio estático (FND-06.2). No conviene moverla a otro lado:

- referencia código por `ruta:línea` y se verifica en CI, algo imposible en una wiki externa;
- cada PR actualiza código y documentación juntos, de modo que nunca se desincronizan;
- el sitio publicado (GitHub Pages) es la cara del portafolio, sin coste.

Lo único que vive fuera del repositorio: secretos (baúl de llaves), datos generados de volumen (almacenamiento de objetos) y artefactos de modelos (registro de MLflow).

Organización del sitio por público: **Portafolio** (qué evaluar y dónde), **Aprendizaje**, **Operación**, **Arquitectura** (C4, ADR, contratos) y **Estándares**. El `README.md` raíz y la página de portafolio van en **español e inglés**, para no cerrar la puerta a procesos de selección internacionales.

---

## 8. Reglas para algoritmos y lógica de negocio

Las reglas de negocio complejas (catálogo en [00-vision-y-negocio.md](00-vision-y-negocio.md#4-lógica-de-negocio-compleja)) cumplen siempre:

1. **Especificación por ejemplos** antes del código: escenarios en Gherkin escritos en FND-03.4 o en el plan, que se convierten en pruebas ejecutables.
2. **Análisis de complejidad** en tiempo y espacio en el plan y en el código (Javadoc del algoritmo), con el tamaño de entrada esperado según los requisitos no funcionales.
3. **Justificación de la elección**: si el problema óptimo es NP-difícil o caro (asignación, combinación de promociones, rutas), se documenta la cota del problema exacto y la heurística o aproximación elegida, con su garantía o su error medido.
4. **Benchmark con JMH** para los algoritmos en el camino crítico y **pruebas basadas en propiedades** (jqwik) para sus invariantes.
5. **Dominio puro**: el algoritmo vive en el núcleo de dominio, sin dependencias de framework, para poder probarlo y medirlo aislado.
