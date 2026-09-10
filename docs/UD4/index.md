# UD4: Inteligencia Artificial (RA4 · 5 h)

> **Resultado de aprendizaje**: identificar aplicaciones de la IA en el sector ASIR describiendo las mejoras de su implantación (CE RA4.a–f). Ponderación del RA4: **14 %** (80 % actividades + 20 % cuestionario). Enfoque: **la IA como herramienta del administrador y como carga de trabajo que debe operar**.

## 1. La IA en la automatización y optimización (CE RA4.a)

La IA rinde donde hay **volumen y repetición**: clasificar miles de eventos de log, priorizar alertas, predecir qué disco va a fallar, responder lo de siempre a los usuarios. No sustituye al criterio del técnico; le quita el trabajo mecánico para dejarle el que exige juicio.

!!! example "Del mar de alertas a 5 avisos útiles"
    Un Zabbix sin afinar genera 300 alertas/semana que nadie mira. Un modelo de detección de anomalías sobre esas series aprende el patrón normal (copias nocturnas, picos de facturación) y solo avisa de lo raro: el backup que duró el triple o el tráfico saliente a las 4:00. Mismo sistema, décima parte de ruido.

## 2. IA + Big Data = rentabilidad (CE RA4.b)

Sin datos no hay IA, y sin análisis los datos son lastre. El ciclo que debe montar el ASIR:

```
captura (logs, sensores, tickets) → almacena (BBDD, series temporales) → procesa (pipelines) → modela → actúa (alerta, informe, automatismo)
```

Cada fase es infraestructura: retención y copias de los datasets, permisos de acceso, entornos de entrenamiento. La rentabilidad aparece cuando el modelo evita una parada, un fraude o una mala compra de stock.

## 3. Presente y futuro: qué está pasando en 2026 (CE RA4.c–d)

- **IA generativa integrada** en ofimática, programación y atención al cliente (asistentes que redactan, resumen y responden).
- **Visión artificial** en industria y comercio (control de calidad, conteo, seguridad).
- **Mantenimiento predictivo** y optimización energética como casos con retorno medible.
- Sectores con implantación más intensa: banca (fraude), salud (diagnóstico por imagen), logística (rutas), industria (calidad y energía) y **operaciones IT** (AIOps: el nuestro).

!!! tip "Hype vs. realidad"
    Si un comercial dice «IA» y el producto es un formulario con tres reglas fijas, es marketing. Pregunta siempre: ¿qué modelo? ¿entrenado con qué datos? ¿cómo se evalúa y quién lo reentrena? Ese escepticismo técnico es empleabilidad.

## 4. Lenguajes y piezas que debes reconocer (CE RA4.e)

- **Python**: el idioma franco de la IA (scikit-learn, pandas, PyTorch). No hace falta ser científico de datos, pero sí leer un script y ejecutarlo.
- **SQL**: el dato vive en bases de datos; quien no consulta, no analiza.
- **Bash + API REST**: pegar modelos con el resto de la infraestructura (un script que llama al modelo y actúa).
- **R y Julia**: nichos estadísticos; conócelos de nombre.

## 5. La IA en el sector ASIR: operar IA (CE RA4.f)

Doble papel del administrador:

**a) Usar IA en tu trabajo diario.**

- Asistentes de código para generar scripts, playbooks de Ansible o consultas SQL (revisando siempre el resultado: la IA *inventa* con total seguridad).
- Resumen de incidentes y redacción de informes y documentación.
- Análisis de logs: pedirle patrones y correlaciones antes de bucear a mano.

**b) Operar cargas de IA para otros.**

- **Modelos locales** (Ollama y similares): montar un LLM interno para que los datos de la empresa no salgan a terceros —privacidad por diseño, clave con RGPD—.
- **Dimensionar hardware**: VRAM de GPU, RAM y almacenamiento para modelos; colas y horarios para entrenamientos.
- **Despliegue y ciclo de vida**: versionar modelos como versionas software, monitorizar su deriva (cuando empieza a fallar porque el mundo cambió) y mantener el pipeline de datos que los alimenta.

!!! example "LLM interno en una asesoría"
    En vez de pegar contratos de clientes en un chatbot público, el despacho despliega un modelo local en su servidor con GPU media. Los documentos no salen de la oficina (cumplimiento RGPD), la respuesta es suficiente para resumir y clasificar, y el coste es una inversión única en hardware en lugar de una suscripción por usuario. Decisión típica de arquitectura ASIR:evaluar modelo, hardware, red y copias.

## 6. Riesgos, ética y normas (cierra el RA4)

- **Sesgos**: un modelo entrenado con datos sesgados discrimina (p. ej., filtrados de currículums). Revisar datos y resultados es tarea técnica y ética.
- **Alucinaciones**: la IA genera texto verosímil aunque sea falso. Verificar siempre antes de actuar o publicar.
- **Privacidad**: lo que pegas en un servicio externo deja de ser tuyo. Datos personales → modelos locales o contratos con garantías.
- **Seguridad**: deepfakes, phishing hiperpersonalizado y malware asistido. La IA también ataca: toca defender con IA.
- **Empleo**: automatiza tareas, no profesiones enteras; el perfil que sobrevive es el que sabe dirigir estas herramientas.
- **Normativa**: el **AI Act europeo** clasifica los sistemas por riesgo (mínimo → prohibido: p. ej., vigilancia biométrica masiva) y exige transparencia y supervisión humana. Como administrador, te afectará al desplegar o contratar estos sistemas.

## 7. Para practicar

- [Prácticas UD4](../practicas/UD4/index.md): tarea asistida por IA + análisis comparativo con/sin IA.
- **Glosario mínimo del RA4**: machine/deep learning, entrenamiento/inferencia, modelo, dataset, sesgo, alucinación, LLM, RAG, AIOps, GPU/VRAM, AI Act, supervisión humana.
- **Autoevaluación**: describe un flujo completo «dato → modelo → acción» de tu entorno (centro o prácticas) indicando en cada fase qué infraestructura pondrías tú.
