# BE-04 · `customer-service` — capas, virtual threads y datos personales

**Objetivo:** el servicio "clásico" hecho con excelencia: Spring MVC en capas sobre *virtual threads*, con datos personales protegidos y un esquema que evoluciona por versiones.

### BE-04.1 · Esqueleto en capas y perfiles
- **Ola:** 1 · **Profundidad:** B
- **Depende de:** BE-01.2, DB-01.2

**Requerimientos**
- Perfiles de cliente, comercio y repartidor; contrato OpenAPI primero.
- Capas estrictas (API → aplicación → dominio → persistencia) verificadas con ArchUnit; DTO separados de entidades JPA.
- Migración `V1` del esquema.

**Terminado cuando**
- CRUD de perfiles con autorización por propietario y pruebas de integración en verde.

**Aprender y documentar**
- Arquitectura en capas: ventajas reales, fugas típicas y cuándo deja de bastar.

### BE-04.2 · Direcciones, consentimientos y derechos del titular
- **Ola:** 1 · **Profundidad:** B
- **Depende de:** BE-04.1

**Requerimientos**
- **Comercios y sus tiendas** (ubicación, horario, radio de entrega, zona H3): `customer-service` es su dueño (decisión N1).
- Direcciones con geolocalización y validación de cobertura; consentimientos con historial (qué aceptó, cuándo, qué versión del texto).
- Derechos del titular (Ley N.° 29733): exportación de datos personales y solicitud de supresión como proceso asíncrono auditado.
- Migraciones `V2…` y el ejercicio de **renombrar una columna en tres despliegues** definido en DB-01.2.

**Terminado cuando**
- Una solicitud de exportación produce un archivo completo y el renombrado se ejecutó en tres versiones sin romper la versión anterior.

**Aprender y documentar**
- Expandir/contraer con un ejemplo real del proyecto.

### BE-04.3 · Cifrado de campos y rotación de claves
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** BE-04.2, SEC-04.1

**Requerimientos**
- Cifrado de documento, teléfono y dirección con `common-crypto`; búsqueda por documento mediante índice ciego.
- **Evolución del esquema**: columnas cifradas añadidas, migración Java de relleno por lotes y columnas en claro eliminadas en un despliegue posterior.
- Supresión mediante borrado criptográfico; enmascarado en logs y trazas; auditoría de accesos a datos personales.

**Terminado cuando**
- Un volcado de la base no revela datos personales; tras rotar la clave, los datos antiguos siguen legibles.

**Aprender y documentar**
- Cifrado en reposo frente a por campo; qué protege cada uno y de quién.

### BE-04.4 · Virtual threads a fondo
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** BE-04.3, OPS-02.2, DB-02.1

**Requerimientos**
- Comparación con prueba de carga de *platform threads* frente a *virtual threads* sobre el perfil de datos `M`, con resultados publicados.
- Detección de *pinning* con JFR; experimento de agotamiento de HikariCP con virtual threads y su corrección.
- *Scoped values* para el contexto de la petición en lugar de `ThreadLocal`.

**Terminado cuando**
- Informe con metodología, gráficos y conclusiones reproducibles con un comando.

**Aprender y documentar**
- Continuaciones, *carrier threads*, montaje y desmontaje; qué es el *pinning* y qué cambió desde JDK 24; cuándo **no** ayudan (CPU); por qué el *pool* de conexiones pasa a ser el cuello de botella.
