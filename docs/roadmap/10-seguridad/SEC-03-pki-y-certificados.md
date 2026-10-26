# SEC-03 · PKI y gestión de certificados

**Objetivo:** gestión de certificados de nivel empresarial: CA propia para lo interno, certificados públicos para lo externo, vida corta, rotación automática y vigilancia de expiración.

### SEC-03.1 · Diseño de la PKI y CA raíz
- **Ola:** 0 · **Profundidad:** A
- **Depende de:** FND-02.1, SEC-01.1

**Requerimientos**
- Diseño documentado de la jerarquía: **CA raíz** de larga vida, generada por script y guardada fuera del repositorio y fuera de cualquier servicio en línea; **CA intermedia** en Vault (SEC-03.2) que emite los certificados de corta vida. Política de nombres (`*.qhatu.localhost`, nombres internos de servicios), duraciones, algoritmos (ECDSA P-256 frente a RSA, ADR) y extensiones.
- Certificado del propio Vault emitido por la raíz (arranque de la cadena).
- **Confianza de la CA raíz** en los tres lugares necesarios, con script donde sea posible: almacén de Linux en WSL (curl, contenedores), *truststore* de Java (PKCS12) y almacén de Windows **[Windows]** para el navegador.
- `docs/estandares/certificados.md`: quién emite qué, duración, rotación, formatos, prohibiciones.

**Terminado cuando**
- `curl`, una aplicación Java y el navegador de Windows confían en un certificado firmado por la CA sin avisos.

**Aprender y documentar**
- Cadena de confianza X.509, extensiones (SAN, *key usage*), por qué una CA intermedia, *handshake* TLS 1.3, formatos PEM, PKCS12 y JKS.

### SEC-03.2 · TLS y mTLS en toda la infraestructura local
- **Ola:** 0 · **Profundidad:** A
- **Depende de:** SEC-02.1, FND-04.2

**Requerimientos**
- Motor PKI de Vault como CA intermedia firmada por la raíz.
- TLS en PostgreSQL (`verify-full`), Redis, MongoDB, Elasticsearch, registro de esquemas y Kafka con **mTLS** (autenticación de clientes por certificado, base de las ACL de DB-04.1).
- Emisión y renovación automatizadas (agente de Vault o script programado) con certificados de vida corta.
- Configuración de clientes reutilizable para Spring (SSL *bundles*) y Quarkus (registro TLS), con **recarga en caliente** al renovarse el certificado.

**Terminado cuando**
- Una captura de tráfico entre servicio y base de datos está cifrada; un cliente sin certificado es rechazado por Kafka; un certificado renovado se toma sin reiniciar.

**Aprender y documentar**
- mTLS paso a paso; por qué certificados de vida corta reducen la necesidad de revocación (CRL y OCSP).

### SEC-03.3 · Certificados en Kubernetes con cert-manager
- **Ola:** 3 · **Profundidad:** B
- **Depende de:** INF-02.1, SEC-03.2

**Requerimientos**
- cert-manager con emisor de Vault para certificados internos; trust-manager distribuyendo el paquete de la CA a los espacios de nombres.
- Certificado del Gateway y certificados de servicio gestionados por recursos `Certificate`, con renovación automática.
- Adopción retroactiva en todo lo desplegado.

**Terminado cuando**
- Forzar la expiración de un certificado provoca su renovación automática sin caída.

**Aprender y documentar**
- Modelo de cert-manager (`Issuer`, `Certificate`, `CertificateRequest`) y su bucle de reconciliación.

### SEC-03.4 · Certificados públicos y vigilancia de expiración
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-04.2, INF-05.2, OBS-04.1

**Requerimientos**
- Certificados públicos con ACME (Let's Encrypt, primero entorno de *staging*) con desafío DNS-01 vía cert-manager, y alternativa con ACM en AWS y certificados gestionados en Azure, con ADR.
- Inventario de todos los certificados del sistema con su emisor y fecha de expiración, alimentando métricas y **alertas de expiración**.
- Simulacro documentado: rotación de la CA intermedia sin caída.

**Terminado cuando**
- El dominio público sirve un certificado válido renovado automáticamente; la alerta de expiración se dispara en una prueba.

**Aprender y documentar**
- Protocolo ACME y tipos de desafío; Certificate Transparency.
