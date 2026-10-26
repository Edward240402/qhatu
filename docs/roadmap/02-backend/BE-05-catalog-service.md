# BE-05 · `catalog-service` — Quarkus reactivo, Clean Architecture y caché

**Objetivo:** catálogo de lectura intensiva en Quarkus reactivo con MongoDB, caché en Redis y eventos confiables.

### BE-05.1 · Dominio con atributos dinámicos
- **Ola:** 2 · **Profundidad:** B
- **Depende de:** BE-01.2, DB-03.2

**Requerimientos**
- **Clean Architecture**: entidades y casos de uso sin dependencias de framework; adaptadores en el borde. Comparación escrita con la hexagonal de BE-06.
- Productos con variantes y **precio de lista** (el catálogo es su dueño; promociones e impuestos son de `pricing-service`, decisión N1).
- **Esquemas de atributos por categoría con herencia** (una subcategoría hereda y especializa los atributos de su padre), validados al guardar. La resolución del esquema efectivo es O(profundidad) con caché.
- Quarkus REST reactivo con Mutiny y cliente reactivo de MongoDB.

**Terminado cuando**
- Un producto que no cumple el esquema heredado de su categoría es rechazado con un error claro.

**Aprender y documentar**
- Modelo de Quarkus (aumentación en compilación, ArC, Vert.x); hilos de E/S frente a hilos de trabajo; Mutiny (`Uni`, `Multi`) frente a Reactor. Experimento: bloquear el *event loop* y ver la detección.

### BE-05.2 · Imágenes de producto
- **Ola:** 2 · **Profundidad:** B
- **Depende de:** BE-05.1

**Requerimientos**
- Subida directa al almacenamiento de objetos con URL prefirmada de corta duración, límites de tamaño y tipo, verificación del contenido real del archivo.
- Estado de la imagen (pendiente, procesada, rechazada); el procesamiento lo hará la función de INF-06.1, con un procesador local equivalente mientras tanto (es el mismo núcleo, no un sustituto temporal).

**Terminado cuando**
- Un archivo que no es imagen pese a su extensión es rechazado.

**Aprender y documentar**
- URL prefirmadas: cómo se firman y qué se puede restringir.

### BE-05.3 · Reseñas y calificación
- **Ola:** 2 · **Profundidad:** B
- **Depende de:** BE-05.2

**Requerimientos**
- Reseñas solo de compras entregadas (decisión N10): la regla se implementa contra un puerto `PurchaseVerifier`; su adaptador real llega en BE-12.1 al existir `DeliveryCompleted`. Hasta entonces la creación de reseñas está desactivada por *feature flag* (BE-01.3) y las reseñas se cargan con el generador (DB-02.2).
- **Calificación bayesiana** para ordenar con justicia productos con pocas reseñas; actualización incremental en O(1) por reseña.
- Migración perezosa de documentos con campo de versión de esquema (ejercicio de DB-01.2).

**Terminado cuando**
- Un producto con una sola reseña de 5 estrellas no supera a uno con cientos de reseñas de 4,7 en el orden.

**Aprender y documentar**
- Promedio bayesiano y su relación con la confianza estadística.

### BE-05.4 · Caché
- **Ola:** 2 · **Profundidad:** A
- **Depende de:** BE-05.3, DB-03.1

**Requerimientos**
- *Cache-aside* en Redis con TTL con *jitter*, invalidación por evento, protección contra estampida (bloqueo o recálculo anticipado probabilístico), caché negativa.
- Caché HTTP (`ETag`, `Cache-Control`) coordinada con el front.

**Terminado cuando**
- Bajo carga, expirar una clave caliente no dispara la base de datos (demostrado en métricas).

**Aprender y documentar**
- Estrategias de caché y sus fallos (estampida, penetración, avalancha); por qué la invalidación es el problema difícil.

### BE-05.5 · Eventos confiables
- **Ola:** 2 · **Profundidad:** A
- **Depende de:** BE-05.4, DB-04.3

**Requerimientos**
- `ProductChanged` y `ReviewCreated` publicados con outbox sobre MongoDB vía Debezium (o *change streams*, ADR), con esquema en el registro.

**Terminado cuando**
- Matar el servicio tras guardar pero antes de publicar no pierde el evento.

**Aprender y documentar**
- Outbox sobre una base documental: diferencias con PostgreSQL.

### BE-05.6 · Imagen nativa
- **Ola:** 2 · **Profundidad:** B
- **Depende de:** BE-05.5, INF-01.1

**Requerimientos**
- Compilación nativa con GraalVM; pruebas de integración también sobre el binario nativo.
- Tabla comparativa JVM frente a nativo: arranque, memoria en reposo y bajo carga, rendimiento sostenido, tiempo de compilación.

**Terminado cuando**
- La comparativa está publicada y el binario nativo pasa las pruebas.

**Aprender y documentar**
- GraalVM *native image*: análisis de mundo cerrado, inicialización en compilación, reflexión; por qué el rendimiento sostenido puede ser menor que con JIT.
