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

dataset2019=pd.read_csv('./input/datos201912.csv', sep=';').drop(columns=['PROVINCIA',"MUNICIPIO","PUNTO_MUESTREO","ANO"],axis=0)




diccionario_estaciones={
        4:"Pza. de España",
        8:"Escuelas Aguirre",
        11:"Avda. Ramón y Cajal",
        16:"Arturo Soria",
        17:"Villaverde Alto",
        18:"C/Farolillo",
        24:"Casa de Campo",
        27:"Barajas",
        35:"Plaza del Carmen",
        36:"Moratalaz",
        38:"Cuatro Caminos",
        39:"Barrio del Pilar",
        40:"Vallecas",
        47:"Mendez Alvaro",
        48:"Paseo Castellana",
        49:"Retiro",
        50:"Plaza Castilla",
        54:"Ensanche Vallecas",
        55:"Urb. Embajada (Barajas)",
        56:"Plaza Elíptica",
        57:"Sanchinarro",
        58:"El Pardo",
        59:"Parque Juan Carlos I",
        60:"Tres Olivos"
    
    }

diccionario_magnitudes={
    1:{"Name":"Dioxido de azufre","abbreviation":"SO2","unit":"ug/m^3"},
    6:{"Name":"Monoxido de carbono","abbreviation":"CO","unit":"ug/m^3"},
    7:{"Name":"Monoxido de nitrogeno","abbreviation":"NO","unit":"ug/m^3"},
    8:{"Name":"Dioxido de nitrogeno","abbreviation":"NO2","unit":"ug/m^3"},
    9:{"Name":"Particulas<2.5 um","abbreviation":"PM2.5","unit":"ug/m^3"},
    10:{"Name":"Particulas<10 um","abbreviation":"PM10","unit":"ug/m^3"},
    12:{"Name":"Oxidos de nitrogeno","abbreviation":"NOx","unit":"ug/m^3"},
    14:{"Name":"Ozono","abbreviation":"O3","unit":"ug/m^3"},
    20:{"Name":"Tolueno","abbreviation":"TOL","unit":"ug/m^3"},
    30:{"Name":"Benceno","abbreviation":"BEN","unit":"ug/m^3"},
    35:{"Name":"Etilbenceno","abbreviation":"EBE","unit":"ug/m^3"},
    37:{"Name":"Metalixeno","abbreviation":"MXY","unit":"ug/m^3"},
    38:{"Name":"Paraxileno","abbreviation":"PXY","unit":"ug/m^3"},
    39:{"Name":"Ortoxileno","abbreviation":"OXY","unit":"ug/m^3"},
    42:{"Name":"Hidrocarburos totales (Hexano)","abbreviation":"TCH","unit":"mg/m^3"},
    43:{"Name":"Metano","abbreviation":"CH4","unit":"mg/m^3"}
            
                }
            
    

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

