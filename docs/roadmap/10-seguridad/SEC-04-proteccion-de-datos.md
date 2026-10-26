# SEC-04 · Protección de datos y criptografía

### SEC-04.1 · Estándar criptográfico y librería `common-crypto`
- **Ola:** 1 · **Profundidad:** A
- **Depende de:** SEC-02.1, BE-01.1

**Requerimientos**
- `docs/estandares/criptografia.md`: algoritmos permitidos, prohibidos, longitudes, uso de *nonces*, gestión de claves.
- `libs/common-crypto` (Spring y Quarkus):
  - **cifrado de sobre** con Vault Transit (clave de datos local, envuelta por la clave maestra de Vault), AES-GCM con *nonce* único, datos asociados que ligan el texto cifrado a su registro;
  - **índice ciego** (HMAC con clave dedicada) para buscar por igualdad sobre campos cifrados;
  - **rotación de claves** y re-envoltura en segundo plano sin tiempo de inactividad;
  - **borrado criptográfico** (destruir la clave de un titular hace ilegibles sus datos, incluidos respaldos): base del derecho de supresión;
  - enmascarado para logs y trazas.
- Regla ArchUnit: ninguna clase fuera de `common-crypto` usa primitivas criptográficas directamente.
- Pruebas con vectores conocidos y pruebas de manipulación (un bit alterado debe fallar la autenticación).

**Terminado cuando**
- Las pruebas de manipulación fallan como se espera y la rotación se ejecuta sobre datos existentes sin pérdida.

**Aprender y documentar**
- AES-GCM por dentro (contador, etiqueta de autenticación, por qué nunca repetir un *nonce*); cifrado de sobre; índices ciegos y qué información filtran; borrado criptográfico.
