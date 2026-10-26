# ML-03 · Modelo predictivo de demanda

### ML-03.1 · Ingeniería de características
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** ML-01.2

**Requerimientos**
- Retardos, ventanas móviles, calendario (feriados de Perú, quincenas), zona, clima simulado, promociones (desde los eventos de `pricing-service`).
- Pipeline de características probado y reutilizable entre entrenamiento e inferencia (sin desviación entre ambos).

**Terminado cuando**
- Las mismas características se calculan igual en entrenamiento y en inferencia (prueba).

**Aprender y documentar**
- Desviación entre entrenamiento y servicio (*training-serving skew*).

### ML-03.2 · Modelo profundo
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** ML-03.1

**Requerimientos**
- Modelo en PyTorch para series temporales múltiples (candidatos: LSTM con *embeddings* de entidad, Temporal Fusion Transformer, N-HiTS); bucle de entrenamiento propio y comprensible, parada temprana, programación de la tasa de aprendizaje.
- Búsqueda de hiperparámetros registrada en MLflow.

**Terminado cuando**
- El mejor experimento está registrado y se reentrena con un comando.

**Aprender y documentar**
- Retropropagación y descenso de gradiente; por qué recurrentes o atención para secuencias; sobreajuste y regularización. Los *notebooks* de esta sub-fase son material didáctico.

### ML-03.3 · Pronóstico probabilístico y comparación
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** ML-03.2

**Requerimientos**
- Pronóstico por cuantiles (al negocio le sirve el intervalo, no solo el punto).
- Comparación rigurosa contra las líneas base con validación temporal; error por segmento (productos nuevos, zonas con pocos datos); interpretabilidad.
- **Ficha del modelo** (uso previsto, datos, métricas, limitaciones, consideraciones éticas).
- Si el modelo profundo no supera a la línea base, se documenta y se sirve el mejor: esa conclusión vale más en un portafolio que un resultado forzado.

**Terminado cuando**
- El modelo elegido está promovido en MLflow con su ficha y su *notebook* de comparación reproducible.

**Aprender y documentar**
- Pérdida de cuantiles; calibración de intervalos.
