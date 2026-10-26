# 03 · Datos (`DB`)

Las fases `DB` establecen bases, herramientas y prácticas; los servicios las aplican. Los objetos de base de datos de un servicio (tablas, funciones, procedimientos, triggers) viven siempre en las migraciones **de ese servicio**.

| Fase | Título | Olas |
|---|---|---|
| [DB-01](DB-01-postgresql-y-flyway.md) | PostgreSQL base y Flyway | 1 |
| [DB-02](DB-02-datos-sinteticos.md) | Datos sintéticos y simulador de tráfico | 1 a 7 |
| [DB-03](DB-03-nosql.md) | NoSQL: Redis y MongoDB | 1, 2 |
| [DB-04](DB-04-plataforma-de-eventos.md) | Plataforma de eventos: Kafka, esquemas y CDC | 2 |
| [DB-05](DB-05-postgresql-avanzado.md) | PostgreSQL avanzado | 4 |
| [DB-06](DB-06-analitica.md) | Almacén analítico | 6 |
| [DB-07](DB-07-respaldos-y-continuidad.md) | Volcados, respaldos y continuidad | 6 |

Elasticsearch se trata en `BE-08` (servicio de búsqueda), donde su modelado y su uso están acoplados.

## Plan de datos de volumen

Muchas sub-fases necesitan datos realistas en cantidad. En lugar de dejarlo para el final, el generador (`DB-02`) crece en cada ola junto con lo que hay que poblar. Es **determinista**: misma semilla, mismos datos.

| Perfil | Uso | Escala indicativa (se fija en FND-03.2) | Tiempo de carga objetivo |
|---|---|---|---|
| `S` | Desarrollo y pruebas automatizadas | Cientos de comercios, miles de productos y pedidos | Segundos |
| `M` | Demos, pruebas de integración del sistema, pruebas de carga funcionales | Decenas de miles de productos, ~1 M de pedidos | Minutos |
| `L` | Rendimiento, analítica, entrenamiento de modelos | Decenas de millones de eventos y pedidos históricos | Restauración desde instantánea |

| Sub-fase | Ola | Qué añade |
|---|---|---|
| DB-02.1 | 1 | Núcleo del generador, zonas de Lima, clientes, comercios, repartidores |
| DB-02.2 | 2 | Catálogo con atributos heterogéneos, tiendas, existencias |
| DB-02.3 | 4 | Historial de pedidos y pagos con estacionalidad |
| DB-02.4 | 5 | Simulador en vivo: pedidos entrantes y GPS de repartidores |
| DB-02.5 | 6 | Volumen analítico y reproducción de flujos de eventos |
| DB-02.6 | 7 | Reseñas en español peruano y conjunto etiquetado para ML |

Los datos de los perfiles `M` y `L` se generan una vez y se guardan como **instantáneas** (volcados) en el almacenamiento de objetos; restaurarlas es lo habitual, y es a la vez práctica de `DB-07`.

## Requisitos comunes

- Toda consulta importante tiene su plan de ejecución revisado y, si es crítica, una prueba que detecta regresiones de plan.
- Toda conexión usa TLS y un usuario de mínimo privilegio.
- Ningún servicio accede a la base de datos de otro.
