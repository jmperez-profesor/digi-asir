# UD7: Proyecto de Transformación Digital (RA6 · 7 h)

> **Resultado de aprendizaje**: desarrollar un proyecto de transformación digital de una empresa del sector, según sus objetivos (CE RA6.a–k). Ponderación del RA6: **30 %** —el mayor peso del módulo— (80 % actividades + 20 % cuestionario). Enfoque: **memoria técnica que integra UD1–UD6 y alimenta el proyecto intermodular** (aporta RA6.d,f,i,j).

## 1. Qué vas a entregar: la memoria integradora

No es un examen: es el **informe profesional** que un técnico entregaría a la dirección de una empresa (real o ficticia) tras analizarla. Debe demostrar que sabes diagnosticar, priorizar, diseñar la solución, estimar recursos y documentarlo todo. Recoge contenidos de todas las unidades:

| Apartado de la memoria | CE | Unidad que aporta |
|---|---|---|
| Objetivos estratégicos y áreas (producción, negocio, comunicaciones) | a, b | UD1 |
| Áreas digitalizables y encaje con las no digitalizadas | c, d | UD1 + UD2 |
| Necesidades presentes y futuras | e | UD1–UD4 |
| Tecnologías por área (cloud, IA, datos…) | f | UD2, UD3, UD4 |
| Brechas de seguridad por área | g | UD6 |
| Tratamiento y análisis de datos | h | UD5 |
| Integración datos–aplicaciones–plataformas | i | UD3 + UD5 |
| Cambios documentados según la estrategia | j | Transversal |
| Recursos humanos e idoneidad/formación | k | UD1 (cultura) |

## 2. Método en 5 fases

### Fase 1 — Diagnóstico (CE a, b, c)
Inventaría la empresa: qué hace, con qué sistemas trabaja hoy, dónde duele (pedidos a mano, sin copias, sin web). Herramientas: entrevista al «cliente», checklist IT/OT de la UD1 y matriz DAFO de una página.

### Fase 2 — Objetivos y priorización (CE a, e)
Define 2–3 objetivos medibles («reducir a cero las pérdidas por frío», «vender online en 3 meses») y ordénalos por impacto/esfuerzo. Todo lo que propongas debe colgar de un objetivo: sin objetivo no hay proyecto, hay compra de juguetes.

### Fase 3 — Diseño técnico (CE d, f, h, i)
Para cada área: tecnología elegida y por qué, encaje con lo existente, datos que genera y dónde viven, e integración entre piezas. Dibuja la arquitectura en una página (red, servidores, nube, borde).

!!! example "Fragmento de diseño (asesoría, 12 personas)"
    «Servidor local virtualizado (Proxmox) para el programa de nóminas + Nextcloud en VPS para ficheros (CE f,i) + VPN WireGuard y MFA (CE g) + copias 3-2-1 con una externa cifrada (CE h). Coste: ~60 €/mes + 1.200 € de implantación. Plazo: 6 semanas.» Concreto, presupuestado y defendible.

### Fase 4 — Seguridad y personas (CE g, k)
Brecha por área + mitigación, y plan de formación/roles: quién opera cada sistema y qué debe aprender. La mejor arquitectura fracasa si nadie sabe usarla.

### Fase 5 — Roadmap y documentación (CE e, j, k)
Fases con hitos y fechas, costes (implantación + recurrente), riesgos y plan B. Cierra con el resumen ejecutivo de una página: qué, cuánto, cuándo y qué gana la empresa.

## 3. Proyecto intermodular

Esta UD aporta al módulo de proyecto intermodular los CE **RA6.d** (encaje de áreas), **RA6.f** (tecnologías por área), **RA6.i** (integración datos/apps/plataformas) y **RA6.j** (documentación de cambios). Coordina con tu equipo: tu memoria es la parte de infraestructura y datos del proyecto común (F01.PC02 §5.2).

## 4. Criterios de calidad de la memoria

- Cada propuesta cuelga de un objetivo y lleva coste + plazo.
- Nada de «soluciones mágicas»: toda tecnología va con su administración (copias, accesos, monitorización).
- Lenguaje profesional, diagramas propios y fuentes citadas (incluida esta web y la normativa: RGPD, ENS, NIS2 donde aplique).
- Extensión orientativa: 8–12 páginas + anexos (presupuesto, diagramas, cronograma).

## 5. Para practicar

- [Prácticas UD7](../practicas/UD7/index.md): plantilla de memoria y lista de verificación por CE.
- **Autoevaluación**: coge tu memoria y subraya dónde aparece cada CE de la **a** a la **k**. Si alguno no aparece, la memoria está incompleta.
