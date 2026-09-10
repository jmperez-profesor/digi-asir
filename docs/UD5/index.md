# UD5: Big Data y Ciclo de Vida del Dato (RA5 · 3 h)

> **Resultado de aprendizaje**: evaluar la importancia de los datos y su protección en una economía digital (CE RA5.a–h en esta UD; el CE RA5.i —seguridad y regulación— corresponde a la UD6). Ponderación del RA5: **14 %** (80 % actividades + 20 % cuestionario). Enfoque: **el dato como activo que el administrador captura, guarda, sirve y destruye**.

## 1. Dato ≠ información ≠ conocimiento (CE RA5.a)

- **Dato**: hecho bruto sin contexto. `23.4`, `2026-11-02T03:14`, `192.168.1.40`.
- **Información**: dato + contexto que responde una pregunta. «La cámara 3 marcó 23,4 °C a las 3:14».
- **Conocimiento**: información + experiencia que permite decidir. «Con ese patrón, la cámara fallará en dos semanas: programa el mantenimiento».

El trabajo del ASIR está en los dos primeros escalones: que el dato **exista, esté íntegro y llegue** a quien lo convierte en decisiones.

## 2. El ciclo de vida del dato (CE RA5.b)

Todo dato recorre siete fases; en cada una hay una responsabilidad de sistemas:

| Fase | En qué consiste | Tarea típica del ASIR |
|---|---|---|
| **1. Generación** | Sensores, aplicaciones, logs, formularios | Asegurar la captura (agentes, MQTT, syslog) y el reloj sincronizado (NTP: sin hora común no hay correlación) |
| **2. Almacenamiento** | Guardar de forma fiable y localizable | Elegir motor (PostgreSQL, InfluxDB), dimensionar discos, cifrar en reposo |
| **3. Tratamiento** | Limpiar, normalizar, transformar (ETL) | Automatizar pipelines con scripts y programarlos (cron/systemd timers) |
| **4. Análisis** | Extraer patrones (estadística, ML) | Proveer entornos y accesos con permisos mínimos |
| **5. Compartición y visualización** | Paneles e informes para decidir | Desplegar Grafana/Metabase con autenticación y HTTPS |
| **6. Uso** | Explotación en el negocio | Controlar quién accede a qué (RBAC) y auditarlo |
| **7. Eliminación** | Borrado seguro al expirar su vida útil | Políticas de retención + borrado certificado (RGPD: lo veremos en la UD6) |

!!! example "Logs de un servidor web"
    Generación (Nginx escribe access.log) → almacenamiento (rotación con logrotate, 90 días) → tratamiento (script que parsea a CSV) → análisis (top IPs con error 403: ¿ataque?) → visualización (panel semanal) → uso (bloquear la IP en el cortafuegos) → eliminación (borrado tras un año). Siete fases, un solo fichero.

## 3. Big Data: cuando «mucho» cambia las reglas (CE RA5.c–d)

**Big Data** = conjuntos tan grandes, rápidos o variados que las herramientas tradicionales no los procesan. Se resume en las **V**:

- **Volumen**: terabytes que no caben en un disco (replicas, clústeres).
- **Velocidad**: miles de eventos/segundo (hay que decidir en streaming, no en diferido).
- **Variedad**: tablas, JSON, imágenes, texto libre.
- **Veracidad**: sensores que mienten y logs corruptos; validar es obligatorio.
- **Valor**: si nadie lo convierte en decisiones, es coste eléctrico.

Relación con IA/ML (CE RA5.c): el *machine/deep learning* son las técnicas que extraen patrones de esos volúmenes; la IA es el consumidor final del dato bien gobernado. Sin ciclo de vida sano, no hay IA que valga.

## 4. Ciencia de datos y almacenamiento (CE RA5.e–h)

Etapas típicas de un proyecto de datos: **definir la pregunta → capturar → limpiar → modelar → validar → desplegar → vigilar**. El ASIR sostiene las piezas subrayadas: captura, almacenamiento, despliegue del modelo y vigilancia de que sigue funcionando (deriva).

**Almacenaje en cloud/nube** (CE RA5.f–g): buckets S3-compatibles para histórico barato, bases gestionadas (DBaaS) para no operar el motor, y regla de oro: **el cloud no exime de copias ni de cifrado** —relee la UD3—.

**Objetivos de la ciencia de datos en la empresa** (CE RA5.h): describir lo pasado (informes), predecir (demanda, fallos), prescribir (qué hacer) y automatizar la decisión cuando el riesgo lo permite.

!!! warning "El dato también pesa"
    Guardarlo todo «por si acaso» cuesta discos, copias, energía y riesgo legal. Define retención con el negocio: qué se guarda, cuánto tiempo y cuándo se destruye. El mejor dato es el necesario.

## 5. Para practicar

- [Prácticas UD5](../practicas/UD5/index.md): pipeline completo con un log real (captura → panel → decisión).
- **Glosario mínimo (CE a–h)**: dato, información, conocimiento, ciclo de vida, ETL, Big Data, 5 V, serie temporal, data warehouse/lake, retención, RBAC.
- **Autoevaluación**: dibuja el ciclo de vida de *un* dato de tu centro (p. ej., un parte de incidencia) indicando en cada fase la herramienta y el riesgo si falla.
