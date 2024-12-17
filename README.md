# <div align="center">**Proyecto de Monitoreo de la Calidad del Aire**</div>

Este repositorio contiene los archivos y la información necesaria para implementar un sistema de monitoreo ambiental que utiliza un microcontrolador, sensores y almacenamiento en una tarjeta SD. El proyecto incluye la lectura de parámetros de calidad del aire, temperatura y humedad, con capacidad de registro en tiempo real gracias al módulo DS3231 y almacenamiento en una tarjeta SD.

---

## <div align="center">**Requisitos**</div>

- **Hardware:**
  - Raspberry Pi Pico. <img src="https://cdn0.iconfinder.com/data/icons/flat-round-system/512/raspberry-512.png" alt="Raspberry" width="25px" height="25px">
  - Sensores MQ135 y DHT11.
  - Módulo DS3231. <img src="https://github.com/user-attachments/assets/5d843261-7b65-420f-99b1-73e55835d2a2" alt="time" width="25px" height="25px">
  - Módulo de tarjeta SD. <img src="https://github.com/user-attachments/assets/cfc1c692-7575-4d88-987b-36bd0772bbb0" alt="Raspberry" width="25px" height="25px">
  - Protoboard y cables de conexión. <img src="https://github.com/user-attachments/assets/a1f984f3-760c-44f6-866c-1b4f400f03a0" alt="Raspberry" width="30px" height="25px">

- **Software:**
  - MicroPython instalado en el microcontrolador. <img src="https://github.com/user-attachments/assets/3a4e22bd-00fa-446a-b890-a409270a4937" alt="time" width="25px" height="25px">
  - Herramienta de desarrollo como Thonny IDE. <img src="https://github.com/user-attachments/assets/d8c96d92-d5bc-4de3-a065-1c212fbdc632" alt="time" width="25px" height="25px">

---

## <div align="center">**Componentes del Proyecto**</div>

1. **Microcontrolador:** Raspberry Pi Pico.
   
3. **Sensores:**
   
   - **MQ135:** Para medir calidad del aire (CO, CO2, etanol, NH4, tolueno y acetona).
   - **DHT11:** Para medir temperatura y humedad.
     
5. **Módulos adicionales:**
   
   - **DS3231:** Reloj en tiempo real (RTC).
   - **Tarjeta SD:** Para almacenamiento de datos.
     
7. **Protoboard y cables de conexión.**

  > [!WARNING]  
  > Asegurate de usar los mismos pines de conexión o edita el codigo segun tu necesidad
---

## <div align="center">**Archivos del Proyecto**</div>

### **1. `main.py`**

   - Programa principal para la captura de datos.
   - Funcionalidades:
     - Lectura de datos de sensores.
     - Registro de datos en un archivo CSV en la tarjeta SD.
     - Logs del sistema para control de eventos.

### **2. `ds3231.py`**

   - Librería para interactuar con el módulo DS3231.
   - Funciones principales:
     - Configuración de fecha y hora.
     - Lectura de la hora actual.

### **3. `sd_manager.py`**

   - Gestión de la tarjeta SD.
   - Funciones principales:
     - Montaje y verificación del sistema de archivos.
     - Creación de directorios y escritura de archivos.

### 4. **`sdcard.py`**

   - Controlador de bajo nivel para la tarjeta SD.
   - Compatible con el sistema de archivos de MicroPython.

---

## <div align="center">**Diagrama de conexiones**</div>

![Hernesto-diagrama](https://github.com/user-attachments/assets/3fe12d5e-5e2f-449d-8cac-cac1d03efe41)

---

## <div align="center">**Uso del Proyecto**</div>

1. **Carga de Archivos:**
   
   - Sube los archivos del repositorio (`main.py`, `ds3231.py`,  `sd_manager.py`, `sdcard.py`) al sistema de archivos del microcontrolador.
     
3. **Configuración Inicial:**
   
   - Ajusta los parámetros necesarios en `main.py` (por ejemplo, la fecha/hora inicial en caso de ser necesario).
     
     
    ```bash
    from ds3231 import set_time

  
    set_time(año, mes, dia, hora, minuto, segundo)  # Ejecuta esto UNA VEZ y luego coméntalo
    ```
     
5. **Ejecución:**
   - Ejecuta el archivo `main.py` desde el IDE para iniciar el monitoreo y registro de datos.
     
6. **Análisis de Datos:**
   - Extrae la tarjeta SD para analizar los datos almacenados en formato CSV.

---

## <div align="center">**Contribuciones**</div>

Si deseas contribuir a este proyecto, puedes hacerlo mediante **pull requests** o reportando problemas en la sección de **issues**.

---

## Creditos y Agradecimientos

### **Contribuyentes :**

- [@SamuelEscalante](https://github.com/SamuelEscalante)
- [@ManuelaMayorga](https://github.com/ManuelaMayorga)
- [@MarianaMera12](https://github.com/MarianaMera12)
- [@EmmanuelQuintero](https://github.com/EmmanuelQuintero)
- [@mdlangeles](https://github.com/mdlangeles)
  
¡Gracias por visitar nuestro repositorio! Esperamos que encuentre útil este proyecto. Si ha sido útil o simplemente te gustó, ¡considera darle una estrella al repositorio! 🌟

Nos encantaría escuchar sus comentarios, sugerencias o contribuciones.

¡Gracias por tu apoyo! 👋
