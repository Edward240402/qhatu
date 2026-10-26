# FE-05 · Portales por rol y reportes

### FE-05.1 · Portal de comercio sobre GraphQL
- **Ola:** 6 · **Profundidad:** B
- **Depende de:** FE-01.2, BE-15.4

**Requerimientos**
- Gestión de catálogo, existencias, pedidos y liquidaciones del comercio consumiendo la API GraphQL de `partner-service` (cliente con caché normalizada, fragmentos por componente).
- Interfaz de importación masiva (subida, progreso, informe de errores) y gestión de suscripciones de webhooks (alta, prueba, registro de entregas, reenvío).
- **(Opcional)** microfrontend con Native Federation, con ADR honesto sobre si se justifica.

**Terminado cuando**
- Un comercio importa un archivo, ve sus errores y configura un webhook desde el portal.

**Aprender y documentar**
- Caché normalizada en clientes GraphQL y su invalidación.

### FE-05.2 · Portales de soporte y administración
- **Ola:** 6 · **Profundidad:** B
- **Depende de:** FE-05.1, BE-11.3, BE-01.3

**Requerimientos**
- Soporte: búsqueda de pedidos, historia completa del pedido, estado de sagas y acciones manuales auditadas, cola de revisión de fraude.
- Administración: usuarios y roles, comercios, parámetros, *feature flags*.
- Tablas con paginación, orden y filtros del lado del servidor.

**Terminado cuando**
- Cada acción administrativa queda en la auditoría y es visible en el portal.

**Aprender y documentar**
- Control de acceso en la interfaz frente a en la API.

### FE-05.3 · Reportes y comprobantes
- **Ola:** 6 · **Profundidad:** B
- **Depende de:** FE-05.2, BE-17.2, BE-16.4

**Requerimientos**
- Solicitud asíncrona de reportes, progreso, descarga (PDF y Excel) y programación recurrente; exportación en el cliente solo para conjuntos pequeños.
- Descarga de comprobantes por cliente y comercio.

**Terminado cuando**
- Un comercio descarga el reporte de sus liquidaciones y no puede obtener datos de otro por ninguna vía.

**Aprender y documentar**
- Descarga de archivos grandes en el navegador.
