"""
Modulo de obtención de datos. Este modulo realiza dos funciones en el siguiente orden:
1. Cargar el dataset de medidas del año 2019 y desechar 4 columnas sin información relevante para el informe
2. Definir dos diccionarios para interpretar las claves del dataset: diccionario_estaciones y diccionario_magnitudes
   según la documentación obtenida en https://datos.madrid.es/FWProjects/egob/Catalogo/MedioAmbiente/Aire/Ficheros/Interprete_ficheros_%20calidad_%20del_%20aire_global.pdf
"""

import os
import pandas as pd
import time
from datetime import date
from src.diccionarios import *

dataset2019=pd.read_csv('./input/datos201912.csv', sep=';').drop(columns=['PROVINCIA',"MUNICIPIO","PUNTO_MUESTREO","ANO"],axis=0)

def format_day_month():
    today = date.today()
    dia,mes,ano = today.strftime("%d"),today.strftime("%m"),today.strftime("%y")
    dia,verificacion_dia="D"+dia, "V"+dia
    return dia, verificacion_dia, int(mes),ano


def get_last_year_data(estacion,dataset=dataset2019):
    dia, verificacion, mes,ano=format_day_month()
    datos_ano_pasado=dataset.copy() #Esto es necesario para evitar problemas con la variable almacenada
    datos_ano_pasado=datos_ano_pasado.loc[dataset.ESTACION==int(estacion)].loc[dataset.MES==mes].loc[dataset[verificacion]!='N'][['MAGNITUD',dia]]
    datos_ano_pasado['Valores']=datos_ano_pasado[dia]
    datos_ano_pasado['Magnitudes']=[diccionario_magnitudes[tecnica]['Name'] for tecnica in datos_ano_pasado['MAGNITUD']]
    datos_ano_pasado['Abreviatura']=[diccionario_magnitudes[tecnica]['abbreviation'] for tecnica in datos_ano_pasado['MAGNITUD']]
    datos_ano_pasado['Unidades']=[diccionario_magnitudes[tecnica]['unit'] for tecnica in datos_ano_pasado['MAGNITUD']]
    datos_ano_pasado=datos_ano_pasado[["Magnitudes","Valores","Unidades","Abreviatura"]]
    print(f"Datos correspondientes al año {2019} a la estacion {diccionario_estaciones[int(estacion)]}.")
    print(datos_ano_pasado)
    return datos_ano_pasado



