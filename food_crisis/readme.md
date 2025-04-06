# Proyecto Análisis de Precios de Comida en el mundo 

Este proyecto tiene como objetivo analizar el conjunto de datos de precios de alimentos del programa mundial de alimentos (WFP), que proporciona información sobre los precios de alimentos en diferentes países a lo largo del tiempo. El análisis incluye la limpieza de datos, exploración, visualización interactiva y la implementación de modelos de Machine Learning y Deep Learning para predecir fluctuaciones en los precios de los alimentos y estudiar cómo las políticas económicas y comerciales afectan los mercados globales.


##  Objetivo

Este conjunto de datos permite analizar las tendencias o variaciones a lo largo del tiempo del costo de productos básicos en diferentes países. 

Se pretende estudiar la crisis de abastecimiento y cómo los 
aranceles comerciales afectan los precios de los alimentos 
a nivel mundial. 

El objetivo de este proyecto será desarrollar un modelo para predecir fluctuaciones de precios y evaluar el impacto de políticas económicas en la seguridad alimentaria.


## Estructura

En el contenido de este proyecto se encuentra una carpeta
data que contiene el dataset que se va a usar.

En la carpeta graphics se guardan las imágenes generadas por 
el script notebook de Python.

En el archivo food_prices_analysis.ipynb se encuentra el análisis de datos y modelado del dataset de precios de alimentos globales.

Esto incluye los siguientes puntos: 

## ETL: Carga y limpieza de datos

En esta etapa, se realiza el proceso de extracción, transformación y carga (ETL) de los datos. Los datos se cargan desde el conjunto de datos de Kaggle, se limpian (eliminando o imputando valores faltantes), se transforman (normalización y escala de variables) y se organizan en un formato adecuado para su posterior análisis.


## EDA: Análisis Exploratorio de Datos y estadísticas avanzadas

El Análisis Exploratorio de Datos (EDA) se lleva a cabo para comprender mejor las características del conjunto de datos. Se exploran patrones, distribuciones y relaciones entre variables utilizando medidas estadísticas básicas, análisis de correlación y pruebas de hipótesis. Además, se calculan estadísticas avanzadas para obtener una visión detallada de los datos y su comportamiento.


## Visualización interactiva con Seaborn, Matplotlib y Potly

Se utilizan herramientas de visualización como Seaborn, Matplotlib y Plotly para crear gráficos estáticos e interactivos. Estas visualizaciones ayudan a comprender mejor las tendencias y patrones en los datos, mostrando distribuciones, correlaciones y la evolución temporal de los precios de los alimentos. Las gráficas interactivas proporcionan una manera efectiva de explorar los datos en profundidad y obtener insights claros.


## Modelos de Machine Learning 

En este proyecto, se implementan varios modelos de Machine Learning para predecir los precios de los alimentos y analizar patrones de variabilidad.

### Random Forest
El Random Forest es un modelo basado en un conjunto de árboles de decisión. Este enfoque es robusto frente al sobreajuste y es capaz de capturar relaciones no lineales entre las variables. Se utiliza para mejorar la precisión de las predicciones sobre los precios de los alimentos.

## Optimización y escalabilidad
El proyecto también tiene en cuenta la optimización y la escalabilidad de los modelos y el proceso de análisis de datos. Se aplican técnicas avanzadas para mejorar el rendimiento del modelo, como la selección de características, la regularización, y la optimización de hiperparámetros. 