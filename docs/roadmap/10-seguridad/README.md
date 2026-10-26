# 10 · Seguridad (`SEC`)

Frente nuevo que reúne lo que antes estaba disperso: modelo de amenazas, gestión de secretos, **PKI y certificados**, criptografía de datos, cadena de suministro y seguridad en ejecución. La seguridad de identidad (OAuth2, OIDC, JWT) vive en `BE-02` por estar acoplada al backend, pero sigue estos estándares.

Varias fases tienen sub-fases en olas distintas: empiezan en local en la ola 0 y evolucionan hasta la nube. Desde la ola 0, **ningún componente nuevo se integra sin TLS**.

| Fase | Título | Olas |
|---|---|---|
| [SEC-01](SEC-01-modelo-de-amenazas.md) | Modelo de amenazas y estándares | 0 |
| [SEC-02](SEC-02-secretos.md) | Gestión de secretos con Vault | 0, 3, 8 |
| [SEC-03](SEC-03-pki-y-certificados.md) | PKI y gestión de certificados | 0, 3, 8 |
| [SEC-04](SEC-04-proteccion-de-datos.md) | Protección de datos y criptografía | 1 |
| [SEC-05](SEC-05-cadena-de-suministro.md) | Análisis estático y cadena de suministro | 1, 3 |
| [SEC-06](SEC-06-seguridad-en-ejecucion.md) | DAST, políticas y seguridad en ejecución | 3, 8, 10 |

## Requisitos comunes

- Toda comunicación de red usa TLS con verificación completa del certificado; nunca `insecure-skip-verify` ni *truststores* que acepten todo.
- Ningún secreto en el repositorio, en imágenes, en variables de entorno de manifiestos versionados ni en logs.
- Mínimo privilegio en todo: usuarios de base de datos, ACL de Kafka, políticas de Vault, roles de nube, cuentas de servicio de Kubernetes.
- Cada control de seguridad tiene una prueba automatizada que falla si el control desaparece.
