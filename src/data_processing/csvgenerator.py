import time
import csv
import serial

# Configuración de la comunicación serial
puerto_serial = 'COM9'  # Reemplaza 'COM9' con el puerto serial correcto
baud_rate = 9600  # Ajusta el baud rate según la configuración de tu Arduino

def mostrar_mensaje(mensaje, duracion):
    print(mensaje)
    time.sleep(duracion)

def recibir_datos_arduino():
    arduino = serial.Serial(puerto_serial, baud_rate, timeout=1)
    arduino.flushInput()

    datos = []

    inicio = time.time()
    while time.time() - inicio < 5:  # Recoger datos durante 5 segundos
        try:
            linea = arduino.readline().decode('utf-8').strip()
            valores = linea.split(',')  # Separar los valores por la coma
            if len(valores) == 2:
                data1 = int(valores[0])
                data2 = int(valores[1])
                datos.append([data1, data2])
        except Exception as e:
            print(f"Error al leer los datos: {e}")
            break

    arduino.close()
    return datos

def guardar_en_csv(data, label, writer):
    for d in data:
        writer.writerow(d + [label])

def ciclo_rest_contraccion():
    timestamp = int(time.time())
    with open(f"datos_rest_{timestamp}.csv", 'w', newline='') as archivo_rest, open(f"datos_contraccion_{timestamp}.csv", 'w', newline='') as archivo_contraccion:
        writer_rest = csv.writer(archivo_rest)
        writer_contraccion = csv.writer(archivo_contraccion)

        writer_rest.writerow(['data1', 'data2', 'label'])
        writer_contraccion.writerow(['data1', 'data2', 'label'])

        for _ in range(4):
            mostrar_mensaje("REST", 5)

            # Realizar la recepción de datos durante el ciclo de "REST"
            datos_rest = recibir_datos_arduino()
            guardar_en_csv(datos_rest, 0, writer_rest)

            mostrar_mensaje("CONTRACCION", 5)

            datos_contraccion = recibir_datos_arduino()
            guardar_en_csv(datos_contraccion, 1, writer_contraccion)

# Mostrar "INICIO" durante 3 segundos
print("INICIO")
time.sleep(3)

# Mostrar rest y contracción en secuencia
ciclo_rest_contraccion()
