# Prácticas UD02: Hardening y Auditoría de Seguridad

## Práctica 2.1: Endurecimiento (Hardening) de Servidores y Análisis de Puertos

### Objetivo
Aplicar técnicas de bastionado en un entorno simulado y comprobar la reducción de la superficie de ataque mediante escaneo de puertos.

### Tareas a Realizar
1. **Auditoría inicial**:
   - Ejecutar un escaneo de puertos locales/remotos mediante `nmap` para identificar servicios expuestos.
   ```bash
   nmap -sV -p- <ip_objetivo>
   ```
2. **Aplicación de medidas de hardening**:
   - Desactivación de servicios no requeridos (ej. Telnet, FTP sin cifrar, SNMP público).
   - Configuración de reglas estrictas en el cortafuegos (iptables / UFW / Firewalld).
3. **Verificación posterior**:
   - Comprobar que los puertos cerrados ya no responden a conexiones externas.

### Cuestiones de Comprobación
- ¿Qué diferencia existe entre un escaneo de puertos SYN (`-sS`) y un escaneo connect (`-sT`)?
- ¿Por qué el principio de mínimo privilegio reduce el impacto de una brecha de seguridad?
