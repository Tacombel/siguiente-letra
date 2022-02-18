import csv
import re
from unicodedata import normalize

listado_de_palabras = []
with open('0_palabras_todas.txt', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        listado_de_palabras.append(row[0])

listado_de_palabras_sin_tildes = []
for e in listado_de_palabras:
    s = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", e), 0, re.I
    )
    listado_de_palabras_sin_tildes.append(s)

with open('listado_de_palabras_sin_tildes.txt', 'w') as file:
    for item in listado_de_palabras_sin_tildes:
        file.write("%s\n" % item)
