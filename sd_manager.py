import machine
import sdcard
import uos

def montar_sd(directorio="/sd"):
    """
    Monta la tarjeta SD en el directorio especificado.
    Si el montaje falla, se lanza una excepción.
    
    Args:
        directorio (str): Directorio donde se montará la tarjeta SD.

    Returns:
        bool: True si el montaje es exitoso.
    """
    spi = machine.SPI(0,
                      baudrate=50000,  # Velocidad baja
                      polarity=0,
                      phase=0,
                      bits=8,
                      firstbit=machine.SPI.MSB,
                      sck=machine.Pin(2),
                      mosi=machine.Pin(3),
                      miso=machine.Pin(4))
    cs = machine.Pin(1, machine.Pin.OUT)

    try:
        sd = sdcard.SDCard(spi, cs)
        print("Tarjeta SD detectada.")

        # Monta directamente el sistema de archivos
        vfs = uos.VfsFat(sd)
        uos.mount(vfs, directorio)
        print(f"Sistema de archivos montado en {directorio}.")
        return True
    except Exception as e:
        print(f"Error al montar la tarjeta SD: {e}")
        return False

def directorio_existe(directorio):
    """
    Verifica si un directorio existe.

    Args:
        directorio (str): Ruta del directorio a verificar.

    Returns:
        bool: True si el directorio existe, False en caso contrario.
    """
    try:
        uos.listdir(directorio)
        return True
    except OSError:
        return False
