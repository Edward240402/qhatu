# INF-08 · Malla de servicios y mTLS

### INF-08.1 · Malla con mTLS y autorización entre servicios
- **Ola:** 8 · **Profundidad:** C
- **Depende de:** INF-04.4, INF-07.1

**Requerimientos**
- Malla elegida con ADR (Istio en modo *ambient* o Linkerd), en minikube y en una nube.
- mTLS estricto entre servicios con identidad SPIFFE; políticas de autorización de servicio a servicio alineadas con el mapa de contextos.
- Comparación de la resiliencia de la malla (reintentos, *timeouts*) con la de la aplicación: qué va en cada capa sin duplicar. Relación con el mTLS de SEC-03.2 (infraestructura) y cuándo se superponen.
- Coste medido en latencia y recursos.

**Terminado cuando**
- Una llamada no autorizada entre servicios es rechazada por política y el tráfico interno capturado está cifrado.

**Aprender y documentar**
- Identidad de cargas de trabajo (SPIFFE); *sidecar* frente a *ambient*; confianza cero.
