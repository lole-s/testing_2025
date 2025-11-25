# **GUÍA PRÁCTICA — REDES (Trabaja Práctico -Recuperatorio)**

**Tema:** IP – MAC – Cliente/Servidor
**Materiales:**

* 2 notebooks con Windows 10/11
* 1 cable de red **directo** (UTP común, Windows hace auto-MDI-X)
* Wireshark
* Visual Studio Code + extensión **Live Server**
* App: **Simon PROA** ([https://github.com/lole-s/simon-proa](https://github.com/lole-s/simon-proa))

---

# **1. Objetivo de la actividad**

Los estudiantes deberán:

* Conectar dos PC entre sí directamente.
* Configurar IP fija.
* Identificar la dirección MAC.
* Levantar un servidor web con Live Server.
* Acceder desde la otra PC como cliente.
* Ver tráfico básico (ARP, ICMP, HTTP) con Wireshark.

---

# **2. Paso 1 — Conectar las computadoras**

Conectar ambas notebooks entre sí usando **solo un cable de red** (sin router).

Windows 10/11 detecta automáticamente el tipo de cable (auto-MDI-X), por lo que funciona directamente.

---

# **3. Paso 2 — Configurar IP fija en ambos equipos**

### **Equipo A**

1. Inicio → Configuración → Red e Internet → **Cambiar opciones del adaptador**
2. Clic derecho en Ethernet → **Propiedades**
3. Seleccionar: **Protocolo de Internet versión 4 (TCP/IPv4)**
4. Configurar:

   * IP: `192.168.1.10`
   * Máscara: `255.255.255.0`
   * Gateway: dejar en blanco
   * DNS: dejar en blanco

### **Equipo B**

Configurar igual, pero con otra IP:

* IP: `192.168.1.20`
* Máscara: `255.255.255.0`

### **Comprobar conectividad**

Desde el Equipo A:

```
ping 192.168.1.20
```

Desde el Equipo B:

```
ping 192.168.1.10
```

Si responde: Conexión lista!m, sino: 1. buscar en internet que podría ser, 2. pedir ayuda

---

# **4. Paso 3 — Obtener la MAC**

En cada PC:

1. Abrir **CMD**
2. Ejecutar:

   ```
   ipconfig /all
   ```
3. Anotar **Dirección física** (formato XX-XX-XX-XX-XX-XX)

**Explicación breve:**
La dirección MAC (Media Access Control) es el identificador único que tiene cada placa de red del mundo.
Es como el DNI o la matrícula de la placa de red (es único por dispositivo y depende del Hardware, es decir del fabricante).

---

# **5. Paso 4 — Levantar el SERVIDOR con la app Simon PROA**

### **En el Equipo A (servidor):**

1. Instalar Visual Studio Code (si no está).
2. Abrir VSCode → Extensions → instalar **Live Server**.
3. Descargar la app Simon PROA:

   ```
   https://github.com/lole-s/simon-proa
   ```
4. Abrir la carpeta del proyecto desde VSCode.
5. Abrir `index.html`.
6. Clic derecho → **Open with Live Server**.

Esto abre un servidor web, normalmente en un puerto como:

```
http://192.168.1.10:5500
```

(La IP debe coincidir con la del Equipo A.)

### **Verificar**

Abrir el navegador del Equipo A y entrar a esa dirección.
Debe verse el **juego Simon PROA**.

---

# **6. Paso 5 — Acceder desde la otra PC (cliente)**

En el Equipo B:

1. Abrir el navegador.
2. Ingresar la IP del servidor:

```
http://192.168.1.10:5500
```

Si todo está bien, se cargará la página **Simon PROA**, pero servida por la otra notebook.

**Explicación breve:**

* El **Equipo A = servidor** (ofrece la página).
* El **Equipo B = cliente** (la descarga).
* Se comunican usando el puerto del SERVIDOR WEB(Live Server).( ¿que puerto usa? les voy a preguntar esto)

---

# **7. Paso 6 — Analizar con Wireshark (básico)**

### En cualquiera de los dos equipos:
0. Descargar e Instalar en caso de ser necesario
1. Abrir **Wireshark**.
2. Seleccionar la interfaz Ethernet.
3. Iniciar captura.

### Observar:

* **ARP** (preguntas “¿Quién tiene 192.168.1.x?”)

  ```
  arp
  ```
* **ICMP** al hacer ping

  ```
  icmp
  ```
* **HTTP** cuando el cliente carga la página

  ```
  http
  ```

---

# **8. Actividad final / pequeño informe**

Hacer un documento para entregar con un lindo títulos y que contenega los siguientes items:
- Las IP y MAC de ambos equipos.
- Captura de pantalla del ping funcionando
- Foto o captura del Simon PROA cargado desde la otra PC
- Captura de Wireshark mostrando ARP, ICMP y HTTP
- Breve explicación (3–5 líneas) de qué significa cliente/servidor

