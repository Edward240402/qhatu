# INF-02 · Kubernetes local con minikube

**Objetivo:** despliegue completo en Kubernetes local con prácticas de producción, a partir de la ola 3. Todo servicio posterior nace con su *chart*.

### INF-02.1 · Clúster local multi-nodo y entrada
- **Ola:** 3 · **Profundidad:** A
- **Depende de:** INF-01.2, OBS-01.2

**Requerimientos**
- minikube con controlador `docker` en WSL2 y **tres nodos etiquetados como zonas** (`topology.kubernetes.io/zone`); la memoria la limita `.wslconfig`. Perfil reducido para equipos con poca memoria.
- **Gateway API** (ADR de la implementación; `ingress-nginx` está retirado) como **balanceador de carga** de entrada.
- Espacios de nombres, cuotas, RBAC de mínimo privilegio, cuentas de servicio por carga de trabajo, Pod Security Standards nivel `restricted`.
- Acceso desde el navegador de Windows (`minikube tunnel`, resolución de nombres) documentado en `docs/operacion/04-minikube.md`.

**Terminado cuando**
- Un comando crea el clúster desde cero y un servicio de prueba responde por HTTPS a través del Gateway.

**Aprender y documentar**
- Arquitectura del plano de control y bucle de reconciliación; cómo llega una petición desde fuera hasta un contenedor (Gateway → Service → EndpointSlice → *pod*).

### INF-02.2 · *Charts* de Helm y estándar de Kubernetes
- **Ola:** 3 · **Profundidad:** A
- **Depende de:** INF-02.1, SEC-03.3, SEC-02.2

**Requerimientos**
- *Chart* de librería común y *chart* por servicio para todo lo existente; esquema de valores validado; pruebas de *charts*. ADR Helm frente a Kustomize.
- `docs/estandares/kubernetes.md` y `docs/estandares/alta-disponibilidad.md` (ver [README](README.md#alta-disponibilidad-por-capa)).
- En cada carga de trabajo: peticiones y límites, sondas de arranque, preparación y vida diferenciadas, `securityContext` restrictivo, PDB, distribución por zonas, `preStop` coordinado con el apagado ordenado.
- Migraciones Flyway como Job previo al despliegue.
- `helm lint` y kubeconform en CI.

**Terminado cuando**
- Una actualización continua bajo carga no produce errores visibles y matar un *pod* tampoco.

**Aprender y documentar**
- Ciclo de vida de un *pod* y de un despliegue; por qué las sondas mal configuradas causan caídas en cascada. Experimentos: fallo de sonda, `OOMKilled` provocado.

### INF-02.3 · Componentes con estado mediante operadores
- **Ola:** 3 · **Profundidad:** B
- **Depende de:** INF-02.2

**Requerimientos**
- Operadores: CloudNativePG (PostgreSQL con réplicas), Strimzi (Kafka con 3 *brokers* y temas como recursos), ECK (Elasticsearch), y operadores o *charts* oficiales para Redis y MongoDB; todos configurados para alta disponibilidad entre las tres zonas simuladas.
- Respaldos programados de los operadores hacia el almacenamiento de objetos.

**Terminado cuando**
- Matar el *pod* primario de PostgreSQL provoca la conmutación automática y los servicios se recuperan sin intervención.

**Aprender y documentar**
- Qué es un operador y el patrón de controlador; `StatefulSet` frente a operador.

### INF-02.4 · Autoescalado y políticas de red
- **Ola:** 3 · **Profundidad:** B
- **Depende de:** INF-02.3

**Requerimientos**
- HPA por CPU y por métricas propias; **KEDA** por retraso de consumidores de Kafka.
- NetworkPolicies con **denegación por defecto** y permisos explícitos alineados con el mapa de contextos.

**Terminado cuando**
- KEDA escala un consumidor al acumular mensajes y una conexión no permitida entre servicios es rechazada.

**Aprender y documentar**
- Cómo decide el HPA; escalar por métricas de cola frente a por CPU.
