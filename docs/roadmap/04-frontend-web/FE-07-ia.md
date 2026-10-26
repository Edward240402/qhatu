# FE-07 · Integración con IA

### FE-07.1 · Asistente de compra
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** FE-04.3, BE-18.2

**Requerimientos**
- Conversación en *streaming* (SSE) con tarjetas de producto citadas y acciones (añadir al carrito, ver pedido), cancelación de la respuesta, historial.
- El contenido generado se trata como no confiable (saneado, sin ejecutar HTML) y se marca como generado; se puede reportar una respuesta.

**Terminado cuando**
- Una E2E cubre una conversación que termina en un producto añadido al carrito y un intento de obtener datos ajenos que es rechazado.

**Aprender y documentar**
- Consumo de SSE en Angular; patrones de experiencia de usuario para IA generativa.

### FE-07.2 · Búsqueda semántica, reseñas y pronóstico
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** FE-07.1, ML-04.3

**Requerimientos**
- Búsqueda semántica en el catálogo (híbrida, desde BE-18.1).
- Resumen de reseñas con el sentimiento del modelo de ML-02.
- Para comercios: pronóstico de demanda con intervalos en el dashboard y sugerencias de reposición; borrador asistido de descripciones con revisión humana obligatoria.

**Terminado cuando**
- El pronóstico se muestra con su intervalo y la fecha de la versión del modelo que lo produjo.

**Aprender y documentar**
- Cómo comunicar incertidumbre (intervalos) a usuarios de negocio.
