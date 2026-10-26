# BE-17 · `reporting-service` — consultas analíticas y reportes

### BE-17.1 · API de consultas analíticas
- **Ola:** 6 · **Profundidad:** B
- **Depende de:** DB-06.2, BE-02.3

**Requerimientos**
- Consultas agregadas sobre ClickHouse para los dashboards (ventas, demanda, reparto, búsqueda), con control de acceso por rol y por comercio aplicado en la consulta.
- Caché de resultados costosos; límites de consulta por usuario; cancelación de consultas abandonadas.

**Terminado cuando**
- Las consultas de los dashboards responden dentro del objetivo sobre el perfil `L`, y un comercio no puede obtener agregados de otro.

**Aprender y documentar**
- CQRS extendido a un almacén analítico.

### BE-17.2 · Generación asíncrona de reportes
- **Ola:** 6 · **Profundidad:** B
- **Depende de:** BE-17.1

**Requerimientos**
- Reportes PDF y Excel generados en *streaming* (memoria acotada), estado consultable, archivo en almacenamiento de objetos con URL prefirmada y caducidad.
- Programación de reportes recurrentes y envío por correo.

**Terminado cuando**
- Un reporte de un millón de filas se genera con memoria acotada, demostrado con métricas del *heap*.

**Aprender y documentar**
- Generación de documentos en *streaming*.
