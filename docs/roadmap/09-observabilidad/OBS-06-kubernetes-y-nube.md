# OBS-06 · Observabilidad en Kubernetes y nube

### OBS-06.1 · Pila en el clúster
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-04.4

**Requerimientos**
- Pila desplegada con operadores y *charts*; métricas del clúster, eventos de Kubernetes y logs de todos los *pods*.
- Almacenamiento de largo plazo en almacenamiento de objetos; retención y coste por señal.
- Anotaciones de eventos del sistema en los dashboards: despliegues, cambios de *flags*, escalados, experimentos de caos.

**Terminado cuando**
- Los dashboards y alertas de local funcionan sin cambios en EKS.

**Aprender y documentar**
- Descubrimiento de objetivos de recolección en Kubernetes; dimensionamiento y coste de la observabilidad.

### OBS-06.2 · Multi-entorno y servicios gestionados
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** OBS-06.1, INF-05.4

**Requerimientos**
- Mismos dashboards con variables de clúster y de nube.
- Integración de métricas de servicios gestionados (bases de datos, balanceadores, CDN, funciones).
- Comparativa documentada con CloudWatch y Azure Monitor: cuándo usar cada uno.

**Terminado cuando**
- Una sola vista muestra minikube, EKS y AKS.

**Aprender y documentar**
- Observabilidad propia frente a nativa de la nube.
