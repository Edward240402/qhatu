# INF-03 · Terraform multi-nube

### INF-03.1 · Estructura, estado y federación
- **Ola:** 8 · **Profundidad:** A
- **Depende de:** INF-02.4, OPS-04.2

**Requerimientos**
- `modules/` reutilizables con una **interfaz común** (`network`, `cluster`, `database`, `cache`, `registry`, `secrets`, `object-storage`, `cdn`, `dns-tls`) y una implementación por nube; `live/<nube>/<entorno>/<capa>/` que los compone.
- Estado remoto con bloqueo y cifrado, creado por un *bootstrap* documentado; un estado por entorno y por capa (red, plataforma, datos) para limitar el radio de impacto.
- Versiones de proveedores fijadas y archivo de bloqueo versionado.
- Autenticación de CI a ambas nubes con **OIDC federado**, sin claves de larga duración.

**Terminado cuando**
- El estado nunca existió en local y el CI se autentica sin secretos estáticos.

**Aprender y documentar**
- Grafo de dependencias y ciclo plan/apply; qué contiene el estado y por qué es sensible; federación OIDC entre GitHub y la nube.

### INF-03.2 · Calidad, coste y deriva
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** INF-03.1

**Requerimientos**
- En CI: `fmt`, `validate`, TFLint, Checkov o Trivy, `terraform test`, **Infracost** y el `plan` como comentario del PR.
- Etiquetado obligatorio y **presupuestos con alertas** en ambas nubes antes de cualquier recurso con coste.
- Detección de deriva programada; procedimiento **levantar → demostrar → destruir** con verificación de que no queda nada facturando.

**Terminado cuando**
- Un PR de infraestructura muestra plan, hallazgos de seguridad y diferencia de coste.

**Aprender y documentar**
- Diseño de módulos y sus anti-patrones; FinOps básico.
