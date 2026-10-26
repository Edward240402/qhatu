# BE-18 · `assistant-service` — IA generativa en el backend

**Objetivo:** asistente de compra con respuestas fundamentadas en datos reales del producto y sin más permisos que la persona que lo usa.

### BE-18.1 · Recuperación aumentada (RAG)
- **Ola:** 7 · **Profundidad:** A
- **Depende de:** BE-08.4, BE-01.2

**Requerimientos**
- *Embeddings* del catálogo actualizados por eventos.
- ADR del almacén vectorial: Elasticsearch (ya existente; búsqueda híbrida BM25 + kNN con fusión por rango recíproco) frente a pgvector. Recomendación: Elasticsearch, para no añadir un almacén solo por variedad.
- Citas de los productos usados en cada respuesta.

**Terminado cuando**
- Un conjunto de preguntas de prueba recupera los productos esperados por encima del umbral definido.

**Aprender y documentar**
- *Embeddings* y búsqueda por similitud (HNSW); búsqueda híbrida y RRF; RAG frente a ajuste fino.

### BE-18.2 · Conversación y llamada a herramientas
- **Ola:** 7 · **Profundidad:** A
- **Depende de:** BE-18.1, BE-09.4

**Requerimientos**
- Spring AI con el proveedor detrás de una abstracción (Claude API en local; en la nube, el endpoint gestionado del proveedor si está disponible, ver INF-04.4 e INF-05.4).
- Respuestas en *streaming* por SSE.
- Herramientas: buscar productos, consultar estado de los pedidos **del propio usuario** (la autorización del usuario se propaga a la herramienta), añadir al carrito.

**Terminado cuando**
- Una prueba automatizada demuestra que el asistente no puede revelar pedidos de otro usuario aunque se le pida.

**Aprender y documentar**
- Cómo funciona la llamada a herramientas; por qué el modelo nunca debe tener más permisos que el usuario.

### BE-18.3 · Servidor MCP, defensas y evaluación
- **Ola:** 7 · **Profundidad:** A
- **Depende de:** BE-18.2

**Requerimientos**
- Servidor MCP con capacidades de solo lectura del producto.
- Defensas: tratamiento de inyección de instrucciones en contenido del catálogo y reseñas, filtrado de datos personales, límites de coste por usuario, auditoría.
- Evaluación automatizada en CI con conjunto de preguntas y respuestas esperadas; observabilidad de tokens, coste y latencia.

**Terminado cuando**
- La evaluación supera el umbral y un intento de inyección embebido en una reseña no altera el comportamiento.

**Aprender y documentar**
- Protocolo MCP; OWASP Top 10 para aplicaciones con LLM.
