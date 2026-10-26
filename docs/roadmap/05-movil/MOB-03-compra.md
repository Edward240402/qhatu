# MOB-03 · Compra, modo sin conexión y pagos

### MOB-03.1 · Catálogo y carrito sin conexión
- **Ola:** 9 · **Profundidad:** B
- **Depende de:** MOB-02.2, BE-08.3, BE-09.2

**Requerimientos**
- Búsqueda, catálogo y carrito multi-comercio.
- **Modo sin conexión**: base local, *stale-while-revalidate*, cola de acciones pendientes sincronizada al recuperar la red con resolución de conflictos.

**Terminado cuando**
- Se navega el catálogo en modo avión y las acciones pendientes se sincronizan al volver la red.

**Aprender y documentar**
- Diseño *offline-first*.

### MOB-03.2 · *Checkout* y pagos
- **Ola:** 9 · **Profundidad:** B
- **Depende de:** MOB-03.1, BE-10.2, BE-11.2

**Requerimientos**
- Cotización, *checkout* y estado de la saga; SDK móvil de la pasarela con tokenización en el dispositivo; billeteras del sistema si la pasarela lo permite.
- Idempotencia ante reintentos por mala red.

**Terminado cuando**
- Cortar la red a mitad del pago no duplica el cobro.

**Aprender y documentar**
- Ciclo de vida de la app y trabajo en segundo plano durante un pago.
