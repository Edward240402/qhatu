# 06 · Deep Learning y MLOps (`ML`)

Dos modelos con propósitos distintos:

| | Modelo A — consumido | Modelo B — propio |
|---|---|---|
| Qué es | Modelo de lenguaje **preentrenado** para español | Modelo **predictivo entrenado por nosotros** con datos del producto |
| Tarea | Sentimiento y moderación de reseñas | Pronóstico de demanda por producto, zona y franja horaria |
| Entrenamiento | Ninguno (evaluación propia y optimización para servir) | Completo, en PyTorch, con seguimiento de experimentos |
| Dónde se usa | Resumen de reseñas en web y móvil; alerta de moderación | Dashboard de demanda, sugerencias de reposición, pre-posicionamiento de repartidores |

La IA generativa (asistente con RAG) está en el backend: `BE-18`.

| Fase | Título | Ola |
|---|---|---|
| [ML-01](ML-01-entorno-y-datos.md) | Entorno, datos y líneas base | 7 |
| [ML-02](ML-02-modelo-preentrenado.md) | Modelo preentrenado para reseñas | 7 |
| [ML-03](ML-03-modelo-de-demanda.md) | Modelo predictivo de demanda | 7 |
| [ML-04](ML-04-inferencia-e-integracion.md) | Servicio de inferencia e integración | 7 |
| [ML-05](ML-05-mlops.md) | MLOps: ciclo de vida | 7 |

## Requisitos comunes

- Python con entorno reproducible (`uv` con archivo de bloqueo), tipado y lint.
- Los *notebooks* sirven para explorar y explicar; la lógica reutilizable vive en módulos con pruebas. Los *notebooks* se versionan sin salidas pesadas y se ejecutan de principio a fin en CI.
- Semillas fijas: todo resultado reportado se regenera con un comando.
- Los datos son sintéticos (DB-02): se documenta cómo se generaron y qué limita eso las conclusiones.
