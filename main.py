import time
import dht
from MQ135 import MQ135  # Asegúrate de tener esta librería para el MQ135
from ds3231 import get_time  # Importa la función desde el módulo DS3231
import os
from sd_manager import montar_sd, directorio_existe

# Ruta para guardar los archivos en la tarjeta SD
directorio_sd = "/sd"
archivo_txt = f"{directorio_sd}/datos_gases_y_clima_calibrados.txt"
archivo_logs = f"{directorio_sd}/logs_sistema.txt"  # Archivo para logs

# Intentar montar la tarjeta SD
if not directorio_existe(directorio_sd):
    if not montar_sd(directorio_sd):
        print("No se pudo montar la tarjeta SD. Saliendo del programa.")
        raise SystemExit

# Función para escribir datos en el archivo de logs
def escribir_log(mensaje):
    """Registra eventos en el archivo de log."""
    year, month, day, hour, minute, second = get_time()
    formatted_time = f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"
    with open(archivo_logs, mode='a') as log_file:
        log_file.write(f"{formatted_time} - {mensaje}\n")

# Función para verificar si un archivo existe y contiene datos
def archivo_existe_y_tiene_datos(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return archivo.readline() != ''
    except OSError:
        return False

# Verificar si el archivo ya tiene datos, si no escribir la cabecera
if not archivo_existe_y_tiene_datos(archivo_txt):
    with open(archivo_txt, mode='w') as archivo:
        archivo.write("Timestamp,CO (ppm),CO2 (ppm),Ethanol (ppm),NH4 (ppm),Tolueno (ppm),Acetone (ppm),Temperatura (°C),Humedad (%)\n")

# Inicializar el sensor MQ135 y DHT11
mq135 = MQ135()
sensor_dht11 = dht.DHT11(machine.Pin(6))
ultimo_registro = time.time()

try:
    print("Iniciando medición de gases y clima...\n")
    escribir_log("Inicio de la medición de gases y clima.")
    
    while True:
        try:
            sensor_dht11.measure()
            temp_dht11 = sensor_dht11.temperature()
            hum_dht11 = sensor_dht11.humidity()
            escribir_log("Sensor DHT11 funcionando")
        except OSError:
            print("Error al leer el sensor DHT11")
            escribir_log("Error al leer el sensor DHT11")
            temp_dht11 = None
            hum_dht11 = None

        if temp_dht11 is not None and hum_dht11 is not None:
            CO = mq135.get_calibrated_CO(temp_dht11, hum_dht11)
            CO2 = mq135.get_calibrated_CO2(temp_dht11, hum_dht11)
            Ethanol = mq135.get_calibrated_Ethanol(temp_dht11, hum_dht11)
            NH4 = mq135.get_calibrated_NH4(temp_dht11, hum_dht11)
            Tolueno = mq135.get_calibrated_Toluene(temp_dht11, hum_dht11)
            Acetone = mq135.get_calibrated_Acetone(temp_dht11, hum_dht11)
            escribir_log("Nuevo registro añadido")

        year, month, day, hour, minute, second = get_time()
        formatted_time = f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"

        print(f"{formatted_time} - CO: {CO} ppm, CO2: {CO2} ppm, Ethanol: {Ethanol} ppm, NH4: {NH4} ppm, Tolueno: {Tolueno} ppm, Acetone: {Acetone} ppm, Temp: {temp_dht11}°C, Hum: {hum_dht11}%")
        print("-----\n")

        # Guardar los datos en el archivo
        with open(archivo_txt, mode='a') as archivo:
            archivo.write(f"{formatted_time},{CO},{CO2},{Ethanol},{NH4},{Tolueno},{Acetone},{temp_dht11},{hum_dht11}\n")

        tiempo_transcurrido = time.time() - ultimo_registro
        escribir_log(f"Tiempo desde el último registro: {tiempo_transcurrido:.2f} segundos")
        ultimo_registro = time.time()

        time.sleep(2)

except KeyboardInterrupt:
    print("Medición detenida por el usuario.")
    escribir_log("Medición detenida por el usuario.")
