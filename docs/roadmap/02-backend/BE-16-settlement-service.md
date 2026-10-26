# BE-16 · `settlement-service` — libro mayor, liquidación y facturación

**Objetivo:** el dominio financiero: libro mayor de doble entrada, liquidación periódica a comercios y comprobantes electrónicos. Es el caso donde la lógica en la base de datos y los hilos de plataforma son la elección correcta.

### BE-16.1 · Libro mayor de doble entrada
- **Ola:** 6 · **Profundidad:** A
- **Depende de:** DB-05.3, BE-11.3

**Requerimientos**
- Asientos con débitos y créditos que siempre suman cero, por pedido, pago, comisión, reembolso y contracargo; tabla particionada por fecha.
- **Inmutabilidad** garantizada por triggers (sin `UPDATE` ni `DELETE`; las correcciones son asientos de reverso).
- Saldo por cuenta con funciones SQL y vistas materializadas.

**Terminado cuando**
- Cualquier `UPDATE` o `DELETE` sobre el libro es rechazado y el balance global es cero tras cualquier secuencia de operaciones (prueba de propiedades).

**Aprender y documentar**
- Contabilidad de doble entrada para ingenieros; por qué un libro mayor inmutable.

### BE-16.2 · Proceso de liquidación con Spring Batch
- **Ola:** 6 · **Profundidad:** A
- **Depende de:** BE-16.1

**Requerimientos**
- Trabajo de Spring Batch: lectura por fragmentos, particionado por comercio, reinicio desde el punto de fallo, omisión y reintento controlados.
- Cálculo intensivo en CPU con **hilos de plataforma** en un `ExecutorService` dimensionado, comparado con virtual threads y con *parallel streams*.
- Una sola ejecución entre réplicas; se ejecutará como `CronJob` en Kubernetes.

**Terminado cuando**
- Un trabajo interrumpido a mitad se reanuda sin duplicar liquidaciones; el informe de dimensionamiento de hilos está publicado.

**Aprender y documentar**
- Modelo de Spring Batch (`JobRepository`, *chunks*, reinicio); dimensionamiento de *pools* (ley de Little, CPU frente a E/S, ley de Amdahl); modelo de memoria de Java.

### BE-16.3 · Comisiones, retenciones y conciliación
- **Ola:** 6 · **Profundidad:** A
- **Depende de:** BE-16.2, BE-09.5

**Requerimientos**
- Base de la comisión según la decisión N4 (precio pagado más descuento financiado por la plataforma) e IGV sobre la comisión.
- Comisiones por tramos de volumen y categoría, retenciones por contracargos, ajustes por devoluciones parciales; implementadas con **procedimientos almacenados y funciones** (ADR de DB-05.2).
- **Cambio de la firma de una función** usada por procedimientos, gestionado con migraciones repetibles y compatibilidad (ejercicio de DB-01.2).
- **Conciliación** contra el reporte de la pasarela: emparejamiento exacto por *hash join* (O(n + m)) y emparejamiento difuso de lo no emparejado (monto y fecha dentro de tolerancia), con lista de diferencias para revisión.

**Terminado cuando**
- La conciliación de un día con diferencias sembradas a propósito las identifica todas y no inventa otras.

**Aprender y documentar**
- Algoritmos de emparejamiento de registros; por qué esta lógica va en la base de datos (o por qué no).

### BE-16.4 · Comprobantes electrónicos
- **Ola:** 6 · **Profundidad:** A
- **Depende de:** BE-16.3

**Requerimientos**
- Modelo de emisión de la decisión N9: comprobantes de productos por cuenta de cada comercio (serie por comercio) y comprobantes propios de Qhatu por envío y por comisión.
- Emisión de boletas y facturas con IGV, series y **correlativos sin huecos** (requisito legal que obliga a resolver concurrencia: secuencia con bloqueo por serie, no una secuencia de PostgreSQL, que admite huecos).
- Envío simulado a un OSE (operador de servicios electrónicos) con estados, reintentos y comunicación de baja.
- La generación del PDF la hará la función de INF-06.2; mientras tanto, generación en proceso con el mismo núcleo.

**Terminado cuando**
- Bajo concurrencia, los correlativos de una serie son consecutivos y sin huecos.

**Aprender y documentar**
- Por qué las secuencias de las bases de datos admiten huecos; facturación electrónica en Perú a nivel conceptual.
