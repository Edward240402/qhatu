# 08 · Calidad, pruebas y CI/CD (`OPS`)

La calidad se verifica en cada cambio, de forma automática. **GitHub Actions** es la herramienta principal; **Jenkins** se implementa como pipeline equivalente para un subconjunto (OPS-04.5), porque sigue siendo muy común en empresas peruanas. La seguridad del pipeline (SAST, dependencias, firma) está en el frente [SEC](../10-seguridad/README.md).

| Fase | Título | Olas |
|---|---|---|
| [OPS-01](OPS-01-integracion-continua.md) | Integración continua | 0, 1 |
| [OPS-02](OPS-02-estrategia-de-pruebas.md) | Estrategia y automatización de pruebas | 1 a 4 |
| [OPS-03](OPS-03-contratos-y-api-testing.md) | Gobierno de contratos, Postman y Newman | 1, 2 |
| [OPS-04](OPS-04-entrega-continua.md) | Entrega continua, GitOps y registro de contenedores | 3, 8 |
| [OPS-05](OPS-05-rendimiento-y-caos.md) | Rendimiento, caos y capacidad | 10 |
| [OPS-06](OPS-06-publicacion.md) | Publicación 1.0 y portafolio | 10 |

## Matriz de pruebas: qué se ejecuta y cuándo

La regla: **cuanto más rápida y determinista es una prueba, antes se ejecuta**. Las lentas o costosas se ejecutan donde su señal justifica su coste. Esta matriz se formaliza en `docs/estandares/pruebas.md` (OPS-02.1) y cada sub-fase indica qué niveles le aplican.

| Nivel | Local / *pre-commit* | PR | Fusión a `main` | Nocturno | Antes de liberar | Tras desplegar | Producción continua |
|---|---|---|---|---|---|---|---|
| Formato, lint, compilación con análisis | ● | ● | | | | | |
| Detección de secretos | ● | ● | | | | | |
| Unitarias y de dominio | ● | ● | ● | | | | |
| Arquitectura (ArchUnit, Modulith) | ● | ● | | | | | |
| Propiedades (jqwik) | ○ | ● | | ● (más casos) | | | |
| Componente y *slices* | ○ | ● | ● | | | | |
| Integración con Testcontainers | ○ | ● (afectados) | ● (todos) | | | | |
| Migraciones (desde versión anterior) | | ● | | | ● | | |
| Contrato (Pact) y compatibilidad de esquemas | | ● | ● (`can-i-deploy`) | | ● | | |
| Lint y cambios incompatibles de API | | ● | | | | | |
| Escenarios de negocio (Cucumber) | | ● | ● | | | | |
| SAST, dependencias, Sonar | | ● | ● | ● (base completa) | | | |
| E2E de API (Newman) | | | ● | | ● | ● (humo) | |
| E2E de interfaz (Playwright) | | ○ (críticos) | ● | ● (completo) | ● | | |
| Accesibilidad y regresión visual | | ● | | ● | | | |
| Mutación (PIT) | | ○ (código cambiado) | | ● | | | |
| DAST (ZAP) | | ● (línea base) | | ● (autenticado) | ● | | |
| Carga de humo (k6) | | | ● | | | | |
| Carga, estrés, resistencia | | | | ● (semanal) | ● | | |
| Relevancia de búsqueda y evaluación de IA | | ● | | ● | | | |
| Caos | | | | ● (programado) | ● | | |
| Restauración de respaldos | | | | ● | | | |
| Análisis del canario | | | | | | ● | |
| Monitoreo sintético | | | | | | | ● |

● siempre · ○ opcional o parcial

## Requisitos comunes

- El pipeline de PR tiene un objetivo de duración (por ejemplo, menos de 10 minutos) y se mide; si se excede, se optimiza (paralelismo, ejecución solo de lo afectado, caché), nunca se quitan pruebas.
- Una prueba inestable se pone en **cuarentena formal** (issue, responsable, fecha); nunca se desactiva en silencio.
