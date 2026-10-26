# Estado de las sub-fases

Fuente de verdad del avance. La actualiza `/fase` en cada paso. Las filas se generan con
`python3 scripts/roadmap/roadmap.py estado`, que conserva los estados ya registrados.

Estados: `PENDIENTE` → `EN ANÁLISIS` → `PLANIFICADA` → `EN IMPLEMENTACIÓN` → `CERRADA` (o `BLOQUEADA`, con motivo en Notas).

| # | Ola | Sub-fase | Título | Estado | Cerrada el | Notas |
|---|---|---|---|---|---|---|
| 1 | 0 | FND-01.1 | Estructura del monorepo y convenciones | PENDIENTE | | |
| 2 | 0 | OPS-01.1 | Esqueleto de CI y seguridad del pipeline | PENDIENTE | | |
| 3 | 0 | FND-01.2 | Gobierno del repositorio, versionado y seguimiento del trabajo | PENDIENTE | | |
| 4 | 0 | FND-05.1 | Skill, subagentes, permisos, hooks y MCP | PENDIENTE | | |
| 5 | 0 | FND-02.1 | Entorno WSL2 y herramientas versionadas | PENDIENTE | | |
| 6 | 0 | FND-02.2 | Build multi-módulo de Maven | PENDIENTE | | |
| 7 | 0 | FND-02.3 | Perfiles de Maven y calidad en compilación | PENDIENTE | | |
| 8 | 0 | FND-03.1 | Event storming y mapa de contextos | PENDIENTE | | |
| 9 | 0 | FND-03.2 | Arquitectura objetivo y requisitos no funcionales | PENDIENTE | | |
| 10 | 0 | FND-03.3 | Guías de estilo y contratos esqueleto | PENDIENTE | | |
| 11 | 0 | FND-03.4 | Reglas de negocio especificadas por ejemplos | PENDIENTE | | |
| 12 | 0 | SEC-01.1 | Modelo de amenazas, clasificación de datos y estándar de seguridad | PENDIENTE | | |
| 13 | 0 | FND-04.1 | Almacenes de datos | PENDIENTE | | |
| 14 | 0 | FND-04.2 | Mensajería y búsqueda | PENDIENTE | | |
| 15 | 0 | SEC-03.1 | Diseño de la PKI y CA raíz | PENDIENTE | | |
| 16 | 0 | SEC-02.1 | Vault en modo servidor en local | PENDIENTE | | |
| 17 | 0 | SEC-03.2 | TLS y mTLS en toda la infraestructura local | PENDIENTE | | |
| 18 | 0 | FND-06.1 | Estructura, plantillas y listas de terminado | PENDIENTE | | |
| 19 | 0 | FND-06.2 | Sitio publicado y verificación automática | PENDIENTE | | |
| 20 | 1 | DB-01.1 | Convenciones de PostgreSQL y mínimo privilegio | PENDIENTE | | |
| 21 | 1 | DB-01.2 | Estrategia de migraciones con Flyway | PENDIENTE | | |
| 22 | 1 | OPS-01.2 | Pipeline de Java | PENDIENTE | | |
| 23 | 1 | BE-01.1 | Librerías técnicas compartidas | PENDIENTE | | |
| 24 | 1 | OBS-01.1 | Pila de observabilidad como código | PENDIENTE | | |
| 25 | 1 | OBS-01.2 | Estándar de instrumentación | PENDIENTE | | |
| 26 | 1 | DB-03.1 | Redis | PENDIENTE | | |
| 27 | 1 | BE-02.1 | Keycloak como código | PENDIENTE | | |
| 28 | 1 | BE-02.2 | Flujos, tokens y políticas | PENDIENTE | | |
| 29 | 1 | BE-02.3 | Librerías de autorización | PENDIENTE | | |
| 30 | 1 | OPS-02.1 | Estrategia, matriz y base de pruebas | PENDIENTE | | |
| 31 | 1 | BE-01.2 | Plantillas de servicio | PENDIENTE | | |
| 32 | 1 | BE-01.3 | *Feature flags* | PENDIENTE | | |
| 33 | 1 | SEC-05.1 | SAST, SonarQube, dependencias y secretos | PENDIENTE | | |
| 34 | 1 | SEC-04.1 | Estándar criptográfico y librería `common-crypto` | PENDIENTE | | |
| 35 | 1 | BE-03.1 | Enrutamiento y borde HTTPS | PENDIENTE | | |
| 36 | 1 | BE-03.2 | Patrón BFF y sesiones | PENDIENTE | | |
| 37 | 1 | BE-03.3 | Límites de tasa y resiliencia en el borde | PENDIENTE | | |
| 38 | 1 | BE-04.1 | Esqueleto en capas y perfiles | PENDIENTE | | |
| 39 | 1 | OPS-03.1 | Gobierno de OpenAPI | PENDIENTE | | |
| 40 | 1 | INF-01.1 | Imágenes endurecidas | PENDIENTE | | |
| 41 | 1 | INF-01.2 | Sistema completo en Compose | PENDIENTE | | |
| 42 | 1 | BE-04.2 | Direcciones, consentimientos y derechos del titular | PENDIENTE | | |
| 43 | 1 | OPS-03.2 | Postman y Newman | PENDIENTE | | |
| 44 | 1 | OPS-02.2 | Base de pruebas de carga | PENDIENTE | | |
| 45 | 1 | BE-04.3 | Cifrado de campos y rotación de claves | PENDIENTE | | |
| 46 | 1 | DB-02.1 | Núcleo del generador y datos maestros | PENDIENTE | | |
| 47 | 1 | BE-04.4 | Virtual threads a fondo | PENDIENTE | | |
| 48 | 1 | FE-01.1 | *Workspace* y sistema de diseño | PENDIENTE | | |
| 49 | 1 | FE-01.2 | Autenticación por BFF, roles y seguridad del navegador | PENDIENTE | | |
| 50 | 2 | DB-04.1 | Kafka como plataforma | PENDIENTE | | |
| 51 | 2 | DB-04.2 | Registro de esquemas y evolución | PENDIENTE | | |
| 52 | 2 | OPS-03.3 | Gobierno de AsyncAPI, Protobuf y GraphQL | PENDIENTE | | |
| 53 | 2 | DB-04.3 | Kafka Connect y Debezium | PENDIENTE | | |
| 54 | 2 | DB-03.2 | MongoDB | PENDIENTE | | |
| 55 | 2 | BE-05.1 | Dominio con atributos dinámicos | PENDIENTE | | |
| 56 | 2 | BE-05.2 | Imágenes de producto | PENDIENTE | | |
| 57 | 2 | BE-05.3 | Reseñas y calificación | PENDIENTE | | |
| 58 | 2 | BE-05.4 | Caché | PENDIENTE | | |
| 59 | 2 | BE-05.5 | Eventos confiables | PENDIENTE | | |
| 60 | 2 | BE-06.1 | Dominio hexagonal de existencias | PENDIENTE | | |
| 61 | 2 | BE-06.2 | API gRPC | PENDIENTE | | |
| 62 | 2 | DB-02.2 | Catálogo, tiendas y existencias | PENDIENTE | | |
| 63 | 2 | BE-06.3 | Estrategias de concurrencia comparadas | PENDIENTE | | |
| 64 | 2 | OPS-02.4 | Mutación y propiedades | PENDIENTE | | |
| 65 | 2 | BE-06.4 | Asignación de tiendas a un pedido | PENDIENTE | | |
| 66 | 2 | BE-06.5 | Eventos, expiración y tolerancia a fallos | PENDIENTE | | |
| 67 | 2 | OBS-02.1 | JVM, RED/USE y dashboards generados | PENDIENTE | | |
| 68 | 2 | OBS-02.2 | Dependencias y métricas de negocio | PENDIENTE | | |
| 69 | 2 | OBS-05.1 | Perfilado continuo y JFR | PENDIENTE | | |
| 70 | 2 | BE-05.6 | Imagen nativa | PENDIENTE | | |
| 71 | 3 | BE-08.1 | Modelado de índices y análisis de texto | PENDIENTE | | |
| 72 | 3 | BE-08.2 | Proyección desde eventos | PENDIENTE | | |
| 73 | 3 | OPS-02.3 | Pruebas de contrato dirigidas por el consumidor | PENDIENTE | | |
| 74 | 3 | BE-08.3 | Consultas y relevancia | PENDIENTE | | |
| 75 | 3 | BE-08.4 | Operación de Elasticsearch | PENDIENTE | | |
| 76 | 3 | FE-02.1 | Búsqueda y catálogo | PENDIENTE | | |
| 77 | 3 | FE-02.2 | Caché en capas, PWA y SSR | PENDIENTE | | |
| 78 | 3 | SEC-06.1 | OWASP ZAP en el pipeline de PR | PENDIENTE | | |
| 79 | 3 | INF-02.1 | Clúster local multi-nodo y entrada | PENDIENTE | | |
| 80 | 3 | SEC-03.3 | Certificados en Kubernetes con cert-manager | PENDIENTE | | |
| 81 | 3 | SEC-02.2 | Vault en Kubernetes y credenciales dinámicas | PENDIENTE | | |
| 82 | 3 | INF-02.2 | *Charts* de Helm y estándar de Kubernetes | PENDIENTE | | |
| 83 | 3 | INF-02.3 | Componentes con estado mediante operadores | PENDIENTE | | |
| 84 | 3 | INF-02.4 | Autoescalado y políticas de red | PENDIENTE | | |
| 85 | 3 | OPS-04.1 | Publicación de artefactos y versionado por componente | PENDIENTE | | |
| 86 | 3 | SEC-05.2 | SBOM, firma de imágenes y procedencia | PENDIENTE | | |
| 87 | 3 | OPS-04.2 | GitOps local con Argo CD | PENDIENTE | | |
| 88 | 4 | DB-05.1 | Diagnóstico y rendimiento de consultas | PENDIENTE | | |
| 89 | 4 | DB-05.2 | Funciones, procedimientos y triggers con pruebas | PENDIENTE | | |
| 90 | 4 | DB-05.3 | Particionado y seguridad a nivel de fila | PENDIENTE | | |
| 91 | 4 | BE-07.1 | Dinero, impuestos y listas de precios | PENDIENTE | | |
| 92 | 4 | BE-07.2 | Motor de promociones | PENDIENTE | | |
| 93 | 4 | BE-07.3 | Cotización congelada y eventos | PENDIENTE | | |
| 94 | 4 | BE-08.5 | Precios y promociones en la búsqueda | PENDIENTE | | |
| 95 | 4 | BE-09.1 | Dominio del pedido | PENDIENTE | | |
| 96 | 4 | BE-09.2 | Persistencia, carrito y concurrencia | PENDIENTE | | |
| 97 | 4 | BE-09.3 | Outbox y consumidores idempotentes | PENDIENTE | | |
| 98 | 4 | BE-09.4 | Modelo de lectura (CQRS) | PENDIENTE | | |
| 99 | 4 | BE-10.1 | Dominio de pagos y primera pasarela | PENDIENTE | | |
| 100 | 4 | BE-10.2 | Segunda pasarela y resiliencia completa | PENDIENTE | | |
| 101 | 4 | BE-10.3 | Webhooks entrantes y conciliación | PENDIENTE | | |
| 102 | 4 | BE-10.4 | Módulo de riesgo y fraude | PENDIENTE | | |
| 103 | 4 | BE-11.1 | Orquestador y camino feliz | PENDIENTE | | |
| 104 | 4 | OBS-03.1 | Propagación por límites asíncronos y muestreo | PENDIENTE | | |
| 105 | 4 | BE-11.2 | Compensaciones y recuperación | PENDIENTE | | |
| 106 | 4 | OBS-03.2 | Trazabilidad de negocio y auditoría | PENDIENTE | | |
| 107 | 4 | BE-11.3 | Operación de sagas y coreografía | PENDIENTE | | |
| 108 | 4 | BE-09.5 | Cancelaciones y devoluciones parciales | PENDIENTE | | |
| 109 | 4 | DB-02.3 | Historial transaccional | PENDIENTE | | |
| 110 | 4 | OPS-02.5 | Pruebas de extremo a extremo del sistema | PENDIENTE | | |
| 111 | 4 | FE-02.3 | Carrito | PENDIENTE | | |
| 112 | 4 | FE-03.1 | *Checkout* con cotización | PENDIENTE | | |
| 113 | 4 | FE-03.2 | Pasarela de pagos | PENDIENTE | | |
| 114 | 4 | FE-03.3 | Estado de la saga e idempotencia | PENDIENTE | | |
| 115 | 5 | BE-12.1 | Esqueleto orientado a eventos | PENDIENTE | | |
| 116 | 5 | BE-13.1 | Ingesta reactiva de posiciones | PENDIENTE | | |
| 117 | 5 | BE-13.2 | Almacenamiento de posiciones | PENDIENTE | | |
| 118 | 5 | DB-02.4 | Simulador de tráfico en vivo | PENDIENTE | | |
| 119 | 5 | BE-12.2 | Algoritmo de asignación por lotes | PENDIENTE | | |
| 120 | 5 | BE-12.3 | Agrupación de pedidos y rutas | PENDIENTE | | |
| 121 | 5 | BE-12.4 | Agregaciones en tiempo real con Kafka Streams | PENDIENTE | | |
| 122 | 5 | BE-07.4 | Tarifa de envío y recargo dinámico | PENDIENTE | | |
| 123 | 5 | BE-13.3 | Difusión a clientes y backpressure | PENDIENTE | | |
| 124 | 5 | BE-13.4 | Suavizado, geocercas y tiempo estimado | PENDIENTE | | |
| 125 | 5 | BE-14.1 | Consumo, plantillas y preferencias | PENDIENTE | | |
| 126 | 5 | BE-14.2 | WhatsApp Cloud API | PENDIENTE | | |
| 127 | 5 | BE-14.3 | Correo, *push* y conmutación de canal | PENDIENTE | | |
| 128 | 5 | FE-04.1 | Direcciones y cobertura con Google Maps | PENDIENTE | | |
| 129 | 5 | FE-04.2 | Seguimiento en vivo | PENDIENTE | | |
| 130 | 5 | OBS-03.3 | Monitorización de usuarios reales | PENDIENTE | | |
| 131 | 5 | FE-04.3 | WhatsApp y centro de notificaciones | PENDIENTE | | |
| 132 | 5 | OBS-04.1 | SLI y SLO como código | PENDIENTE | | |
| 133 | 5 | OBS-04.2 | Guías de respuesta e incidentes | PENDIENTE | | |
| 134 | 6 | DB-06.1 | ClickHouse e ingesta desde Kafka | PENDIENTE | | |
| 135 | 6 | DB-06.2 | Modelo dimensional, calidad y linaje | PENDIENTE | | |
| 136 | 6 | DB-02.5 | Volumen analítico y reproducción de eventos | PENDIENTE | | |
| 137 | 6 | DB-07.1 | Volcados lógicos y restauración | PENDIENTE | | |
| 138 | 6 | DB-07.2 | Recuperación a un punto en el tiempo y simulacro | PENDIENTE | | |
| 139 | 6 | DB-07.3 | Volcados anonimizados para entornos inferiores | PENDIENTE | | |
| 140 | 6 | BE-15.1 | Monolito modular y autenticación de integradores | PENDIENTE | | |
| 141 | 6 | BE-15.2 | API GraphQL | PENDIENTE | | |
| 142 | 6 | BE-15.3 | Webhooks salientes | PENDIENTE | | |
| 143 | 6 | BE-15.4 | Importación masiva de archivos | PENDIENTE | | |
| 144 | 6 | BE-16.1 | Libro mayor de doble entrada | PENDIENTE | | |
| 145 | 6 | BE-16.2 | Proceso de liquidación con Spring Batch | PENDIENTE | | |
| 146 | 6 | BE-16.3 | Comisiones, retenciones y conciliación | PENDIENTE | | |
| 147 | 6 | BE-16.4 | Comprobantes electrónicos | PENDIENTE | | |
| 148 | 6 | BE-17.1 | API de consultas analíticas | PENDIENTE | | |
| 149 | 6 | BE-17.2 | Generación asíncrona de reportes | PENDIENTE | | |
| 150 | 6 | FE-05.1 | Portal de comercio sobre GraphQL | PENDIENTE | | |
| 151 | 6 | FE-05.2 | Portales de soporte y administración | PENDIENTE | | |
| 152 | 6 | FE-05.3 | Reportes y comprobantes | PENDIENTE | | |
| 153 | 6 | FE-06.1 | Dashboards analíticos | PENDIENTE | | |
| 154 | 6 | FE-06.2 | Panel en tiempo real | PENDIENTE | | |
| 155 | 7 | DB-02.6 | Reseñas y conjunto etiquetado | PENDIENTE | | |
| 156 | 7 | ML-01.1 | Entorno y extracción de datos | PENDIENTE | | |
| 157 | 7 | ML-01.2 | Análisis exploratorio y líneas base | PENDIENTE | | |
| 158 | 7 | ML-02.1 | Selección y evaluación propia | PENDIENTE | | |
| 159 | 7 | ML-02.2 | Optimización para servir | PENDIENTE | | |
| 160 | 7 | ML-03.1 | Ingeniería de características | PENDIENTE | | |
| 161 | 7 | ML-03.2 | Modelo profundo | PENDIENTE | | |
| 162 | 7 | ML-03.3 | Pronóstico probabilístico y comparación | PENDIENTE | | |
| 163 | 7 | ML-04.1 | Servicio `ml-inference` | PENDIENTE | | |
| 164 | 7 | ML-04.2 | Integración asíncrona de reseñas | PENDIENTE | | |
| 165 | 7 | ML-04.3 | Integración por lotes del pronóstico | PENDIENTE | | |
| 166 | 7 | BE-18.1 | Recuperación aumentada (RAG) | PENDIENTE | | |
| 167 | 7 | BE-18.2 | Conversación y llamada a herramientas | PENDIENTE | | |
| 168 | 7 | BE-18.3 | Servidor MCP, defensas y evaluación | PENDIENTE | | |
| 169 | 7 | FE-07.1 | Asistente de compra | PENDIENTE | | |
| 170 | 7 | FE-07.2 | Búsqueda semántica, reseñas y pronóstico | PENDIENTE | | |
| 171 | 7 | ML-05.1 | Reentrenamiento automatizado | PENDIENTE | | |
| 172 | 7 | ML-05.2 | Monitoreo y despliegue seguro de modelos | PENDIENTE | | |
| 173 | 8 | INF-07.1 | Validación en local | PENDIENTE | | |
| 174 | 8 | INF-03.1 | Estructura, estado y federación | PENDIENTE | | |
| 175 | 8 | INF-03.2 | Calidad, coste y deriva | PENDIENTE | | |
| 176 | 8 | INF-04.1 | Red y EKS | PENDIENTE | | |
| 177 | 8 | INF-04.2 | Borde: balanceo, CDN, DNS, certificados y WAF | PENDIENTE | | |
| 178 | 8 | INF-04.3 | Servicios gestionados y secretos | PENDIENTE | | |
| 179 | 8 | INF-04.4 | Despliegue del sistema y demostración | PENDIENTE | | |
| 180 | 8 | OBS-06.1 | Pila en el clúster | PENDIENTE | | |
| 181 | 8 | OPS-04.3 | Promoción entre entornos en la nube | PENDIENTE | | |
| 182 | 8 | INF-05.1 | Red y AKS | PENDIENTE | | |
| 183 | 8 | INF-05.2 | Borde | PENDIENTE | | |
| 184 | 8 | INF-05.3 | Servicios gestionados y secretos | PENDIENTE | | |
| 185 | 8 | INF-05.4 | Despliegue del sistema y comparativa | PENDIENTE | | |
| 186 | 8 | OBS-06.2 | Multi-entorno y servicios gestionados | PENDIENTE | | |
| 187 | 8 | SEC-02.3 | Secretos en la nube y rotación | PENDIENTE | | |
| 188 | 8 | SEC-03.4 | Certificados públicos y vigilancia de expiración | PENDIENTE | | |
| 189 | 8 | INF-07.2 | Multi-zona en la nube | PENDIENTE | | |
| 190 | 8 | INF-07.3 | Recuperación ante desastres regional | PENDIENTE | | |
| 191 | 8 | INF-06.1 | Procesamiento de imágenes | PENDIENTE | | |
| 192 | 8 | INF-06.2 | Generación de comprobantes en Quarkus nativo | PENDIENTE | | |
| 193 | 8 | INF-06.3 | Receptor de webhooks | PENDIENTE | | |
| 194 | 8 | OPS-04.4 | Entrega progresiva | PENDIENTE | | |
| 195 | 8 | OPS-04.5 | Pipeline equivalente en Jenkins | PENDIENTE | | |
| 196 | 8 | OPS-04.6 | Métricas DORA | PENDIENTE | | |
| 197 | 8 | INF-08.1 | Malla con mTLS y autorización entre servicios | PENDIENTE | | |
| 198 | 8 | SEC-06.2 | Políticas de admisión y detección en ejecución | PENDIENTE | | |
| 199 | 9 | MOB-01.1 | Proyecto, arquitectura y entorno | PENDIENTE | | |
| 200 | 9 | MOB-01.2 | Diseño adaptable y adaptativo | PENDIENTE | | |
| 201 | 9 | MOB-02.1 | OIDC y almacenamiento seguro | PENDIENTE | | |
| 202 | 9 | MOB-02.2 | Endurecimiento según OWASP MASVS | PENDIENTE | | |
| 203 | 9 | MOB-03.1 | Catálogo y carrito sin conexión | PENDIENTE | | |
| 204 | 9 | MOB-03.2 | *Checkout* y pagos | PENDIENTE | | |
| 205 | 9 | MOB-04.1 | Seguimiento, *push* y WhatsApp | PENDIENTE | | |
| 206 | 9 | MOB-04.2 | Modo repartidor | PENDIENTE | | |
| 207 | 9 | MOB-05.1 | Asistente de compra | PENDIENTE | | |
| 208 | 9 | MOB-05.2 | Reportes y dashboards en tableta | PENDIENTE | | |
| 209 | 9 | MOB-06.1 | Pruebas en dispositivos | PENDIENTE | | |
| 210 | 9 | MOB-06.2 | Distribución y telemetría | PENDIENTE | | |
| 211 | 10 | OPS-05.1 | Campaña de rendimiento | PENDIENTE | | |
| 212 | 10 | OPS-05.2 | Ingeniería del caos | PENDIENTE | | |
| 213 | 10 | OPS-05.3 | Capacidad y coste | PENDIENTE | | |
| 214 | 10 | BE-19.1 | Perfilado y ajuste | PENDIENTE | | |
| 215 | 10 | BE-19.2 | Comparativa de modelos de ejecución | PENDIENTE | | |
| 216 | 10 | BE-19.3 | Revisión de decisiones | PENDIENTE | | |
| 217 | 10 | OBS-05.2 | Casos prácticos de diagnóstico | PENDIENTE | | |
| 218 | 10 | SEC-06.3 | Escaneo autenticado completo y verificación ASVS | PENDIENTE | | |
| 219 | 10 | FE-08.1 | Auditoría y actualización | PENDIENTE | | |
| 220 | 10 | OPS-06.1 | Versión 1.0 y página de portafolio | PENDIENTE | | |
