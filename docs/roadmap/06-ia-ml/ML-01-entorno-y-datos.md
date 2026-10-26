# ML-01 · Entorno, datos y líneas base

### ML-01.1 · Entorno y extracción de datos
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** DB-06.2, DB-02.5

**Requerimientos**
- Estructura `ml/`: `notebooks/`, `src/`, `models/`, `serving/`; datos fuera del repositorio.
- MLflow (experimentos y registro de modelos) en el Compose; versionado de conjuntos de datos con DVC contra el almacenamiento de objetos.
- Extracción desde ClickHouse con consultas versionadas.

**Terminado cuando**
- Un comando reproduce la extracción y registra el conjunto de datos con su huella.

**Aprender y documentar**
- Por qué versionar datos además de código.

### ML-01.2 · Análisis exploratorio y líneas base
- **Ola:** 7 · **Profundidad:** B
- **Depende de:** ML-01.1

**Requerimientos**
- *Notebook* de análisis: estacionalidad, tendencia, efectos de zona y calendario, calidad de datos.
- División temporal sin fuga de información del futuro; validación con ventana deslizante.
- Líneas base obligatorias: ingenuo estacional y *gradient boosting*. El modelo profundo debe superarlas para justificarse.

**Terminado cuando**
- Las líneas base están registradas en MLflow con sus métricas y se reproducen con un comando.

**Aprender y documentar**
- Fuga de datos en series temporales; métricas de pronóstico (MAE, sMAPE, pérdida de cuantiles) y cuál importa al negocio.
