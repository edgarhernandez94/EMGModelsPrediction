import serial
import pandas as pd
import numpy as np
import joblib

# Configuración de la comunicación serial
puerto_serial = 'COM9'  # Reemplaza 'COM9' con el puerto serial correcto
baud_rate = 9600  # Ajusta el baud rate según la configuración de tu Arduino

# Cargar el modelo desde el archivo pkl
model = joblib.load('decision_tree_model.pkl')

def calcular_features(datos):
    df = pd.DataFrame(data=datos, columns=['data1', 'data2'])
    df['SD'] = np.std(df[['data1', 'data2']], axis=1)
    df['Mean'] = np.mean(df[['data1', 'data2']], axis=1)
    df['Amplitud'] = np.max(df[['data1', 'data2']], axis=1) - np.min(df[['data1', 'data2']], axis=1)
    return df[['SD', 'Mean', 'Amplitud']]

def realizar_prediccion(features):
    # Hacer la predicción utilizando el modelo cargado
    prediccion = model.predict(features)

    # Imprimir la predicción (0 o 1)
    print("Predicción:")
    print(prediccion)

# Inicializar la comunicación serial con Arduino
arduino = serial.Serial(puerto_serial, baud_rate, timeout=1)

# Inicializar la lista de datos en tiempo real
datos_arduino = []

while True:
    if arduino.in_waiting > 0:
        linea = arduino.readline().decode('utf-8').strip()
        valores = linea.split(',')  # Separar los valores por la coma
        if len(valores) == 2:
            data1 = int(valores[0])
            data2 = int(valores[1])
            datos_arduino.append([data1, data2])

        # Si se han recibido suficientes datos, realizar la clasificación
        if len(datos_arduino) >= 1:
            # Calcular los features en tiempo real
            features = calcular_features(datos_arduino)

            # Realizar la predicción en tiempo real
            realizar_prediccion(features)

            # Limpiar la lista de datos para la próxima clasificación
            datos_arduino = []

# Cerrar la comunicación serial con Arduino
arduino.close()
