# INF-07 · Alta disponibilidad y recuperación ante desastres

**Objetivo:** demostrar con ensayos, no con diagramas, que el sistema sobrevive a la pérdida de una zona y que puede recuperarse de la pérdida de una región.

### INF-07.1 · Validación en local
- **Ola:** 8 · **Profundidad:** A
- **Depende de:** INF-02.4, OPS-04.2

**Requerimientos**
- Auditoría de todo lo desplegado contra `alta-disponibilidad.md`, con correcciones.
- Ensayos en el minikube de tres zonas: drenar una zona completa bajo carga; perder el primario de PostgreSQL, un *broker* de Kafka, un nodo de Elasticsearch, el primario de Redis y un miembro de MongoDB.
- Medición de impacto por ensayo: errores visibles, tiempo de recuperación, pérdida de datos (debe ser cero para lo confirmado).

**Terminado cuando**
- Drenar una zona bajo carga no consume más presupuesto de error del permitido por los SLO.

**Aprender y documentar**
- Consenso y elección de líder (Raft en Kafka KRaft, Vault y Elasticsearch); replicación síncrona frente a asíncrona en PostgreSQL y su efecto sobre el RPO.

### INF-07.2 · Multi-zona en la nube
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-04.4, INF-05.4, INF-07.1

**Requerimientos**
- Activación temporal de la configuración de alta disponibilidad completa en una nube (bases gestionadas multi-zona, nodos en tres zonas).
- Ensayo de conmutación de la base de datos gestionada y de pérdida de nodos, grabado.

**Terminado cuando**
- La conmutación de la base gestionada se completa con el impacto medido y dentro del objetivo.

**Aprender y documentar**
- Qué garantiza realmente un servicio gestionado "multi-zona".

### INF-07.3 · Recuperación ante desastres regional
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-07.2, DB-07.2

**Requerimientos**
- Estrategia activo-pasivo (respaldo y restauración o *pilot light*, ADR con coste): respaldos y WAL replicados a otra región, imágenes replicadas, Terraform capaz de levantar la región secundaria.
- Simulacro: perder la región primaria y recuperar en la secundaria, midiendo RPO y RTO.
- Conmutación de DNS por comprobación de salud.

**Terminado cuando**
- El simulacro recupera el servicio en otra región con RPO y RTO medidos y documentados.

**Aprender y documentar**
- Estrategias de recuperación ante desastres y su coste; por qué activo-activo multi-región no se justifica aquí.
