import os
import pandas as pd

# Ruta de la carpeta que contiene los archivos CSV
carpeta = 'C:/Users/edgar/OneDrive/Escritorio/Juanjoproject'

# Obtener la lista de archivos CSV en la carpeta
csv_files = [file for file in os.listdir(carpeta) if file.endswith('.csv')]

# Variables para el seguimiento del archivo con menor número de filas
min_filas = float('inf')
archivo_min_filas = None

# Recorrer cada archivo CSV y obtener su tamaño de filas
for file in csv_files:
    # Construir la ruta completa del archivo
    archivo_csv = os.path.join(carpeta, file)
    
    # Leer el archivo CSV
    df = pd.read_csv(archivo_csv)
    
    # Obtener el número de filas
    filas = df.shape[0]
    
    # Verificar si es el archivo con menor número de filas hasta el momento
    if filas < min_filas:
        min_filas = filas
        archivo_min_filas = file

# Calcular el número de filas divisible entre 100 más cercano
num_filas_divisible = min_filas - (min_filas % 100)

# Recorrer cada archivo CSV y truncar a num_filas_divisible
for file in csv_files:
    # Construir la ruta completa del archivo
    archivo_csv = os.path.join(carpeta, file)
    
    # Leer el archivo CSV
    df = pd.read_csv(archivo_csv)
    
    # Truncar el DataFrame al número de filas divisible entre 100
    df_truncado = df.head(num_filas_divisible)
    
    # Guardar el DataFrame truncado en el mismo archivo CSV
    df_truncado.to_csv(archivo_csv, index=False)