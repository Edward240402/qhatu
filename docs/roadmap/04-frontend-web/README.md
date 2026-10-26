# 04 · Frontend web (`FE`)

Angular en su versión estable vigente (referencia: 22), con las prácticas actuales: componentes *standalone*, *signals*, sin Zone.js, control de flujo nativo. El front es secundario frente al backend en este portafolio, pero se construye a nivel profesional.

| Fase | Título | Olas |
|---|---|---|
| [FE-01](FE-01-cascaron-y-autenticacion.md) | Cascarón, autenticación y roles | 1 |
| [FE-02](FE-02-catalogo-y-cache.md) | Búsqueda, catálogo, carrito y caché | 3, 4 |
| [FE-03](FE-03-checkout-y-pagos.md) | *Checkout*, pagos y datos sensibles | 4 |
| [FE-04](FE-04-tiempo-real.md) | Tiempo real: Google Maps y WhatsApp | 5 |
| [FE-05](FE-05-portales-y-reportes.md) | Portales por rol y reportes | 6 |
| [FE-06](FE-06-dashboards.md) | Dashboards de análisis de datos | 6 |
| [FE-07](FE-07-ia.md) | Integración con IA | 7 |
| [FE-08](FE-08-calidad-final.md) | Calidad final | 10 |

## Requisitos comunes a toda sub-fase `FE`

Lista completa en `docs/estandares/dod-frontend.md`:

- TypeScript estricto; ESLint con reglas de límites entre librerías; formato forzado.
- Clientes de API **generados desde el contrato** (OpenAPI o GraphQL), nunca tipos escritos a mano que lo dupliquen.
- Pruebas unitarias y de componente; E2E con Playwright de los flujos de la sub-fase.
- Accesibilidad WCAG 2.2 AA verificada con axe; navegación por teclado.
- Diseño adaptable; español de Perú y moneda PEN por defecto, preparado para internacionalización.
- Nada sensible en almacenamiento del navegador, URLs ni logs.
- Desde OBS-03.3, telemetría de errores y rendimiento del navegador.
