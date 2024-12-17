import machine

# Inicializar el bus I2C
i2c = machine.I2C(0, scl=machine.Pin(13), sda=machine.Pin(12))  # Pines GPIO1 (SCL) y GPIO0 (SDA)
ds3231_address = 0x68  # Dirección I2C del DS3231

def bcd_to_decimal(bcd):
    """Convierte un número en formato BCD a decimal."""
    return (bcd >> 4) * 10 + (bcd & 0x0F)

def decimal_to_bcd(decimal):
    """Convierte un número decimal a formato BCD."""
    return ((decimal // 10) << 4) + (decimal % 10)

def set_time(year, month, day, hour, minute, second):
    """Configura la hora en el módulo DS3231."""
    i2c.writeto(ds3231_address, bytearray([
        0,  # Dirección de inicio para escritura
        decimal_to_bcd(second),
        decimal_to_bcd(minute),
        decimal_to_bcd(hour),
        0,  # Día de la semana (no usado)
        decimal_to_bcd(day),
        decimal_to_bcd(month),
        decimal_to_bcd(year - 2000)  # Solo los últimos dos dígitos del año
    ]))

def get_time():
    """Lee la hora desde el módulo DS3231."""
    i2c.writeto(ds3231_address, bytearray([0]))  # Dirección de inicio para lectura
    data = i2c.readfrom(ds3231_address, 7)  # Leer 7 bytes de datos
    second = bcd_to_decimal(data[0])
    minute = bcd_to_decimal(data[1])
    hour = bcd_to_decimal(data[2])
    day = bcd_to_decimal(data[4])
    month = bcd_to_decimal(data[5])
    year = bcd_to_decimal(data[6]) + 2000
    return year, month, day, hour, minute, second

#set_time(2024, 12, 5, 10,38,20)