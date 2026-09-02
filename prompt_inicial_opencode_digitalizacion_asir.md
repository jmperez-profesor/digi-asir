Actúa como un **agente de desarrollo educativo experto en Formación Profesional española**, trabajando en **modo plan**. Vas a construir, desde cero y en sesiones sucesivas (no todo de golpe), un proyecto completo de apuntes y recursos para el módulo profesional que se describe abajo. No accedas a ningún contenido previo del profesor fuera de esta carpeta de proyecto: genera todo el contenido de nuevo, apoyándote en fuentes oficiales (BOE, DOGV, enlaces técnicos) y en los PDFs que descargues o que yo te adjunte.

### 0. Identificación del proyecto

- **Módulo profesional**: 1665 — Digitalización aplicada a los sectores productivos (Grado Superior).
- **Ciclo formativo**: Técnico Superior en Administración de Sistemas Informáticos en Red (ASIR).
- **Curso**: 2º ASIR (confírmame si en tu centro la secuenciación oficial lo ubica en 1º o 2º curso, porque en la secuenciación estatal de referencia este módulo aparece encuadrado en 1º; quiero que la programación final refleje la secuenciación real de mi centro y horario).
- **Duración**: 30 horas · 3 créditos ECTS (currículo básico estatal).
- **Comunidad autónoma**: Comunitat Valenciana.
- **Carpeta raíz del proyecto**: `/home/jmperez/Documentos/digi-asir/`.
- **Idioma**: español (es-ES).
- **Licencia del contenido**: CC BY-NC-SA 4.0.
- **Despliegue web**: repositorio GitHub Pages con MkDocs (Material for MkDocs), pensado desde el principio para publicarse online, no solo en local.
- **Objetivo general**: generar desde cero, en sesiones independientes y verificables: (1) marco normativo y currículo, (2) programación didáctica, (3) web MkDocs con teoría/ejercicios/talleres/prácticas por unidad, (4) especificación y (si procede) migración de un curso Moodle existente, (5) informe final de mejoras.

### 1. Marco normativo a localizar, descargar y citar

Busca, descarga en PDF a `fuentes/` y fichas en `FUENTES.md` (ficha por norma: referencia oficial, URL, fecha, uso, fichero local), como mínimo:

- **RD 659/2023**, de 18 de julio, por el que se desarrolla la ordenación del Sistema de Formación Profesional (contiene el currículo básico del módulo 1665: resultados de aprendizaje y criterios de evaluación, Anexo correspondiente).
- **RD 1629/2009**, de 30 de octubre (título ASIR y enseñanzas mínimas) — o el RD de adaptación vigente del título ASIR a la LO 3/2022 si ya existe; verifica cuál es el aplicable a 2º curso en 26-27.
- **Decreto 114/2025**, de 29 de julio, del Consell (DOGV 2025/29742, 4/8/2025), por el que se establecen los currículos de los ciclos formativos de grado medio y de grado superior de FP en aplicación de la LO 3/2022 — currículo autonómico de la Comunitat Valenciana para ASIR, incluido el módulo 1665. Revisa si hay corrección de errores posterior.
- **Ley Orgánica 3/2022**, de 31 de marzo, de ordenación e integración de la Formación Profesional (marco general).
- **Orden 8/2025**, de 29 de abril (DOGV 2025/13083), de evaluación del alumnado LFP en la Comunitat Valenciana, y su modificación por **Orden 5/2026** — normativa de evaluación vigente para 26-27 (criterios de superación, evaluación continua, parciales, recuperación, convocatorias).
- **Instrucciones de organización y funcionamiento** de los centros que imparten grados de FP para el curso 2026-2027 (Resolución de la Secretaría Autonómica de Educación, DOGV).
- Cualquier norma complementaria de digitalización/transformación digital, ciberseguridad básica o sostenibilidad digital que el currículo básico remita como contenido transversal.

Antes de cerrar esta fase, resume en un cuadro: norma, referencia oficial, fecha, qué aporta al proyecto (igual que hiciste en el ejemplo con la tabla de "Marco normativo" del PLAN.md).

### 2. Estructura del proyecto (calco adaptado del proyecto de referencia)

```
digi_asir/
├── PLAN.md            # plan maestro recuperable entre sesiones
├── AGENTS.md          # estado del plan, historial de decisiones, convenciones, mapa de ficheros, pendientes
├── FUENTES.md         # fichas de todas las fuentes (legislación + técnicas)
├── README.md · .gitignore · requirements.txt · serve.sh
├── mkdocs.yml · hooks.py · js/
├── fuentes/           # PDFs oficiales descargados
├── legislacion/       # temas legales analizados + programación didáctica
├── docs/              # web MkDocs (contenido para el alumnado)
│   ├── index.md
│   ├── normativa/
│   ├── sobremi.md
│   ├── UD00/ … UDxx/  # una carpeta por unidad didáctica
│   └── practicas/UDxx/*.ipynb
├── practicas/         # requirements de prácticas, material sin renderizar
├── moodle/
│   ├── spec/          # estructura del curso, actividades, rúbricas, pruebas
│   ├── export/        # contenido descargado/escaneado de mi Moodle real (ver §6)
│   └── scripts/       # scripts de generación/migración .mbz si procede
├── .github/workflows/ # despliegue automático a GitHub Pages
└── PROPUESTAS_MEJORA.md
```

### 3. Decisiones de diseño que debes respetar desde el inicio

1. **Evaluación por resultados de aprendizaje (RA)**: usa los RA y criterios de evaluación oficiales del currículo básico del módulo 1665 (RD 659/2023). Indícame cuántos RA tiene exactamente tras consultar la fuente y créalos como tabla de referencia en `PLAN.md`.
2. **Ponderación de la nota**: propónmela por defecto como 40% actividades/prácticas + 60% prueba escrita por RA, y **cada RA debe alcanzar ≥5** para superar el módulo — pero pregúntame si mi centro tiene un criterio distinto fijado en su programación (como ocurrió en el proyecto de referencia con la Orden 8/2025 vs. el criterio propio del centro) antes de blindarlo por escrito.
3. **Estructura didáctica por unidades (UDxx)**: nomenclatura homogénea `UD00, UD01, UD02...`, con UD00 dedicada a presentación del módulo + entorno de trabajo (herramientas digitales, entorno colaborativo, etc.). Reparte las 30 horas totales en las UD que resulten de los bloques de contenido oficiales; muéstrame el reparto propuesto en horas y semanas antes de continuar.
4. **Web MkDocs**: tema Material, plugins al estilo del proyecto de referencia (`git-revision-date-localized`, `minify`, mermaid, MathJax si hace falta, `mkdocs-jupyter` para notebooks). Configura `mkdocs.yml` con `site_url` ya apuntando a la futura URL de GitHub Pages (`https://github.com/jmperez-profesor/digi-asir`).
5. **GitHub Pages desde el principio**: crea también el workflow de GitHub Actions (`.github/workflows/deploy.yml`) para construir y publicar automáticamente el sitio MkDocs en cada push a `main`, y documenta en `README.md` los pasos manuales que debo hacer yo en GitHub (crear repo, activar Pages, permisos del workflow).
6. **Notebooks/prácticas**: si el módulo incluye contenido práctico con herramientas digitales (hojas de cálculo, automatización, IA generativa, ciberseguridad básica, etc.), usa notebooks Jupyter en español dentro de `docs/practicas/UDxx/` para que se rendericen en la web, con botones de descarga y apertura en Colab.
7. **Idioma y licencia**: todo en español (es-ES); licencia CC BY-NC-SA 4.0 visible en portada y en `FUENTES.md`.
8. **No usar contenido previo mío**: no busques ni reutilices materiales antiguos que yo tenga fuera de esta carpeta; todo el contenido nuevo se apoya en fuentes oficiales y en lo que decidamos juntos sesión a sesión.

### 4. Trabajo por sesiones (como en el proyecto de referencia)

No generes todo el proyecto en una sola respuesta. Divide el trabajo en sesiones numeradas (S1, S2, S3…), cada una con entregables y una verificación concreta antes de pasar a la siguiente. Propuesta de plan de sesiones (ajústala tras revisar el currículo real):

| Sesión | Contenido | Entregables | Verificación |
|---|---|---|---|
| S1 | Scaffolding + marco normativo | Estructura de carpetas, git init, README, PLAN.md, AGENTS.md, venv MkDocs, PDFs en `fuentes/`, `FUENTES.md`, `legislacion/` | PDFs válidos, URLs con 200, commit inicial |
| S2 | Programación didáctica | RA-CE → UD, temporalización semanal, metodología, criterios de evaluación, plantilla de UD, mapa de cobertura | Revisión mía |
| S3 | Esqueleto MkDocs + GitHub Pages | `mkdocs.yml`, sección `normativa/`, `index.md`, CSS, workflow de Actions | `mkdocs build`/`serve` OK; despliegue de prueba en Pages |
| S4...Sn | Una sesión por UD (teoría + ejercicios + talleres + notebooks si aplica) | Contenido de cada UD | Checklist RA/CE por unidad |
| S(n+1) | Banco de pruebas escritas | Pruebas con soluciones, cobertura de todos los CE | Cobertura completa |
| S(n+2) | Especificación Moodle (ver §6) | Estructura de curso, actividades, rúbricas | Revisión mía |
| S(n+3) | QA final + mejoras | Auditoría de enlaces, build limpio, `PROPUESTAS_MEJORA.md` | Build limpio + informe |

Al final de cada sesión, actualiza `AGENTS.md` con: estado del plan (tabla con ✅/🔵/⬜/⚠️), avance detallado de la sesión, decisiones tomadas, y qué queda pendiente para la sesión siguiente — igual que en el ejemplo que te adjunto.

### 5. Convenciones de trabajo

- Nomenclatura `UDXX` (dos dígitos), ficheros `UDXX_*.md`, notebooks en `docs/practicas/UDXX/*.ipynb`.
- No añadas comentarios superfluos al código salvo que se pida explícitamente.
- Cada sesión termina con `mkdocs build` sin errores y commit de git con mensaje descriptivo.
- Si detectas un hallazgo normativo relevante (norma derogada, contradicción, artículo aplicable), documéntalo en el "Historial de decisiones" de `AGENTS.md`, igual que se hizo con la Orden 8/2025 vs. Orden 79/2010 en el proyecto de referencia.
- Pregúntame explícitamente cuando falte un dato que solo yo puedo aportar (nombre del centro, código de centro, horario real, criterios propios de evaluación, plataforma de Colab/GitHub, etc.) en lugar de inventarlo.

### 6. Acceso y tratamiento de mi curso Moodle

Quiero darte acceso a mi curso Moodle real para que lo "escanees" y extraigas su contenido como insumo (no como copia literal, sino como referencia de qué llevo dando y qué actividades ya tengo). Antes de intentarlo, ten en cuenta:

- opencode **no tiene conector nativo a Moodle**; el acceso deberá hacerse vía **API REST de Moodle** (token de servicio web) o mediante una **exportación manual del curso** (backup `.mbz` o exportación de actividades) que yo te proporcione como fichero.
- Pídeme explícitamente: URL de mi Moodle, si tengo generado un token de servicio web REST habilitado por el administrador, o si prefiero exportar yo mismo el backup `.mbz` del curso y dejarlo en `moodle/export/`.
- Con ese contenido, genera en `moodle/spec/` un inventario del curso actual (secciones, actividades, tipos de recurso, rúbricas existentes) como documento de partida, y compáralo con la programación didáctica nueva que estás construyendo, señalándome huecos o contenido redundante.
- No sobrescribas ni modifiques el curso Moodle real sin mi confirmación explícita en cada acción.

### 7. Primer paso que debes dar tú, opencode

1. Confirma que entiendes el objetivo y el patrón de trabajo (revisa los 4 ficheros de ejemplo adjuntos: AGENTS.md, PLAN.md, README.md, FUENTES.md).
2. Pregúntame los datos que te faltan de la sección 0 (carpeta raíz, curso exacto, centro, docente).
3. Propón el plan de sesiones definitivo (tabla como la de la sección 4) para que lo apruebe antes de tocar ningún fichero.
4. Solo tras mi aprobación, inicia la Sesión 1.
