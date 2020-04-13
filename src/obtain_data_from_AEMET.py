import requests
import os
from datetime import date
from src.diccionarios import *
from dotenv import load_dotenv
load_dotenv()


#Function that we use to get data from AEMET, making a call to its API.
def get_data_from_AEMET():
    url = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/28079"
    apiKey = os.getenv("AEMET_APIKEY")
    querystring ={"api_key":apiKey}
    response = requests.get(url, headers={"Accept": "application/json"}, params=querystring)
    datos=requests.get(url=response.json()['datos'])
    prediccion=datos.json()
    return prediccion

#This function prints on screen the data from get_data_from_AEMET()
def print_data_from_AEMET(prediccion):
    print("Predicción meteorológica para el día de hoy del AEMET:")
    print(f"\t·El estado del cielo es {prediccion[0]['prediccion']['dia'][0]['estadoCielo'][0]['descripcion'].lower()}.")
    print(f"\t·La humedad relativa oscila entre {prediccion[0]['prediccion']['dia'][0]['humedadRelativa']['minima']}% y {prediccion[0]['prediccion']['dia'][0]['humedadRelativa']['maxima']}%.")
    print(f"\t·La probabilidad de precipitacion es del {prediccion[0]['prediccion']['dia'][0]['probPrecipitacion'][0]['value']}%.")
    print(f"\t·La temperatura oscila entre {prediccion[0]['prediccion']['dia'][0]['temperatura']['minima']} ºC y {prediccion[0]['prediccion']['dia'][0]['temperatura']['maxima']} ºC.")
    print(f"\t·La sensación térmica oscila entre {prediccion[0]['prediccion']['dia'][0]['sensTermica']['minima']} ºC y {prediccion[0]['prediccion']['dia'][0]['sensTermica']['maxima']} ªC.")

#This function saves the data as variables from get_data_from_AEMET()
def store_data_from_AEMET(prediccion):
    estado_cielo=prediccion[0]['prediccion']['dia'][0]['estadoCielo'][0]['descripcion']
    hum_rel_min=prediccion[0]['prediccion']['dia'][0]['humedadRelativa']['minima']
    hum_rel_max=prediccion[0]['prediccion']['dia'][0]['humedadRelativa']['maxima']
    prob_precipitacion=prediccion[0]['prediccion']['dia'][0]['probPrecipitacion'][0]['value']
    temp_max=prediccion[0]['prediccion']['dia'][0]['temperatura']['maxima']
    temp_min=prediccion[0]['prediccion']['dia'][0]['temperatura']['minima']
    sens_temp_max=prediccion[0]['prediccion']['dia'][0]['sensTermica']['maxima']
    sens_temp_min=prediccion[0]['prediccion']['dia'][0]['sensTermica']['minima']
    return estado_cielo,hum_rel_min,hum_rel_max,prob_precipitacion,temp_min,temp_max,sens_temp_min,sens_temp_max

#This function saves the data from get_data_from_AEMET() on a file
def save_data_from_AEMET(prediccion,estacion,ano):
    today = date.today()
    dia,mes,ano = today.strftime("%d"),today.strftime("%m"),today.strftime("%y")
    filename=f"{ano}{mes}{dia}_{diccionario_estaciones[int(estacion)]}_prediccionAEMET.txt"
    ruta=os.getcwd()
    os.chdir("./output")
    file=open(filename,'w')
    file.write(f"Predicción meteorológica para el {dia}/{mes}/{ano} del AEMET:\n")
    file.write(f"\t·El estado del cielo es {prediccion[0]['prediccion']['dia'][0]['estadoCielo'][0]['descripcion'].lower()}.\n")
    file.write(f"\t·La humedad relativa oscila entre {prediccion[0]['prediccion']['dia'][0]['humedadRelativa']['minima']}% y {prediccion[0]['prediccion']['dia'][0]['humedadRelativa']['maxima']}%.\n")
    file.write(f"\t·La probabilidad de precipitacion es del {prediccion[0]['prediccion']['dia'][0]['probPrecipitacion'][0]['value']}%.\n")
    file.write(f"\t·La temperatura oscila entre {prediccion[0]['prediccion']['dia'][0]['temperatura']['minima']} ºC y {prediccion[0]['prediccion']['dia'][0]['temperatura']['maxima']} ºC.\n")
    file.write(f"\t·La sensación térmica oscila entre {prediccion[0]['prediccion']['dia'][0]['sensTermica']['minima']} ºC y {prediccion[0]['prediccion']['dia'][0]['sensTermica']['maxima']} ªC.\n")
    file.close()
    os.chdir(ruta)

    
