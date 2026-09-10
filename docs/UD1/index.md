# UD1: Digitalización en los Sistemas Productivos (RA1 · 5 h)

> **Resultado de aprendizaje**: analizar el concepto de digitalización y su repercusión en los sectores productivos, identificando entornos IT y OT (CE RA1.a–g). Ponderación del RA1: **14 %** (80 % actividades + 20 % cuestionario). Enfoque de la unidad: **el administrador de sistemas como habilitador técnico de la digitalización**.

## 1. Digitalización ≠ transformación digital

- **Digitalización**: pasar información y procesos analógicos a formato digital. Escanear albaranes, cobrar con TPV, controlar el stock en una hoja de cálculo. Primer paso: táctico y barato.
- **Transformación digital**: rediseñar el negocio apoyándose en tecnología. No es «hacer lo mismo con ordenadores», sino cambiar *qué* se ofrece y *cómo* se opera: vender online, anticipar la demanda con datos, automatizar la planta.

!!! example "Ejemplo 2026: taller de impresión textil"
    Un taller que solo publica su catálogo en una web se ha **digitalizado**. Cuando además conecta la tienda con el inventario, automatiza pedidos al proveedor según el stock y ofrece personalización del producto en la web, se ha **transformado**: vende fuera de su ciudad y sabe qué diseños funcionan antes de imprimirlos. Detrás de cada uno de esos pasos hay un administrador de sistemas: el VPS donde corre la tienda, las copias de seguridad, los certificados, la VPN del taller.

!!! tip "Contexto 2026 (España)"
    Transformarse ya no es opcional: la **factura electrónica** (Ley Crea y Crece + Reglamento VeriFactu) obliga a digitalizar la facturación, los fondos **Kit Digital** financian la adopción en pymes y la directiva **NIS2** eleva las exigencias de ciberseguridad. Cada obligación legal es trabajo de infraestructura: sistemas, redes y seguridad.

## 2. Cómo la tecnología cambia la empresa (y qué pinta el sysadmin)

La implantación digital impacta en cuatro frentes (CE RA1.b); en cada uno, el administrador de sistemas tiene un papel concreto:

| Frente | Qué cambia | Papel del administrador de sistemas |
|---|---|---|
| **Estructura organizativa** | Aparecen roles técnicos y se externaliza lo no estratégico | Dimensionar qué se queda dentro (servidores, red) y qué se externaliza (hosting, MSP); documentar la infraestructura |
| **Procesos y operaciones** | Se automatiza lo repetitivo: menos errores, más velocidad | Desplegar el ERP, automatizar copias y despliegues con scripts, monitorizar servicios |
| **Cultura** | Resistencia al cambio; hace falta formación | Formar a usuarios, redactar manuales sencillos, ser el «campeón digital» que acompaña el cambio |
| **Clientes y mercado** | Nuevos canales (tienda online, reservas web) | Mantener esos canales en pie: disponibilidad, rendimiento, certificados, copias |

!!! warning "Riesgos que debe cubrir el sysadmin"
    Dependencia del proveedor cloud (¿y si cae?), plan de contingencia para procesos críticos y seguridad desde el día uno: copias 3-2-1, control de accesos y parches. Digitalizar sin copias ni bastionado es construir sobre arena.

## 3. Entornos IT y OT (CE RA1.c–d)

### 3.1. Entorno IT (*Information Technology*)

Tecnologías que gestionan **información**: servidores, redes, virtualización, ERP/CRM, correo, copias de seguridad. Prioridades: confidencialidad, integridad y disponibilidad de los datos. **Este es el territorio natural del ASIR.**

Departamentos IT típicos en una empresa mediana (y su correspondencia con módulos del ciclo):

- **Sistemas / infraestructura**: servidores físicos y virtuales (Proxmox, Hyper-V), almacenamiento, red.
- **Redes y comunicaciones**: VLAN, VPN (WireGuard), cortafuegos, wifi corporativa.
- **Datos y analítica**: SGBD (PostgreSQL, MySQL), informes y cuadros de mando (Grafana).
- **Ciberseguridad**: identidades, bastionado, detección y respuesta a incidentes.
- **Soporte (*help desk*)**: atención a usuarios, gestión de incidencias y activos.
- **Proyectos e innovación**: migraciones, evaluación de tecnologías emergentes.

!!! note "Pyme pequeña"
    Una empresa de 7 personas no tiene estos departamentos: los **externaliza** (el ERP en un VPS gestionado, la web en un hosting, el soporte en un MSP). Decidir qué externalizar, contratarlo bien y supervisarlo también es administración de sistemas.

### 3.2. Entorno OT (*Operational Technology*)

Tecnología que controla el **mundo físico**: autómatas (**PLC**), supervisión (**SCADA**), control distribuido (**DCS**), sensores y actuadores. Prioridades: seguridad de las personas, continuidad operativa y **tiempo real**. Para el ASIR es el entorno «vecino»: cada vez más conectado a nuestras redes, con sus propias reglas (equipos que duran décadas y no se pueden reiniciar a la ligera).

### 3.3. Diferencias clave de un vistazo

| Aspecto | IT | OT |
|---|---|---|
| Gestiona | Datos e información | Máquinas y procesos físicos |
| Fallo típico | Fuga o pérdida de datos | Parada de producción o accidente |
| Ritmo de cambio | Rápido (parches frecuentes) | Lento (equipos de décadas, ventanas de parada escasas) |
| Prioridad nº 1 | Confidencialidad | Seguridad física y disponibilidad |

## 4. Tecnologías de digitalización en planta y en negocio (CE RA1.e)

### En planta (enfoque operativo)

- **Automatización y control**: PLC + SCADA gobernando líneas en tiempo real.
- **IoT y sensores**: temperatura, vibración, consumo; datos continuos para **mantenimiento predictivo** (detectar un rodamiento que va a fallar *antes* de que pare la línea).
- **Gemelos digitales**: réplica virtual para simular cambios sin riesgo.
- **Redes industriales**: segmentación OT, pasarelas y captación de datos hacia los sistemas de gestión.

### En negocio (enfoque empresarial, el que despliega el ASIR)

- **Virtualización y nube**: consolidar servidores físicos en un hipervisor o migrar cargas a IaaS.
- **ERP** (p. ej., Odoo sobre un VPS endurecido): finanzas, inventario y logística en una plataforma.
- **Monitorización centralizada**: Zabbix o Prometheus + Grafana vigilando servicios, red y copias.
- **Teletrabajo seguro**: VPN, MFA y políticas de acceso para trabajar desde fuera.
- **Analítica e IA**: previsión de demanda y detección de anomalías sobre los logs.

!!! example "El mismo dato, dos usos"
    El sensor de una cámara frigorífica (OT) evita que se estropee el género; ese dato, recogido por una pasarela y mostrado en un Grafana (IT), permite comparar el consumo de todas las tiendas y renegociar la tarifa eléctrica. Tender ese puente —red, servidor, panel— es trabajo ASIR.

## 5. Convergencia IT–OT (CE RA1.f)

Históricamente, IT y OT vivían separados: redes distintas, proveedores distintos, ni el mismo vocabulario. La **Industria 4.0** los obliga a converger: los sensores OT publican datos (típicamente por **MQTT**) que las aplicaciones IT consumen, y las decisiones de negocio bajan hasta la planta.

**Qué cambia para el administrador**: la red OT deja de ser «cosa de los de mantenimiento». Hay que segmentarla (VLAN, cortafuegos entre mundos), inventariar esos activos, parchear lo parcheable y monitorizar el tráfico IT↔OT. Un PLC expuesto a internet es la puerta de entrada a toda la empresa; y un ransomware en IT puede acabar parando la producción.

## 6. Ventajas de digitalizar de extremo a extremo (CE RA1.g)

Digitalizar un solo departamento («islas digitales») da poco; el valor aparece al conectar **producción → sistemas → cliente**:

1. **Eficiencia operativa**: la automatización elimina errores manuales y tiempos muertos.
2. **Costes y desperdicio**: mantenimiento predictivo y stock ajustado a la demanda real.
3. **Decisiones basadas en datos**: del «yo creo» al panel con cifras en tiempo real.
4. **Agilidad**: infraestructura elástica (más CPU/RAM con dos clics) en vez de comprar hierro.
5. **Experiencia de cliente**: servicios siempre disponibles y tiempos de respuesta cortos.
6. **Activos bajo control**: inventario, monitorización y ciclo de vida del hardware.
7. **Seguridad y cumplimiento**: trazabilidad y evidencias automáticas para auditorías (ENS, RGPD, VeriFactu).

!!! example "Caso 2026: obrador que vende online"
    Un obrador instala sensores de temperatura en cámaras (OT, 300 €), virtualiza su antiguo PC de facturación en el hipervisor del taller, conecta la tienda online con el stock y programa copias externas diarias. Resultado en 6 meses: cero pérdidas por rotura de frío, –20 % de stock inmovilizado y pedidos de fuera de su provincia. Todo montado y mantenido por un técnico de sistemas.

## 7. Para practicar

- [Prácticas UD1](../practicas/UD1/index.md): estudio de caso IT/OT y propuesta de digitalización para una empresa.
- **Glosario mínimo del RA1**: digitalización, transformación digital, IT, OT, PLC, SCADA, DCS, ERP, CRM, IoT, MQTT, hipervisor, MSP, gemelo digital, convergencia IT–OT, mantenimiento predictivo, copia 3-2-1, plan de contingencia.
- **Autoevaluación**: ¿sabrías explicar con un ejemplo propio la diferencia entre digitalizar y transformar? ¿Y dibujar el mapa IT/OT de una pyme indicando qué administrarías tú?
