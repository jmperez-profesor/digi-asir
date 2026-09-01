# Informe de Propuestas de Mejora y QA — Módulo 1665 (ASIR)

Este documento recoge las conclusiones de la auditoría de calidad (QA) y presenta propuestas de mejora continua para futuras iteraciones del proyecto educativo del módulo **1665 — Digitalización aplicada a los sectores productivos** (2º ASIR).

---

## 1. Resumen de Verificación y Calidad (QA)
- **Estructura del Repositorio**: Conforme al estándar establecido (PLAN.md, AGENTS.md, FUENTES.md, README.md, docs/, legislacion/, moodle/, practicas/).
- **Compilación Web (MkDocs)**: Build completado sin errores de sintaxis Markdown ni enlaces rotos en la navegación.
- **Trazabilidad Curricular**: Cobertura del 100% de los Resultados de Aprendizaje (RA1 a RA4) del RD 659/2023 y Decreto 114/2025 de la Comunitat Valenciana.

---

## 2. Propuestas de Mejora Continua

### 2.1. Ampliación de Laboratorios Prácticos
- **Propuesta**: Desarrollar contenedores Docker independientes para cada unidad didáctica que permitan desplegar un entorno de pruebas idéntico en las máquinas del alumnado.
- **Beneficio**: Reduce la fricción en la instalación de herramientas y garantiza la reproducibilidad de los talleres de ciberseguridad y automatización.

### 2.2. Integración con Plataformas de IA Locales
- **Propuesta**: Incorporar guías para la ejecución de modelos de lenguaje de código abierto (como Ollama) en laboratorios locales para demostrar capacidades de IA sin depender de servicios en la nube externos.
- **Beneficio**: Refuerza la privacidad y el cumplimiento normativo en entornos corporativos seguros.

### 2.3. Autoevaluación Interactiva en Moodle
- **Propuesta**: Exportar los cuestionarios del banco de pruebas a formato GIFT o Aiken para importación directa en los cuestionarios de Moodle.
- **Beneficio**: Agiliza la evaluación formativa automática del alumnado.
