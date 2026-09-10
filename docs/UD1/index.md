# UD1: Digitalización en los Sistemas Productivos (RA1 · 5 h)

> **Resultado de aprendizaje**: analizar el concepto de digitalización y su repercusión en los sectores productivos, identificando entornos IT y OT (CE RA1.a–g). Ponderación del RA1: **14 %** (80 % actividades + 20 % cuestionario).

## 1. Digitalización ≠ transformación digital

Los dos términos se confunden a menudo, pero describen realidades distintas:

- **Digitalización**: convertir información y procesos analógicos a formato digital. Escanear albaranes, cobrar con TPV, usar hojas de cálculo en vez de libretas. Es el *primer paso*, táctico y barato.
- **Transformación digital**: rediseñar el modelo de negocio apoyándose en tecnología. No es «hacer lo mismo con ordenadores», sino cambiar *qué* se ofrece y *cómo* se trabaja: vender online en vez de solo en tienda, anticipar la demanda con datos, automatizar la producción.

!!! example "Ejemplo 2026: taller de impresión textil"
    Un taller que solo crea una página web con su catálogo se ha **digitalizado**. El mismo taller, cuando conecta su tienda online con el inventario, automatiza los pedidos a proveedores según el stock y ofrece personalización del producto en la web, se ha **transformado**: vende fuera de su ciudad, reduce errores y conoce qué diseños funcionan antes de imprimirlos.

!!! tip "Contexto 2026 (España)"
    La transformación ya no es opcional: la **factura electrónica** (Ley Crea y Crece + Reglamento VeriFactu) obliga a digitalizar la facturación, los fondos **Kit Digital** financian la adopción en pymes, y la directiva europea **NIS2** eleva las exigencias de ciberseguridad. Digitalizarse es también cumplir la ley.

## 2. Cómo la tecnología cambia la empresa

La implantación digital impacta en cuatro frentes (CE RA1.b):

| Frente | Qué cambia | Ejemplo práctico |
|---|---|---|
| **Estructura organizativa** | Aparecen roles nuevos (administrador de sistemas, analista de datos) y se externaliza lo no estratégico | Una pyme no monta su propio CPD: contrata hosting cloud y un MSP para el soporte |
| **Procesos y operaciones** | Se automatiza lo repetitivo: menos errores, respuesta más rápida | Un ERP confirma pedidos, descuenta stock y genera la factura sin intervención manual |
| **Cultura** | Resistencias al cambio («siempre se hizo así»); hace falta formación y comunicación | Plan de formación de 2 h/semana durante la implantación + un «campeón digital» por departamento |
| **Clientes y mercado** | Nuevos canales (tienda online, reservas web) y datos para personalizar | Sistema de reservas online para una peluquería: menos llamadas, menos ausencias (recordatorios por SMS) |

!!! warning "Riesgos que hay que gestionar"
    Dependencia tecnológica (¿qué pasa si cae el proveedor cloud?), plan de contingencia para procesos críticos y ciberseguridad desde el día uno. Digitalizar sin copias de seguridad ni control de accesos es construir sobre arena.

## 3. Entornos IT y OT (CE RA1.c–d)

Toda empresa digitalizada combina dos mundos tecnológicos:

### 3.1. Entorno IT (*Information Technology*)

Tecnologías que gestionan **información**: servidores, redes, ERP/CRM, correo, desarrollo de software, copias de seguridad. Sus prioridades: confidencialidad, integridad y disponibilidad de los datos.

Departamentos IT típicos en una empresa mediana:

- **Sistemas / infraestructura**: servidores, red, virtualización, copias de seguridad.
- **Desarrollo de software**: aplicaciones internas y web (aquí encaja el perfil DAW).
- **Datos y analítica**: bases de datos, informes, cuadros de mando.
- **Ciberseguridad**: identidades, accesos, respuesta a incidentes.
- **Soporte (*help desk*)**: atención a usuarios internos y clientes.
- **Proyectos e innovación**: migraciones, evaluación de tecnologías emergentes.

!!! note "Pyme pequeña"
    Una empresa de 7 personas no tiene estos departamentos: los **externaliza** (gestoría con su propio software, tienda online mantenida por una agencia, soporte del proveedor). Saber delegar también es administrar sistemas.

### 3.2. Entorno OT (*Operational Technology*)

Tecnología que controla el **mundo físico**: autómatas programables (**PLC**), sistemas de supervisión (**SCADA**), control distribuido (**DCS**), sensores y actuadores. Sus prioridades: seguridad de las personas, continuidad operativa y tiempo real (un retardo de segundos puede parar una línea).

### 3.3. Diferencias clave de un vistazo

| Aspecto | IT | OT |
|---|---|---|
| Gestiona | Datos e información | Máquinas y procesos físicos |
| Fallo típico | Fuga o pérdida de datos | Parada de producción o accidente |
| Ritmo de cambio | Rápido (actualizaciones frecuentes) | Lento (equipos que duran décadas) |
| Prioridad nº 1 | Confidencialidad de la información | Seguridad física y disponibilidad |

## 4. Tecnologías de digitalización en planta y en negocio (CE RA1.e)

### En planta (enfoque operativo)

- **Automatización y control**: PLC + SCADA para gobernar líneas en tiempo real.
- **IoT y sensores**: temperatura, vibración, consumo; datos continuos para mantenimiento predictivo (p. ej., detectar un rodamiento que va a fallar *antes* de que pare la línea).
- **Gemelos digitales**: réplica virtual de una máquina o proceso para simular cambios sin riesgo.
- **Realidad aumentada**: un técnico ve sobre la máquina las instrucciones de reparación con unas gafas o el móvil.

### En negocio (enfoque empresarial)

- **ERP** (p. ej., Odoo, de código abierto): finanzas, inventario, RR. HH. y logística en una sola plataforma.
- **CRM**: historial de clientes para vender y fidelizar mejor.
- **Nube**: almacenamiento y software accesible desde cualquier sitio.
- **Analítica e IA**: prever demanda, detectar fraude, personalizar ofertas.
- **Blockchain**: trazabilidad inmutable (origen de un lote alimentario, por ejemplo).

!!! example "El mismo dato, dos usos"
    El sensor de una cámara frigorífica (OT) evita que se estropee el género; ese mismo dato, agregado en un panel web (IT), permite al gerente comparar el consumo eléctrico de todas sus tiendas y renegociar la tarifa. Ese puente es la convergencia.

## 5. Convergencia IT–OT (CE RA1.f)

Históricamente, IT y OT vivían separados: redes distintas, proveedores distintos, ni siquiera el mismo vocabulario. La **Industria 4.0** los obliga a converger: los sensores OT publican datos (a menudo por **MQTT**) que las aplicaciones IT consumen, y las decisiones de negocio (parar una línea, lanzar una oferta) bajan hasta la planta.

**Motores de la convergencia en 2026**: digitalización de procesos industriales, IoT barato y ubicuo, y la necesidad de unificar datos dispersos (ERP + sensores + redes sociales) para decidir con información completa.

**Condición**: gobernanza conjunta de **datos y seguridad**. Un PLC expuesto a internet sin protección es la puerta de entrada a toda la empresa (y al revés: un ransomware en IT puede llegar a parar la producción).

## 6. Ventajas de digitalizar de extremo a extremo (CE RA1.g)

Digitalizar solo un departamento («islas digitales») da poco; el valor aparece al conectar **producción → gestión → cliente** (transformación integral):

1. **Eficiencia operativa**: automatizar elimina errores manuales y tiempos muertos.
2. **Costes y desperdicio**: mantenimiento predictivo y stock ajustado a la demanda real.
3. **Decisiones basadas en datos**: del «yo creo» al panel con cifras en tiempo real.
4. **Agilidad**: líneas flexibles y catálogos que cambian sin reimprimir nada.
5. **Experiencia de cliente**: personalización web, chatbots que resuelven dudas al instante, seguimiento de pedido.
6. **Activos bajo control**: sistemas AMS alargan la vida útil de la maquinaria.
7. **Seguridad y cumplimiento**: trazabilidad automática para auditorías (sanidad, alimentación, facturación).

!!! example "Caso 2026: obrador que vende online"
    Un obrador instala sensores de temperatura en cámaras (OT, 300 €), conecta su tienda online con el stock del ERP (IT) y activa avisos automáticos al repartidor. Resultado en 6 meses: cero pérdidas por rotura de frío, –20 % de stock inmovilizado y pedidos de fuera de su provincia. Inversión recuperada antes del año.

## 7. Para practicar

- [Prácticas UD1](../practicas/UD1/index.md): estudio de caso IT/OT y propuesta de digitalización para una empresa.
- **Glosario mínimo del RA1**: digitalización, transformación digital, IT, OT, PLC, SCADA, DCS, ERP, CRM, IoT, gemelo digital, convergencia IT–OT, mantenimiento predictivo, plan de contingencia.
- **Autoevaluación**: ¿sabrías explicar con un ejemplo propio la diferencia entre digitalizar y transformar? ¿Y clasificar cinco sistemas de tu centro en IT u OT?
