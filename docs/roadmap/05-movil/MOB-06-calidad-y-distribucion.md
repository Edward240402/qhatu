# MOB-06 · Calidad y distribución

### MOB-06.1 · Pruebas en dispositivos
- **Ola:** 9 · **Profundidad:** B
- **Depende de:** MOB-05.2

**Requerimientos**
- E2E en emuladores en CI para los flujos críticos; *golden tests* en la matriz de tamaños.
- Presupuestos de tamaño de la app y de tiempo de arranque.

**Terminado cuando**
- Las E2E móviles corren en CI y los presupuestos se verifican.

**Aprender y documentar**
- Estrategias de prueba en móvil y su coste.

### MOB-06.2 · Distribución y telemetría
- **Ola:** 9 · **Profundidad:** C
- **Depende de:** MOB-06.1, OBS-03.3

**Requerimientos**
- Firma con secretos gestionados (Fastlane); compilación de iOS en ejecutores macOS de CI; distribución a evaluadores (Firebase App Distribution, TestFlight si hay cuenta).
- Reporte de fallos y telemetría con trazas que continúan en el backend.

**Terminado cuando**
- Una etiqueta de versión genera compilaciones firmadas y distribuidas automáticamente.

**Aprender y documentar**
- Firma de aplicaciones en Android e iOS y publicación en tiendas.
