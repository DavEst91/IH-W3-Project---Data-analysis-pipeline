from fpdf import FPDF
from src.obtain_data_from_AEMET import *
from src.diccionarios import *
from src.summarize_contamination_data import *
import os 
from datetime import date

def generate_pdf(estacion,ano,output):
    pdf = FPDF()
    pdf.add_page()
    ##GET AEMET DATA##
    filename=save_data_from_AEMET(get_data_from_AEMET(),estacion,ano)
    current_route=os.getcwd()
    os.chdir("./output")
    AEMET_DATA=open(filename,'r')
    data=AEMET_DATA.read()
    AEMET_DATA.close
    os.remove(filename)
    os.chdir(current_route)

    ##GET SUMMARIZED TABLE##    
    filename=concat_calculate(get_summary_table_old_data(int(estacion),int(ano)),get_summary_table_new_data(int(estacion)),estacion,output)
    os.chdir("./output")
    summarized_table=open(filename,'r')
    
    summarized_table_splitted=[linea.split(',') for linea in summarized_table.read().split('\n')]
    
    #os.chdir(current_route)


    
    pdf.set_font('Arial', 'B', 16)
    today = date.today()
    dia,mes,ano= today.strftime("%d"),today.strftime("%m"),today.strftime("%y")

    cabecera=f"Informe de la calidad del aire para la estación de {diccionario_estaciones[estacion]} del {dia}/{mes}/{ano}:"
    
    pdf.set_font('Arial', '', 12)
    pdf.cell(w=160, h = 8, txt =cabecera, border = 10, ln = 10, 
           align = '', fill = False, )
    pdf.multi_cell(160,8, data, border = 0, 
                  fill= False)
    col_width = pdf.w / 10
    row_height = pdf.font_size
    for row in summarized_table_splitted:
        for item in row:
            pdf.cell(col_width, row_height*1.5,
                     txt=item, border=1)
        pdf.ln(row_height*1.5)
    

    pdf.output('tuto1.pdf')

generate_pdf(56,2015,'pdf')


