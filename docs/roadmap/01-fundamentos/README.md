# 01 · Fundamentos (`FND`)

Todo lo que debe existir antes del primer microservicio: repositorio, cadena de herramientas, modelo del dominio, contratos, entorno local y sistema de agentes. Son sub-fases cortas, pero fijan los estándares que el resto del proyecto hace cumplir (ver [90-gobierno-transversal.md](../90-gobierno-transversal.md)).

| Fase | Título | Olas |
|---|---|---|
| [FND-01](FND-01-repositorio.md) | Repositorio, convenciones y gestión del trabajo | 0 |
| [FND-02](FND-02-entorno-y-build.md) | Entorno WSL, cadena de herramientas y build | 0 |
| [FND-03](FND-03-dominio-y-contratos.md) | Dominio, requisitos y contratos | 0 |
| [FND-04](FND-04-infraestructura-local.md) | Infraestructura local con Docker Compose | 0 |
| [FND-05](FND-05-agentes.md) | Sistema de agentes de desarrollo | 0 |
| [FND-06](FND-06-documentacion.md) | Esqueleto y sitio de documentación | 0 |

## Formato de las sub-fases (todos los frentes)

```
### <ID> · <título>
- **Ola:** N · **Profundidad:** A|B|C
- **Depende de:** <IDs de sub-fases> | —

**Requerimientos** · **Terminado cuando** · **Aprender y documentar**
```

Además de lo que dice cada sub-fase, siempre aplica la definición de terminado común de `ROADMAP.md` y la lista de terminado del frente (`docs/estandares/dod-<frente>.md`, creada en FND-06.1).
