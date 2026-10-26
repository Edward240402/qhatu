# FE-06 · Dashboards de análisis de datos

### FE-06.1 · Dashboards analíticos
- **Ola:** 6 · **Profundidad:** B
- **Depende de:** FE-05.3, BE-17.1, DB-02.5

**Requerimientos**
- Ventas, demanda (mapa de calor por zona y hora), desempeño de reparto, embudo de compra y búsquedas sin resultados, con filtros cruzados y desglose.
- Librería de gráficos con ADR (referencia: Apache ECharts); la agregación ocurre en ClickHouse y el front recibe series ya reducidas.
- Rendimiento: renderizado en lienzo, *web workers* para transformaciones, cancelación de peticiones obsoletas.
- Gráficos accesibles (alternativa tabular, paletas seguras para daltonismo).

**Terminado cuando**
- Los dashboards responden a los filtros dentro del objetivo sobre el perfil `L`.

**Aprender y documentar**
- Elección del tipo de gráfico según la pregunta; reducción de series temporales.

### FE-06.2 · Panel en tiempo real
- **Ola:** 6 · **Profundidad:** B
- **Depende de:** FE-06.1, BE-12.4

**Requerimientos**
- Panel operativo alimentado por las agregaciones de Kafka Streams: pedidos pendientes, repartidores disponibles y recargo por zona sobre el mapa.

**Terminado cuando**
- Con el simulador en escenario de hora punta, el panel refleja el aumento de demanda y del recargo en segundos.

**Aprender y documentar**
- Visualización de datos en *streaming* sin saturar el navegador.
