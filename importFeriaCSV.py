# Crear o actualizar ferias del agricultor dado un archivo csv

import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'sitio.settings'
django.setup()
import csv
from ferias.models import Feria
from ferias.utils import PROVINCIAS

# cambiar por la direccion donde guardaron el archivo de ferias
link = "C:/Users/tyron/Desktop/feria.csv"

def load():
    print("Abriendo archivo...")
    with open(link, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader) # saltar headers
        for row in reader:
            # invertir diccionario de Provincias
            prov =  dict((v,k) for k,v in PROVINCIAS).get(row[7])
            _, created = Feria.objects.update_or_create(
                feria_id=row[0],
                defaults={
                    'codigo_url' : row[1],
                    'nombre' : row[2],
                    'conocida_como' : row[3],
                    'comite' : row[4],
                    'administrador' : row[5],
                    'telefono' : row[6],
                    'provincia' : prov,
                    'canton' : row[8],
                    'distrito' : row[9],
                    'direccion' : row[10],
                    'latitud' : row[11] if row[11] != '' else 0.0,
                    'longitud' : row[12] if row[12] != '' else 0.0,
                    'estacionamiento' : row[14] == 'Si',
                    'parqueo_bicicleta' : row[15] == 'Si',
                    'sanitarios' : row[16] == 'Si',
                    'campo_ferial' : row[17] == 'Si',
                    'bajo_techo' : row[18] == 'Si',
                    'agua_potable' : row[19] == 'Si',
                    'metodo_pago' : row[20],
                    'accesibilidad' : row[21] == 'Si'
                }               
            )
        print("Listo!")

if __name__ == '__main__':
    load()
