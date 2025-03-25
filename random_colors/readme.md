# Proyecto de Análisis y Visualización de Datos en Python

## Autor
Nerea Valdés Egocheaga

## Descripción
Este proyecto demuestra habilidades en Python mediante la organización de código, análisis de datos y visualización de datos. Se estructura en carpetas para una mejor organización.

## Estructura del Proyecto

El proyecto presenta la siguiente estructura de carpetas y archivos.

requirements.txt: Lista de dependencias del proyecto.

### data

dataset.csv: Un archivo de datos de ejemplo generado que usaremos para el análisis y visualización.

### scripts

analysis.py: Script que contiene funciones para el análisis de datos. Por ejemplo, cargará dataset.csv, calculará estadísticas descriptivas, etc.

visualization.py: Script que utiliza matplotlib para crear gráficos basados en los datos de dataset.csv.


### utils

helpers.py: Módulo con funciones auxiliares que podrían ser utilizadas en los scripts principales para tareas repetitivas o comunes.

## Instalación y uso 

1. Clona el repositorio o descarga los archivos.
2. Instala las dependencias
    El archivo requirements contiene las dependencias de este proyecto que son:
        numpy: para generar datos aleatorios
        pandas: para manipular datos
        matplotlib: para visualizar datos

   ```bash
   pip install -r requirements.txt

3. Genera el dataset de ejemplo ejecutando:
    ```bash 
    python utils/helpers.py

4. Realiza el análisis de los datos con el comando:
    ```bash 
    python scripts/analysis.py

5. Visualiza los datos con:
    ```bash 
    python scripts/visualization.py