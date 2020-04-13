import sys, pandas, os, numpy
from src.cleaning_data import *
from src.obtain_old_contamination_data import *
from src.obtain_new_contamination_data import *
from src.obtain_data_from_AEMET import *
from src.summarize_contamination_data import *
from src.create_graphs import*

def output_screen(estacion,ano,output):
    try:
        print_data_from_AEMET(get_data_from_AEMET())
    except:
        pass
    print(f"Mostrando tabla resumen de las medidas realizadas en la estacion {diccionario_estaciones[int(estacion)]} desde el año {ano}.")

    print(concat_calculate(get_summary_table_old_data(int(estacion),int(ano)),get_summary_table_new_data(int(estacion))))
    create_plots(int(estacion),int(ano),output)
