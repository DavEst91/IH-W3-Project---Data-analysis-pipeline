# IH: W3 Project - Data analysis pipeline

Data from Madrid air quality is freely offered by [Ayuntamiento de Madrid](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=aecb88a7e2b73410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default).The historical data can be downloaded and the daily updated data are publicated on this [website](http://www.mambiente.madrid.es/opendata/horario.txt)

Meteorological data is freely offered by [AEMET Open Data](https://opendata.aemet.es/centrodedescargas/inicio)

In the file [Interprete_ficheros_calidad_del_aire.pdf](https://github.com/DavEst91/data-analysis-pipeline/blob/master/Interprete_ficheros_%20calidad_%20del_%20aire_global.pdf) you can find the information provided by Ayuntamiento de Madrid to interpretate its data.


## Description:
We have created a program that obtains today's prediction of meteorological data from AEMET and todays air quality data from Ayuntamiento de Madrid. Then we search in the database for the air quality data on the same day in the last ten years and offer today's prediction from AEMET, a summarize table for the air quality data and a graph for each measured magnitudes.The results can be filtered from the measuring station we want data from and the year since we want data.

Outputs can be only shown in screen or stored as files.

## Requirements:

You need to have installed the following Python 3 libraries: 
* pandas
* numpy
* matplotlib
* requests
* datetime
* dotenv
* io
* seaborn
* argparse

Also you need to get an [ApiKey for AEMET API](https://opendata.aemet.es/centrodedescargas/altaUsuario) and save it in a .env file located in the parent directory as AEMET_APIKEY=<your_apikey>

## Usage:

```
python3 main.py --estacion <ref code> --year <Year since you want information in format AAAA> --output <screen or file>
```
Code of measuring stations response to international encoding and therefore are not changed. You can find them in the table below and the correspondent ref code for this program.
<center>
  
| ISO code | ref code |    Measuring station    |
|:--------:|:--------:|:-----------------------:|
|  2807904 |     4    |      Pza. de España     |
|  2807908 |     8    |     Escuelas Aguirre    |
|  2807911 |    11    |   Avda. Ramón y Cajal   |
|  2807916 |    16    |       Arturo Soria      |
|  2807917 |    17    |     Villaverde Alto     |
|  2807918 |    18    |       C/Farolillo       |
|  2807924 |    24    |      Casa de Campo      |
|  2807927 |    27    |         Barajas         |
|  2807935 |    35    |     Plaza del Carmen    |
|  2807936 |    36    |        Moratalaz        |
|  2807938 |    38    |      Cuatro Caminos     |
|  2807939 |    39    |     Barrio del Pilar    |
|  2807940 |    40    |         Vallecas        |
|  2807947 |    47    |      Mendez Alvaro      |
|  2807948 |    48    |     Paseo Castellana    |
|  2807949 |    49    |          Retiro         |
|  2807950 |    50    |      Plaza Castilla     |
|  2807954 |    54    |    Ensanche Vallecas    |
|  2807955 |    55    | Urb. Embajada (Barajas) |
|  2807956 |    56    |      Plaza Elíptica     |
|  2807957 |    57    |       Sanchinarro       |
|  2807958 |    58    |         El Pardo        |
|  2807959 |    59    |   Parque Juan Carlos I  |
|  2807960 |    60    |       Tres Olivos       |

</center>
