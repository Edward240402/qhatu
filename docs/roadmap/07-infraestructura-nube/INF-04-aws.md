# INF-04 · AWS

### INF-04.1 · Red y EKS
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-03.2

**Requerimientos**
- VPC en tres zonas, subredes públicas y privadas, salida controlada, *endpoints* privados para servicios de AWS.
- EKS con nodos gestionados (incluidos *spot* y arm64/Graviton para coste) y EKS Pod Identity.

**Terminado cuando**
- El clúster está operativo y un *pod* accede a un servicio de AWS sin claves.

**Aprender y documentar**
- Modelo de red de EKS (CNI de VPC, IP por *pod*); IAM: roles, políticas e identidad de cargas de trabajo.

### INF-04.2 · Borde: balanceo, CDN, DNS, certificados y WAF
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-04.1, FE-02.2

**Requerimientos**
- ALB gestionado desde el clúster (AWS Load Balancer Controller con Gateway API), Route 53, certificados de ACM, AWS WAF.
- Web y imágenes de producto servidas desde S3 detrás de CloudFront con control de acceso de origen.

**Terminado cuando**
- El dominio público sirve la web desde la CDN y la API desde el balanceador, por HTTPS válido.

**Aprender y documentar**
- ALB frente a NLB; cómo funciona una CDN (caché en el borde, invalidación).

### INF-04.3 · Servicios gestionados y secretos
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-04.2

**Requerimientos**
- RDS PostgreSQL (Multi-AZ documentado; tamaño mínimo para la demo), ElastiCache, S3 cifrado y sin acceso público, ECR con escaneo e inmutabilidad, Secrets Manager + KMS con External Secrets, SQS para el receptor de webhooks.
- Kafka con Strimzi en el clúster; MSK documentado como variante con su comparativa de coste. Elasticsearch con ECK; OpenSearch Service como variante.

**Terminado cuando**
- Los servicios del clúster usan los gestionados con identidad de carga de trabajo y TLS.

**Aprender y documentar**
- Cifrado de sobre con KMS; servicio gestionado frente a operador: qué se gana y qué se pierde.

### INF-04.4 · Despliegue del sistema y demostración
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-04.3, OPS-04.2

**Requerimientos**
- Despliegue de todo el sistema por GitOps (Argo CD en el clúster) con los mismos *charts* e imágenes.
- Correo por SES; LLM por Bedrock si el modelo elegido está disponible (verificar), con autenticación por identidad.
- Manual `docs/operacion/05-aws.md` con coste estimado por hora; demo grabada; `destroy` verificado sin recursos huérfanos.

**Terminado cuando**
- El sistema completo funciona en EKS creado solo con Terraform y el pipeline, la demo está grabada y la cuenta queda sin recursos facturables.

**Aprender y documentar**
- Qué cambió respecto de minikube y por qué.
