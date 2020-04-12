import sys, pandas as pd, os, numpy as np
from src.obtain_new_contamination_data import *
from src.obtain_old_contamination_data import *


def get_summary_table_old_data(estacion,ano):
    listado_magnitudes=[]
    for magnitud in list(diccionario_magnitudes.values()):
        listado_magnitudes.append(magnitud['Name'])
    
    tabla_resumen=pd.DataFrame(columns=listado_magnitudes)
    
    for year in range(int(ano),2020):
        dataset=get_last_years_data(estacion,year)
        add_to_dataset=[]
        for magnitud in listado_magnitudes:
            if magnitud in list(dataset.Magnitudes.values):
                add_to_dataset.append(float(dataset['Valores'].loc[dataset['Magnitudes']==magnitud].values))
            else:
                add_to_dataset.append(np.nan)
        dataset_to_add=pd.DataFrame(data=[add_to_dataset], columns=listado_magnitudes)
        tabla_resumen=pd.concat([tabla_resumen,dataset_to_add]).dropna(axis=1,how='all')
    tabla_resumen['year']=list(range(ano,2020))
    tabla_resumen.set_index('year',inplace=True )
    return(tabla_resumen)

def get_summary_table_new_data(estacion):
    dataset=get_dataset_today(estacion)
    listado_magnitudes=[]
    for magnitud in list(diccionario_magnitudes.values()):
        listado_magnitudes.append(magnitud['Name'])

    tabla_resumen=pd.DataFrame(columns=listado_magnitudes)
    add_to_dataset=[]
    for magnitud in listado_magnitudes:
            if magnitud in list(dataset.Magnitudes.values):
                add_to_dataset.append(float(dataset['Valores'].loc[dataset['Magnitudes']==magnitud].values))
            else:
                add_to_dataset.append(np.nan)
    dataset_to_add=pd.DataFrame(data=[add_to_dataset], columns=listado_magnitudes)
    tabla_resumen=pd.concat([tabla_resumen,dataset_to_add]).dropna(axis=1,how='all')
    tabla_resumen['year']=2020
    tabla_resumen.set_index('year',inplace=True )
    return(tabla_resumen)

def concat_calculate(table_old,table_new):
    tabla_resumen=pd.concat([table_old,table_new]).T
    tabla_resumen['media']=tabla_resumen.mean(axis=1).round(1)
    tabla_resumen['std']=tabla_resumen.std(axis=1).round(1)
    return tabla_resumen

