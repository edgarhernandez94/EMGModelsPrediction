import os
import pandas as pd
import numpy as np
from scipy.signal import periodogram

# Paso 1: Obtener la lista de archivos CSV en la carpeta actual
csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]

# Paso 2: Procesar cada archivo CSV
dataframes = []
prev_amplitude_signal1 = None
prev_amplitude_signal2 = None
for file in csv_files:
    # Cargar el archivo CSV
    data = pd.read_csv(file)

    # Iterar por el DataFrame en grupos de 20 filas
    for i in range(0, len(data), 20):
        segment = data[i:i+20]

        if not segment.empty:
            # Obtener los datos del DataFrame
            datos1 = segment['data1'].values  
            datos2 = segment['data2'].values  
            label = segment.iloc[0, -1]  # Usar el primer label del segmento

            # Calcular las características
            integral_signal1 = np.sum(datos1)
            media_signal1 = np.mean(datos1)
            desviacion_estandar_signal1 = np.std(datos1)
            amplitud_maxima_signal1 = np.max(datos1) - np.min(datos1)
            integral_signal2 = np.sum(datos2)
            media_signal2 = np.mean(datos2)
            desviacion_estandar_signal2 = np.std(datos2)
            amplitud_maxima_signal2 = np.max(datos2) - np.min(datos2)

            # Calcular el periodograma y la frecuencia de las señales
            frecuencia1, periodograma1 = periodogram(datos1)
            frecuencia2, periodograma2 = periodogram(datos2)
            
            # Calcular el valor máximo del periodograma
            max_periodograma1 = np.max(periodograma1)
            max_periodograma2 = np.max(periodograma2)

            # Calcular el Porcentaje de fatiga
            if prev_amplitude_signal1 is not None:
                fatigue_percentage_signal1 = amplitud_maxima_signal1 - prev_amplitude_signal1
            else:
                fatigue_percentage_signal1 = np.nan  # Para el primer registro no hay amplitud anterior
            
            if prev_amplitude_signal2 is not None:
                fatigue_percentage_signal2 = amplitud_maxima_signal2 - prev_amplitude_signal2
            else:
                fatigue_percentage_signal2 = np.nan  # Para el primer registro no hay amplitud anterior

            # Actualizar los valores de la amplitud anterior
            prev_amplitude_signal1 = amplitud_maxima_signal1
            prev_amplitude_signal2 = amplitud_maxima_signal2

            # Crear un nuevo DataFrame con las características
            features = pd.DataFrame({
                'Integral_Signal1': [integral_signal1],
                'Media_Signal1': [media_signal1],
                'Standard_Deviation_Signal1': [desviacion_estandar_signal1],
                'Amplitude_Signal1': [amplitud_maxima_signal1],
                'Max_Periodogram_Signal1': [max_periodograma1],
                'Fatigue_Percentage_Signal1': [fatigue_percentage_signal1],
                'Integral_Signal2': [integral_signal2],
                'Media_Signal2': [media_signal2],
                'Standard_Deviation_Signal2': [desviacion_estandar_signal2],
                'Amplitude_Signal2': [amplitud_maxima_signal2],
                'Max_Periodogram_Signal2': [max_periodograma2],
                'Fatigue_Percentage_Signal2': [fatigue_percentage_signal2],
                'Label': [label]  # Nota el cambio aquí, ahora estamos pasando una lista
            })

            dataframes.append(features)

# Paso 3: Combinar los dataframes en uno solo
features = pd.concat(dataframes, ignore_index=True)

# Paso 4: Guardar el DataFrame en un archivo CSV
features.to_csv('features.csv', index=False)
