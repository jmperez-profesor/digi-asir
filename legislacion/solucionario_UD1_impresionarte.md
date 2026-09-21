# Solucionario y guía de aula — Reto «ImpresiónArte» (UD1)

> **Uso docente. No publicar en la web del alumnado.** Este documento contiene la solución modelo, los problemas previsibles y las respuestas a las preguntas que suelen surgir en el aula.

---

## Parte 1. Solución modelo del ejercicio

> Qué debería contener un documento de grupo bien hecho. No es la única respuesta válida: se evalúa la justificación, no la coincidencia literal.

### Bloque A — Exploración con Copilot

**Problemas del taller que deberían aparecer:**
- Sin presencia online (ni web, ni tienda, ni redes): dependen del boca a boca y de la clientela local.
- Gestión de pedidos manual: pedidos perdidos, duplicados o mal anotados.
- Inventario descontrolado: compran tela/hilo de más o se quedan sin stock en plena campaña.
- Producción sin datos: no saben qué diseños se venden ni cuánto tardan.
- Sin previsión de demanda: no pueden anticiparse a campañas (vuelta al cole, fiestas).
- Imagen de empresa desactualizada frente a competidores digitales.

**Soluciones que suele proponer Copilot (y son válidas):**
- Web corporativa + tienda online con catálogo.
- ERP (Odoo, Holded) para pedidos, stock y facturación.
- Redes sociales y catálogo digital.
- Facturación electrónica.
- Analítica de ventas para decidir catálogo.
- Automatización de avisos a clientes (email/WhatsApp).

### Bloque B — ¿Digitalizar o transformar?

| Caso | Respuesta | Justificación |
|---|---|---|
| Escanear facturas en papel | **Digitalización** | Solo convierte un soporte físico a digital; el proceso no cambia. |
| Tienda online conectada al inventario | **Transformación** | Cambia el modelo de negocio (nuevo canal) y los procesos (stock automático). |

**Ejemplos propios** (deben ser originales, no copiados de la IA):
- *Digitalizar*: pasar la lista de clientes del cuaderno a Excel.
- *Transformar*: un sistema de reservas online que avisa al cliente y actualiza la agenda solo.

!!! warning "Error típico"
    Muchos alumnos escribirán que «digitalizar es lo pequeño y transformar lo grande». Es una aproximación aceptable, pero hay que corregirla: la diferencia real es **el alcance del cambio** (¿cambia solo el formato, o cambia el proceso/modelo/cultura?), no el tamaño.

### Bloque C — Tipos de cambio

| Solución | Tipo de transformación |
|---|---|
| Tienda online | **Modelo de negocio** |
| ERP de pedidos y stock | **Procesos empresariales** |
| Analítica de ventas / IA de recomendación | **Procesos** o **dominio** (según el enfoque) |
| Formación del equipo en herramientas digitales | **Cultura de la organización** |
| Sensores en las impresoras textiles | **Dominio empresarial** (núcleo operativo) |

!!! note "Matiz importante"
    El ERP puede clasificarse como **procesos** (automatiza flujos) y a la vez habilitar un **modelo de negocio** nuevo. No hay una única casilla correcta: lo que se evalúa es que **justifiquen** la elección.

### Bloque D — Verificación y tabla de huella

Ejemplo de verificación real:
- **Afirmación de Copilot**: «Odoo es gratuito para una empresa pequeña».
- **Contraste**: Odoo tiene una versión Community gratuita, pero el alojamiento, la implantación y los módulos avanzados se pagan. Fuente: web oficial de Odoo / comparativas.
- **Conclusión del grupo**: aceptamos que hay versión gratuita, pero matizamos que el coste real está en la puesta en marcha.

Ejemplo de tabla de huella:

| Qué propuso la IA | ¿Lo aceptamos? | ¿Qué cambiamos y por qué? |
|---|---|---|
| Contratar un ERP de pago | Sí, pero… | Empezar con la versión Community y valorar migrar después: 7 personas no amortizan una licencia grande. |
| Crear una app móvil propia | No | Desproporcionado para su tamaño; una tienda online responsive cubre lo mismo. |
| Usar IA para predecir demanda | Sí | Con datos de ventas; al principio bastará con una hoja de cálculo. |

### Bloque E — Plan de digitalización (ejemplo)

| Prior. | Medida | Problema que resuelve | Tipo de cambio | Herramienta | Coste aprox. | Riesgo |
|---|---|---|---|---|---|---|
| 1 | Tienda online con catálogo | Falta de canal de venta | Modelo de negocio | WooCommerce / Shopify | 0–30 €/mes | Poca visibilidad inicial |
| 2 | ERP de pedidos y stock | Descontrol de inventario | Procesos | Odoo Community | 0 € + implantación | Curva de aprendizaje |
| 3 | Factura electrónica | Cumplimiento y errores manuales | Procesos | VeriFactu / gestoría | Bajo | Adaptación del personal |
| 4 | Analítica de ventas | No saber qué vender | Procesos / dominio | Hoja de cálculo → BI | 0 € | Datos mal introducidos |

!!! tip "Orden razonable"
    Se espera que prioricen **lo barato y de alto impacto** primero (canal online, orden interno) y dejen para el final lo caro o lo que depende de tener datos (IA, analítica avanzada).

---

## Parte 2. Problemas previsibles y cómo resolverlos

### A) Problemas técnicos

| Problema | Solución rápida |
|---|---|
| No pueden compartir el Word en edición | Debe hacerse desde el propio Word online (botón **Compartir → Permitir edición**). Copiar el enlace y pegarlo en el chat del grupo. No vale descargarlo y reenviarlo. |
| No todos entran con la cuenta del centro | Verificar que usan la cuenta educativa (Microsoft 365 del centro), no una personal. Si el centro no la da, crear un documento de grupo y que solo escriba el «Piloto». |
| Copilot no aparece o está limitado | Tener un plan B: usar Copilot en Edge o la versión web. Si no hay acceso, permitir que un miembro consulte desde su móvil y pegue los resultados. |
| Se pisan al escribir en el mismo documento | Repartir secciones por miembro y no escribir todos a la vez en la misma celda. Usar comentarios para dudas. |
| Pierden el trabajo | Word online guarda solo; pero recordar **no cerrar sin conexión**. Comprobar que aparece «Guardado». |

### B) Problemas conceptuales

| Problema | Cómo reconducirlo |
|---|---|
| Confunden digitalizar con transformar | Preguntar: «¿Esto cambia solo el formato, o cambia cómo funciona la empresa?». Si solo cambia el formato → digitalizar. |
| No saben qué es un ERP | Analogía: «Es el cerebro que une pedidos, stock y facturas en un solo sitio». No hace falta que sepan usarlo. |
| Clasifican todo como «procesos» | Recordar los 4 tipos y pedir que justifiquen: «¿Esto cambia la forma de trabajar, lo que vendes, cómo lo produces o cómo piensa el equipo?». |
| Creen que la IA «lo sabe todo» | Insistir en la verificación: pedirles que busquen el precio real de una herramienta. |
| Respuestas muy genéricas («mejorar la eficiencia») | Exigir concreción: «¿Qué herramienta? ¿Para qué proceso? ¿Cuánto cuesta?». |

### C) Problemas de dinámica de grupo

| Problema | Solución |
|---|---|
| Uno hace todo y el resto mira | El historial de versiones de Word delata quién escribe. Repartir secciones y usar los roles. |
| Discuten por el reparto | El profesor asigna roles al azar; nadie elige. |
| Se quedan sin tiempo | Recordar el cronómetro proyectado; el Bloque E es el mínimo imprescindible. |
| Copian y pegan a lo bruto | La tabla de huella es la salvaguarda: sin ella, no se califica. |

### D) Problemas de la propia IA

| Problema | Solución |
|---|---|
| Copilot inventa precios o herramientas | Justo lo que buscamos: usar el error como evidencia en la tabla de huella. |
| Respuestas idénticas en todos los grupos | Pedir ejemplos propios y valorar la originalidad. |
| Copilot no entiende el contexto español | Añadir al prompt: «en España, para una pyme de 7 personas». |
| Devuelve demasiado texto | Pedirle «resume en 5 puntos» o «en una tabla». |

---

## Parte 3. Preguntas que te pueden hacer (y respuestas)

!!! question "¿Tenemos que usar Copilot obligatoriamente o podemos usar ChatGPT?"
    Para esta actividad usamos **Copilot** porque está integrado en Microsoft 365 del centro y garantiza protección de datos. Si alguien no tiene acceso, puede usar otra IA, pero debe indicarlo en el documento.

!!! question "¿Cuántas medidas tiene que tener el plan?"
    Mínimo **4**. Si os da tiempo y están bien justificadas, podéis añadir más, pero es mejor 4 sólidas que 8 sin justificar.

!!! question "¿Los precios tienen que ser exactos?"
    No. Buscamos un **orden de magnitud** y que justifiquéis la fuente. Si no encontráis un precio, poned un rango y explicad de dónde sale.

!!! question "¿La fuente verificada puede ser la propia web de la herramienta?"
    Sí, es válida. También una noticia, un comparador o un catálogo. Lo que no vale es «lo ha dicho la IA».

!!! question "¿Qué escribo en la tabla de huella si acepto todo lo de la IA?"
    Eso es sospechoso. Revisad: seguramente habrá algo que cambiar, matizar o adaptar. Si de verdad aceptáis todo, explicad **por qué** cada propuesta encaja.

!!! question "¿Podemos poner un ejemplo de empresa que no sea de impresión textil?"
    Para el caso de ImpresiónArte no; para la fuente verificada, sí: cualquier pyme real que se haya digitalizado sirve como comparación.

!!! question "¿El documento lo entregamos o lo ves tú directamente?"
    Lo veo directamente porque está compartido conmigo en edición. No hace falta que me enviéis nada; solo aseguraos de que yo tengo acceso.

!!! question "¿Y si no nos da tiempo a acabar en clase?"
    El documento queda guardado en la nube. Podéis continuar donde lo dejasteis; la sesión 2 está para cerrarlo. Lo que no se puede es empezar de cero el 27/09.

!!! question "¿Puedo escribir en el documento desde el móvil?"
    Sí, Word online funciona en móvil, pero es incómodo para las tablas. Mejor un ordenador; si no, repartíos para que quien tenga móvil aporte ideas y quien tenga PC escriba.

!!! question "¿Se puede saber quién ha escrito cada cosa?"
    Sí. Word online guarda el historial de versiones y los cambios por autor. Por eso pedimos que cada uno escriba en su sección.

!!! question "¿La IA cuenta como fuente? ¿Hay que citarla?"
    La IA es una **herramienta**, no una fuente. Se cita la fuente real que confirma el dato, no la respuesta de Copilot.

!!! question "¿Qué pasa si Copilot nos da una respuesta en inglés o muy larga?"
    Pedidle: «responde en español y en una tabla de 5 filas». Aprender a pedir bien es parte del ejercicio.

!!! question "¿Esto entra en el examen?"
    Los conceptos que descubráis aquí (digitalización vs transformación, tipos, plan) son la base de la UD1 y **sí** entran. Por eso la sesión 3 los formaliza.

---

## Parte 4. Rejilla rápida de corrección

| Indicador | Insuficiente | Bien | Excelente |
|---|---|---|---|
| Diferencia digitalizar/transformar | No la distingue | La define con un ejemplo | La define, da ejemplos propios y matiza |
| Clasificación por tipos | Clasifica sin justificar | Clasifica y justifica | Clasifica, justifica y admite matices |
| Plan de medidas | Menos de 4 o sin orden | 4 ordenadas con datos | 4+ priorizadas, con coste, riesgo y fuente |
| Tabla de huella | Ausente o vacía | Completa | Completa y con decisiones argumentadas |
| Uso de la IA | Copia literal | Usa y adapta | Usa, verifica y corrige a la IA |
| Trabajo en equipo | Uno hace todo | Reparto visible | Roles claros y documento coherente |
