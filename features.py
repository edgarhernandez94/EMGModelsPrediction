import os
import pandas as pd
import numpy as np

# Paso 1: Obtener la lista de archivos CSV en la carpeta actual
csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]

# Paso 2: Procesar cada archivo CSV
dataframes = []
for file in csv_files:
    # Cargar el archivo CSV
    data = pd.read_csv(file)
    
    # Calcular las características SD, Mean y Amplitud
    data['SD'] = np.std(data[['data1', 'data2']], axis=1)
    data['Mean'] = np.mean(data[['data1', 'data2']], axis=1)
    data['Amplitud'] = np.max(data[['data1', 'data2']], axis=1) - np.min(data[['data1', 'data2']], axis=1)
    
    # Agregar el dataframe procesado a la lista
    dataframes.append(data[['SD', 'Mean', 'Amplitud', 'label']])

# Paso 3: Combinar los dataframes en uno solo
features = pd.concat(dataframes, ignore_index=True)

# Paso 4: Guardar los datos en un nuevo archivo CSV
features.to_csv('features.csv', index=False)
