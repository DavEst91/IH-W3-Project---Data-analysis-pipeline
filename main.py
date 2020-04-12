import sys, pandas, os, numpy
from src.cleaning_data import *
from argparse import ArgumentParser
from src.obtain_old_contamination_data import *
from src.obtain_new_contamination_data import *
from src.obtain_data_from_AEMET import *

parser = ArgumentParser(description="Este programa es para obtener información sobre la calidad del aire")
parser.add_argument("--estacion",help="este es el número de la estacion meteorologica de la que desea obtener información", default=49)
parser.add_argument("--ano",help="este es el ano desde el que desea obtener informacion en formato AAAA", default=2019)
args = parser.parse_args()

print_data_from_AEMET(get_data_from_AEMET())

for i in range(int(args.ano),2020):
	print_last_years_data(args.estacion,i)

get_dataset_today(args.estacion)

