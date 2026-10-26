# INF-06 · Serverless

**Objetivo:** usar funciones donde el patrón de carga lo justifica (eventos esporádicos o en ráfagas), en ambas nubes, con el mismo núcleo y adaptadores por proveedor.

### INF-06.1 · Procesamiento de imágenes
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-04.3, INF-05.3, BE-05.2

**Requerimientos**
- Al subir una imagen de producto: evento de almacenamiento (S3 → EventBridge → Lambda; Blob → Event Grid → Functions) → miniaturas, validación y aviso a `catalog-service`.
- Núcleo compartido con el procesador local de BE-05.2 (puertos y adaptadores).
- Infraestructura con Terraform, mínimo privilegio, DLQ, idempotencia, trazas que continúan en el sistema; pruebas locales con LocalStack y Azurite.

**Terminado cuando**
- Subir una imagen produce miniaturas en ambas nubes, con la traza completa.

**Aprender y documentar**
- Modelo de ejecución y concurrencia de una función; reintentos e idempotencia en disparadores de eventos.

### INF-06.2 · Generación de comprobantes en Quarkus nativo
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-06.1, BE-16.4

**Requerimientos**
- Función que genera el PDF del comprobante bajo demanda, en **Quarkus nativo**.
- Medición de arranque en frío: nativo frente a JVM y frente a SnapStart en Lambda.

**Terminado cuando**
- El informe de arranque en frío está publicado y la función reemplaza a la generación en proceso de BE-16.4.

**Aprender y documentar**
- Arranque en frío y técnicas para reducirlo; modelo de costes de las funciones.

### INF-06.3 · Receptor de webhooks
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-06.1, BE-10.3, BE-14.2

**Requerimientos**
- Función HTTP que recibe webhooks de pasarelas y de WhatsApp, valida la firma y encola en SQS / Service Bus; un puente lleva los mensajes a Kafka. La disponibilidad para recibir webhooks deja de depender del clúster.
- ADR: cuándo función y cuándo contenedor, con el coste estimado de cada opción.

**Terminado cuando**
- Con el clúster detenido, los webhooks se aceptan y se procesan al recuperarse.

**Aprender y documentar**
- Desacoplar la ingesta de la disponibilidad del procesamiento.
