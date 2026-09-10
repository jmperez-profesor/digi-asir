# UD3: Computación en la Nube (RA3 · 5 h)

> **Resultado de aprendizaje**: identificar los sistemas basados en cloud/nube y su influencia en los sistemas digitales (CE RA3.a–e). Ponderación del RA3: **14 %** (80 % actividades + 20 % cuestionario). Enfoque: **criterio de administrador para decidir qué va a la nube, qué se queda en local y cómo se opera**.

## 1. Qué es la nube, sin humo (CE RA3.a)

La «nube» no es magia: son **ordenadores de otros, alquilados por horas y gobernados por API**. Lo que cambia frente al servidor del armario es el modelo: pasas de comprar hierro (CAPEX) a pagar uso (OPEX), y de escalar comprando máquinas a escalar con dos clics.

**Niveles / modelos de servicio** — la pregunta clave es *qué gestionas tú y qué gestiona el proveedor*:

| Modelo | El proveedor gestiona | Tú gestionas | Ejemplo |
|---|---|---|---|
| **IaaS** (infraestructura) | Hardware, virtualización, red física | SO, aplicaciones, datos, copias | Un VPS en Hetzner/OVH con tu Debian + Odoo |
| **PaaS** (plataforma) | Todo lo anterior + SO, BBDD, runtime | Tu código y tus datos | Desplegar una app en un hosting gestionado o un DBaaS |
| **SaaS** (software) | Absolutamente todo | Solo tus datos y usuarios | Google Workspace, Microsoft 365, un CRM online |

!!! tip "Regla sysadmin"
    Cuanto más subes (IaaS → SaaS), menos control y menos trabajo operativo. Elige el nivel más alto que cumpla tus requisitos… salvo que el requisito sea precisamente el control (soberanía del dato, RGPD, latencia).

**Modelos de despliegue**: nube **pública** (recursos compartidos), **privada** (tu propio cloud con Proxmox/OpenStack) e **híbrida** (lo crítico en casa, los picos en la pública). En 2026 la híbrida es la opción por defecto de la pyme sensata.

## 2. Para qué sirve la nube en una empresa (CE RA3.b)

- **Procesar datos** sin comprar servidores (picos de facturación, informes pesados).
- **Intercambiar información** entre sedes y teletrabajadores (Nextcloud, VPN + nube).
- **Ejecutar aplicaciones** accesibles desde cualquier sitio (ERP, CRM, tienda online).
- **Sobrevivir a desastres**: la copia externa en otra región es tu póliza de seguros (recuerda la 3-2-1 de la UD1).

!!! example "Caso: gestoría de 12 personas"
    Servidor local de 2016 con el programa de nóminas + ficheros en carpetas compartidas. Migración: ficheros a Nextcloud en VPS (IaaS), nóminas en SaaS del proveedor, copia diaria cifrada a otra región y VPN WireGuard para el teletrabajo. Resultado: el robo o incendio de la oficina ya no es una catástrofe, y el coste mensual es menor que un contrato de mantenimiento del hierro viejo.

## 3. El borde: edge, fog y mist (CE RA3.c–d)

Enviar *todo* a la nube falla cuando necesitas **respuesta inmediata**, tienes **poco ancho de banda** o los datos **no deben salir** del recinto. Ahí entra la computación en el borde:

- **Edge computing**: procesar junto a la fuente. El mini-PC de la nave filtra los datos de 200 sensores y solo sube agregados cada 5 minutos. Menos latencia, menos tráfico, menos factura cloud.
- **Fog computing** («niebla»): una capa intermedia entre el borde y la nube —nodos locales (el servidor de la tienda, el gateway de la fábrica)— que pre-procesan y coordinan varios dispositivos edge.
- **Mist computing** («niebla fina»): el procesamiento baja hasta los propios dispositivos de red/sensores (microcontroladores que deciden solos: «si vibración > X, para el motor»).

```
[sensor] → mist (decide en ms) → fog (agrega por nave) → edge (panel local) → cloud (histórico + IA)
```

!!! example "Por qué no todo va a la nube"
    Una cámara de visión artificial que inspecciona 30 piezas/segundo no puede esperar la respuesta de un datacenter a 800 km: el análisis corre en una GPU local (edge); a la nube solo viajan las estadísticas y las fotos de piezas defectuosas. Latencia, ancho de banda y privacidad, resueltos de un plumazo.

## 4. Ventajas (y letra pequeña) en sistemas conectados (CE RA3.e)

**Ventajas reales**: elasticidad (crecer en campaña sin comprar nada), disponibilidad (SLA del 99,9 % que tu armario no da), acceso global, copias georredundantes y coste predecible.

**Letra pequeña que el ASIR debe vigilar**:

- **Dependencia y salida**: entrar es fácil; salir (egress de datos, formatos propietarios) es caro. Diseña la salida antes de entrar.
- **Seguridad compartida**: el proveedor protege *la* nube; tú proteges lo que pones *en* la nube (accesos, MFA, cifrado, copias).
- **Soberanía y RGPD**: datos personales preferiblemente en UE; revisa dónde replica tu proveedor.
- **Costes que se desbocan**: una VM olvidada encendida factura cada mes. Etiqueta, monitoriza y apaga lo que no se usa (FinOps casero con el panel de facturación + alertas).

## 5. Para practicar

- [Prácticas UD3](../practicas/UD3/index.md): diagrama de despliegue híbrido + comparativa IaaS/PaaS/SaaS.
- **Glosario mínimo del RA3**: IaaS, PaaS, SaaS, nube pública/privada/híbrida, CAPEX/OPEX, SLA, región/zona, edge, fog, mist, latencia, soberanía del dato, FinOps.
- **Autoevaluación**: ante una pyme con servidor local de 8 años, ¿qué llevarías a la nube, qué dejarías en local y dónde pondrías el edge? Justifica cada decisión con un riesgo y un coste.
