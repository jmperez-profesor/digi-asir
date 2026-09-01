# Análisis de Brechas (Gap Analysis) — Moodle vs Nuevo Currículo (1665)

Este documento analiza las diferencias entre los materiales previos o tradicionales de Moodle y las exigencias del nuevo currículo básico (RD 659/2023) para el módulo **1665 — Digitalización aplicada a los sectores productivos** en 2º de ASIR.

---

## 1. Identificación de Brechas (Gaps)

| Área de Análisis | Contenido Tradicional / Moodle Antiguo | Exigencia Nuevo Currículo (RD 659/2023) | Brecha Detectada | Acción de Mitigación Propuesta |
|---|---|---|---|---|
| **Enfoque Tecnológico** | Enfoque genérico de ofimática y uso básico de Internet. | Enfoque técnico específico para administración de sistemas (IaaS, Cloud, contenedores). | Brecha de nivel y especialización técnica. | Reorientar los talleres hacia la automatización de sistemas y virtualización (UD01 y UD03). |
| **Ciberseguridad** | Conceptos básicos de contraseñas y antivirus de usuario. | Hardening de servidores, cumplimiento normativo (ENS, RGPD) y análisis de vulnerabilidades. | Falta de profundidad en bastionado de sistemas. | Incorporar prácticas específicas con herramientas de escaneo y cortafuegos (UD02). |
| **Inteligencia Artificial** | No contemplada en temarios anteriores. | Uso de herramientas de IA aplicada, análisis predictivo de logs y scripting automatizado. | Ausencia total de contenidos de IA en sistemas. | Desarrollar cuadernos Jupyter interactivos (`.ipynb`) para análisis de logs (UD03). |
| **Sostenibilidad** | Contenido ambiental generalista sin métricas TIC. | Green Computing, eficiencia energética en centros de datos y cálculo de métricas PUE. | Desconexión con la eficiencia en CPDs. | Integrar teoría específica sobre PUE y casos prácticos de optimización energética (UD04). |

---

## 2. Conclusiones y Plan de Alineación
Para alinear el curso Moodle con los estándares actuales:
1. Reestructurar las actividades prácticas utilizando la plataforma web MkDocs como fuente de teoría actualizada.
2. Habilitar entregas de prácticas mediante cuadernos Jupyter e informes técnicos en Markdown.
3. Asegurar que cada Resultado de Aprendizaje cuente con su correspondiente instrumento de evaluación verificado.
