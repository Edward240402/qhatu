# 02 · Backend (`BE`)

Frente principal del portafolio. Cada servicio demuestra un conjunto **distinto** de temas, y la mayoría incorpora lógica de negocio no trivial con su análisis de complejidad (ver [00-vision-y-negocio.md](../00-vision-y-negocio.md#4-lógica-de-negocio-compleja)).

| Fase | Servicio | Runtime | Arquitectura | Olas |
|---|---|---|---|---|
| [BE-01](BE-01-plataforma-comun.md) | Plataforma común | Spring Boot y Quarkus | — | 1 |
| [BE-02](BE-02-identidad.md) | Identidad | Keycloak | — | 1 |
| [BE-03](BE-03-gateway.md) | `gateway` | Spring Cloud Gateway (WebFlux) | — | 1 |
| [BE-04](BE-04-customer-service.md) | `customer-service` | Spring MVC + virtual threads | Capas | 1 |
| [BE-05](BE-05-catalog-service.md) | `catalog-service` | Quarkus reactivo | Clean | 2 |
| [BE-06](BE-06-inventory-service.md) | `inventory-service` | Quarkus + virtual threads | Hexagonal | 2 |
| [BE-07](BE-07-pricing-service.md) | `pricing-service` | Spring Boot | Núcleo funcional, capa imperativa | 4, 5 |
| [BE-08](BE-08-search-service.md) | `search-service` | Spring Boot + Elasticsearch | CQRS (modelo de lectura) | 3, 4 |
| [BE-09](BE-09-order-service.md) | `order-service` | Spring MVC + virtual threads | Hexagonal + CQRS | 4 |
| [BE-10](BE-10-payment-service.md) | `payment-service` | Spring MVC + virtual threads | Hexagonal | 4 |
| [BE-11](BE-11-saga-de-compra.md) | Saga de compra | (en `order-service`) | Orquestación | 4 |
| [BE-12](BE-12-dispatch-service.md) | `dispatch-service` | Spring Boot + Kafka Streams | Orientada a eventos | 5 |
| [BE-13](BE-13-tracking-service.md) | `tracking-service` | Spring WebFlux | Reactiva | 5 |
| [BE-14](BE-14-notification-service.md) | `notification-service` | Quarkus Reactive Messaging | Orientada a eventos | 5 |
| [BE-15](BE-15-partner-service.md) | `partner-service` | Spring Boot + Spring Modulith + GraphQL | Monolito modular | 6 |
| [BE-16](BE-16-settlement-service.md) | `settlement-service` | Spring Boot + Spring Batch | Capas | 6 |
| [BE-17](BE-17-reporting-service.md) | `reporting-service` | Spring Boot | CQRS (lado analítico) | 6 |
| [BE-18](BE-18-assistant-service.md) | `assistant-service` | Spring Boot + Spring AI | Clean | 7 |
| [BE-19](BE-19-endurecimiento.md) | Endurecimiento y rendimiento | — | — | 10 |

## Requisitos comunes a toda sub-fase `BE`

No se repiten en cada sub-fase; siempre aplican (lista completa en `docs/estandares/dod-backend.md`):

- **Contrato primero**: OpenAPI, AsyncAPI, proto o GraphQL actualizado y revisado antes de implementar; el código se valida contra el contrato en las pruebas.
- **Arquitectura asignada** verificada con reglas ArchUnit.
- Errores RFC 9457, validación de entrada, paginación según `api.md`.
- Seguridad: servidor de recursos OAuth2, autorización por rol, *scope* y **propiedad del recurso**; mínimo privilegio; TLS en todas las conexiones.
- Configuración externalizada; secretos desde Vault; perfiles `local`, `compose`, `k8s`.
- Pruebas: unitarias de dominio, integración con Testcontainers (nunca H2 en lugar de PostgreSQL), contrato; umbrales de cobertura y mutación de `pruebas.md`.
- Telemetría: logs JSON con traza, métricas técnicas y de negocio, *spans* en operaciones de negocio; *liveness*, *readiness* y *startup* diferenciados; apagado ordenado.
- Migraciones Flyway versionadas según `migraciones.md`; nunca se edita una migración aplicada.
- Desde INF-02.2: *chart* de Helm. Siempre: Dockerfile según `contenedores.md` y su entrada en el manual de operación.
- Lógica de negocio compleja según la sección 8 de [90-gobierno-transversal.md](../90-gobierno-transversal.md#8-reglas-para-algoritmos-y-lógica-de-negocio): escenarios ejecutables, complejidad documentada, JMH y pruebas de propiedades.
