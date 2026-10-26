# SEC-02 · Gestión de secretos con Vault

**Objetivo:** un baúl de llaves real desde el día uno, que evoluciona a Kubernetes y a los servicios gestionados de cada nube.

### SEC-02.1 · Vault en modo servidor en local
- **Ola:** 0 · **Profundidad:** A
- **Depende de:** SEC-03.1, FND-04.1

**Requerimientos**
- Vault en **modo servidor** con almacenamiento integrado (Raft) y TLS con el certificado emitido en SEC-03.1; no el modo `dev`, que no se parece a producción. Inicialización y *unseal* documentados; claves de *unseal* fuera del repositorio.
- Motores: KV v2 (secretos estáticos), Transit (cifrado como servicio para SEC-04.1), PKI (para SEC-03.2).
- Métodos de autenticación: AppRole para servicios en Compose; usuario/contraseña con MFA para la persona administradora.
- Políticas de mínimo privilegio por servicio, dispositivo de auditoría activado.
- Script idempotente que deja Vault configurado como código (o Terraform con el proveedor de Vault, ADR).
- `docs/estandares/secretos.md`: qué es un secreto, dónde vive cada tipo, rotación, prohibiciones.

**Terminado cuando**
- Reiniciar el contenedor exige *unseal* y los datos persisten; un AppRole no puede leer secretos de otro servicio.

**Aprender y documentar**
- Arquitectura de Vault: *seal/unseal*, Shamir, *barrier*, *leases*, *tokens* y políticas; por qué el modo `dev` es engañoso.

### SEC-02.2 · Vault en Kubernetes y credenciales dinámicas
- **Ola:** 3 · **Profundidad:** A
- **Depende de:** INF-02.1, SEC-02.1, DB-01.1

**Requerimientos**
- Vault en el clúster en alta disponibilidad (3 réplicas Raft), autenticación de Kubernetes por cuenta de servicio.
- **External Secrets Operator** sincronizando secretos a los *pods*; nunca secretos en claro en Git.
- **Credenciales dinámicas de base de datos** (motor de bases de datos de Vault): cada réplica de un servicio obtiene un usuario de PostgreSQL temporal, renovado y revocado automáticamente; integración con el *pool* de conexiones.
- Adopción retroactiva en los servicios ya desplegados.

**Terminado cuando**
- Un servicio funciona con credenciales que caducan y se renuevan sin reinicio; revocar el *lease* corta su acceso.

**Aprender y documentar**
- Secretos estáticos frente a dinámicos; *leases* y revocación; patrones de entrega de secretos a *pods* (ESO, agente de Vault, CSI) y sus compromisos.

### SEC-02.3 · Secretos en la nube y rotación
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-04.3, INF-05.3

**Requerimientos**
- External Secrets contra AWS Secrets Manager y Azure Key Vault con identidad de carga de trabajo (sin claves estáticas).
- Rotación automática de la credencial de base de datos gestionada en ambas nubes, con los servicios tomando la nueva sin caída.
- Auditoría de acceso a secretos visible en la observabilidad.
- ADR: Vault en la nube frente al servicio gestionado de cada proveedor.

**Terminado cuando**
- Una rotación forzada en cada nube no produce errores en los servicios.

**Aprender y documentar**
- Modelos de identidad de cargas de trabajo en AWS y Azure; diferencias entre Secrets Manager y Key Vault.
