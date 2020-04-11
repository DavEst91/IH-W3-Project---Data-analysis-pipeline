import sys, pandas, os, numpy
from src.cleaning_data import *
from argparse import ArgumentParser
from src.obtaining_new_data import *
parser = ArgumentParser(description="Este programa es para obtener información sobre la calidad del aire")
parser.add_argument("--estacion",help="este es el número de la estacion meteorologica de la que desea obtener información meteorológica", default=49)
args = parser.parse_args()


get_last_year_data(args.estacion)
get_dataset_today(args.estacion)

