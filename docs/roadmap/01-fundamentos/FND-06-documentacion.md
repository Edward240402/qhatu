# FND-06 · Esqueleto y sitio de documentación

**Objetivo:** que documentar sea rellenar una plantilla, y que la documentación sea la cara del portafolio.

### FND-06.1 · Estructura, plantillas y listas de terminado
- **Ola:** 0 · **Profundidad:** B
- **Depende de:** FND-01.1

**Requerimientos**
- Estructura y plantillas de [91-estandar-documentacion.md](../91-estandar-documentacion.md): `docs/aprendizaje/`, `docs/operacion/`, `docs/estandares/`, índices por tema y por frente.
- `docs/estandares/documentacion.md`.
- **Listas de terminado por frente** (`docs/estandares/dod-backend.md`, `dod-frontend.md`, `dod-movil.md`, `dod-datos.md`, `dod-infra.md`, `dod-ml.md`): la definición común más lo propio del frente. `/fase` y el revisor las usan en cada cierre.

**Terminado cuando**
- Existen todas las plantillas y listas, y el skill `/fase` las referencia.

**Aprender y documentar**
- Modelo Diátaxis (tutorial, guía, referencia, explicación) y cómo se aplica aquí.

### FND-06.2 · Sitio publicado y verificación automática
- **Ola:** 0 · **Profundidad:** B
- **Depende de:** FND-06.1, OPS-01.1

**Requerimientos**
- Sitio estático (MkDocs Material o Docusaurus, ADR) publicado en GitHub Pages por CI, con secciones Portafolio, Aprendizaje, Operación, Arquitectura y Estándares.
- Verificación en CI de enlaces rotos y de referencias `ruta:línea` obsoletas.
- `README.md` raíz en **español e inglés**, orientado a quien evalúa: qué es, diagrama, cómo verlo funcionar en 5 minutos, y el mapa "si te interesa X, mira Y".

**Terminado cuando**
- El sitio se publica desde CI y un enlace roto hace fallar el pipeline.

**Aprender y documentar**
- Documentación como código; cómo funciona un generador de sitios estáticos y su publicación.
