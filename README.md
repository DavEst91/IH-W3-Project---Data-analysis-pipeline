# IH: W3 Project -Data analysis pipeline

Data from Madrid air quality is freely offered by [Ayuntamiento de Madrid](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=aecb88a7e2b73410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default).The historical data can be downloaded and the daily updated data are publicated on this [website](http://www.mambiente.madrid.es/opendata/horario.txt)

Meteorological data is freely offered by [AEMET Open Data](https://opendata.aemet.es/centrodedescargas/inicio)


## Abstract:
We have created a program that obstains todays prediction of meteorolical data from AEMET and todays air quality data from Ayuntamiento de Madrid.Then we search in the database for the air quality data at the same day in the last ten years and offer todays prediction from AEMET, a summarize table for the air quality data and a graph for each measured magnitud.

The results can be filtered from the measuring station we want data from and the year since we want data.


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


