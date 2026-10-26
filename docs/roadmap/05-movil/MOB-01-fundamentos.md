# MOB-01 · Fundamentos y diseño adaptable

### MOB-01.1 · Proyecto, arquitectura y entorno
- **Ola:** 9 · **Profundidad:** C
- **Depende de:** FE-01.1, OPS-01.1

**Requerimientos**
- ADR del entorno de desarrollo en WSL/Windows (ver [README](README.md)).
- Arquitectura por capas y por funcionalidad; gestión de estado con ADR (Riverpod o Bloc); navegación declarativa con enlaces profundos.
- *Flavors* `dev`, `staging`, `prod` con configuración separada; manejo global de errores.
- Pipeline de CI del móvil (análisis, pruebas, compilación Android).

**Terminado cuando**
- La app arranca en el emulador contra el backend local por HTTPS.

**Aprender y documentar**
- Árbol de *widgets*, elementos y objetos de render.

### MOB-01.2 · Diseño adaptable y adaptativo
- **Ola:** 9 · **Profundidad:** B
- **Depende de:** MOB-01.1

**Requerimientos**
- Puntos de quiebre, `LayoutBuilder`; navegación que cambia (barra inferior → carril lateral → maestro-detalle en tableta); orientación y plegables.
- Sistema de diseño con los *tokens* de la web; tema claro y oscuro; internacionalización.
- Capturas automatizadas en la matriz de dispositivos en CI.

**Terminado cuando**
- Las pantallas base se ven correctas en toda la matriz de dispositivos.

**Aprender y documentar**
- Restricciones de diseño en Flutter; adaptable frente a adaptativo.
