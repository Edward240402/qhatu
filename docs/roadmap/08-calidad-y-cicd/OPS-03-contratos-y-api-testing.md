# OPS-03 · Gobierno de contratos, Postman y Newman

### OPS-03.1 · Gobierno de OpenAPI
- **Ola:** 1 · **Profundidad:** B
- **Depende de:** BE-04.1

**Requerimientos**
- Spectral según `api.md`; detección de cambios incompatibles en el PR (oasdiff); validación de la implementación contra el contrato en las pruebas.
- Documentación navegable publicada en el sitio; generación de clientes para web, móvil y servicios.
- Simulación de APIs desde el contrato para desbloquear al front.

**Terminado cuando**
- Un cambio incompatible es señalado en el PR y bloquea la fusión salvo cambio de versión mayor.

**Aprender y documentar**
- Qué hace incompatible un cambio de API; estrategias de versionado.

### OPS-03.2 · Postman y Newman
- **Ola:** 1 · **Profundidad:** B
- **Depende de:** BE-04.2, BE-03.2, INF-01.2

**Requerimientos**
- Colecciones versionadas en `tests/postman/` por servicio y por flujo de negocio; entornos `local`, `compose`, `minikube`, `aws`, `azure`; autenticación OAuth2 automatizada; aserciones de esquema y de negocio.
- Newman en CI tras cada fusión y como **prueba de humo tras cada despliegue**; reporte publicado.
- Cada servicio nuevo añade su colección (forma parte de la lista de terminado del backend).

**Terminado cuando**
- Newman corre en el pipeline y su fallo bloquea la promoción.

**Aprender y documentar**
- Pruebas de API con Postman frente a pruebas de contrato: qué cubre cada una.

### OPS-03.3 · Gobierno de AsyncAPI, Protobuf y GraphQL
- **Ola:** 2 · **Profundidad:** B
- **Depende de:** DB-04.2

**Requerimientos**
- AsyncAPI del bus completo con referencias a los esquemas del registro; validación y publicación como documentación.
- Compatibilidad de esquemas contra el registro en el PR.
- Buf (lint y cambios incompatibles) para Protobuf; inspector de esquemas para GraphQL (cambios incompatibles y uso de campos obsoletos).

**Terminado cuando**
- Un cambio incompatible en un evento, un proto o el esquema GraphQL bloquea el PR.

**Aprender y documentar**
- AsyncAPI frente a OpenAPI; evolución de esquemas GraphQL sin versiones.
