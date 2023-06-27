# Proyecto de Monitoreo Muscular

Este proyecto consiste en una solución de monitoreo muscular utilizando un Arduino y un modelo de clasificación. El objetivo es adquirir datos electromiográficos en dos condiciones: estado de reposo y estado de contracción muscular, y utilizar estos datos para realizar predicciones en tiempo real sobre el estado de contracción.

## Componentes del Proyecto

El proyecto consta de los siguientes elementos:

1. **Código Fuente**: El código está dividido en tres partes principales:

    - `codigo1.py`: Este archivo contiene las funciones necesarias para la adquisición de datos del Arduino, almacenamiento en archivos CSV y el ciclo de reposo y contracción muscular.

    - `codigo2.py`: Aquí se encuentra el código para procesar los archivos CSV generados por el código anterior, calculando características como la desviación estándar, la media, la amplitud y el periodograma de las señales. Estos datos se combinan en un solo DataFrame y se guardan en un archivo CSV final.

    - `codigo3.py`: Este archivo contiene el código para realizar la comunicación serial con el Arduino en tiempo real. Adquiere datos en tiempo real, calcula las características correspondientes y utiliza un modelo de clasificación previamente entrenado para realizar predicciones en tiempo real sobre el estado de contracción muscular.

2. **Modelo de Clasificación**: El modelo de clasificación utilizado para realizar las predicciones se guarda en un archivo de extensión `.pkl`. En este proyecto, se utiliza un modelo de árbol de decisión entrenado previamente. Puedes reemplazarlo con otro modelo si lo deseas.

3. **Archivos CSV**: Los datos adquiridos durante el ciclo de reposo y contracción muscular se guardan en archivos CSV separados. Estos archivos se procesan posteriormente para extraer características y generar un archivo CSV final con los datos procesados.

## Instrucciones de Uso

A continuación, se presentan las instrucciones para utilizar este proyecto:

1. Conexión del Arduino:
   - Conecta tu Arduino al puerto serie especificado en el código fuente (variable `puerto_serial` en `codigo1.py` y `codigo3.py`). Asegúrate de que el baud rate coincida con la configuración de tu Arduino (variable `baud_rate` en `codigo1.py` y `codigo3.py`).

2. Ejecución del Proyecto:
   - Ejecuta el archivo `codigo1.py` para realizar el ciclo de reposo y contracción muscular. Este código adquirirá datos del Arduino durante un período de tiempo específico para cada estado y los guardará en archivos CSV separados.

   - Luego, ejecuta el archivo `codigo2.py` para procesar los archivos CSV generados en el paso anterior. Este código calculará características adicionales a partir de los datos y generará un archivo CSV final llamado `features.csv`.

   - Finalmente, ejecuta el archivo `codigo3.py` para realizar la comunicación serial en tiempo real con el Arduino. Este código adquirirá datos en tiempo real, calculará las características correspondientes y utilizará el modelo de clasificación para realizar predicciones en tiempo real sobre el estado de contracción muscular.

## Dependencias

El proyecto utiliza las siguientes dependencias:

- `time`: Librería estándar de Python para trabajar con tiempos y esperas.
- `csv`: Librería estánd
