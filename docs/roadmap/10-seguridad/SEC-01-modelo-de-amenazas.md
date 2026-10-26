# SEC-01 · Modelo de amenazas y estándares

### SEC-01.1 · Modelo de amenazas, clasificación de datos y estándar de seguridad
- **Ola:** 0 · **Profundidad:** A
- **Depende de:** FND-03.2

**Requerimientos**
- Modelo de amenazas STRIDE sobre el diagrama de contenedores, con fronteras de confianza; cada amenaza con su mitigación prevista y la sub-fase donde se implementa.
- `docs/estandares/clasificacion-de-datos.md`: niveles (público, interno, confidencial, personal, personal sensible, datos de pago) con ejemplos de Qhatu y el tratamiento obligatorio de cada nivel (cifrado, enmascarado, retención, registro de acceso). Alineado con la Ley N.° 29733 y su reglamento.
- `docs/estandares/seguridad.md`: nivel objetivo de OWASP ASVS, OWASP API Security Top 10 y Top 10 para aplicaciones con LLM; reglas de autenticación, autorización, validación de entrada, cabeceras, registro de seguridad.

**Terminado cuando**
- Cada amenaza tiene una mitigación asignada a una sub-fase concreta del roadmap.

**Aprender y documentar**
- STRIDE y cómo se hace un modelo de amenazas útil (no decorativo); qué exige la ley peruana de protección de datos a un sistema como este.
