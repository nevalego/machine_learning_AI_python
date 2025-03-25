# Proyecto de Análisis Estadístico y Visualización de Datos en Python con un proyecto Kaggle

## Autor
Nerea Valdés Egocheaga

## Descripción

Se va a utilizar un conjunto de datos de la plataforma Kaggle que se llama "Social Media Sentiment Analysis". 

* https://www.kaggle.com/datasets/abdullah0a/social-media-sentiment-analysis-dataset

Este dataset contiene comentarios de redes sociales recopilados de plataformas como Reddit y Twitter.
El propósito es comprender mejor este conjunto de datos de redes sociales mediante un análisis exhaustivo del dataset obteniendo insights valiosos y presentandolos de manera clara con diferentes visualizaciones. 


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
    El archivo requirements contiene las dependencias de este proyecto, de las cuales las principales son:
        
    * pandas → Para la manipulación de datos.

    * numpy → Para cálculos numéricos.

    * matplotlib → Para visualización básica.

    * seaborn → Para gráficos estadísticos.

    * jupyterlab → Para trabajar en notebooks.

    Para generar el archivo automáticamente se puede usar:
   ```bash
   pip freeze > requirements.txt

3. Carga y prepara el dataset ejecutando el notebook notebooks/data_preparation.ipynb

4. Realiza el análisis estadístico de los datos ejecutando el notebook notebooks/statistical_analysis.ipynb

5. Visualiza los datos ejecutando el notebook notebooks/data_visualization.ipynb


## Análisis final y conclusiones