import sys, pandas as pd, os, numpy as np
from src.obtain_new_contamination_data import *
from src.obtain_old_contamination_data import *




listado_magnitudes=[]

for magnitud in list(diccionario_magnitudes.values()):
    listado_magnitudes.append(magnitud['Name'])



tabla_resumen=pd.DataFrame(columns=listado_magnitudes)
for i in range(2010,2019):
    dataset=get_last_years_data(56,i)
    add_to_dataset=[]
    for j in listado_magnitudes:
        if j in list(dataset.Magnitudes.values):
            add_to_dataset.append(float(dataset['Valores'].loc[dataset['Magnitudes']==j].values))
        else:
            add_to_dataset.append(np.nan)
    dataset_to_add=pd.DataFrame(data=[add_to_dataset], columns=listado_magnitudes)
    tabla_resumen=pd.concat([tabla_resumen,dataset_to_add]).dropna(axis=1,how='all')
    
tabla_resumen['year']=list(range(2010,2019))
tabla_resumen.set_index('year',inplace=True )
print(tabla_resumen.T)

