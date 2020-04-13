import sys, pandas, os, numpy
from src.cleaning_data import *
from argparse import ArgumentParser
from src.obtain_old_contamination_data import *
from src.obtain_new_contamination_data import *
from src.obtain_data_from_AEMET import *
from src.summarize_contamination_data import *
from src.output_functions import *
parser = ArgumentParser(description="Este programa es para obtener información sobre la calidad del aire")
parser.add_argument("--estacion",help="El número de la estacion meteorologica de la que desea obtener información", default=38)
parser.add_argument("--ano",help="El ano desde el que desea obtener informacion en formato AAAA", default=2018)
parser.add_argument("--output",help="Forma en la que se desea el output", default="screen")
args = parser.parse_args()

if args.output=='screen':
    output_screen(args.estacion,args.ano,args.output)
    
