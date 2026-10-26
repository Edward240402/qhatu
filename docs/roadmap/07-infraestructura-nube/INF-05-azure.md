# INF-05 · Azure

Mismas capas que AWS, usando la misma interfaz de módulos de Terraform.

### INF-05.1 · Red y AKS
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-03.2

**Requerimientos**
- VNet en zonas de disponibilidad, subredes, salida controlada, *endpoints* privados.
- AKS con Entra Workload ID.

**Terminado cuando**
- Un *pod* accede a un servicio de Azure sin claves.

**Aprender y documentar**
- Modelo de identidad de Azure (Entra ID, identidades administradas) frente a IAM de AWS; redes de AKS.

### INF-05.2 · Borde
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-05.1, FE-02.2

**Requerimientos**
- Application Gateway for Containers con Gateway API, Azure DNS, certificados gestionados, WAF.
- Web e imágenes desde Storage detrás de Front Door.

**Terminado cuando**
- El dominio público sirve web y API por HTTPS válido.

**Aprender y documentar**
- Diferencias de modelo entre el borde de AWS y el de Azure.

### INF-05.3 · Servicios gestionados y secretos
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-05.2

**Requerimientos**
- PostgreSQL Flexible Server, Redis gestionado (verificar la oferta vigente), Blob Storage, ACR, Key Vault con External Secrets, Service Bus.
- Kafka con Strimzi; Event Hubs con interfaz Kafka documentado como variante, incluyendo sus diferencias de compatibilidad.

**Terminado cuando**
- Los servicios usan los gestionados con identidad de carga de trabajo y TLS.

**Aprender y documentar**
- Key Vault frente a Secrets Manager.

### INF-05.4 · Despliegue del sistema y comparativa
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-05.3, INF-04.4

**Requerimientos**
- Sistema completo por GitOps con **los mismos *charts* e imágenes**, cambiando solo valores; correo con Communication Services; LLM vía Microsoft Foundry si está disponible.
- **Tabla de equivalencias AWS ↔ Azure** con lo que la abstracción no pudo ocultar.
- Manual `docs/operacion/06-azure.md`; demo grabada; `destroy` verificado.

**Terminado cuando**
- El sistema funciona en AKS sin cambios en imágenes ni *charts*.

**Aprender y documentar**
- Qué es portable entre nubes y qué no, con ejemplos del proyecto.
