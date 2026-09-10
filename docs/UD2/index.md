# UD2: Tecnologías Habilitadoras Digitales (RA2 · 5 h)

> **Resultado de aprendizaje**: caracterizar las THD necesarias para transformar empresas en entornos digitales, describiendo características y aplicaciones (CE RA2.a–g). Ponderación del RA2: **14 %** (80 % actividades + 20 % cuestionario). Enfoque: **qué debe desplegar, integrar y mantener el administrador de sistemas**.

## 1. Qué son las THD y por qué mandan en 2026

Las **tecnologías habilitadoras digitales (THD)** son el conjunto de herramientas —conectividad, datos, automatización, inteligencia— que hacen posible la transformación digital. Sin ellas no hay tienda online, ni mantenimiento predictivo, ni teletrabajo: son la infraestructura sobre la que se construye todo lo demás.

Características comunes (CE RA2.a):

- **Adaptables y escalables**: sirven a un autónomo y a una multinacional (del VPS de 6 €/mes al clúster Kubernetes).
- **Interconectadas**: hablan entre sí mediante APIs y protocolos estándar (MQTT, REST, SNMP).
- **Automatizadoras**: eliminan tareas repetitivas y reducen el error humano.
- **Generadoras de datos**: todo deja rastro medible, la materia prima de las decisiones.
- **Centradas en las personas**: si la herramienta no la usa nadie, es dinero tirado.

!!! tip "Criterio sysadmin"
    Ante cada THD pregúntate siempre lo mismo: ¿quién la administra, dónde se ejecuta, cómo se copia y cómo se protege? La tecnología que no puedas mantener no la despliegues.

## 2. El mapa THD que debe dominar un ASIR (CE RA2.a)

### 2.1. Conectividad y comunicación inteligente

- **5G y redes privadas**: latencia de milisegundos para robots, cámaras y flotas. En 2026 proliferan las redes privadas 5G en polígonos y puertos.
- **IoT**: sensores y actuadores conectados. Para el sysadmin se traducen en: broker **MQTT** (Mosquitto), segmentación de red para dispositivos y gestión de certificados.
- **Fibra + WiFi 6/7 + VPN**: la base sobre la que viaja todo lo demás.

!!! example "Caso: nave logística"
    200 sensores de temperatura y puertas publicando por MQTT a un broker en un mini-PC, que vuelca a una base de datos temporal y un Grafana. Coste de infraestructura: cientos de euros. Valor: alertas antes de que se rompa la cadena de frío.

### 2.2. Gestión avanzada de datos

- **Big Data y analítica**: recoger mucho, quedarse con lo útil (agregación, retención, cuadros de mando).
- **Bases de datos modernas**: relacionales para el negocio (PostgreSQL), series temporales para sensores (InfluxDB).
- **Blockchain**: registro distribuido e inmutable para trazabilidad (lotes alimentarios, certificados). Úsalo donde la confianza entre partes sea el problema; para todo lo demás, una base de datos basta.

### 2.3. Fabricación avanzada

- **Robótica colaborativa (cobots)**: brazos que trabajan junto a personas; se programan y supervisan por red.
- **Impresión 3D / fabricación aditiva**: piezas bajo demanda, menos stock y menos desperdicio.
- **Automatización (PLC/SCADA)**: el mundo OT que el ASIR debe saber segmentar y monitorizar sin pararlo.

### 2.4. Tecnologías inmersivas

- **Realidad aumentada (RA)**: instrucciones superpuestas sobre la máquina para el técnico de campo.
- **Realidad virtual (RV)**: formación de operarios sin riesgo ni paradas.
- Para sistemas: son clientes exigentes de red (ancho de banda, latencia) y de almacenamiento.

> La **IA** y la **ciberseguridad** también son THD, pero tienen unidad propia (UD4 y UD6): aquí basta saber que las atraviesan todas.

## 3. Las THD crean valor dentro y fuera (CE RA2.b–f)

**Valor interno** (planta + oficinas):

- Automatización de tareas y reducción de costes.
- Convergencia IT/OT: mismos datos para el operario y el gerente.
- Decisiones basadas en datos en vez de intuiciones.

**Valor externo** (clientes y mercado):

- **Productos**: personalización masiva (recomendadores), prototipado digital antes de fabricar, productos conectados (el reloj que mide tu pulso).
- **Servicios**: bajo demanda (plataformas), por suscripción en vez de compra única, servicios conectados que se ajustan solos.
- **Mercados nuevos**: economía del dato, espacios virtuales, criptoactivos y, sobre todo, mercados globales sin barrera geográfica para quien tenga infraestructura.

!!! example "De vender cajas a vender suscripción"
    Un proveedor de copias de seguridad local reconvierte su negocio: en vez de vender NAS, ofrece «copia gestionada» mensual (hardware + monitorización + restauración garantizada). Misma tecnología, modelo distinto, ingresos recurrentes. Eso es innovar en servicios con THD.

## 4. THD y economía sostenible (CE RA2.c)

Las THD optimizan recursos: riego que solo se activa con el suelo seco (ahorro de agua), rutas de reparto calculadas con tráfico real (menos combustible), impresión 3D que usa solo el material necesario, parques eólicos que orientan sus palas con IA. Economía circular incluida: rastrear prendas para reciclarlas, alargar la vida del hardware con mantenimiento predictivo.

!!! warning "La otra cara"
    Digitalizar también contamina: fabricar dispositivos consume recursos escasos, los centros de datos devoran electricidad y agua, y la **obsolescencia programada** genera residuos electrónicos. El ASIR sostenible: consolida servidores (virtualización), alarga la vida útil del hardware, ajusta la climatización del CPD y exige eficiencia energética (PUE) a sus proveedores. Lo veremos a fondo en la UD4/UD5… y en tu factura eléctrica.

## 5. Mejoras en IT y OT + informe (CE RA2.f–g)

Recapitulando el impacto por entorno:

| Entorno | Mejora típica por las THD | Ejemplo |
|---|---|---|
| **IT (negocio)** | Procesos unificados, dato único, trabajo remoto | ERP + VPN + copias externas: la empresa sigue operando desde cualquier sitio |
| **OT (planta)** | Control en tiempo real, menos paradas | Sensores + SCADA con avisos al móvil del encargado |
| **IT+OT juntos** | Visión completa del negocio | El gerente ve en un panel producción, stock y ventas a la vez |

**Informe de la unidad (CE RA2.g)**: elabora el cuadro THD → características → áreas de aplicación con un ejemplo real por tecnología (puede ser de tu entorno: centro, empresa de prácticas, proveedor local). Tienes la plantilla y los criterios en [Prácticas UD2](../practicas/UD2/index.md).

## 6. Para practicar

- **Glosario mínimo del RA2**: THD, 5G, IoT, MQTT, Big Data, blockchain, cobot, gemelo digital, RA/RV, Industria 4.0/5.0, economía circular, obsolescencia programada, PUE.
- **Autoevaluación**: elige una THD y explica (1) qué problema resuelve, (2) qué infraestructura necesita un ASIR para sostenerla y (3) qué riesgo introduce si se despliega mal.
