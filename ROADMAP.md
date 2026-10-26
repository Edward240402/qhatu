# Qhatu — Roadmap maestro

> **Qhatu** (quechua: *mercado*) es un marketplace multi-comercio con logística de última milla en tiempo real para Perú.
> Este archivo **orquesta** el proyecto: qué documento manda en cada frente, el orden canónico de implementación y las reglas comunes.

## 1. Objetivos

1. **Portafolio senior (backend-first).** Cada tecnología queda demostrada con una decisión justificada, código de calidad de producción, lógica de negocio real y evidencia verificable (pruebas, dashboards, informes de carga, pipelines en verde).
2. **Aprendizaje profundo.** Cada tema se entiende: por qué se usa, cómo funciona por dentro y cómo falla. Una sub-fase **no está terminada** sin su documentación de aprendizaje ([91-estandar-documentacion.md](docs/roadmap/91-estandar-documentacion.md)).

## 2. Mapa de documentos

| Documento | Contenido |
|---|---|
| [00-vision-y-negocio.md](docs/roadmap/00-vision-y-negocio.md) | Negocio, servicios, lógica de negocio compleja, tipos de integración, trazabilidad requisito → sub-fase |
| [01-fundamentos/](docs/roadmap/01-fundamentos/README.md) `FND` | Repositorio, entorno WSL, build, dominio, contratos, infraestructura local, agentes, documentación |
| [02-backend/](docs/roadmap/02-backend/README.md) `BE` | Microservicios Java 25: Spring Boot, WebFlux, Quarkus, Spring Modulith |
| [03-datos/](docs/roadmap/03-datos/README.md) `DB` | PostgreSQL, Flyway, NoSQL, Kafka y CDC, analítica, respaldos, datos sintéticos |
| [04-frontend-web/](docs/roadmap/04-frontend-web/README.md) `FE` | Angular |
| [05-movil/](docs/roadmap/05-movil/README.md) `MOB` | Flutter |
| [06-ia-ml/](docs/roadmap/06-ia-ml/README.md) `ML` | Deep Learning y MLOps |
| [07-infraestructura-nube/](docs/roadmap/07-infraestructura-nube/README.md) `INF` | Contenedores, Kubernetes, Terraform, AWS, Azure, serverless, alta disponibilidad |
| [08-calidad-y-cicd/](docs/roadmap/08-calidad-y-cicd/README.md) `OPS` | Pruebas y su matriz, contratos, Postman/Newman, CI/CD, GitOps, rendimiento |
| [09-observabilidad/](docs/roadmap/09-observabilidad/README.md) `OBS` | OpenTelemetry, Grafana, trazas, SLO, perfilado |
| [10-seguridad/](docs/roadmap/10-seguridad/README.md) `SEC` | Amenazas, secretos, PKI y certificados, criptografía, cadena de suministro, DAST |
| [90-gobierno-transversal.md](docs/roadmap/90-gobierno-transversal.md) | Cómo se hacen cumplir los estándares, profundidad, Git y versionado, gestión del trabajo, algoritmos |
| [91-estandar-documentacion.md](docs/roadmap/91-estandar-documentacion.md) | Plantillas de aprendizaje y manual de operación |
| [92-guia-claude-code.md](docs/roadmap/92-guia-claude-code.md) | Cómo trabajar este proyecto con Claude Code |
| [CLAUDE.md](CLAUDE.md) | Instrucciones permanentes para el agente |
| [docs/fases/ESTADO.md](docs/fases/ESTADO.md) | Tablero de avance, generado desde este archivo |

Cada frente es una carpeta con un `README.md` (requisitos comunes del frente e índice) y un archivo por fase. Cada fase se divide en **sub-fases**, que son la unidad de trabajo.

## 3. Cómo se ejecuta una sub-fase

Toda sub-fase (`BE-09.3`, `DB-05.2`, …) pasa por **tres pasos separados con aprobación entre cada uno**. El comando `/fase <ID>` detecta en qué paso está y ejecuta solo el siguiente.

| Paso | Qué produce | Toca código |
|---|---|---|
| 1. Análisis de dependencias | `docs/fases/<ID>/01-analisis.md` | No |
| 2. Planificación | `docs/fases/<ID>/02-plan.md` | No |
| 3. Implementación y cierre | Código, pruebas, documentación, `docs/fases/<ID>/03-cierre.md` | Sí |

Tamaño objetivo de una sub-fase: 1 a 3 sesiones, hasta unas 12 tareas, un resultado demostrable. Detalle en [90-gobierno-transversal.md](docs/roadmap/90-gobierno-transversal.md#1-unidad-de-trabajo-la-sub-fase) y [92-guia-claude-code.md](docs/roadmap/92-guia-claude-code.md).

## 4. Olas e hitos

Cada ola termina en un **hito demostrable** de punta a punta. Nunca se construye un frente completo de forma aislada.

| Ola | Tema | Hito demostrable |
|---|---|---|
| 0 | Fundamentos | Repo gobernado, entorno reproducible en WSL, dominio y reglas especificados, infraestructura local con TLS y Vault |
| 1 | Esqueleto andante | Login desde Angular → gateway (BFF) → `customer-service` cifrado → PostgreSQL, con traza en Grafana y CI con Sonar en verde |
| 2 | Catálogo, inventario y eventos | Catálogo con caché y eventos confiables; reserva de stock con cero sobreventa bajo carga |
| 3 | Búsqueda y plataforma Kubernetes | Búsqueda con Elasticsearch en la web; todo desplegado por GitOps en minikube de tres zonas con imágenes firmadas |
| 4 | Compra distribuida | Compra multi-comercio con promociones, pago en sandbox, saga con compensaciones y devoluciones parciales, en una sola traza |
| 5 | Tiempo real | Asignación por lotes, seguimiento en mapa en vivo, recargo dinámico y WhatsApp; SLO y alertas activos |
| 6 | Integraciones, finanzas y analítica | API GraphQL y webhooks para comercios, liquidación y facturación, dashboards sobre decenas de millones de eventos, PITR ensayado |
| 7 | Inteligencia artificial | Asistente con RAG, sentimiento de reseñas con modelo preentrenado, pronóstico de demanda propio y su ciclo MLOps |
| 8 | Nube y alta disponibilidad | El mismo sistema en EKS y AKS desde Terraform, con serverless, malla, pérdida de zona y de región ensayadas |
| 9 | Móvil | App de cliente y repartidor con paridad funcional (paralelizable desde el fin de la ola 5) |
| 10 | Endurecimiento y publicación | Informes de rendimiento, caos y seguridad; versión 1.0 y portafolio publicados |

## 5. Orden canónico de sub-fases

Este es el orden que siguen `/fase` y el validador (`python3 scripts/roadmap/roadmap.py validar`), que comprueba que **ninguna sub-fase depende de otra posterior**. Dentro de una ola se respeta el orden; dos sub-fases consecutivas sin dependencia entre sí pueden hacerse en paralelo en *worktrees* distintos.

#### Ola 0 · Fundamentos
`FND-01.1` → `OPS-01.1` → `FND-01.2` → `FND-05.1` → `FND-02.1` → `FND-02.2` → `FND-02.3` → `FND-03.1` → `FND-03.2` → `FND-03.3` → `FND-03.4` → `SEC-01.1` → `FND-04.1` → `FND-04.2` → `SEC-03.1` → `SEC-02.1` → `SEC-03.2` → `FND-06.1` → `FND-06.2`

#### Ola 1 · Esqueleto andante
`DB-01.1` → `DB-01.2` → `OPS-01.2` → `BE-01.1` → `OBS-01.1` → `OBS-01.2` → `DB-03.1` → `BE-02.1` → `BE-02.2` → `BE-02.3` → `OPS-02.1` → `BE-01.2` → `BE-01.3` → `SEC-05.1` → `SEC-04.1` → `BE-03.1` → `BE-03.2` → `BE-03.3` → `BE-04.1` → `OPS-03.1` → `INF-01.1` → `INF-01.2` → `BE-04.2` → `OPS-03.2` → `OPS-02.2` → `BE-04.3` → `DB-02.1` → `BE-04.4` → `FE-01.1` → `FE-01.2`

#### Ola 2 · Catálogo, inventario y eventos
`DB-04.1` → `DB-04.2` → `OPS-03.3` → `DB-04.3` → `DB-03.2` → `BE-05.1` → `BE-05.2` → `BE-05.3` → `BE-05.4` → `BE-05.5` → `BE-06.1` → `BE-06.2` → `DB-02.2` → `BE-06.3` → `OPS-02.4` → `BE-06.4` → `BE-06.5` → `OBS-02.1` → `OBS-02.2` → `OBS-05.1` → `BE-05.6`

#### Ola 3 · Búsqueda y plataforma Kubernetes
`BE-08.1` → `BE-08.2` → `OPS-02.3` → `BE-08.3` → `BE-08.4` → `FE-02.1` → `FE-02.2` → `SEC-06.1` → `INF-02.1` → `SEC-03.3` → `SEC-02.2` → `INF-02.2` → `INF-02.3` → `INF-02.4` → `OPS-04.1` → `SEC-05.2` → `OPS-04.2`

#### Ola 4 · Compra distribuida
`DB-05.1` → `DB-05.2` → `DB-05.3` → `BE-07.1` → `BE-07.2` → `BE-07.3` → `BE-08.5` → `BE-09.1` → `BE-09.2` → `BE-09.3` → `BE-09.4` → `BE-10.1` → `BE-10.2` → `BE-10.3` → `BE-10.4` → `BE-11.1` → `OBS-03.1` → `BE-11.2` → `OBS-03.2` → `BE-11.3` → `BE-09.5` → `DB-02.3` → `OPS-02.5` → `FE-02.3` → `FE-03.1` → `FE-03.2` → `FE-03.3`

#### Ola 5 · Tiempo real
`BE-12.1` → `BE-13.1` → `BE-13.2` → `DB-02.4` → `BE-12.2` → `BE-12.3` → `BE-12.4` → `BE-07.4` → `BE-13.3` → `BE-13.4` → `BE-14.1` → `BE-14.2` → `BE-14.3` → `FE-04.1` → `FE-04.2` → `OBS-03.3` → `FE-04.3` → `OBS-04.1` → `OBS-04.2`

#### Ola 6 · Integraciones, finanzas y analítica
`DB-06.1` → `DB-06.2` → `DB-02.5` → `DB-07.1` → `DB-07.2` → `DB-07.3` → `BE-15.1` → `BE-15.2` → `BE-15.3` → `BE-15.4` → `BE-16.1` → `BE-16.2` → `BE-16.3` → `BE-16.4` → `BE-17.1` → `BE-17.2` → `FE-05.1` → `FE-05.2` → `FE-05.3` → `FE-06.1` → `FE-06.2`

#### Ola 7 · Inteligencia artificial
`DB-02.6` → `ML-01.1` → `ML-01.2` → `ML-02.1` → `ML-02.2` → `ML-03.1` → `ML-03.2` → `ML-03.3` → `ML-04.1` → `ML-04.2` → `ML-04.3` → `BE-18.1` → `BE-18.2` → `BE-18.3` → `FE-07.1` → `FE-07.2` → `ML-05.1` → `ML-05.2`

#### Ola 8 · Nube y alta disponibilidad
`INF-07.1` → `INF-03.1` → `INF-03.2` → `INF-04.1` → `INF-04.2` → `INF-04.3` → `INF-04.4` → `OBS-06.1` → `OPS-04.3` → `INF-05.1` → `INF-05.2` → `INF-05.3` → `INF-05.4` → `OBS-06.2` → `SEC-02.3` → `SEC-03.4` → `INF-07.2` → `INF-07.3` → `INF-06.1` → `INF-06.2` → `INF-06.3` → `OPS-04.4` → `OPS-04.5` → `OPS-04.6` → `INF-08.1` → `SEC-06.2`

#### Ola 9 · Móvil
`MOB-01.1` → `MOB-01.2` → `MOB-02.1` → `MOB-02.2` → `MOB-03.1` → `MOB-03.2` → `MOB-04.1` → `MOB-04.2` → `MOB-05.1` → `MOB-05.2` → `MOB-06.1` → `MOB-06.2`

#### Ola 10 · Endurecimiento y publicación
`OPS-05.1` → `OPS-05.2` → `OPS-05.3` → `BE-19.1` → `BE-19.2` → `BE-19.3` → `OBS-05.2` → `SEC-06.3` → `FE-08.1` → `OPS-06.1`

## 6. Reglas transversales (no negociables)

1. **Sin atajos.** Nada de soluciones temporales, `TODO` sin issue, pruebas deshabilitadas o debilitadas, supresiones sin justificación, credenciales en el repositorio ni configuración "solo para que levante". Si algo no cabe con calidad, se recorta alcance de forma explícita, nunca calidad.
2. **Contrato primero.** OpenAPI, AsyncAPI, Protobuf o GraphQL antes que la implementación.
3. **Estándares con mecanismo de cumplimiento** y **adopción retroactiva** cuando un estándar se introduce o endurece ([90-gobierno-transversal.md](docs/roadmap/90-gobierno-transversal.md#3-estándares-cómo-se-hacen-cumplir)).
4. **Decisiones registradas** en ADR. **Versiones verificadas** en su fuente oficial y fijadas en `docs/versiones.md`.
5. **Lógica de negocio con rigor**: escenarios ejecutables, complejidad documentada, benchmark y pruebas de propiedades.
6. **Definición de terminado** de toda sub-fase:
   - criterios de "Terminado cuando" demostrados con evidencia;
   - pruebas del nivel que corresponda según la matriz de pruebas, en verde en CI;
   - análisis estático y de vulnerabilidades sin hallazgos nuevos bloqueantes;
   - telemetría presente en lo construido;
   - lista de terminado del frente (`docs/estandares/dod-<frente>.md`) cumplida;
   - documentación de aprendizaje y manual de operación actualizados;
   - `03-cierre.md` escrito, `ESTADO.md` actualizado, issue cerrado por el PR.
7. **Idioma.** Código, commits, nombres de API y eventos en inglés. Documentación en español; `README` y página de portafolio también en inglés.

## 7. Expectativas realistas

El alcance equivale al trabajo de un equipo pequeño: 220 sub-fases. Para una persona con apoyo de agentes, la estimación honesta es de **12 a 18 meses a tiempo parcial**. Por eso:

- El proyecto es **presentable desde el hito de la ola 4** (compra distribuida con lógica de precios, saga, observabilidad, Kubernetes y CI). Todo lo posterior suma.
- Lo marcado como **(opcional)** es lo primero que se recorta.
- La nube cuesta dinero: las sub-fases de la ola 8 se diseñan para levantar, ensayar, grabar y destruir, con presupuestos y alertas desde el primer `apply`.
