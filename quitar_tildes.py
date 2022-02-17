import csv
import unidecode

listado_de_palabras = []
with open('0_palabras_todas.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        listado_de_palabras.append(row[0])

listado_de_palabras_sin_tildes = []
for e in listado_de_palabras:
    sin_tildes = unidecode.unidecode(e)
    listado_de_palabras_sin_tildes.append(sin_tildes)

with open('listado_de_palabras_sin_tildes.txt', 'w') as file:
    for item in listado_de_palabras_sin_tildes:
        file.write("%s\n" % item)
