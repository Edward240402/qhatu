# OPS-04 · Entrega continua, GitOps y registro de contenedores

**Principio:** construir una vez, firmar, publicar en el registro y **promover el mismo artefacto** por *digest* entre entornos. El pipeline de CI nunca tiene credenciales del clúster: Argo CD extrae los cambios desde Git.

### OPS-04.1 · Publicación de artefactos y versionado por componente
- **Ola:** 3 · **Profundidad:** B
- **Depende de:** INF-02.2, SEC-05.1

**Requerimientos**
- Imágenes publicadas en el **registro de contenedores** (GHCR) etiquetadas con versión semántica y *digest*; *charts* de Helm como artefactos OCI.
- release-please activo para cada componente existente: versión, `CHANGELOG.md` y etiqueta `componente/vX.Y.Z` por componente.
- Políticas de retención e inmutabilidad de etiquetas.

**Terminado cuando**
- Fusionar un cambio en un servicio produce solo la nueva versión de ese servicio, con su imagen y *chart* publicados.

**Aprender y documentar**
- Formato de imagen OCI, manifiestos e índices multi-arquitectura; por qué desplegar por *digest*.

### OPS-04.2 · GitOps local con Argo CD
- **Ola:** 3 · **Profundidad:** B
- **Depende de:** OPS-04.1, INF-02.4

**Requerimientos**
- Argo CD en minikube con patrón aplicación de aplicaciones o ApplicationSets; directorio `deploy/environments/local`.
- CI actualiza el *digest* en el directorio del entorno mediante un PR automático; Argo CD sincroniza con autocorrección.
- Inicio de sesión único en Argo CD con Keycloak y RBAC.

**Terminado cuando**
- Fusionar un cambio despliega automáticamente en minikube, y un cambio manual en el clúster es revertido por Argo CD.

**Aprender y documentar**
- Despliegue por empuje frente a por extracción; reconciliación y deriva.

### OPS-04.3 · Promoción entre entornos en la nube
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-04.4

**Requerimientos**
- Entornos en la nube con promoción por PR, aprobación manual para el entorno superior, migraciones como etapa controlada, réplica de imágenes a ECR y ACR.
- Pruebas de humo (Newman) y verificación de salud tras desplegar; vuelta atrás documentada y probada.

**Terminado cuando**
- Una versión se promueve de un entorno a otro sin reconstruir la imagen, y una vuelta atrás se ejecuta en minutos.

**Aprender y documentar**
- Entrega continua frente a despliegue continuo.

### OPS-04.4 · Entrega progresiva
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** OPS-04.3, OBS-04.1

**Requerimientos**
- Argo Rollouts: despliegue canario de `order-service` con análisis automático sobre métricas (tasa de error, latencia, SLO) y vuelta atrás automática.

**Terminado cuando**
- Un despliegue con un error inyectado es revertido por el análisis sin intervención.

**Aprender y documentar**
- Estrategias de despliegue (continuo, azul-verde, canario) y sus requisitos.

### OPS-04.5 · Pipeline equivalente en Jenkins
- **Ola:** 8 · **Profundidad:** C
- **Depende de:** OPS-04.3

**Requerimientos**
- Jenkins configurado como código (JCasC), agentes efímeros en Kubernetes, librería compartida, `Jenkinsfile` declarativo para un servicio Java y para la web, que produce el mismo artefacto que GitHub Actions.
- Comparativa escrita entre ambos.

**Terminado cuando**
- El artefacto de Jenkins es idéntico (mismo *digest* con build reproducible) al de GitHub Actions.

**Aprender y documentar**
- Modelo de Jenkins (controlador, agentes, pipeline como código).

### OPS-04.6 · Métricas DORA
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** OPS-04.4

**Requerimientos**
- Frecuencia de despliegue, tiempo de entrega de cambios, tasa de fallo y tiempo de recuperación, calculadas desde GitHub y Argo CD y mostradas en Grafana.

**Terminado cuando**
- El dashboard muestra las cuatro métricas con datos reales del proyecto.

**Aprender y documentar**
- Qué miden las métricas DORA y cómo se distorsionan.
