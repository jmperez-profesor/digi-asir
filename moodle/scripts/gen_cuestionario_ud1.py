#!/usr/bin/env python3
"""Genera el cuestionario UD1 (20 preguntas, con retroalimentación) en formato GIFT para Moodle.

Salida: moodle/export/UD1_cuestionario_ImpresionArte.gift
Importar en Moodle: Banco de preguntas -> Importar -> formato GIFT.
"""
import os
import re

OUT = os.path.join(os.path.dirname(__file__), "..", "export", "UD1_cuestionario_ImpresionArte.gift")


def esc(t: str) -> str:
    """Escapa los caracteres especiales de GIFT: ~ = # { } :"""
    return re.sub(r"([~=#{}:])", r"\\\1", t)


# Cada pregunta: (titulo, enunciado, [(opcion, correcta, feedback)], feedback_general)
Q = []

# ---------------------------------------------------------------- Bloque 1: 10 preguntas del libro
Q.append((
    "UD1-01 Plan de digitalización",
    "Un plan de digitalización prepara a la empresa para la transformación digital porque…",
    [
        ("Evita identificar áreas específicas que podrían beneficiarse de dicho plan.", False,
         "Es justo al revés: el plan comienza con un diagnóstico que IDENTIFICA las áreas que más se benefician."),
        ("Incluye estrategias para combatir la resistencia al cambio que pueda aparecer.", False,
         "Es cierto que el plan incluye gestión del cambio, pero es solo una de sus partes. La opción que mejor explica su función global es la que habla de optimizar las inversiones."),
        ("Evita introducir nuevos riesgos y mejorar así la seguridad y el cumplimiento.", False,
         "Un plan no \"evita\" riesgos: los identifica y los gestiona (ciberseguridad desde el diseño). Digitalizar abre nuevas superficies de ataque."),
        ("Ayuda a optimizar las inversiones en tecnología, capacitación y cambio organizacional.", True,
         "¡Correcto! El plan reparte presupuesto y tiempo entre tecnología, formación y cambio organizativo para maximizar el retorno."),
    ],
    "Ver apartado 1.1 de los apuntes (Plan de digitalización).",
))

Q.append((
    "UD1-02 Aspectos clave de la transformación",
    "¿Cuál de los siguientes NO es un aspecto clave en el proceso de transformación digital?",
    [
        ("Enfoque en mejorar la experiencia del cliente.", False,
         "Sí es un aspecto clave: canales digitales, personalización, chatbots, fidelización."),
        ("Cambio de la cultura organizacional.", False,
         "Sí es un aspecto clave, y de hecho el que hace real la transformación: sin cambio de mentalidad, las herramientas se abandonan."),
        ("El uso de datos y analíticas.", False,
         "Sí es un aspecto clave: decidir con datos y predecir (demanda, ofertas personalizadas)."),
        ("Dispositivos más potentes para los empleados.", True,
         "¡Correcto! Comprar equipos más potentes es una inversión en hardware, no un aspecto clave de la transformación. La tecnología es un medio, no el fin."),
    ],
    "Ver apartado 1.2 de los apuntes (Transformación digital).",
))

Q.append((
    "UD1-03 Características del entorno OT",
    "Una de las principales características de un entorno OT es…",
    [
        ("El uso de sensores y dispositivos conectados para recopilar datos.", True,
         "¡Correcto! La OT supervisa y controla procesos físicos mediante sensores, actuadores, PLC y SCADA que recogen datos del entorno físico."),
        ("La seguridad de las aplicaciones y los datos.", False,
         "Eso es más propio del entorno IT. En OT la prioridad histórica es la seguridad física y la disponibilidad del proceso."),
        ("El uso de sistemas de gestión empresarial.", False,
         "Los sistemas de gestión empresarial (ERP, CRM…) pertenecen al entorno IT."),
        ("La implantación de herramientas de comunicación.", False,
         "Las herramientas de comunicación (correo, comunicaciones unificadas) son del entorno IT."),
    ],
    "Ver apartado 3.2 de los apuntes (Entorno OT).",
))

Q.append((
    "UD1-04 Digitalización en negocio",
    "¿Cuáles de los siguientes aspectos corresponden a la digitalización en negocio?",
    [
        ("Big data.", False,
         "Big data es un aspecto de la digitalización en negocio, pero no el único: la respuesta correcta incluye los tres."),
        ("Inteligencia artificial.", False,
         "La IA y el machine learning son digitalización en negocio, pero no los únicos: la respuesta correcta incluye los tres."),
        ("Blockchain.", False,
         "Blockchain (trazabilidad y seguridad de transacciones) es digitalización en negocio, pero no el único: la respuesta correcta incluye los tres."),
        ("Big data, inteligencia artificial y blockchain (todos ellos).", True,
         "¡Correcto! Además de ERP, computación en la nube e IoT, big data, IA y blockchain son tecnologías de la digitalización en negocio."),
    ],
    "Ver apartado 4.2 de los apuntes (Digitalización en negocio).",
))

Q.append((
    "UD1-05 Ciberseguridad y transformación",
    "¿Por qué es importante que tengamos en cuenta aspectos de la ciberseguridad en el proceso de transformación digital?",
    [
        ("Porque la ciberseguridad es una cuestión que está muy de moda y puede favorecer nuestra imagen de empresa.", False,
         "La ciberseguridad no es cuestión de moda ni de imagen: es una necesidad de protección."),
        ("Para mantenernos conectados a internet.", False,
         "La conectividad no depende de la ciberseguridad; esta protege lo que se conecta."),
        ("Porque hay que asegurar los datos y sistemas críticos del negocio.", True,
         "¡Correcto! Al digitalizar, los datos y sistemas críticos quedan expuestos a nuevas amenazas y hay que protegerlos."),
        ("Porque los ordenadores necesitan un antivirus.", False,
         "El antivirus es solo una herramienta concreta; la ciberseguridad abarca personas, procesos, copias, accesos y configuración."),
    ],
    "Ver apartado 2.5 de los apuntes (Desafíos y responsabilidades).",
))

Q.append((
    "UD1-06 Digitalización vs transformación",
    "¿Es lo mismo digitalización que transformación digital?",
    [
        ("Sí, porque la digitalización siempre implica una transformación digital.", False,
         "No: se puede digitalizar (escanear facturas) sin cambiar nada más en la empresa."),
        ("No. La transformación digital es un proceso más profundo que la digitalización.", True,
         "¡Correcto! La digitalización convierte formatos; la transformación cambia procesos, modelo de negocio y cultura."),
        ("No. La digitalización es un proceso más profundo que la transformación digital.", False,
         "Es al revés: la digitalización suele ser un paso previo y más acotado."),
        ("Sí. De hecho, los dos términos se utilizan indistintamente.", False,
         "Se confunden a menudo, pero describen cosas distintas: alcance y profundidad del cambio."),
    ],
    "Ver apartado 1 de los apuntes (tabla comparativa).",
))

Q.append((
    "UD1-07 Tipos de transformación digital",
    "¿Cuál de los siguientes NO es un tipo de transformación digital?",
    [
        ("Transformación digital de la cultura de la organización.", False,
         "Sí es un tipo: cambia la mentalidad y la forma de trabajar de las personas."),
        ("Transformación digital de los procesos en la empresa.", False,
         "Sí es un tipo: flujos de trabajo internos y externos."),
        ("Transformación digital en la gestión de residuos.", True,
         "¡Correcto! No es un tipo. Los cuatro tipos son: procesos, modelo de negocio, dominio empresarial y cultura de la organización."),
        ("Transformación digital del modelo de negocio.", False,
         "Sí es un tipo: cambia la propuesta de valor y cómo se llega al mercado (p. ej., abrir una tienda online)."),
    ],
    "Ver apartado 1.2 de los apuntes (cuatro tipos de transformación).",
))

Q.append((
    "UD1-08 Efecto en procesos y operaciones",
    "Uno de los principales efectos de la implantación de la tecnología en los procesos y operaciones de la empresa es…",
    [
        ("La reducción de errores como consecuencia de la automatización.", True,
         "¡Correcto! Automatizar reduce los errores propios del trabajo manual y libera recursos para tareas de más valor."),
        ("El aumento en la carga de trabajo de los empleados responsables de los procesos.", False,
         "Al contrario: la automatización libera tiempo de las personas."),
        ("La necesidad de asignar más recursos a esos procesos y operaciones.", False,
         "Al contrario: se liberan recursos que pueden dedicarse a actividades más estratégicas."),
        ("La reducción de la jornada laboral de los empleados.", False,
         "No es un efecto directo de la implantación tecnológica en los procesos."),
    ],
    "Ver apartado 2.2 de los apuntes (Transformación de procesos y operaciones).",
))

Q.append((
    "UD1-09 Entorno IT",
    "¿A qué nos referimos con el término entorno IT?",
    [
        ("Al conjunto de la información de una organización con las tecnologías y sistemas que tratan esa información.", True,
         "¡Correcto! IT (Information Technology) gestiona información y datos: servidores, redes, ERP, bases de datos, software y su seguridad."),
        ("A todos los dispositivos electrónicos instalados en la empresa, incluidos los de los empleados.", False,
         "Es una definición demasiado amplia e imprecisa: el entorno IT se define por su enfoque en la información, no por \"todos los dispositivos\"."),
        ("A la tecnología usada para supervisar los dispositivos de una empresa.", False,
         "Eso se parece más a la definición de OT (supervisar y controlar dispositivos y procesos físicos)."),
        ("Al software que controla directamente las máquinas de una planta industrial.", False,
         "Eso describe sistemas de control propios del entorno OT, no del IT."),
    ],
    "Ver apartado 3.1 de los apuntes (Entorno IT).",
))

Q.append((
    "UD1-10 Enfoque operativo",
    "Al enfoque operativo en el proceso de digitalización de un entorno empresarial se le conoce como…",
    [
        ("Digitalización en negocio.", False,
         "La digitalización en negocio es el enfoque EMPRESARIAL (RR. HH., finanzas, logística, clientes)."),
        ("Digitalización en empresa.", False,
         "No es una denominación utilizada para el enfoque operativo."),
        ("Digitalización en sistema.", False,
         "No es una denominación utilizada para el enfoque operativo."),
        ("Digitalización en planta.", True,
         "¡Correcto! El enfoque operativo (producción y procesos industriales físicos) se llama digitalización en planta."),
    ],
    "Ver apartado 4 de los apuntes (Tecnologías en planta y en negocio).",
))

# ---------------------------------------------------------------- Bloque 2: 10 preguntas ImpresiónArte
Q.append((
    "UD1-11 ImpresiónArte: ERP y entorno IT",
    "Sara y Samuel implantan un ERP que unifica pedidos, stock y facturación de ImpresiónArte. ¿A qué entorno pertenece principalmente este sistema?",
    [
        ("Entorno IT (tecnología de la información).", True,
         "¡Correcto! Un ERP gestiona información y procesos de negocio sobre servidores, bases de datos y redes: es entorno IT."),
        ("Entorno OT (tecnología operativa).", False,
         "La OT controla máquinas y procesos físicos (PLC, sensores, SCADA). Un ERP gestiona información, no controla la impresora."),
        ("Ninguno: un ERP no pertenece a ningún entorno.", False,
         "Todo sistema tecnológico de una empresa encaja en IT, OT o en la unión de ambos."),
        ("Entorno OT, porque está en el taller.", False,
         "La ubicación física no define el entorno; lo define su función. El ERP trata información, aunque esté en el taller."),
    ],
    "Los ERP, bases de datos, servidores y redes son el núcleo del entorno IT (apartado 3.1).",
))

Q.append((
    "UD1-12 ImpresiónArte: elementos OT",
    "En el taller de ImpresiónArte, ¿cuál de los siguientes elementos pertenece al entorno OT?",
    [
        ("El servidor que aloja la tienda online.", False,
         "Eso es IT: gestiona información y servicios web."),
        ("El PLC que controla la temperatura del túnel de secado de las camisetas.", True,
         "¡Correcto! Un PLC (controlador lógico programable) supervisa y controla un proceso físico en tiempo real: es el ejemplo típico de OT."),
        ("El programa de facturación electrónica.", False,
         "Eso es IT: software de gestión empresarial."),
        ("El correo electrónico del equipo.", False,
         "Eso es IT: comunicaciones."),
    ],
    "OT = tecnología para supervisar y controlar dispositivos y procesos físicos: PLC, SCADA, DCS, sensores (apartado 3.2).",
))

Q.append((
    "UD1-13 ImpresiónArte: IT frente a OT",
    "Samuel analiza el taller. ¿Cuál de estas afirmaciones sobre IT y OT es CORRECTA?",
    [
        ("IT gestiona información y datos; OT controla máquinas y procesos físicos.", True,
         "¡Correcto! Esa es la diferencia esencial entre ambos entornos."),
        ("IT controla las máquinas del taller y OT gestiona la facturación.", False,
         "Está invertido: la facturación es IT y el control de máquinas es OT."),
        ("IT y OT son lo mismo, solo cambia el nombre.", False,
         "Son ámbitos distintos, con prioridades, tecnologías y ritmos de cambio diferentes."),
        ("OT solo existe en grandes fábricas y nunca en un taller pequeño.", False,
         "Cualquier taller con máquinas controladas electrónicamente (impresoras, secadoras, prensas) tiene elementos OT, aunque sea a pequeña escala."),
    ],
    "Ver la tabla comparativa IT/OT del apartado 3.2: fallo típico (fuga de datos frente a parada de producción) y prioridad (confidencialidad frente a disponibilidad y seguridad física).",
))

Q.append((
    "UD1-14 ImpresiónArte: convergencia IT-OT",
    "Samuel quiere que el estado y el consumo de las impresoras textiles (OT) aparezcan automáticamente en el ERP (IT) para decidir qué imprimir y cuándo comprar tinta. ¿Cómo se denomina esta integración?",
    [
        ("Convergencia IT-OT.", True,
         "¡Correcto! La convergencia IT-OT integra y alinea la tecnología de la información con la tecnología operativa para decidir con datos reales de planta."),
        ("Digitalización analógica.", False,
         "Ese concepto no describe la unión de los entornos IT y OT."),
        ("Externalización de servicios.", False,
         "Externalizar es contratar a un proveedor externo, no integrar IT y OT."),
        ("Segmentación de red.", False,
         "La segmentación es una medida de seguridad que SEPARA redes; la convergencia es la integración de los dos mundos."),
    ],
    "Ver apartado 3.3 de los apuntes (Convergencia de IT y OT): datos unificados, eficiencia operativa y decisiones informadas.",
))

Q.append((
    "UD1-15 ImpresiónArte: Industria 4.0",
    "ImpresiónArte quiere conectar sus impresoras con sensores IoT, enviar sus datos a la nube y analizarlos para optimizar la producción. ¿Con qué concepto se relaciona esta idea?",
    [
        ("Industria 4.0.", True,
         "¡Correcto! La Industria 4.0 (cuarta revolución industrial) conecta máquinas, sensores y sistemas mediante IoT, datos, nube y analítica para fabricar de forma más eficiente y flexible."),
        ("Industria 1.0, basada en la mecanización con vapor.", False,
         "La Industria 1.0 corresponde a la mecanización con energía de vapor (siglo XVIII-XIX), sin conectividad digital."),
        ("Una tienda online.", False,
         "La tienda online es un cambio en el modelo de negocio, no la conexión de la planta."),
        ("Un plan de contingencia.", False,
         "El plan de contingencia son las medidas para continuar operando ante imprevistos; no trata de conectar las máquinas."),
    ],
    "La Industria 4.0 es uno de los principales factores impulsores de la convergencia IT-OT (apartado 3.3).",
))

Q.append((
    "UD1-16 ImpresiónArte: riesgo de la convergencia",
    "Tras conectar las impresoras a la red de oficina de ImpresiónArte, un ransomware que entra por un PC de administración podría paralizar la producción. ¿Qué medida reduce mejor este riesgo?",
    [
        ("Segmentar la red separando IT y OT (VLAN y cortafuegos) y vigilar el tráfico entre ambas.", True,
         "¡Correcto! La segmentación limita el movimiento del atacante: un incidente en IT no debe poder llegar a los equipos de planta."),
        ("Conectar todos los equipos a una única red plana para simplificar.", False,
         "Una red plana facilita justo lo contrario: que un ransomware llegue a todas partes."),
        ("Desactivar las copias de seguridad para ahorrar espacio.", False,
         "Las copias (regla 3-2-1) son una defensa clave frente al ransomware."),
        ("Dejar las impresoras con acceso directo desde internet para el soporte remoto.", False,
         "Exponer equipos de planta a internet multiplica el riesgo; cualquier acceso remoto debe estar controlado."),
    ],
    "La convergencia exige gestión centralizada de la seguridad: segmentar, inventariar activos y parchear lo parcheable (apartado 3.3).",
))

Q.append((
    "UD1-17 ImpresiónArte: mantenimiento predictivo",
    "Unos sensores miden el desgaste de los cabezales de las impresoras de ImpresiónArte y avisan para sustituirlos antes de que fallen. ¿Qué ventaja de la transformación digital integral ilustra este ejemplo?",
    [
        ("Reducción de costes y desperdicios mediante mantenimiento predictivo.", True,
         "¡Correcto! Monitorizar equipos con IoT y analizar los datos permite programar el mantenimiento y evitar paradas no planificadas."),
        ("Cumplimiento normativo.", False,
         "El cumplimiento normativo se basa en registros precisos y auditorías, no en prever averías."),
        ("Mejora de la experiencia del cliente.", False,
         "Indirectamente puede mejorar los plazos, pero el ejemplo ilustra la gestión de activos y la reducción de paradas."),
        ("Resistencia al cambio.", False,
         "La resistencia al cambio es un desafío, no una ventaja."),
    ],
    "Ver apartado 5 de los apuntes: gestión eficiente de activos (AMS) y reducción de costes y desperdicios.",
))

Q.append((
    "UD1-18 ImpresiónArte: gemelo digital",
    "Un gemelo digital de la impresora textil de ImpresiónArte permitiría…",
    [
        ("Simular y optimizar su funcionamiento en una réplica virtual antes de cambiar nada en la máquina real.", True,
         "¡Correcto! Un gemelo digital es una réplica virtual de un objeto, proceso o sistema real, creada con datos y modelos de simulación, para probar cambios sin riesgo."),
        ("Sustituir físicamente la impresora por una más moderna.", False,
         "Un gemelo digital es virtual: no reemplaza ni compra maquinaria."),
        ("Duplicar automáticamente la producción sin consumir materiales.", False,
         "No produce camisetas: solo simula el comportamiento de la máquina."),
        ("Eliminar la necesidad de personal en el taller.", False,
         "El gemelo digital ayuda a decidir mejor; no elimina el trabajo humano."),
    ],
    "Los gemelos digitales son una tecnología de digitalización en planta (apartado 4.1).",
))

Q.append((
    "UD1-19 ImpresiónArte: planta o negocio",
    "La tienda online de ImpresiónArte, conectada con el inventario y la facturación del ERP, es un ejemplo de…",
    [
        ("Digitalización en negocio.", True,
         "¡Correcto! Afecta a las funciones de gestión y comerciales (ventas, clientes, inventario, facturación): enfoque empresarial."),
        ("Digitalización en planta.", False,
         "La digitalización en planta se aplica a la producción física (sensores, autómatas, gemelos digitales), no a la venta online."),
        ("Entorno OT exclusivamente.", False,
         "Una tienda online y un ERP son IT, no OT."),
        ("Ninguna digitalización: solo es una web.", False,
         "Una tienda conectada a inventario y facturación cambia el modelo de negocio y los procesos: es mucho más que una web."),
    ],
    "Ver apartado 4.2 de los apuntes (Digitalización en negocio).",
))

Q.append((
    "UD1-20 ImpresiónArte: eficiencia",
    "Gracias a la automatización, ImpresiónArte imprime el mismo número de camisetas gastando menos tinta y menos horas de trabajo. ¿Qué ha mejorado?",
    [
        ("La eficiencia operativa: mismos resultados con menos recursos.", True,
         "¡Correcto! Eficiencia = generar los mismos resultados con la menor cantidad de recursos."),
        ("La productividad: más resultados con los mismos recursos.", False,
         "Aquí el resultado (nº de camisetas) no aumenta; lo que baja son los recursos. Eso es eficiencia, no productividad."),
        ("La convergencia IT-OT.", False,
         "La convergencia es la integración de los entornos IT y OT; el enunciado describe un resultado, no una integración."),
        ("La resistencia al cambio.", False,
         "La resistencia al cambio es un desafío cultural, no una mejora."),
    ],
    "Ver apartado 5 de los apuntes (eficiencia frente a productividad).",
))


def render() -> str:
    lines = [
        "// Cuestionario UD1 · Digitalización en los sistemas productivos · Reto ImpresiónArte",
        "// Módulo 1665 · 2º ASIR · 20 preguntas con retroalimentación",
        "// Importar: Banco de preguntas > Importar > formato GIFT",
        "// Recomendado: activar \"Barajar respuestas\" en el cuestionario",
        "$CATEGORY: $course$/UD1 ImpresiónArte",
        "",
    ]
    for titulo, enunciado, opciones, general in Q:
        lines.append(f"::{esc(titulo)}::{esc(enunciado)} {{")
        for texto, correcta, fb in opciones:
            marca = "=" if correcta else "~"
            lines.append(f"\t{marca}{esc(texto)}#{esc(fb)}")
        lines.append(f"\t####{esc(general)}")
        lines.append("}")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    out = os.path.abspath(OUT)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(render())
    # Validación básica
    assert len(Q) == 20, len(Q)
    for t, _, ops, _ in Q:
        assert sum(1 for _, c, _ in ops if c) == 1, f"{t}: debe haber exactamente 1 correcta"
        assert len(ops) == 4, t
    print(f"OK: {len(Q)} preguntas -> {out}")
