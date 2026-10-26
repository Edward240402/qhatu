# 07 · Infraestructura y nube (`INF`)

Principio rector: **el mismo artefacto y los mismos manifiestos** corren en local, en minikube, en AWS y en Azure; solo cambia la configuración por entorno. La portabilidad es la demostración. La gestión de secretos y certificados en la nube está en [SEC](../10-seguridad/README.md); la entrega continua y GitOps en [OPS-04](../08-calidad-y-cicd/OPS-04-entrega-continua.md).

| Fase | Título | Olas |
|---|---|---|
| [INF-01](INF-01-contenedores.md) | Contenedores | 1 |
| [INF-02](INF-02-kubernetes-local.md) | Kubernetes local con minikube | 3 |
| [INF-03](INF-03-terraform.md) | Terraform multi-nube | 8 |
| [INF-04](INF-04-aws.md) | AWS | 8 |
| [INF-05](INF-05-azure.md) | Azure | 8 |
| [INF-06](INF-06-serverless.md) | Serverless | 8 |
| [INF-07](INF-07-alta-disponibilidad.md) | Alta disponibilidad y recuperación ante desastres | 8 |
| [INF-08](INF-08-malla-de-servicios.md) | Malla de servicios y mTLS | 8 |

## Alta disponibilidad por capa

Resumen del estándar `docs/estandares/alta-disponibilidad.md` (se crea en INF-02.2 a partir de los objetivos de FND-03.2 y se valida en INF-07):

| Capa | Mecanismo |
|---|---|
| Servicios sin estado | ≥ 2 réplicas (≥ 3 en críticos), distribución por zona, PDB, sondas correctas, apagado ordenado, sesiones fuera del proceso (Redis) |
| Gateway y balanceador | Varias réplicas tras el balanceador gestionado multi-zona |
| PostgreSQL | CloudNativePG con primario y réplicas en otras zonas y conmutación automática; en la nube, RDS Multi-AZ y Flexible Server con alta disponibilidad por zona |
| Kafka | 3 *brokers* en zonas distintas, factor de réplica 3, `min.insync.replicas=2`, `acks=all`, conciencia de rack |
| Redis | Réplicas con Sentinel o modo clúster; en la nube, la opción gestionada con réplica en otra zona |
| MongoDB | Conjunto de réplicas de 3 miembros en zonas distintas |
| Elasticsearch | 3 nodos elegibles como maestro; réplicas de cada *shard* en otra zona |
| Keycloak y Vault | Keycloak en clúster con caché distribuida; Vault con Raft de 3 nodos |
| Web | Archivos estáticos en almacenamiento de objetos detrás de una CDN (múltiples puntos de presencia) |
| Móvil | Tolerancia a fallos del backend: caché, modo sin conexión, reintentos idempotentes |
| Inferencia de ML | Réplicas sin estado; respuesta de respaldo si no está disponible |
| Región | Recuperación ante desastres activo-pasivo documentada y ensayada una vez (INF-07.3) |

En local, la alta disponibilidad se demuestra con un clúster de minikube de **tres nodos etiquetados como zonas**: drenar una "zona" debe ser invisible para el usuario. La alta disponibilidad real en la nube cuesta dinero: se levanta, se ensaya, se graba y se destruye.

## Servicios de nube: cuáles y por qué

Se usan los servicios gestionados cuando aportan algo que el clúster no da bien; si no, se documentan como variante.

| Necesidad | AWS | Azure | Uso |
|---|---|---|---|
| Kubernetes gestionado | EKS | AKS | Base |
| Balanceador de carga | ALB (AWS Load Balancer Controller + Gateway API) | Application Gateway for Containers | Base |
| Registro de contenedores | ECR | ACR | Base |
| Baúl de llaves y claves | Secrets Manager + KMS | Key Vault | Base |
| PostgreSQL gestionado | RDS | Database for PostgreSQL Flexible Server | Base |
| Redis gestionado | ElastiCache | Azure Managed Redis (verificar; Azure Cache for Redis anunció su retiro) | Base |
| Almacenamiento de objetos | S3 | Blob Storage | Base |
| CDN y sitio estático | CloudFront + S3 | Front Door + Storage | Base: web e imágenes de producto |
| DNS y certificados | Route 53, ACM | Azure DNS, certificados gestionados | Base |
| WAF | AWS WAF | WAF de Front Door / Application Gateway | Base |
| Funciones | Lambda | Azure Functions | Base (INF-06) |
| Enrutamiento de eventos | EventBridge | Event Grid | Base: eventos de almacenamiento hacia funciones |
| Cola gestionada | SQS | Service Bus | Base: desacoplar webhooks entrantes del clúster |
| Correo transaccional | SES | Communication Services Email | Base (BE-14) |
| LLM gestionado | Bedrock | Microsoft Foundry | Base si el modelo elegido está disponible (verificar); autenticación por identidad, sin claves |
| Identidad de cargas de trabajo | EKS Pod Identity | Entra Workload ID | Base |
| Presupuestos y costes | Budgets, Cost Explorer | Cost Management | Base |
| Kafka gestionado | MSK | Event Hubs (interfaz Kafka) | Variante documentada (por defecto Strimzi) |
| Búsqueda gestionada | OpenSearch Service | Elastic Cloud (marketplace) | Variante documentada (por defecto ECK); OpenSearch no es 100 % compatible con Elasticsearch |

**Descartados a propósito**, para no añadir servicios sin justificación: Step Functions / Durable Functions (la saga ya está implementada y es objeto de aprendizaje), SageMaker / Azure ML (la inferencia ONNX en el clúster basta), Cognito / Entra External ID (Keycloak), ECS / Container Apps (se eligió Kubernetes), Redshift / Synapse (ClickHouse), Kinesis (Kafka), DocumentDB / Cosmos DB con API de MongoDB (compatibilidad parcial; se usa el operador).
