# FE-03 · *Checkout*, pagos y datos sensibles

### FE-03.1 · *Checkout* con cotización
- **Ola:** 4 · **Profundidad:** B
- **Depende de:** FE-02.3, BE-07.3

**Requerimientos**
- Flujo por pasos con formularios tipados y validación; dirección, franja de entrega, cupones.
- Desglose de la cotización (IGV, descuentos por línea, envío) con la explicación de promociones aplicadas y no aplicadas; aviso si la cotización caduca.

**Terminado cuando**
- Lo que el cliente ve coincide céntimo a céntimo con lo que cobra el backend (prueba E2E).

**Aprender y documentar**
- Formularios tipados y validación asíncrona en Angular.

### FE-03.2 · Pasarela de pagos
- **Ola:** 4 · **Profundidad:** A
- **Depende de:** FE-03.1, BE-10.2

**Requerimientos**
- Campos alojados o SDK de la pasarela para tokenizar en el navegador: los datos de tarjeta nunca tocan nuestro front ni nuestro backend; 3-D Secure; manejo de cada estado de pago.
- **Cifrado de campos sensibles** propios (por ejemplo, documento de identidad) con Web Crypto y la clave pública del backend (JWE), como defensa adicional a TLS; ADR sobre cuándo esto aporta y cuándo es teatro de seguridad.

**Terminado cuando**
- Una inspección de red no muestra datos de tarjeta hacia nuestros dominios y el pago en sandbox se completa con 3-D Secure.

**Aprender y documentar**
- Tokenización y alcance PCI; 3-D Secure; JWE y JWS.

### FE-03.3 · Estado de la saga e idempotencia
- **Ola:** 4 · **Profundidad:** B
- **Depende de:** FE-03.2, BE-11.2

**Requerimientos**
- Estado de la compra en vivo por SSE ("reservando", "autorizando", "esperando al comercio", "confirmado" o motivo de fallo, incluido el rechazo de un comercio con su reembolso parcial).
- **Bandeja de pedidos del comercio**: aceptar o rechazar sub-pedidos dentro del plazo y marcar envíos como listos (decisión N7), sobre la API REST de `order-service`. Sus componentes se reutilizan después en el portal de FE-05.1.
- `Idempotency-Key` generada por intento de compra; recargar o hacer doble clic no duplica.

**Terminado cuando**
- Recargar la página a mitad del pago no cobra dos veces (prueba E2E).

**Aprender y documentar**
- Diseñar una interfaz honesta sobre consistencia eventual.
