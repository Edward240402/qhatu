# 91 · Estándar de documentación

Dos familias de documentos, con públicos distintos, que **se actualizan en cada sub-fase** como parte de su definición de terminado:

| Familia | Carpeta | Para quién | Tono |
|---|---|---|---|
| **Aprendizaje** | `docs/aprendizaje/` | Tú, y quien evalúe tu profundidad técnica | Explicativo, a fondo |
| **Operación** | `docs/operacion/` | Alguien que no conoce el proyecto y quiere usarlo | Conciso, paso a paso, sin teoría |

Más los registros: `docs/adr/` (decisiones), `docs/estandares/` (reglas que se hacen cumplir) y `docs/fases/<ID>/` (análisis, plan y cierre de cada sub-fase). Todo vive en el repositorio y se publica como sitio (ver [90-gobierno-transversal.md](90-gobierno-transversal.md#7-dónde-vive-la-documentación)).

---

## A. Documentación de aprendizaje

### Organización

Un documento **por tecnología o patrón**, no por sub-fase, porque un tema reaparece en varias sub-fases y debe crecer en un solo lugar:

```
docs/aprendizaje/
  README.md                       # índice por tema y por frente; ruta de lectura sugerida
  java/virtual-threads.md         spring/autoconfiguracion.md      quarkus/modelo-de-ejecucion.md
  reactivo/backpressure.md        patrones/saga.md                 patrones/outbox-y-cdc.md
  arquitectura/estilos.md         resiliencia/patrones.md          kafka/fundamentos.md
  datos/postgresql-planificador.md  datos/flyway-y-evolucion.md   busqueda/elasticsearch.md
  seguridad/oauth2-oidc-jwt.md    seguridad/pki-y-tls.md           algoritmos/asignacion.md
  kubernetes/…  observabilidad/…  ml/…  frontend/…  movil/…
  _experimentos/<tema>/           # scripts invocados desde los documentos
```

Cuando una sub-fase vuelve a tocar un tema, **amplía** su documento con una sección nueva; no crea otro.

### Profundidad según el nivel de la sub-fase

Cada sub-fase declara su nivel ([90-gobierno-transversal.md](90-gobierno-transversal.md#4-profundidad-profesional-siempre-a-fondo-donde-importa)). Las secciones de la plantilla son las mismas; cambia lo que se exige en ellas:

| Sección | Nivel A · Dominio | Nivel B · Profesional | Nivel C · Competente |
|---|---|---|---|
| 2. Cómo funciona por dentro | Mecanismo interno completo, con casos límite y referencias a especificaciones | Lo necesario para diseñar, operar y diagnosticar | Conceptos clave |
| 4. Experimentos | Varios, incluidos de fallo y mediciones propias | Al menos uno de uso y uno de fallo | Al menos uno |
| 6. Alternativas | Comparación con datos del proyecto | Comparación razonada | Mención y criterio |
| 7. Preguntas | 8 a 10, nivel entrevista senior | 5 | 3 |

### Plantilla obligatoria

```markdown
# <Tecnología o patrón>

> **En una frase:** qué es y para qué lo usamos en Qhatu.
> **Sub-fases donde se aplica:** BE-09.3, BE-11.1 · **Nivel:** A · **Última revisión:** AAAA-MM-DD · **Versión usada:** x.y

## 1. El problema
Qué pasa si NO se usa. Un ejemplo concreto del dominio de Qhatu.

## 2. Cómo funciona por dentro
El mecanismo real, no la descripción de la API. Diagramas Mermaid cuando haya flujo,
estados o interacción. Debe permitir predecir el comportamiento en un caso nuevo.

## 3. Cómo lo usamos aquí
Decisiones y su ADR. Recorrido por el código con referencias `ruta/Archivo.java:línea`
y fragmentos cortos comentados. Configuración relevante, parámetro por parámetro.

## 4. Experimentos reproducibles
Para cada uno: objetivo, requisitos, comandos exactos (bash en WSL), qué observar
(dashboard, log, métrica) y cómo interpretarlo. Siempre al menos uno de fallo.

## 5. Errores comunes y cómo diagnosticarlos
Síntoma → causa → cómo confirmarlo → corrección.

## 6. Alternativas y cuándo NO usarlo

## 7. Preguntas para comprobar que lo entendí
Con la respuesta plegada (<details>).

## 8. Referencias
Fuentes primarias (documentación oficial, JEP, RFC, KIP) siempre que existan.
```

Los documentos de **algoritmos** añaden: definición formal del problema, complejidad del problema exacto, algoritmo elegido con su complejidad en tiempo y espacio, garantía o error medido, y enlace al benchmark JMH.

### Reglas de calidad

1. **Profundidad sobre amplitud.** "Un virtual thread es un hilo ligero" no basta; hay que explicar continuaciones, *carrier threads* y qué ocurre en una llamada bloqueante.
2. **Verificable.** Toda afirmación sobre comportamiento se apoya en un experimento o en una fuente primaria. Lo no verificado se marca como tal.
3. **Enlazado al código real.** Las referencias `ruta:línea` se comprueban en CI (FND-06.2).
4. **Experimentos ejecutables** tal cual, preferiblemente como scripts en `_experimentos/`.
5. **Sin relleno.** No se copia la documentación oficial; se enlaza y se escribe lo que no dice.
6. **Comparaciones con datos propios** cuando el proyecto implementa dos enfoques.

### Diario de aprendizaje

En cada `docs/fases/<ID>/03-cierre.md`, una sección breve **"Lo que aprendí"**: sorpresas, errores cometidos, qué haría distinto. Es material directo para entrevistas.

---

## B. Manual de operación

Para alguien que **nunca vio el proyecto**. Conciso pero completo: cada documento se sigue de principio a fin sin leer otro, salvo los requisitos.

```
docs/operacion/
  README.md                  # qué manual usar según lo que quieras hacer
  00-requisitos.md           # preparación de WSL2, hardware, herramientas versionadas, cuentas externas, doctor.sh
  01-local-individual.md     # levantar cada microservicio o artefacto por separado
  02-docker.md               # construir y correr cada imagen suelta
  03-docker-compose.md       # sistema completo o por perfiles
  04-minikube.md             # Kubernetes local de tres zonas
  05-aws.md                  # Kubernetes en AWS (EKS)
  06-azure.md                # Kubernetes en Azure (AKS)
  07-datos-de-prueba.md      # perfiles S/M/L, instantáneas, usuarios y roles, tarjetas de sandbox
  08-solucion-de-problemas.md
  runbooks/                  # guías de respuesta enlazadas desde las alertas (OBS-04.2)
```

### Contenido obligatorio de cada manual de nivel (01 a 06)

1. **Para qué sirve** este nivel y cuándo elegirlo.
2. **Requisitos específicos**, con el comando para verificar cada uno.
3. **Levantar**: pasos numerados con comandos exactos en bash desde WSL2. Si un paso se hace en Windows (confiar la CA, abrir el emulador, editar `.wslconfig`), se marca **[Windows]** con la ruta o el comando exacto.
4. **Verificar**: URL, comando de salud y salida esperada.
5. **Acceder**: tabla de URLs, puertos y credenciales de prueba.
6. **Bajar**: detener conservando datos, y limpiar por completo.
7. **Problemas frecuentes** de ese nivel.
8. En la nube: **coste estimado por hora** y cómo comprobar que no quedó nada facturando.

### `01-local-individual.md`

Una fila por artefacto, mantenida en cada sub-fase que añade uno:

| Artefacto | Depende de (infra) | Levantar | Puerto | Salud | Detener |
|---|---|---|---|---|---|
| `customer-service` | PostgreSQL, Keycloak, Vault | `./mvnw -pl services/customer-service spring-boot:run -Dspring-boot.run.profiles=local` | 8081 | `/actuator/health` | Ctrl+C |

Incluye modo de desarrollo con recarga (DevTools, `quarkus:dev`, `ng serve`, `flutter run`), depuración remota desde IntelliJ y cómo levantar solo la infraestructura mínima de cada uno.

### Reglas de calidad

1. **Probado desde un clon limpio** al cerrar la sub-fase que lo cambia; la evidencia va en `03-cierre.md`.
2. **Un comando por paso**, con su resultado esperado.
3. **Sin teoría**: se enlaza a `docs/aprendizaje/`.
4. **Automatizado donde se pueda**: los procedimientos largos se convierten en objetivos de `task`.
5. **Verificado en CI**: los niveles local, Docker, Compose y minikube se ejecutan en un flujo programado con los mismos comandos del manual.
6. **Entorno de referencia: WSL2 sobre Windows 11**; debe funcionar igual en Linux nativo. Las particularidades de WSL van en `00-requisitos.md` y `08-solucion-de-problemas.md`.
7. **Sin secretos reales.**

---

## C. Qué documenta cada sub-fase

El plan (paso 2 de `/fase`) lista: documentos de aprendizaje a crear o ampliar con sus experimentos, manuales de operación afectados, estándares nuevos o modificados, y ADR. El cierre verifica que cada uno existe y cumple su plantilla.
