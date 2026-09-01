# Banco de Pruebas Escritas y Soluciones — Módulo 1665

Este documento recopila las pruebas de evaluación escritas asociadas a cada Resultado de Aprendizaje (RA) del módulo **1665 — Digitalización aplicada a los sectores productivos** (2º ASIR), junto con sus criterios de corrección y soluciones detalladas.

---

## Prueba de Evaluación — RA1: Transformación Digital (UD01)

### Enunciado
1. **(2.5 puntos)** Explique qué es una Tecnología Habilitadora Digital (THD) y cite tres ejemplos prácticos aplicados a la administración de sistemas en red.
2. **(2.5 puntos)** Describa las diferencias principales entre una infraestructura local (*on-premise*) y una arquitectura híbrida en la nube (*cloud computing*).
3. **(5.0 puntos)** Caso práctico: Una empresa de logística tradicional desea migrar sus servidores de bases de datos locales a un entorno virtualizado en la nube para evitar caídas estacionales. Razone los pasos críticos que debe seguir el administrador de sistemas para garantizar la continuidad operativa.

### Solución y Criterios de Corrección
- **Pregunta 1**: Definición correcta de THD (tecnologías que transforman los modelos productivos). Ejemplos: Computación en la nube, contenedorización (Docker/Kubernetes), Big Data / Analítica de logs.
- **Pregunta 2**: Comparativa clara en costes (CAPEX vs OPEX), escalabilidad, mantenimiento físico y seguridad perimetral.
- **Pregunta 3**: Evaluación de la planificación de migración, respaldo previo (backup), pruebas de estrés, estrategia de DNS/red y monitorización post-migración.

---

## Prueba de Evaluación — RA2: Ciberseguridad y Privacidad (UD02)

### Enunciado
1. **(3.0 puntos)** Defina el concepto de *hardening* (endurecimiento) de sistemas y enumere tres buenas prácticas aplicables en servidores Linux de producción.
2. **(3.0 puntos)** ¿Qué relación existe entre el principio de mínimo privilegio y la reducción de la superficie de ataque? Razone la respuesta.
3. **(4.0 puntos)** Explique brevemente los objetivos principales del Esquema Nacional de Seguridad (ENS) y su importancia en la administración pública y sectores estratégicos.

### Solución y Criterios de Corrección
- **Pregunta 1**: Definición de bastionado/endurecimiento. Buenas prácticas: cerrar puertos innecesarios, desactivar cuentas por defecto/root por SSH, aplicar parches de seguridad periódicos.
- **Pregunta 2**: Explicación de cómo limitar permisos reduce el impacto potencial si una cuenta o servicio es comprometido.
- **Pregunta 3**: Propósito del ENS (crear condiciones de seguridad en el uso de medios electrónicos). Principios básicos: seguridad como proceso integral, gestión de riesgos, proporcionalidad.

---

## Prueba de Evaluación — RA3: Automatización e Inteligencia Artificial (UD03)

### Enunciado
1. **(4.0 puntos)** Describa cómo el uso de cuadernos Jupyter (`.ipynb`) y lenguajes de scripting (Python) facilita las tareas rutinarias de un administrador de sistemas.
2. **(6.0 puntos)** Caso práctico: Se requiere analizar un fichero de registros de acceso web (`access.log`) para detectar IPs con alta tasa de códigos de error HTTP 403 (prohibido). Explique la lógica del script o utilice pseudo-código / funciones con `pandas` para resolverlo.

### Solución y Criterios de Corrección
- **Pregunta 1**: Ventajas de la automatización (reducción de errores humanos, rapidez, reproducibilidad) y utilidad de los notebooks para experimentación y documentación interactiva.
- **Pregunta 2**: Carga del fichero, filtrado de columnas (`status == 403`), agrupación por IP (`groupby('ip')`) y conteo de ocurrencias.

---

## Prueba de Evaluación — RA4: Sostenibilidad Digital (UD04)

### Enunciado
1. **(4.0 puntos)** ¿Qué mide la métrica PUE (*Power Usage Effectiveness*) en un centro de datos y cuál es el valor ideal teórico?
2. **(6.0 puntos)** Calcule el PUE de un CPD que consume un total de 400 kW de potencia eléctrica general, sabiendo que los servidores y equipos de almacenamiento IT consumen 250 kW. Analice el resultado obtenido y proponga dos medidas de mejora energética.

### Solución y Criterios de Corrección
- **Pregunta 1**: Definición de PUE (ratio entre energía total y energía IT). Valor ideal: 1.0.
- **Pregunta 2**: Cálculo: $\text{PUE} = 400 / 250 = 1.6$. Análisis: indica que por cada vatio dedicado a computación, se gastan 0.6 vatios en refrigeración/pérdidas. Medidas: optimización de climatización, pasillos fríos/calientes, consolidación de servidores.
