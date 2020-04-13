import os
import pandas as pd
import time
from datetime import date
from input.diccionarios import *


def format_day_month():
    today = date.today()
    dia,mes= today.strftime("%d"),today.strftime("%m")
    dia,verificacion_dia="D"+dia, "V"+dia
    return dia, verificacion_dia, int(mes)


def print_last_years_data(estacion,ano):
    dia, verificacion, mes=format_day_month()
    path_to_file=f"./input/datos{ano }.csv"
    datos_ano_anterior=pd.read_csv(path_to_file, sep=';').drop(columns=['PROVINCIA',"MUNICIPIO","PUNTO_MUESTREO","ANO"],axis=0)
    datos_ano_anterior=datos_ano_anterior.loc[datos_ano_anterior.ESTACION==int(estacion)].loc[datos_ano_anterior.MES==mes].loc[datos_ano_anterior[verificacion]!='N'][['MAGNITUD',dia]]
    datos_ano_anterior['Valores']=datos_ano_anterior[dia]
    datos_ano_anterior['Magnitudes']=[diccionario_magnitudes[tecnica]['Name'] for tecnica in datos_ano_anterior['MAGNITUD']]
    datos_ano_anterior['Abreviatura']=[diccionario_magnitudes[tecnica]['abbreviation'] for tecnica in datos_ano_anterior['MAGNITUD']]
    datos_ano_anterior['Unidades']=[diccionario_magnitudes[tecnica]['unit'] for tecnica in datos_ano_anterior['MAGNITUD']]
    datos_ano_anterior=datos_ano_anterior[["Magnitudes","Valores","Unidades","Abreviatura"]]
    print(f"Datos correspondientes al año {ano} a la estacion {diccionario_estaciones[int(estacion)]}.")
    print(datos_ano_anterior)


def get_last_years_data(estacion,ano):
    dia, verificacion, mes=format_day_month()
    path_to_file=f"./input/datos{ano}.csv"
    datos_ano_anterior=pd.read_csv(path_to_file, sep=';').drop(columns=['PROVINCIA',"MUNICIPIO","PUNTO_MUESTREO","ANO"],axis=0)
    datos_ano_anterior=datos_ano_anterior.loc[datos_ano_anterior.ESTACION==int(estacion)].loc[datos_ano_anterior.MES==mes].loc[datos_ano_anterior[verificacion]!='N'][['MAGNITUD',dia]]
    datos_ano_anterior['Valores']=datos_ano_anterior[dia]
    datos_ano_anterior['Magnitudes']=[diccionario_magnitudes[tecnica]['Name'] for tecnica in datos_ano_anterior['MAGNITUD']]
    datos_ano_anterior['Abreviatura']=[diccionario_magnitudes[tecnica]['abbreviation'] for tecnica in datos_ano_anterior['MAGNITUD']]
    datos_ano_anterior['Unidades']=[diccionario_magnitudes[tecnica]['unit'] for tecnica in datos_ano_anterior['MAGNITUD']]
    datos_ano_anterior=datos_ano_anterior[["Magnitudes","Valores","Unidades","Abreviatura"]]
    return datos_ano_anterior




