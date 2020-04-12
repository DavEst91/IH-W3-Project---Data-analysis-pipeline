import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.summarize_contamination_data import *
from src.diccionarios import *
import seaborn as sns

sns.set()

tabla_resumen=concat_calculate(get_summary_table_old_data(56,2015),get_summary_table_new_data(56)).T
tabla_resumen=tabla_resumen.dropna(axis=1)

for magnitud in list(tabla_resumen.columns):
    plt.scatter(list(tabla_resumen.index)[:-2],list(tabla_resumen[magnitud])[:-2],s=50)
    plt.title(label=magnitud)
    for elemento in diccionario_magnitudes:
        if diccionario_magnitudes[elemento]['Name']==magnitud:
            ylabel=diccionario_magnitudes[elemento]["abbreviation"]+" ("+diccionario_magnitudes[elemento]["unit"]+")"
    plt.ylabel(ylabel)
    plt.xlabel('Year')
    plt.show()