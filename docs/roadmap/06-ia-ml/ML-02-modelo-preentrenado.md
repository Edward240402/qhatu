# ML-02 · Modelo preentrenado para reseñas

### ML-02.1 · Selección y evaluación propia
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** ML-01.1, DB-02.6

**Requerimientos**
- Evaluar varios modelos preentrenados en español o multilingües con licencia compatible; ficha con origen, licencia y limitaciones.
- **Evaluación propia** sobre el conjunto etiquetado de DB-02.6 (español peruano), con matriz de confusión y análisis de errores. No se confía en las métricas publicadas.

**Terminado cuando**
- El informe compara los candidatos y justifica el elegido.

**Aprender y documentar**
- Arquitectura *transformer* a nivel conceptual (atención, *tokens*, *embeddings*); aprendizaje por transferencia.

### ML-02.2 · Optimización para servir
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** ML-02.1

**Requerimientos**
- Exportación a ONNX y cuantización; latencia y exactitud medidas antes y después.
- Artefacto registrado en MLflow con su huella.

**Terminado cuando**
- El modelo cuantizado mantiene la exactitud dentro del margen fijado y cumple el presupuesto de latencia en CPU.

**Aprender y documentar**
- Qué es ONNX y qué hace la cuantización.
