# 00 · Visión, negocio y arquitectura objetivo

## 1. El negocio

**Qhatu** es un marketplace multi-comercio con reparto propio de última milla en Lima. Se eligió porque justifica de forma natural cada tecnología de la lista, sin forzarla:

| Necesidad técnica | De dónde sale en el negocio |
|---|---|
| Alta carga transaccional | Campañas tipo *Cyber Days*: miles de reservas de stock por segundo sobre los mismos productos |
| Saga | Una compra multi-comercio toca cotización, inventario, pago y despacho, cada uno con su base de datos |
| Reactividad y backpressure | Miles de repartidores enviando GPS cada pocos segundos; clientes viendo el mapa en vivo |
| Mensajería asíncrona | Notificaciones, asignación de repartidores, proyecciones de lectura, búsqueda, analítica |
| Resiliencia | Pasarelas de pago y APIs externas (WhatsApp, Maps) que fallan o se degradan |
| Cifrado y PKI | Datos personales (Ley N.° 29733), documentos, datos de pago tokenizados; TLS y mTLS en todo |
| SP, triggers, funciones, particiones | Libro mayor, liquidación a comercios, comprobantes, tablas que crecen sin límite |
| NoSQL y búsqueda | Catálogo con atributos heterogéneos, proyecciones, telemetría, búsqueda en español |
| Big data y dashboards | Ventas, demanda por zona y hora, desempeño de reparto |
| Integraciones empresariales | Comercios grandes que conectan su ERP: API GraphQL, webhooks salientes, carga masiva de archivos |
| Modelo preentrenado | Sentimiento y moderación de reseñas en español |
| Modelo predictivo propio | Pronóstico de demanda por producto, zona y franja horaria |
| IA en el producto | Asistente de compra con RAG y consulta de pedidos |
| Google Maps y WhatsApp | Direcciones, cobertura, seguimiento; avisos de estado del pedido |
| Roles | Cliente, comercio, repartidor, soporte, administrador, integrador |
| Serverless | Procesamiento de imágenes, comprobantes en PDF, recepción de webhooks |

**Flujo central:** el cliente arma un carrito con productos de uno o varios comercios → obtiene una cotización (precios, IGV, promociones, envío) → confirma → se reserva stock en las tiendas elegidas → se cobra → se asignan repartidores → seguimiento en vivo → entrega → reseña → liquidación y comprobante.

## 2. Servicios

Cada servicio tiene **una arquitectura y un estilo de comunicación asignados a propósito**. La justificación de cada uno va en un ADR (FND-03.2).

| Servicio | Runtime | Arquitectura | Comunicación | Datos | Fase |
|---|---|---|---|---|---|
| `gateway` (BFF) | Spring Cloud Gateway (WebFlux) | — | Reactivo | Redis | BE-03 |
| Identidad | Keycloak como código | — | OIDC / OAuth2 | PostgreSQL | BE-02 |
| `customer-service` | Spring MVC + virtual threads | Capas | REST | PostgreSQL cifrado por campo | BE-04 |
| `catalog-service` | Quarkus reactivo | Clean | REST reactivo + eventos | MongoDB + Redis | BE-05 |
| `inventory-service` | Quarkus + virtual threads | Hexagonal | gRPC + eventos | PostgreSQL + Redis | BE-06 |
| `pricing-service` | Spring Boot | Núcleo funcional, capa imperativa | REST + eventos | PostgreSQL + Redis | BE-07 |
| `search-service` | Spring Boot | CQRS (modelo de lectura) | REST + eventos | Elasticsearch | BE-08 |
| `order-service` | Spring MVC + virtual threads | Hexagonal + CQRS | REST + Kafka (outbox) | PostgreSQL particionado + MongoDB | BE-09, BE-11 |
| `payment-service` | Spring MVC + virtual threads | Hexagonal | REST + webhooks + Kafka | PostgreSQL + Redis | BE-10 |
| `dispatch-service` | Spring Boot + Kafka Streams | Orientada a eventos | Kafka | PostgreSQL + Redis GEO | BE-12 |
| `tracking-service` | Spring WebFlux | Reactiva | Kafka, WebSocket, SSE | Redis + MongoDB *time-series* | BE-13 |
| `notification-service` | Quarkus Reactive Messaging | Orientada a eventos | Kafka + APIs externas | MongoDB | BE-14 |
| `partner-service` | Spring Boot + Spring Modulith | Monolito modular | GraphQL + webhooks salientes + archivos | PostgreSQL | BE-15 |
| `settlement-service` | Spring Boot + Spring Batch | Capas | Batch + REST | PostgreSQL (SP, funciones, triggers) | BE-16 |
| `reporting-service` | Spring Boot | CQRS (lado analítico) | REST + trabajos asíncronos | ClickHouse + almacenamiento de objetos | BE-17 |
| `assistant-service` | Spring Boot + Spring AI | Clean | SSE + MCP | Elasticsearch (vectores) | BE-18 |
| `ml-inference` | Python, FastAPI, ONNX Runtime | — | REST + Kafka | — | ML-04 |
| Funciones | Lambda / Azure Functions (una en Quarkus nativo) | Puertos y adaptadores | Eventos de almacenamiento, HTTP, colas | S3 / Blob, SQS / Service Bus | INF-06 |

Reglas de diseño: base de datos por servicio; integración solo por API o eventos; saga **orquestada** para la compra y **coreografía** para despacho → notificación.

## 3. Tipos de integración y conexión

| Tipo | Dónde | Por qué ahí |
|---|---|---|
| REST síncrono | Casi todos los servicios hacia el gateway | Interoperabilidad y facilidad de consumo |
| gRPC | `order-service` → `inventory-service` | Baja latencia en el camino crítico de la reserva |
| GraphQL | `partner-service` (integradores y portal de comercio) | Consultas flexibles que agregan datos de varios servicios |
| Kafka (eventos) | Todo el sistema | Desacoplamiento, proyecciones, analítica |
| CDC (Debezium) | Outbox de PostgreSQL y MongoDB | Publicación confiable sin doble escritura |
| WebSocket y SSE | Seguimiento, estado de la saga, asistente | Flujos en tiempo real del servidor al cliente |
| Webhooks entrantes | Pasarelas de pago, WhatsApp | Notificaciones de terceros, con firma y conciliación |
| Webhooks salientes | Hacia los sistemas de los comercios | Integración empresarial al estilo de las grandes plataformas |
| Archivos por lotes | Importación masiva de catálogo y existencias | Integración con ERP y sistemas antiguos |
| Colas gestionadas | Receptor de webhooks serverless | Ingesta disponible aunque el clúster no lo esté |
| MCP | `assistant-service` | Exponer capacidades del producto a agentes de IA |

## 4. Lógica de negocio compleja

No hay servicios que sean solo CRUD. Cada regla se especifica con ejemplos (FND-03.4), se implementa en el núcleo de dominio con su análisis de complejidad, y se verifica con escenarios ejecutables, pruebas de propiedades y benchmark ([reglas](90-gobierno-transversal.md#8-reglas-para-algoritmos-y-lógica-de-negocio)).

| Regla o algoritmo | Problema | Enfoque y complejidad | Sub-fase |
|---|---|---|---|
| Esquemas de atributos con herencia | Validar productos según su categoría y sus ancestros | Resolución O(profundidad) con caché | BE-05.1 |
| Calificación bayesiana | Ordenar con justicia productos con pocas reseñas | Actualización incremental O(1) | BE-05.3 |
| Concurrencia de reservas | Cero sobreventa bajo miles de peticiones | Cuatro estrategias comparadas con mediciones | BE-06.3 |
| Asignación de tiendas | Atender un carrito desde el mínimo de tiendas | Conjuntos de bits O(n·m/64); cobertura de conjuntos (NP-difícil) con aproximación voraz | BE-06.4 |
| Reparto de descuentos | Distribuir un descuento entre líneas sin perder céntimos | Mayor residuo, O(n log n), suma exacta garantizada | BE-07.1 |
| Motor de promociones | Elegibilidad, combinación, topes y presupuestos | Índice por producto y categoría; *branch and bound* acotado por grupos de exclusión | BE-07.2 |
| Recargo dinámico | Precio de envío según oferta y demanda | Rejilla H3 O(1) por zona, ventanas en Kafka Streams, suavizado | BE-07.4, BE-12.4 |
| Relevancia de búsqueda | Resultados útiles en español peruano | BM25 + `function_score` + distancia; evaluación con nDCG en CI | BE-08.3 |
| Pedido multi-comercio | Un pago, varias preparaciones y entregas, fallos parciales | Agregado padre con sub-pedidos y saga con compensación parcial | BE-09.1, BE-11.2 |
| Devoluciones parciales | Reembolsar exactamente con promociones condicionadas | Recalcular con el motor de precios y el reparto | BE-09.5 |
| Riesgo y fraude | Detectar ráfagas y listas de bloqueo | Ventanas deslizantes O(log n); filtro de Bloom O(k) | BE-10.4 |
| Asignación de repartidores | Minimizar la espera total por zona | Poda *k*-cercanos O(n·k); húngaro O(n³) frente a voraz O(E log E) | BE-12.2 |
| Agrupación y rutas | Varias entregas por repartidor con precedencia | Inserción más barata + 2-opt O(s²), error medido frente al óptimo | BE-12.3 |
| Suavizado de GPS y geocercas | Ruido de posición y detección de llegada | Filtro de Kalman O(1); prefiltro H3 + punto-en-polígono | BE-13.4 |
| Webhooks salientes | Entrega confiable a terceros que fallan | *Backoff* con *jitter*, circuito por *endpoint*, orden por clave | BE-15.3 |
| Importación masiva | Millones de filas con memoria constante | *Streaming* O(n) en tiempo, O(1) en memoria, idempotente por fila | BE-15.4 |
| Libro mayor | Dinero que siempre cuadra | Doble entrada inmutable; invariante de suma cero | BE-16.1 |
| Conciliación | Emparejar pagos con el reporte de la pasarela | *Hash join* O(n + m) + emparejamiento difuso | BE-16.3 |
| Correlativos de comprobantes | Numeración legal sin huecos bajo concurrencia | Secuencia con bloqueo por serie | BE-16.4 |
| Pronóstico de demanda | Cuánto se venderá por zona y hora | Modelo profundo probabilístico frente a líneas base | ML-03 |

### 4.1 Decisiones de negocio que mantienen coherentes las reglas entre sí

Las reglas anteriores se tocan entre servicios. Estas decisiones fijan cómo encajan; FND-03.4 escribe escenarios para cada una y ninguna sub-fase puede contradecirlas sin un ADR que actualice esta tabla.

| # | Tema | Decisión |
|---|---|---|
| N1 | Propiedad de los datos maestros | `customer-service` es dueño de comercios y **tiendas** (ubicación, horario, radio de entrega); `catalog-service` del producto y su **precio de lista**; `pricing-service` de impuestos, promociones y tarifas (mantiene una réplica de precios de lista por eventos, con historial); `inventory-service` de las existencias por tienda |
| N2 | Unidades de un pedido | Pedido padre (un pago) → **sub-pedido por comercio** (lo acepta y prepara el comercio) → **envío** por tienda (lo que despacha un repartidor). Si un comercio atiende desde dos tiendas, su sub-pedido tiene dos envíos |
| N3 | Precio al consumidor | Siempre se muestra y cobra con IGV incluido; el comercio puede cargar precios con o sin IGV, y el sistema los normaliza |
| N4 | Financiador de cada promoción | Cada promoción declara quién la paga: plataforma o comercio. La comisión se calcula sobre el precio efectivamente pagado más el descuento financiado por la plataforma; en las devoluciones, el descuento se revierte a quien lo financió |
| N5 | Tarifa de envío | Una tarifa por **sub-pedido**, según la zona H3 del cliente y la del comercio, nunca según la tienda elegida (que se decide después, al reservar). Si el comercio divide en varias tiendas, el coste extra lo absorbe el comercio. "Envío gratis" cubre la tarifa base; el recargo dinámico se cobra salvo que la promoción diga lo contrario |
| N6 | Reserva y cobro | La reserva de stock es **todo o nada**: si un sub-pedido no puede reservarse, se liberan todas y no se cobra. El pago se **autoriza** por el total y se **captura** cuando todos los comercios aceptan; un rechazo tras la captura genera reembolso parcial |
| N7 | Aceptación del comercio | Cada sub-pedido requiere aceptación del comercio dentro de un plazo; si vence o la rechaza, se cancela ese sub-pedido con su compensación. El despacho se solicita cuando el comercio marca el envío como listo |
| N8 | Tiempos | La caducidad de la cotización, la de las reservas y los *timeouts* de la saga se derivan entre sí: la reserva dura más que el paso de pago, que incluye la interacción de 3-D Secure |
| N9 | Comprobantes | Qhatu emite, **por cuenta de cada comercio**, el comprobante de sus productos (serie por comercio), y emite los suyos propios por el envío al cliente y por la comisión al comercio |
| N10 | Reseñas | Solo de compras entregadas. Hasta que existe el evento de entrega (ola 5) la creación de reseñas está desactivada por *feature flag* y las reseñas provienen del generador de datos |
| N11 | Notificaciones | Las transaccionales (estado del pedido, pago, entrega) nunca se retrasan; el horario de silencio aplica solo a las no urgentes |

## 5. Trazabilidad: lo que pediste → dónde se construye

| Requisito | Sub-fases |
|---|---|
| Java 25 (virtual threads, *scoped values*, concurrencia estructurada, AOT cache) | FND-02.2, BE-04.4, BE-12.4, BE-16.2, BE-19.1 |
| Maven con perfiles | FND-02.3 |
| Spring Boot avanzado | BE-01.1, BE-04, BE-07, BE-09, BE-10, BE-15 |
| WebFlux y microservicios reactivos | BE-03, BE-13 |
| Síncronos / asíncronos | BE-04, BE-06.2, BE-10 / BE-12, BE-14 |
| Quarkus | BE-05, BE-06, BE-14, INF-06.2 |
| Resilience4j | BE-03.3, BE-10.2 |
| Capas, hexagonal, clean, eventos, CQRS (+ monolito modular) | BE-04, BE-16 / BE-06, BE-09, BE-10 / BE-05, BE-18 / BE-12, BE-14 / BE-08, BE-09.4, BE-17 / BE-15 |
| Kafka | DB-04, BE-09.3, BE-11, BE-12.4, BE-13, BE-14 |
| HTTPS, certificados | SEC-03 (todas), BE-03.1, INF-02.1 |
| Cifrado de datos | SEC-04.1, BE-04.3, FE-03.2 |
| Alta carga | BE-06.3, OPS-02.2, OPS-05.1 |
| Caché | BE-05.4, BE-07.3, FE-02.2 |
| Threads y virtual threads | BE-04.4, BE-16.2, BE-19.2 |
| Saga | BE-11 |
| Backpressure | BE-13.3, BE-08.2 |
| Redis | DB-03.1, BE-03, BE-05.4, BE-07.2, BE-10.4, BE-12 |
| Elasticsearch | BE-08, BE-18.1 |
| Webhooks y otras conexiones | BE-10.3, BE-15.3, BE-15.4, INF-06.3 (ver sección 3) |
| Balanceador, baúl de llaves, serverless, AWS y Azure, registro | INF-02.1, INF-04, INF-05 / SEC-02 / INF-06 / INF-03 a INF-05 / OPS-04.1 |
| Particiones, SP, triggers, funciones | DB-05, BE-16 |
| Volcado de datos | DB-07 |
| Flyway con versionado real | DB-01.2 (tabla de evoluciones) |
| SQL y NoSQL | DB-01, DB-03 |
| Datos de volumen | DB-02 (todas las olas) |
| Alta disponibilidad | INF-02.3, INF-07, [estándar](07-infraestructura-nube/README.md#alta-disponibilidad-por-capa) |
| Kubernetes, Docker, Terraform | INF-02, INF-01, INF-03 |
| OpenAPI, AsyncAPI | FND-03.3, OPS-03 |
| Pruebas en todos los niveles y cuándo | OPS-02, [matriz](08-calidad-y-cicd/README.md#matriz-de-pruebas-qué-se-ejecuta-y-cuándo) |
| CI/CD con GitHub Actions y Jenkins | OPS-01, OPS-04 |
| Grafana, OpenTelemetry, trazabilidad | OBS (todas) |
| OAuth2 y JWT | BE-02, BE-03.2 |
| DevSecOps, Sonar, OWASP ZAP | SEC-05, SEC-06 |
| Postman y Newman | OPS-03.2 |
| Agentes de IA en el desarrollo | FND-05.1, [92-guia-claude-code.md](92-guia-claude-code.md) |
| Angular, roles, pagos, Maps, WhatsApp, caché, reportes, dashboards, IA | FE-01 a FE-07 |
| Móvil con paridad y diseño adaptable | MOB-01 a MOB-06 |
| Modelo preentrenado y modelo predictivo propio | ML-02, ML-03, ML-04 |

## 6. Temas que añadí a tu lista

Los marcados con ★ los considero imprescindibles para un perfil senior.

| Tema | Por qué | Dónde |
|---|---|---|
| ★ Outbox + CDC e idempotencia de extremo a extremo | Sin esto la saga tiene el problema de la doble escritura | DB-04.3, BE-09.3 |
| ★ Lógica de negocio con algoritmos y su complejidad | Distingue un portafolio senior de uno de CRUD | Sección 4 |
| ★ Testcontainers, contratos, ArchUnit, mutación, propiedades | Calidad verificable, no declarada | OPS-02 |
| ★ Registro de esquemas y evolución | Gobierno de eventos | DB-04.2 |
| ★ GitOps y entrega progresiva | Estándar actual de CD en Kubernetes | OPS-04 |
| ★ Cadena de suministro: SBOM, firma, Renovate | Núcleo de DevSecOps | SEC-05 |
| ★ PKI propia, certificados de vida corta, rotación | Gestión de certificados de nivel empresarial | SEC-03 |
| ★ SLO y alertas por presupuesto de error | Observabilidad profesional | OBS-04 |
| ★ Carga, caos y alta disponibilidad ensayada | Única forma de demostrar "alta carga" y "alta disponibilidad" | OPS-05, INF-07 |
| ★ DDD estratégico, C4, ADR, especificación por ejemplos | Justifica los límites y las reglas | FND-03 |
| gRPC, GraphQL, webhooks salientes, archivos por lotes | Variedad real de integración | Sección 3 |
| Monolito modular con Spring Modulith | Saber cuándo **no** hacer un microservicio | BE-15 |
| Credenciales dinámicas de base de datos | Secretos que caducan solos | SEC-02.2 |
| Gateway API, KEDA, NetworkPolicies, operadores | Kubernetes moderno | INF-02 |
| Malla de servicios y mTLS | Confianza cero entre servicios | INF-08 |
| Imágenes nativas y AOT cache de Java 25 | Arranque y memoria, clave en serverless | BE-05.6, BE-19.1, INF-06.2 |
| Perfilado continuo y JFR | Diagnóstico de CPU, memoria e hilos | OBS-05 |
| RUM en web y móvil | Trazas que empiezan en el dispositivo | OBS-03.3, MOB-06.2 |
| RAG, Spring AI y MCP | La integración con IA más pedida en backend | BE-18 |
| MLOps | Un modelo sin ciclo de vida no es un producto | ML-05 |
| ClickHouse + Kafka Streams | Analítica en tiempo real | DB-06, BE-12.4 |
| CDN, colas y enrutamiento de eventos gestionados | Servicios de nube con uso justificado | [07-infraestructura-nube](07-infraestructura-nube/README.md#servicios-de-nube-cuáles-y-por-qué) |
| *Feature flags* (OpenFeature) | Separar despliegue de liberación | BE-01.3 |
| FinOps | Coste como requisito | INF-03.2, OPS-05.3 |

## 7. Lo que evalué y no incluí (o incluí con matices)

| Tema | Decisión | Motivo |
|---|---|---|
| Elasticsearch para logs | No; se usa Loki | Elasticsearch ya está para búsqueda; duplicar la pila de logs no enseña nada nuevo y cuesta memoria. Se documenta la comparación |
| *Event sourcing* completo | No; CQRS con outbox | Añade complejidad sin necesidad de negocio aquí; se explica cuándo sí |
| Activo-activo multi-región | No; activo-pasivo ensayado | Coste y complejidad desproporcionados para el caso |
| Motor de flujos (Temporal) para la saga | Opcional, como comparación | La saga propia es el objeto de aprendizaje |
| pgvector | No, salvo que el ADR lo cambie | Elasticsearch ya cubre la búsqueda vectorial; un almacén extra solo por variedad debilita la solidez |
| Jira, Confluence, Notion | No; GitHub Projects y documentación en el repo | Ver [90-gobierno-transversal.md](90-gobierno-transversal.md#6-gestión-del-trabajo-github-projects-sin-jira-ni-confluence) |
| Microfrontends | Opcional | Rara vez se justifican con un solo equipo; se documenta el criterio |

## 8. Decisiones abiertas que se cierran en su sub-fase

| Decisión | Recomendación inicial | Se cierra en |
|---|---|---|
| Tecnología móvil | Flutter | FND-03.2 |
| Gestor de versiones de herramientas | `mise` | FND-02.1 |
| Almacenamiento compatible con S3 en local | Verificar estado de MinIO comunitario; alternativas SeaweedFS, Garage | FND-04.1 |
| Pasarelas de pago | Dos con sandbox disponible en Perú | BE-10.1 |
| Cliente Kafka reactivo | Verificar soporte de Reactor Kafka | BE-13.1 |
| Kafka y Elasticsearch gestionados o con operador | Operador (Strimzi, ECK); gestionado como variante | INF-04.3, INF-05.3 |
| Proveedor de LLM | Claude detrás de Spring AI; endpoint gestionado en la nube si está disponible | BE-18.2 |

## 9. Versiones de referencia (octubre 2026)

Punto de partida, **no fuente de verdad**: cada sub-fase verifica y fija versiones en `docs/versiones.md`.

- Java 25 (LTS) · Spring Boot 4.1.x (Spring Framework 7) · Quarkus 3.33 LTS (3.40 LTS en candidata en septiembre de 2026) · Angular 22
- Kafka 4.x (solo KRaft) · PostgreSQL 18 · Keycloak, Redis, MongoDB, Elasticsearch, ClickHouse, Kubernetes, Terraform, Flutter: última estable verificada en la sub-fase que los introduce.
