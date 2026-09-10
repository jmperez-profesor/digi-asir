# UD6: Ciberseguridad (RA5 · 3 h)

> **Resultado de aprendizaje**: valorar la importancia de la seguridad y su regulación en relación con los datos (CE RA5.i). Ponderación dentro del RA5: **14 %** conjunto con la UD5 (80 % actividades + 20 % cuestionario). Enfoque: **lo que el administrador debe proteger, cómo y con qué norma en la mano**.

## 1. Por qué la seguridad es tu problema (CE RA5.i)

Los datos son el activo más robado del siglo: historiales de clientes, nóminas, credenciales bancarias. Un solo incidente puede parar la empresa (ransomware), vaciar cuentas (fraude) o costar una sanción (RGPD). Y el eslabón más atacado no es el cortafuegos: es la **persona** que abre el adjunto.

La tríada que lo resume todo (**CIA**):

- **Confidencialidad**: solo quien debe, accede (permisos, cifrado).
- **Integridad**: nadie lo altera sin dejar rastro (hashes, firmas, control de versiones).
- **Disponibilidad**: está cuando se necesita (copias, redundancia, anti-DDoS).

## 2. Amenazas habituales en la pyme (CE RA5.i)

| Amenaza | Cómo entra | Defensa del ASIR |
|---|---|---|
| **Phishing** | Correo/SMS que suplanta al banco o al jefe | Filtros antispam, MFA (la contraseña robada no basta) y formación con simulacros |
| **Malware / ransomware** | Adjunto, USB, software pirata | Antimalware, parches al día, copias offline que el ransomware no alcance |
| **Fuerza bruta** | Probar miles de claves contra SSH/RDP/web | Claves largas + MFA, fail2ban, no exponer gestión a internet |
| **Ingeniería social** | Engañar a una persona, no a una máquina | Procedimientos (verificar por segunda vía) y cultura de desconfianza sana |
| **Wifi insegura / MITM** | Red abierta o falsa en hotel, cliente, feria | VPN siempre fuera de la oficina; nada sensible en redes ajenas |
| **Robo de identidad** | Suplantar a un usuario con sus datos | Gestión de identidades: altas/bajas puntuales, mínimo privilegio, revisión periódica |

!!! example "Lunes 8:00 en una asesoría"
    Un empleado abre «factura pendiente.exe». A las 8:20 todos los documentos muestran extensión rara: ransomware. Diferencia entre drama y anécdota: copia externa del viernes + inventario de sistemas + procedimiento escrito (aislar, no pagar de inmediato, avisar). La empresa que lo tenía volvió a trabajar a mediodía; la que no, cerró dos semanas.

## 3. Medidas: el kit mínimo del administrador (CE RA5.i)

1. **Contraseñas y MFA**: largas y únicas (gestor), doble factor en todo lo expuesto. Adiós a `Empresa123`.
2. **Copias 3-2-1**: 3 copias, en 2 soportes distintos, 1 externa/offline. Y **probar la restauración**: la copia no probada no existe.
3. **Parches y ciclo de vida**: SO y aplicaciones al día; plan de sustitución para lo obsoleto (un Windows sin soporte es una puerta abierta).
4. **Mínimo privilegio y segmentación**: cada usuario y equipo, solo lo necesario; invitados e IoT en VLAN separada.
5. **Cifrado**: disco (BitLocker/LUKS), tráfico (HTTPS, VPN) y copias cifradas.
6. **Registro y monitorización**: logs centralizados y alertas; sin registro no hay investigación posible tras un incidente.

## 4. Normativa que te obliga (CE RA5.i)

- **RGPD + LOPDGDD**: datos personales solo con base legítima, mínimos y seguros; derechos de los interesados (acceso, supresión…); brechas graves se notifican en **72 h**. Para el ASIR: cifrado, control de accesos, registro de tratamientos y borrado real (relee la fase 7 de la UD5).
- **ENS (Esquema Nacional de Seguridad)**: medidas mínimas para sistemas de la Administración y sus proveedores. Referencia útil aunque seas privado.
- **NIS2 (2026, plenamente aplicable)**: más sectores obligados (energía, salud, digital…), notificación de incidentes en 24 h y **responsabilidad directa de la dirección**. La ciberseguridad deja de ser «cosa de informática».
- **AI Act y VeriFactu**: si despliegas IA o software de facturación, también hay requisitos que auditar.

!!! tip "Plan director para pyme (una página basta)"
    Inventario de activos → riesgos principales → 5 medidas del apartado 3 con responsable y fecha → procedimiento de incidente (aislar, copiar evidencias, avisar, restaurar) → revisión anual. Eso, firmado por dirección, ya es un plan director serio.

## 5. Teletrabajo y cultura (CE RA5.i)

El perímetro ya no es la oficina: es cada portátil. Reglas mínimas: VPN + MFA, disco cifrado, bloqueo automático, nada de equipos personales para datos críticos sin MDM, y formación continua (el clic imprudente se entrena, no se regaña).

> **Nota de fuentes**: el PDF del centro etiquetado como UD6 trata en realidad del *plan de transformación digital* (§6.1–6.2), por lo que se archiva como apoyo de la **UD7**; estos apuntes desarrollan el CE RA5.i con la §5.3 del material de UD5 y normativa vigente (RGPD, ENS, NIS2). Ver `FUENTES.md`.

## 6. Para practicar

- [Prácticas UD6](../practicas/UD6/index.md): protocolo de seguridad básico + cuestionario de amenazas y RGPD.
- **Glosario mínimo (CE RA5.i)**: CIA, phishing, ransomware, MFA, fuerza bruta, MITM, copia 3-2-1, bastionado, ENS, RGPD, NIS2, plan director, incidente/brecha (72 h / 24 h).
- **Autoevaluación**: audita tu aula-taller con la tabla del apartado 2: amenaza, ¿existe aquí?, medida aplicada o pendiente.
