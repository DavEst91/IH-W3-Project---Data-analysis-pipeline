import sys, pandas, os, numpy
from src.cleaning_data import *
from argparse import ArgumentParser
from src.obtain_old_contamination_data import *
from src.obtain_new_contamination_data import *
from src.obtain_data_from_AEMET import *
from src.summarize_contamination_data import *
parser = ArgumentParser(description="Este programa es para obtener información sobre la calidad del aire")
parser.add_argument("--estacion",help="este es el número de la estacion meteorologica de la que desea obtener información", default=49)
parser.add_argument("--ano",help="este es el ano desde el que desea obtener informacion en formato AAAA", default=2019)
args = parser.parse_args()

try:
    print_data_from_AEMET(get_data_from_AEMET())
except:
    pass
print(f"Mostrando tabla resumen de las medidas realizadas en la estacion {diccionario_estaciones[int(args.estacion)]} desde el año {args.ano}.")

print(concat_calculate(get_summary_table_old_data(int(args.estacion),int(args.ano)),get_summary_table_new_data(int(args.estacion))))
