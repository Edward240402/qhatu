# 05 · Móvil (`MOB`)

## Tecnología: Flutter (a confirmar en FND-03.2)

No hay cifras públicas fiables que separen la demanda por framework en Perú: los portales muestran vacantes de Flutter y de React Native, y muchas aceptan cualquiera. A nivel global React Native tiene más vacantes y Flutter crece más rápido. La recomendación se apoya en criterios del proyecto:

| Criterio | Flutter | React Native | Nativo (Kotlin + Swift) |
|---|---|---|---|
| Presencia en vacantes peruanas | Alta | Alta | Alta en banca |
| Una base de código para teléfono y tableta | Sí | Sí | No (dos apps) |
| Diseño adaptable a muchos tamaños | Muy bueno (motor de render propio) | Bueno | Muy bueno |
| Mapas y ubicación en segundo plano | Maduro | Maduro | El mejor |
| Reutiliza el TypeScript de Angular | No (Dart) | Sí | No |
| Coste para una sola persona | Bajo | Bajo | El doble |

**Recomendación: Flutter**, por consistencia visual entre tamaños de pantalla y coste de mantenimiento. React Native es igual de defendible si prefieres aprovechar TypeScript. El ADR se cierra con un conteo de vacantes de 15 minutos en Computrabajo, Indeed Perú, LinkedIn y GetOnBrd (últimos 30 días, Lima y remoto). Si gana React Native, las fases se mantienen y cambian las herramientas.

## Desarrollo móvil desde WSL: dos limitaciones reales

- **Android.** El emulador corre en Windows, no en WSL. MOB-01.1 decide con ADR entre (a) SDK de Flutter y Android en WSL conectados por `adb` al emulador o a un teléfono del lado de Windows, o (b) desarrollo móvil del lado de Windows sobre el repositorio de WSL. Se documenta cómo llega la app al backend en WSL y cómo se instala la CA de la PKI en el emulador.
- **iOS.** Compilar y firmar para iOS **exige macOS**. Sin una Mac, iOS se compila solo en CI con ejecutores macOS (MOB-06.2) y las pruebas en dispositivo se limitan a Android. Se declara tal cual en el portafolio.

## Alcance y orden

Una app con dos modos según el rol: **cliente** (paridad con la web de cliente) y **repartidor** (funciones que solo tienen sentido en móvil). Los portales de comercio y administración se adaptan a tableta con funcionalidad reducida.

La ola 9 es **paralelizable**: desde el fin de la ola 5 se pueden adelantar MOB-01 a MOB-04 en un *worktree* aparte, siempre que sus dependencias estén cerradas.

| Fase | Título | Ola |
|---|---|---|
| [MOB-01](MOB-01-fundamentos.md) | Fundamentos y diseño adaptable | 9 |
| [MOB-02](MOB-02-autenticacion-y-seguridad.md) | Autenticación y seguridad móvil | 9 |
| [MOB-03](MOB-03-compra.md) | Compra, modo sin conexión y pagos | 9 |
| [MOB-04](MOB-04-mapas-y-repartidor.md) | Mapas, seguimiento, notificaciones y modo repartidor | 9 |
| [MOB-05](MOB-05-ia-y-reportes.md) | IA, reportes y dashboards | 9 |
| [MOB-06](MOB-06-calidad-y-distribucion.md) | Calidad y distribución | 9 |

## Requisitos comunes

- Cliente de API generado desde el contrato; análisis estático estricto.
- Pruebas unitarias, de *widget*, *golden* y de integración.
- Probado en teléfono pequeño, teléfono grande y tableta, en vertical y horizontal.
- Accesibilidad: lectores de pantalla y tamaño de fuente del sistema.
