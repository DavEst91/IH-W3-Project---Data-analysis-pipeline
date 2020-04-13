import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from src.summarize_contamination_data import *
from src.diccionarios import *
import seaborn as sns

sns.set()

def create_plots(estacion,ano,output):
    tabla_resumen=concat_calculate(get_summary_table_old_data(estacion,ano),get_summary_table_new_data(estacion)).T
    tabla_resumen=tabla_resumen.dropna(axis=1)

    for magnitud in list(tabla_resumen.columns):
        grafico=plt.plot(list(tabla_resumen.index)[:-2],list(tabla_resumen[magnitud])[:-2],marker='o',label=magnitud)
        plt.title(label=diccionario_estaciones[estacion])
        for elemento in diccionario_magnitudes:
            if diccionario_magnitudes[elemento]['Name']==magnitud:
                ylabel=diccionario_magnitudes[elemento]["abbreviation"]+" ("+diccionario_magnitudes[elemento]["unit"]+")"
        plt.ylabel(ylabel)
        plt.xlabel('Year')
        plt.hlines(list(tabla_resumen[magnitud])[-2],int(list(tabla_resumen.index)[0]),int(list(tabla_resumen.index)[-3]),color='red',label="Valor medio")
        plt.hlines((list(tabla_resumen[magnitud])[-2]+list(tabla_resumen[magnitud])[-1]),int(list(tabla_resumen.index)[0]),int(list(tabla_resumen.index)[-3]),color='green',label="std")
        plt.hlines((list(tabla_resumen[magnitud])[-2]-list(tabla_resumen[magnitud])[-1]),int(list(tabla_resumen.index)[0]),int(list(tabla_resumen.index)[-3]),color='green')
        plt.locator_params(axis='x', nbins=len(list(tabla_resumen.index)[:-2]))
        plt.legend()
        if output=='screen':
            plt.show()

