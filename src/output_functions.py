import sys, pandas, os, numpy
from src.obtain_old_contamination_data import *
from src.obtain_new_contamination_data import *
from src.obtain_data_from_AEMET import *
from src.summarize_contamination_data import *
from src.create_graphs import*

#In this module different functions are defined to get the output in different forms.

def output_screen(estacion,ano,output):
    try:
        print_data_from_AEMET(get_data_from_AEMET())
    except:
        pass
    print(f"Mostrando tabla resumen de las medidas realizadas en la estacion {diccionario_estaciones[int(estacion)]} desde el año {ano}.")

    print(concat_calculate(get_summary_table_old_data(int(estacion),int(ano)),get_summary_table_new_data(int(estacion)),estacion,output))
    create_plots(int(estacion),int(ano),output)


def output_file(estacion, ano, output):
    save_data_from_AEMET(get_data_from_AEMET(),estacion,ano)
    concat_calculate(get_summary_table_old_data(int(estacion),int(ano)),get_summary_table_new_data(int(estacion)),estacion,output)
    create_plots(int(estacion),int(ano),output)
