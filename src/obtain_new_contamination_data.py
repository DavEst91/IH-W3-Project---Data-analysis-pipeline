import requests
import pandas as pd
from io import StringIO 
from src.diccionarios import *

#This is the function that makes the call to Ayuntamiento de Madrid webpage
def obtener_datos_contaminacion_actualizados():
    url="http://www.mambiente.madrid.es/opendata/horario.txt"
    datos_hoy=requests.get(url).text
    StringData=StringIO(datos_hoy)
    df_raw=pd.read_csv(StringData,sep=",",header=None)
    return df_raw

#Cleaning the obtained data
def limpiar_datos_contaminacion_hoy(df_raw):
    df_limpio=df_raw.copy()
    df_limpio=df_limpio.drop(columns=[0,1,4,5,6,7,8])
    for i in df_limpio.columns:
        if df_limpio[i][0]=='N':
            df_limpio=df_limpio.drop(columns=[i,i-1])
        elif df_limpio[i][0]=='V':
            df_limpio=df_limpio.drop(columns=[i])
    return df_limpio

#Making some calculations on the cleaned dataset
def calculos_df_limpio(df_limpio):
    df_limpio['Valores']=df_limpio[list(df_limpio.columns)[2:]].median(axis=1)
    return df_limpio

#This function call all the above and get a cleaned and ordered pandas DataFrame to be used for other functions

def get_dataset_today(estacion):
    dataset_hoy=obtener_datos_contaminacion_actualizados()
    dataset_hoy=limpiar_datos_contaminacion_hoy(dataset_hoy)
    dataset_hoy=calculos_df_limpio(dataset_hoy)
    dataset_hoy=dataset_hoy.loc[dataset_hoy[2]==int(estacion)]
    #Those two values appears in the data but not in the documentation, so we can't know what they are
    dataset_hoy=dataset_hoy[dataset_hoy[3]!=22]
    dataset_hoy=dataset_hoy[dataset_hoy[3]!=44]
    dataset_hoy['Magnitudes']=[diccionario_magnitudes[tecnica]['Name'] for tecnica in dataset_hoy[3]]
    dataset_hoy['Abreviatura']=[diccionario_magnitudes[tecnica]['abbreviation'] for tecnica in dataset_hoy[3]]
    dataset_hoy['Unidades']=[diccionario_magnitudes[tecnica]['unit'] for tecnica in dataset_hoy[3]]
    dataset_hoy=dataset_hoy[["Magnitudes","Valores","Unidades","Abreviatura"]]   
    return dataset_hoy



