# SEC-06 · DAST, políticas y seguridad en ejecución

### SEC-06.1 · OWASP ZAP en el pipeline de PR
- **Ola:** 3 · **Profundidad:** B
- **Depende de:** FE-02.1, OPS-03.2

**Requerimientos**
- Escaneo de línea base de ZAP en cada PR contra el sistema en Compose, y escaneo de API dirigido por los OpenAPI.
- Umbral que rompe el pipeline; archivo de falsos positivos con justificación.
- Hallazgos publicados como alertas de seguridad del repositorio.

**Terminado cuando**
- Quitar una cabecera de seguridad hace fallar el PR.

**Aprender y documentar**
- Cómo funciona un escáner DAST (araña, escaneo pasivo y activo) y sus límites.

### SEC-06.2 · Políticas de admisión y detección en ejecución
- **Ola:** 8 · **Profundidad:** B
- **Depende de:** SEC-05.2, INF-04.4

**Requerimientos**
- Kyverno: solo imágenes firmadas del registro propio, sin contenedores privilegiados, recursos y etiquetas obligatorios, réplicas y PDB según `alta-disponibilidad.md`. En modo auditoría primero, luego en modo bloqueo.
- Falco con reglas para comportamientos anómalos (*shell* en un contenedor, lectura de secretos) y alertas hacia Grafana.
- Aplicado en minikube y en los clústeres de nube.

**Terminado cuando**
- El clúster rechaza una imagen sin firma y Falco alerta al abrir un *shell* en un *pod*.

**Aprender y documentar**
- Controladores de admisión; cómo Falco observa llamadas al sistema (eBPF).

### SEC-06.3 · Escaneo autenticado completo y verificación ASVS
- **Ola:** 10 · **Profundidad:** A
- **Depende de:** SEC-06.2, FE-07.2, BE-15.4

**Requerimientos**
- Escaneo activo **autenticado** de ZAP (contexto con inicio de sesión OIDC, un usuario por rol) contra el entorno de pruebas, programado.
- Corrección de todos los hallazgos altos y medios.
- Modelo de amenazas de SEC-01.1 actualizado al sistema real: cada amenaza con mitigación implementada y la prueba que la verifica.
- Matriz de cumplimiento OWASP ASVS (nivel objetivo), API Security Top 10 y Top 10 para LLM.
- Batería de pruebas de autorización: acceso entre comercios, escalada de rol, IDOR en cada API.

**Terminado cuando**
- El informe autenticado no tiene hallazgos altos ni medios sin tratar y la matriz ASVS está completa.

**Aprender y documentar**
- OWASP Top 10 con el ejemplo concreto de cómo Qhatu evita cada uno.
